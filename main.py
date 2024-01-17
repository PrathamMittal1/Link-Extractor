import streamlit as st
import link_extract
import title_extractor
import pandas as pd
from streamlit_js_eval import streamlit_js_eval

def upload_and_process_file(file):
    st.toast('Please wait... Processing!')
    progress_bar = st.progress(0)
    # Method to get the plain text from the file
    text = link_extract.convert_to_str(file)

    progress_bar.progress(4)
    # Returns a list of extracted URLs
    urls = link_extract.main(text)
    progress_bar.progress(8)

    # List to store extracted links and info
    results = []

    n = len(urls)
    percent_inc = 92 // n
    if percent_inc == 0:
        chunk_size = n // 92
        processed_in_chunk = 0
    percent = 8
    
    # Loop for getting the title of each link-related HTML document
    # Saving them in results list
    for i, url in enumerate(urls):
        results.append((url, title_extractor.main(url)))

        # Update progress bar
        if percent_inc == 0 and percent < 100:
            processed_in_chunk += 1
            if processed_in_chunk == chunk_size:
                percent += 1
                processed_in_chunk = 0
            if percent == 100:
                st.toast("Wait a moment... Finalizing!")
            
        else:
            percent += percent_inc
        progress_bar.progress(percent)
        print(i)

    progress_bar.progress(100)

    return results
    

def display_results_table(df):
    # global df1
    # Displaying the already extracted links
    df1 = st.data_editor(df, column_config={"URL": st.column_config.LinkColumn("URLs"),
                                            "TITLE": st.column_config.Column(width=650),
                                            "GENRE": st.column_config.Column(width=200)},
                                            num_rows='dynamic')
    df1.to_csv('urls.csv', index=False)

def main():
    # Setting the page layout to wide
    st.set_page_config(layout="wide")

    # Title heading
    st.title("Link Extraction and Link Insights")

    # File upload widget
    uploaded_file = st.file_uploader(label='Upload a file')

    # Reading already extracted links
    df = pd.read_csv('urls.csv')
    df = df.drop_duplicates(subset=['URL'])

    # Displaying the already extracted links
    display_results_table(df)

    # Logic for extracting links from uploaded file
    if uploaded_file is not None:
        # Clear the existing results table
        st.write("Processing...")

        # Process the uploaded file
        results = upload_and_process_file(uploaded_file)

        # Create a new DataFrame and concatenate with the existing DataFrame
        new_df = pd.DataFrame(results, columns=['URL', 'TITLE'])
        new_df['GENRE'] = " "
        df = pd.concat([new_df, df])

        # Drop duplicates based on the 'URL' column
        df = df.drop_duplicates(subset=['URL'])

        # Save the updated DataFrame to CSV
        df.to_csv('urls.csv', index=False)

        # Force refresh of the page to show the changes
        streamlit_js_eval(js_expressions="parent.window.location.reload()")


if __name__ == '__main__':
    main()

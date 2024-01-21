# Link Extractor
 Link Extraction and Insights Generator

 ## How to setup
 Step 1. Clone the repository, or download the zip file of the source code and extract the content. <br/>
 Step 2. Go to the project folder and create a virtual environment inside the project folder. Using the command "py -m venv <venv>" <br/>
 Step 3. After activating the virtual environment you created install the requirements.txt using the command "pip install -r requirements.txt" <br/>
 Step 4. In the activated virtual environment run the command 'streamlit run main.py' to run the application. The address will be printed over the console and you can browse the address over your web browser. <br/>

# Now, understanding about the project in detail.

## Aim
The objective of this feature is to first extract the URLs from a document such as text file and then for each link generate a summarized preview text of the content in the document of which the URL is given.


## Approaches 
To extract URLs 

•	One way of extracting URLs from the given text file is regular expression search. A regular expression pattern can match the URLs efficiently from the raw text data. <br/>
•	One approach is to pass the raw text to a Large Language Model (LLM) and using prompting to get the list of links as the response. This is an expensive method as the raw text data can be potentially large and it might easily consume the token limits. <br/>

To generate previews

•	One way is to pass the URL to the LLM and ask the LLM to summarize the content of webpage briefly. <br/>
•	Another way is to Web crawl to extract the natural language from the URL html (by paragraphs <p>). Execute the summarize class algorithm (implemented using NLTK) on the extracted sentences. <br/>


## Benefits and Usage

When a friend sends an article to a WhatsApp group, according to a research at www.assafelovic.com, 65% of group users don’t even click the shared URLs, but 97% of them will read a few lines of the article’s summary. <br/>
So, generating a summary preview of URL links in a WhatsApp chat can really save time and save us from missing any important link or article. <br/>

## Running Time

Tested on exported WhatsApp group chats, one having less than 100 links shared and the other one having a large number of links shared approximately around 700. <br/>
On testing it on a file of 260 lines and 80 links, it gives the final results in about 2 minutes. <br/>
Whereas on testing it on a larger file of 4362 lines and 689 links, it is serving the final results in around 11 minutes.  <br/>

## Project Flow

Let's describe the project flow and features: <br/>

### 1.	File Structure:
•	main.py: The main Streamlit application file where the user interacts with the interface. <br/>
•	link_extract.py: A module for extracting URLs from raw text obtained from PDF or TXT files. <br/>
•	title_extractor.py: A module for extracting the title of HTML documents from given URLs. <br/>

### 2.	Flow:
•	File Upload: <br/>
The main Streamlit app (main.py) starts by allowing users to upload a file. <br/>
Accepted file formats include PDF and TXT. <br/>

•	Display Existing Links: <br/>
o	If there are existing links from previous runs (stored in 'urls.csv'), they are displayed in a table using st.data_editor. <br/>
o	Duplicates are removed based on the 'URL' column. <br/>

•	Processing Uploaded File: <br/>
o	If the user uploads a file, the application initiates the link extraction process. <br/>
o	The upload_and_process_file function in main.py does the following: <br/>
	Converts the file content to raw text using link_extract.convert_to_str. <br/>
	Extracts URLs from the text using the regular expression defined in link_extract.main. <br/>
	Iterates through the extracted URLs, uses title_extractor.main to get the title of the associated HTML documents, and updates the progress bar. <br/>

•	Display Results: <br/>
o	The results are displayed in a table using st.data_editor. <br/>
o	The table includes columns for 'TITLE' and 'URL'. <br/>
o	The results are saved to 'urls.csv' to persist across different sessions. <br/>
•	Page Configuration: <br/>
o	The Streamlit app is configured with a wide layout using st.set_page_config(layout="wide"). <br/>

•	Force Page Refresh: <br/>
o	After processing the uploaded file, the app uses streamlit_js_eval to force a page reload, showing the updated results. <br/>

### 3.	Features:
•	Link Extraction: <br/>
o	URLs are extracted from the uploaded file using a regular expression defined in link_extract.py. <br/>

•	Title Extraction: <br/>
o	The titles of HTML documents associated with the extracted URLs are obtained using title_extractor.py. <br/>

•	Display and Persistence: <br/>
o	The existing links and the newly extracted links are displayed in a table. <br/>
o	Duplicates are removed based on the 'URL' column. <br/>
o	The results are saved to 'urls.csv' for persistence. <br/>

•	User Feedback: <br/>
o	The app provides feedback to the user during processing using a toast message and a progress bar. <br/>
 

## Control Flow Diagram
![alt text](https://github.com/PrathamMittal1/Link-Extractor/blob/main/Images/Flow%20diagram.bmp)
 
## Future Enhancements:
1.	Enhanced Visualizations: <br/>
•	Introduce visualizations, such as charts or graphs, to provide users with insights into the link distribution or characteristics. <br/>
2.	User Authentication: <br/>
•	Implement user authentication mechanisms if needed, especially if there are plans to deploy the application in a multi-user environment. <br/>
3.	Advanced Link Analysis: <br/>
•	Explore possibilities for more advanced link analysis features, such as categorization or sentiment analysis on linked content. <br/>
4.	Integration with External APIs: <br/>
•	Consider integrating with external APIs to enrich link data or fetch additional information about the linked content. <br/>



## Bibliographic References
https://www.assafelovic.com/blog/2016/10/26/url-text-summarizer-using-web-crawling-and-nlp-python
https://docs.streamlit.io/library/api-reference/data/st.data_editor
https://streamlit.io/
https://openai.com/blog/chatgpt

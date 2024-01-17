# Link Extractor
 Link Extraction and Insights Generator


Aim
The objective of this feature is to first extract the URLs from a document such as text file and then for each link generate a summarized preview text of the content in the document of which the URL is given.


Approaches 
To extract URLs 
•	One way of extracting URLs from the given text file is regular expression search. A regular expression pattern can match the URLs efficiently from the raw text data.
•	One approach is to pass the raw text to a Large Language Model (LLM) and using prompting to get the list of links as the response. This is an expensive method as the raw text data can be potentially large and it might easily consume the token limits.
To generate previews
•	One way is to pass the URL to the LLM and ask the LLM to summarize the content of webpage briefly.
•	Another way is to Web crawl to extract the natural language from the URL html (by paragraphs <p>). Execute the summarize class algorithm (implemented using NLTK) on the extracted sentences.

Benefits and Usage
When a friend sends an article to a WhatsApp group, according to a research at www.assafelovic.com, 65% of group users don’t even click the shared URLs, but 97% of them will read a few lines of the article’s summary.
So, generating a summary preview of URL links in a WhatsApp chat can really save time and save us from missing any important link or article.

Running Time
Tested on exported WhatsApp group chats, one having less than 100 links shared and the other one having a large number of links shared approximately around 700.
On testing it on a file of 260 lines and 80 links, it gives the final results in about 2 minutes.
Whereas on testing it on a larger file of 4362 lines and 689 links, it is serving the final results in around 11 minutes. 

Project Flow
Let's describe the project flow and features:

1.	File Structure:
•	main.py: The main Streamlit application file where the user interacts with the interface.
•	link_extract.py: A module for extracting URLs from raw text obtained from PDF or TXT files.
•	title_extractor.py: A module for extracting the title of HTML documents from given URLs.

2.	Flow:
•	File Upload:
The main Streamlit app (main.py) starts by allowing users to upload a file.
Accepted file formats include PDF and TXT.

•	Display Existing Links:
o	If there are existing links from previous runs (stored in 'urls.csv'), they are displayed in a table using st.data_editor.
o	Duplicates are removed based on the 'URL' column.

•	Processing Uploaded File:
o	If the user uploads a file, the application initiates the link extraction process.

o	The upload_and_process_file function in main.py does the following:
	Converts the file content to raw text using link_extract.convert_to_str.
	Extracts URLs from the text using the regular expression defined in link_extract.main.
	Iterates through the extracted URLs, uses title_extractor.main to get the title of the associated HTML documents, and updates the progress bar.

•	Display Results:
o	The results are displayed in a table using st.data_editor.
o	The table includes columns for 'TITLE' and 'URL'.
o	The results are saved to 'urls.csv' to persist across different sessions.
•	Page Configuration:
o	The Streamlit app is configured with a wide layout using st.set_page_config(layout="wide").

•	Force Page Refresh:
o	After processing the uploaded file, the app uses streamlit_js_eval to force a page reload, showing the updated results.

3.	Features:
•	Link Extraction:
o	URLs are extracted from the uploaded file using a regular expression defined in link_extract.py.

•	Title Extraction:
o	The titles of HTML documents associated with the extracted URLs are obtained using title_extractor.py.

•	Display and Persistence:
o	The existing links and the newly extracted links are displayed in a table.
o	Duplicates are removed based on the 'URL' column.
o	The results are saved to 'urls.csv' for persistence.

•	User Feedback:
o	The app provides feedback to the user during processing using a toast message and a progress bar.
 

Control Flow Diagram

 
Future Enhancements:
1.	Enhanced Visualizations:
•	Introduce visualizations, such as charts or graphs, to provide users with insights into the link distribution or characteristics.
2.	User Authentication:
•	Implement user authentication mechanisms if needed, especially if there are plans to deploy the application in a multi-user environment.
3.	Advanced Link Analysis:
•	Explore possibilities for more advanced link analysis features, such as categorization or sentiment analysis on linked content.
4.	Integration with External APIs:
•	Consider integrating with external APIs to enrich link data or fetch additional information about the linked content.



Bibliographic References
https://www.assafelovic.com/blog/2016/10/26/url-text-summarizer-using-web-crawling-and-nlp-python
https://docs.streamlit.io/library/api-reference/data/st.data_editor
https://streamlit.io/
https://openai.com/blog/chatgpt

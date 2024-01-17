import re
from pdfminer.high_level import extract_text
from io import StringIO
# Simple regular expression search in the raw text.

def main(text):
    '''
    This regular expression is designed to match URLs (Uniform Resource Locators) in a text. Let's break it down:
    http[s]?:\/\/
    http: Matches the characters "http" literally.
    [s]?: The square brackets denote a character class, and the ? means that the preceding character (in this case, 's') is optional. This allows for both "http" and "https" to be matched.
    :\/\/: Matches the characters "://" literally. The colon and two slashes are common in the beginning of URLs.
    
    (?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+
    (?: ... ): This is a non-capturing group, used to group the enclosed elements without creating a capturing group.
    [a-zA-Z]: Matches any uppercase or lowercase letter.
    [0-9]: Matches any digit.
    [$-_@.&+]: Matches specific characters often found in URLs like $, -, _, @, ., &, +.
    [!*\(\),]: Matches specific punctuation characters often found in URLs like !, *, (, ), and ,.
    (?:%[0-9a-fA-F][0-9a-fA-F]): Matches percent-encoded characters in URLs, such as %20 for a space.
    The + at the end means that one or more of these characters or character sequences should be present in the URL.

    In summary, this regular expression is a pattern for recognizing URLs, taking into account various characters that may be present in URLs, and supporting both "http" and "https" protocols.
    '''

    urls = re.findall(r"http[s]?:\/\/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", text)
    '''
    print(len(urls))
    for url in urls:
        print(url)'''
    return list(urls)

def convert_to_str(file):
    '''
    Method to extract raw text from the uploaded file.
    Accepted PDF and TXT files.
    '''
    if file.name[-3:].lower() == 'pdf':
        text = extract_text(file)
    else:
        stringio = StringIO(file.getvalue().decode("utf-8"))
        text = stringio.read()
    return text
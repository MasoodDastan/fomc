# It is important to acknowledge that much of the steps taken in the process creating `paragraph_processor` and `text_processor` in the `functions.py` file are inspired and indebted to an exceptional blog (https://highdemandskills.com/topic-trends-fomc/), which served as a valuable resource in understanding and implementing the scraping and preprocessing techniques for the FOMC meeting minutes. The blog's contribution has been pivotal in making this project possible and enhancing its quality.

import requests
from bs4 import BeautifulSoup
import re
import spacy

################
####################
#######################

nlp = spacy.load("en_core_web_lg")
nlp.max_length = 1500000 # In case max_length is set to lower than this.


def paragraph_processor(paragraph, allowed_pos):
    """
    Process a paragraph of text to extract relevant lemmatized tokens.

    Parameters:
        paragraph (str): The input paragraph to process.
        allowed_pos (list): A list of allowed parts-of-speech for tokens.

    Returns:
        list: A list of lemmatized tokens that are not punctuation, stop words, and have allowed parts-of-speech.
    """
    # Use Spacy to tokenize the paragraph and lemmatize each token
    return [
        token.lemma_
        for token in nlp(paragraph.lower())
        if not token.is_punct and not token.is_stop and token.pos_ in allowed_pos
        and len(token.lemma_)>2
    ]

#############
################
##################

def text_processor(date, minparalength=200, allowed_pos=["NOUN", "ADJ", "VERB"], raw_text=False):
    """
    Clean and process text from Federal Reserve minutes webpage for a specific date.

    Parameters:
        date (str): The date for which to fetch and process the text (format: YYYYMMDD).
        minparalength (int): The minimum length of a paragraph to consider (default: 200).
        allowed_pos (list): A list of allowed parts-of-speech for tokens (default: ["NOUN", "ADJ", "VERB", 'ADV']).
        raw_text (bool): If True, returns the raw text as a single string without any processing (default: False).

    Returns:
        If raw_text=True:
            str: A string containing the raw text without any processing.
        If raw_text=False:
            tuple: A tuple containing the following elements:
                - list: A list of processed paragraphs, where each paragraph is a list of lemmatized tokens.
                - list: A list containing the number of tokens in each processed paragraph.
                - str: A string containing all the lemmatized tokens joined together with spaces.
                - int: The total number of lemmatized tokens in the entire text.
    """

    # Define URL and extension based on the provided date
    if date == '20080625':
        url = r'https://www.federalreserve.gov/monetarypolicy/fomc'
        ext = r'.htm'
    elif int(date) >= 20071031:
        url = r'https://www.federalreserve.gov/monetarypolicy/fomcminutes'
        ext = r'.htm'
    elif int(date) >= 19960130:
        url = r'https://www.federalreserve.gov/fomc/minutes/'
        ext = r'.htm'
    elif int(date) >= 19950201:
        url = r'https://www.federalreserve.gov/fomc/MINUTES/1995/'
        ext = r'min.htm'
    elif int(date) >= 19930203:
        url1 = r'https://www.federalreserve.gov/fomc/MINUTES/'
        url2 = date[:4]+'/'
        url = url1 + url2
        ext = r'min.htm'
    else: 
        print('Date is invalid')
        return None

    # Fetch the web page content
    res = requests.get(url + date + ext)
    if res.status_code != 200:
        raise ValueError(f"Error occurred while fetching data for {date}")

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(res.content, 'lxml')
    
    # Extract paragraphs from the HTML content and filter based on minimum length
    minutes_para = [re.sub('((a|p)\.m\.)', '', para.get_text().strip()) 
                    for para in soup.select('p') if len(para.get_text()) > minparalength]


    
    if raw_text:
        # Combine paragraphs into a single raw text without any processing
        text = ' '.join(minutes_para).replace('\r\n', '')
        text = re.sub(r'\s+', ' ', text)  
        return text
    
    else:
        # Process each paragraph to obtain relevant lemmatized tokens
        paragraphs = [paragraph_processor(para, allowed_pos) for para in minutes_para]

        # Filter paragraphs based on the number of tokens (minimum of 10 tokens)
        paragraphs = [para for para in paragraphs if len(para) > 10]

        # Calculate the number of tokens in each paragraph
        length_paragraphs = [len(para) for para in paragraphs]

        # Join all lemmatized tokens together with spaces to form a single string
        all_words = ' '.join(' '.join(para) for para in paragraphs)

        # Calculate the total number of tokens in the entire text
        length_all = sum(length_paragraphs)

        return paragraphs, length_paragraphs, all_words, length_all
    
######################
#########################
#############################


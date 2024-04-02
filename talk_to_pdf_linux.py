# Import necessary libraries
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
nltk.download('punkt')
import numpy as np
import warnings
warnings.filterwarnings('ignore')
from PIL import Image 
import pytesseract 
import sys 
from pdf2image import convert_from_path 
import os

# Function to extract text from PDF
def get_pdf_data(user_resp):
    PDF_file = "A_simple_2D_CNN.pdf"
    # Update the poppler_path according to your system
    pages = convert_from_path(PDF_file, 500, poppler_path='/usr/bin/') 
    image_counter = 1
    for page in pages: 
        filename = "page_"+str(image_counter)+".jpg"
        page.save(filename, 'JPEG') 
        image_counter += 1
    filelimit = image_counter-1
    outfile = "out_text.txt"
    # Update the tesseract_cmd according to your system
    pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
    corpus = ''
    for i in range(1, filelimit + 1): 
        filename = "page_"+str(i)+".jpg"
        text = str(((pytesseract.image_to_string(Image.open(filename))))) 
        text = text.replace('-\n', '')     
        corpus += text
    sent_tokens = nltk.sent_tokenize(corpus)
    return sent_tokens

# Function to normalize text
def LemNormalize(corpus):
    remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
    return nltk.word_tokenize(corpus.lower().translate(remove_punct_dict))

# Greeting inputs and responses
GREETING_INPUTS = ["hi", "hello", "hola", "greetings", "wassup", "hey"]
GREETING_RESPONSES=["howdy", "hi", "hey", "what's good", "hello", "hey there"]

# Function to handle greetings
def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

# Function to generate response
def response(user_response):
    user_response = user_response.lower()
    robo_response = ''
    sent_tokens = get_pdf_data(user_response)
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    try:
        idx = vals.argsort()[0][-2]
    except IndexError:
        robo_response = robo_response+"I apologize, I don't understand."
        return robo_response
    flat = vals.flatten()
    flat.sort()
    score = flat[-2]
    if(score == 0):
        robo_response = robo_response+"I apologize, I don't understand."
    else:
        robo_response = robo_response+sent_tokens[idx]
    sent_tokens.remove(user_response)
    return robo_response

# Main function
flag = True
print("GrassBot: Hi! I will answer your queries.Please Ask. If you want to exit, type Bye!")
while(flag == True):
    user_response = input()
    user_response = user_response.lower()
    if(user_response != 'bye'):
        if(user_response == 'thanks' or user_response =='thank you'):
            flag=False
            print("GrassBot: You are welcome !")
        else:
            if(greeting(user_response) != None):
                print("GrassBot: "+greeting(user_response))
            else:
                print("GrassBot: "+response(user_response))       
    else:
        flag = False
        print("GrassBot: Chat with you later !")
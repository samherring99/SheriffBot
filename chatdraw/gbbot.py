import tweepy #https://github.com/tweepy/tweepy
import json
import markovify
import time
import re

import constants
import nltk
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string
import warnings

#Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

def get_formalities_response(formality) :
    if any(remove_punctuation_marks(formality).lower() in remove_punctuation_marks(greet).lower() for greet in constants.GREETING_INPUTS) :
        return random.choice(constants.GREETING_REPLIES)
    elif any(remove_punctuation_marks(formality).lower() in remove_punctuation_marks(thanks).lower() for thanks in constants.THANKS_INPUTS) :
        return random.choice(constants.THANKS_REPLIES)
    else:
        return ""

def get_lemmatized_tokens(text) :
    normalized_tokens = nltk.word_tokenize(remove_punctuation_marks(text.lower()))
    return [nltk.stem.WordNetLemmatizer().lemmatize(normalized_token) for normalized_token in normalized_tokens]

def get_query_reply(query) :
    documents.append(query)
    tfidf_results = TfidfVectorizer(tokenizer = get_lemmatized_tokens, stop_words = 'english').fit_transform(documents)
    cosine_similarity_results = cosine_similarity(tfidf_results[-1], tfidf_results).flatten()
    # The last will be 1.0 because it is the Cosine Similarity between the first document and itself
    best_index = cosine_similarity_results.argsort()[-2]
    documents.remove(query)
    if cosine_similarity_results[best_index] == 0 :
        return "I am sorry! I don't understand you..."
    else :
        return documents[best_index]

def remove_punctuation_marks(text) :
    punctuation_marks = dict((ord(punctuation_mark), None) for punctuation_mark in string.punctuation)
    return text.translate(punctuation_marks)

if __name__ == "__main__" :
    warnings.filterwarnings("ignore")

    try :
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')

    try :
        nltk.data.find('corpora/wordnet')
    except LookupError:
        nltk.download('wordnet')

    corpus = open('corpus.txt', 'r' , errors = 'ignore').read().lower()
    documents = nltk.sent_tokenize(corpus)

    #print('GeebCityBot: My name is GeebCityBot. I will answer your questions. If you want to exit just type: Bye!')
    
    
    
    end_chat = False
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    
    while end_chat == False :
    
        messages = api.list_direct_messages()
        reply_to = []
        message_list = []
            
        unread = True
        counter = 0
        
        for message in messages:
            idnum = message.message_create['sender_id']
                
            u = api.me()
                
                #print(u.id)
                
            if str(u.id) == str(message.message_create['sender_id']):
                    #remove from reply to
                    #print('sent')
                unread = False
            else:
                if unread == True:
                    #print('reply')
                    print(message.message_create['message_data']['text'])
                    message_list.append(message.message_create['message_data']['text'])
                    reply_to.append(idnum)
                    
                    
        reply_to = list( dict.fromkeys(reply_to) )
        print(reply_to)
    
        if reply_to != []:
            for user in reply_to:
                msg = ''
                user_response = message_list[counter]
                counter += 1
            
                if remove_punctuation_marks(user_response).lower() != 'bye':
        
                    formality_reply = get_formalities_response(str(user_response))
                    #print(formality_reply)
                    
                    if formality_reply != "":
                        msg = formality_reply
                    else:
                        msg = get_query_reply(user_response)
                else:
                    msg = 'Bye! Take care ' + random.choice(constants.SWEETS)
                    #send_chat = True
                msg = re.sub(r"http\S+", "", msg)
                print(msg)
                api.send_direct_message(user, msg)
        else:
            print('No new messages!')
            counter = 0
                
        time.sleep(120)

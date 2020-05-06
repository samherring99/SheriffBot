#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import json
import markovify


#Twitter API credentials
consumer_key = "C2fnFi1KVK5xD5ZaRjjr0kqwk"
consumer_secret = "QoXsX9RM8ytNxKjUjt7ZF7osyPv2yXypUnSfxQhAGA9nqunntM"
access_key = "1000528231840141312-vqNwnIpgh4vWTHDF80aLpPTOVYuhyL"
access_secret = "gCawA9doIGKDhKz9B5DpWn65TCcoSfXwh2cHX70xbf44P"

alleamtweets = []
alluserstweets = []
screen_names = ["@eam_tweet"]
#, "@latkedripsensei", "@llill_rock", "@bigfclout", "@qwontrappinout", "@kookoocashewRoo", "@Fawf24188238", "@NmapTrap", "@ByrdSeason", "@semmigotklout"]
tweez = []
model = []
names = []



idnum = 0


def get_all_tweets(screen_names):
    
    #Twitter only allows access to a users most recent 3240 tweets with this method
    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    
    for screen_name in screen_names:
         #initialize a list to hold all the tweepy Tweets
        alltweets = []
        new_tweets = []
        
        #make initial request for most recent tweets (200 is the maximum allowed count)
        new_tweets = api.user_timeline(id = screen_name, count=200)
        idnum = api.get_user(screen_name = screen_name)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #save the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        
        #keep grabbing tweets until there are no tweets left to grab
        while (len(new_tweets) > 1):
            print(len(new_tweets))
            
            #all subsiquent requests use the max_id param to prevent duplicates
            new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest,include_rts=False)
            
            for tweet in new_tweets:
            #print(tweet.user)
            #print(tweet.retweeted_status)
                if not tweet.retweeted and ('@' not in tweet.text):
                    alleamtweets.append(tweet)
                    print(len(alleamtweets))
            
            #save most recent tweets
            alltweets.extend(alleamtweets)
            
            #update the id of the oldest tweet less one
            oldest = alltweets[-1].id - 1
    
            print ("...%s tweets downloaded so far" % (len(alltweets)))
            
            alluserstweets.extend(alltweets)
   
       
    #write tweet objects to JSON
    
    file = open('tweet.json', 'w')
    file2 = open('data.txt', 'w')
    print ("Writing tweet objects to JSON please wait...")
    for status in alluserstweets:
        json.dump(status._json, file , sort_keys = True ,indent = 4)
        
        if status.text != '' and status.text[0] != '@':
            if (status.text[0] != 'R' and status.text[0] != 'h') and (status.text[1] != 'T' and status.text[1] != 't') :
                file2.write(status.text.encode('utf-8'))
                file2.write('.\n\n')
            
        tweez.append(status.text)
    model = markovify.Text(tweez)
    
    for i in range(50):
        #print(model.make_short_sentence(280))
        api.update_status(model.make_short_sentence(140))
        #print(model.make_short_sentence(140))
    
    #close the file
    print ("Done")
    file.close()
    file2.close()

if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets(screen_names)

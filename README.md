# SheriffBot

SheriffBot is a multi-functionality Twitter bot program. Here are the main features of this repo:

1. Tweeting
    
    The SheriffBot can tweet under Twitter Developer credentials, pulling as many tweets as it can from the list of username Strings in the tweet.py file. 
    This mainly made possible with a simple addition of the markovify library for Python for simple Markov-generated tweets. 
    The tweet.py program then posts 50 (default) 280 character generated tweets to the account linked.
    
2. Chatting

    The SheriffBot can chat! Within the gbbot.py file is found the simple workings for text querying with the data.txt file, feel free to change!

3. Drawing

    Ask the SheriffBot to draw a picture for you in the Twitter DMs by typing "draw me a _____" with your desired object. The qureying code for this is located 
    within the gbbpot.py file and utilizes the Google QuickDraw API to pull the binaries for each requested object from the online database.
    
    Watch:
    
    ![Sample1](/utils/object.png)
    
    
    Cat:
    
    ![Sample2](/utils/my_anvil.gif)
    
    
    
    
This program is in EXTREMELY rudimentary stages, so beware when trying to run! Changes will be made as time progresses, but please reach out with any questions or ideas!

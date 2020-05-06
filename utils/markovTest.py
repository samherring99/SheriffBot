#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 17:52:12 2018

@author: Sammy
"""

import markovify
import tweepy, sys, time
import json

models = []

with open('/Users/Sammy/Desktop/Coding/TwitterBot/tweet.json', 'r') as f:
    text = json.loads(f['text'])
    print(text)
        
model = markovify.Text(text)

for i in range(1000):
    print(model.make_short_sentence(140))
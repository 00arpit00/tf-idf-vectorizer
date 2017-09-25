#!usr/bin/env python
# import sys, json
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import urllib2
import base64
import WordsAPI
from pprint import pprint
from random import randrange
import random

import requests
import csv

# word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
count =1
# response = requests.get(word_site)
# WORDS = response.content.splitlines()
f= open('words.txt','r')
WORDS = f.read().split('\n')
print(WORDS)

# # Load the data that PHP sent us
# data = sys.argv[1:]
doc1 =" "
# Send it to stdout (to PHP)

# for k in range(len(t)-1):
# 	if doc1[k]=='.' and doc1[k+1]!=' ':
# 		t[k]=''
# doc1 = ''.join(t)
def question(k,i):
	y =[]
	t = doc1.split('.')
	for ii in t:
		if len(ii)<10:
			pass
		else:
			if i.lower() in ii.lower():
				ans = i
				ii = ii.lstrip(' ')
				ques = ii.lower().split(i)
				ques = '____'.join(ques)
				ques = ques.capitalize()
				return str(k+1),ques,i
def OnClick():
	global doc1,WORDS,count
	doc1= entry.get()
	lectures = doc1.split('\n')
	# print(lectures)
	vectorizer = TfidfVectorizer()
	X = vectorizer.fit_transform(lectures)
	indices = np.argsort(vectorizer.idf_)[::-1]
	features = vectorizer.get_feature_names()
	top_n = 3
	top_features = [features[i] for i in indices[:top_n]]
	# print(top_features)
	final = []
	for k,i in enumerate(top_features):
		
		t= []
		for data in question(k,i):
			t.append(str(data))
		# print(no,ques,str(answer))
		
		
		options = []
		for i in range(3):
			random_index = randrange(0,len(WORDS))
			options.append(WORDS[random_index])
		options.append(t[-1])
		random.shuffle(options)
		t.extend(options)
		# print(t)
		final.append(t)
		t=[]


	with open("output.csv"+str(count), "wb") as f:
	    writer = csv.writer(f)
	    writer.writerows(final)
	count+=1



from tkinter import *

root = Tk()
root.geometry('500x130+100+100')
root.attributes('-topmost', True)
label = Label(root,text='Enter text here')
label.pack(fill=BOTH,pady=5)
entry = Entry(root,width=50)
entry.pack(pady=10)
button = Button(root, text="Submit", command=OnClick)
button.pack(pady=10)
root.mainloop()

				
	
	

















# url = https://en.wikipedia.org/wiki/



# data = resource.read()
# resource.close()
# soup = BeautifulSoup(data)
# print soup.find('div',id="bodyContent").p

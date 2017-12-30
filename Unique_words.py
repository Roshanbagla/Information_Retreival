from BeautifulSoup import BeautifulSoup
import re
import nltk
import os
from collections import Counter

Totalword=[]
wordvalue={}
freqlist={}

#for line in textfile:
#	list_of_stopword = [i.replace('\n','') for i in textfile]			#used to eliminate the \n at the end of each word.

path="/Users/hiteshwagle/Desktop/TestDataset"
all_file = os.listdir(path)
for every_filename in os.listdir(path):
	print ('***************************' +every_filename +'************************************')
	file=open(os.path.join(path,every_filename),'r')
	for line in file:
		soup=BeautifulSoup(line)					#BeautifulSoup produce unicode
 		text = soup.getText()
		tokens = re.split(r'([\d.]+|\W+)',text)			#type of tokens is list
		#print tokens
		my_list = [str(tokens[x]) for x in range(len(tokens))]				#to remove the unicode I've used this.
		if len(my_list)>1:
			for i in my_list:
				if i.isalnum() or i.isalpha():		# use of alpha numberic and alpha character functions
					Totalword.append(i)
#print len(Totalword)
print Totalword


def totalnumber():
	"""This function is used to calculate the total number of words in the collections
	"""
	total = 0
	freq_of_occurrence= Counter(Totalword)
	print "The frequency of occurrence of each word is:  ",freq_of_occurrence
	for k,v in freq_of_occurrence.items():
		total = total+v
		#print k
	return total

first_part=totalnumber()
print 'The total number of the words in the collection:  '+ str(first_part) 			#printing the total number of words.

def unique():											#this function will calculate the unique number of words.
	unique_words = len((sorted(set(Totalword))))
	print "The Number of Unique words: 		"+str(unique_words)

unique()

def top_words():
	""" To calculate the most frequent words in the collections
	"""
	counter = 0
	freq=Counter(Totalword)						#used counter function for that
	for i,j in freq.most_common():				#storing the words in freqlist dictionary
		freqlist[i]=j
	for w in sorted(freqlist, key=freqlist.get, reverse=True):			#printing the elements of dictionary in the reverse order
		print str(w),freqlist[w]
		counter=counter+1
		if (counter>=50):												#prininting the top 50 most frequent words
			break

top_words()

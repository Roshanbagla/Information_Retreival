Totalword = []
freq_list = {}										'''the dictorary storing all the words and frequency'''
word_doc = {}


path_commonwords="/Users/hiteshwagle/Desktop/common_words.txt"
textfile=open('common_words.txt')

for line in textfile:
	list_of_stopword = [i.replace('\n','') for i in textfile]		"""used to eliminate the \n at the end of each word""".

path="/Users/hiteshwagle/Desktop/cranfieldDocs"
allfile=os.listdir(path)
for filename in os.listdir(path):
	print ('***************************' +filename +'************************************')
	file=open(os.path.join(path,filename),'r')
	for line in file:
		Soup=BeautifulSoup(line)					#BeautifulSoup produce unicode
 		text = Soup.getText()
		tokens=re.split(r'([\d.]+|\W+)',text)			#type of tokens is list
		my_list = [str(tokens[x]) for x in range(len(tokens))]				#to remove the unicode I've used this.
		if len(my_list)>1:
			for i in my_list:
				if i.isalnum() or i.isalpha():		# use of alpha numberic and alpha character functions
					if i not in list_of_stopword and i !='a':
						Totalword.append(i)

					else:
						tokens.remove(i)


for i in Totalword:													#code for inverted index
	count = 1
	if i not in freq_list:
		freq_list[i] = count
	else:
		freq_list[i]+=1
count = Counter(Totalword)

for key,values in count.most_common():
	print key,values,'times'

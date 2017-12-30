def mapping(list):
	"""mapping the each document with all the words in it and storing
		the count of each word"""

	count=Counter(list)
	for key,value in count.most_common():
		freq_list[key]=value
	abc=[]
	abc.append(filename)
	abc.append(freq_list)								#combined list of all the documents after mapping
	map_list.append(abc)
	abc=[]

summ = 0
token_list = []
map_list = []
freq_list = {}
path_commonwords="/Users/hiteshwagle/Desktop/common_words.txt"
textfile=open('common_words.txt')

"""tokenisation"""
for line in textfile:
	list_of_stopword = [i.replace('\n','') for i in textfile]			#used to eliminate the \n at the end of each word.

path="/Users/hiteshwagle/Desktop/cranfieldDocs"
allfile = os.listdir(path)
length= len(allfile)
for filename in allfile:
	print ('***************************' +filename +'************************************')
	file=open(os.path.join(path,filename),'r')
	for line in file:
		Soup=BeautifulSoup(line)					#BeautifulSoup produce unicode
 		text = Soup.getText()
		tokens = re.split(r'([\d.]+|\W+)',text)
		my_list = [str(tokens[x]) for x in range(len(tokens))]				#to remove the unicode I've used this.
		if len(my_list)>1:
			for i in my_list:
				if i.isalnum() or i.isalpha():		# use of alpha numberic and alpha character functions
					if i not in list_of_stopword and i !='a':
						token_list.append(i)
					else:
						tokens.remove(i)
	new_list = token_list

""" tokenization end"""

mapping(new_list )
#score(map_list)
token_list = []
freq_list = {}					#to empty the list and dictionary


single_keylist = []
double_keylist = []
third_keylist = []
print 'Enter the keyword(s)'
keyword=map(str,raw_input().strip().split(" "))				#one word input
start_time = time.time()
print 'the input is ', keyword
if len(keyword)<=1:
	for i in range(length):
		all_key=map_list[i][1]
		#print all_key
		for eachvalue in keyword:										#
			if eachvalue in all_key:
				temp = []
				temp.append(map_list[i][0])
				temp.append(map_list[i][1][eachvalue])
				single_keylist.append(temp)
				temp = []

	single_keylist = sorted(single_keylist, key=operator.itemgetter(1), reverse=True)
	single_keylist = single_keylist[:10]
	for x,y in single_keylist:
		print x,y

""" If user enter 2 input"""

elif (len(keyword)== 2):
	for i in range(length):
		all_key = map_list[i][1]
		#print all_key
		for n in keyword:
			if n in all_key:
				summ = summ+map_list[i][1][n]
		temp = []
		temp.append(map_list[i][0])
		temp.append(summ)
		double_keylist.append(temp)
		summ = 0
		temp = []
	double_keylist=sorted(double_keylist, key=operator.itemgetter(1), reverse=True)
	double_keylist=double_keylist[:10]
	for x,y in double_keylist:
		print x,y

""" If user enter 3 input"""

elif(len(keyword) == 3):
	for i in range(length):
		all_key = map_list[i][1]
		#print all_key
		for n in keyword:
			if n in all_key:
				summ = summ+map_list[i][1][n]
		temp=[]
		temp.append(map_list[i][0])
		temp.append(summ)
		third_keylist.append(temp)
		summ = 0
		temp = []
	third_keylist=sorted(third_keylist, key=operator.itemgetter(1), reverse=True)
	third_keylist=third_keylist[:10]
	for x,y in third_keylist:
		print x,y
print("--- %s seconds ---" % (time.time() - start_time))

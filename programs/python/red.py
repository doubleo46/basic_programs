
def conv(word, index):
	if index == len(word):
		print(' '.join(word))
		return 
	if word[index] == 'x':
		word[index] = "0"
		conv(word, index+1)
		word[index] = "1"
		conv(word, index+1)
		word[index] = 'x'
	else:
		conv(word, index+1)

print("Start")
numbs = list("100x001x001x")
conv(numbs,0)


	

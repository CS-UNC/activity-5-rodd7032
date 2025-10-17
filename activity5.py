words_file = open('CROSSWD.txt','r')

def more_than_20(file):
    data = open(file, 'r') # open any file
    for word in data:
        if len(word.strip()) > 20: #len gets length of word. stripping of extra spaces that might mess up stuff.
            print(word)

#do this instead
words = []
data = open(file, 'r')
words = [x.strip() for x in data if len (x.strip()) > 20]
print(more_than_20('CROSSWD.txt'))

def has_no_e(word):
    if word: #has no e
        return True
    else:
        return False

def uses_only(word,letters):
    return

def all_uses_only(file, letters):
    return
'''
#print([x for x in dir(words_file) if '_' != x[0]]) #all the x's for x in the file if underscore isnt first character.

#data = [1,3,2,8,5,6,10]
#print([2*x for x in data if x%2 == 0]) #ex

print(words_file.readline()) 
words = []

for line in words_file:
    print(line.strip()) #instead of read line. this thing stops the loop cuz read line is infinite. 
    #words.append(line) # /n indicates new line. the strip will remove anything extra.

print(words) '''
from pyvi import ViTokenizer

stopWords = []
file = open(r'C:\Users\ASUS\Desktop\Class\stopWords.txt', encoding='utf8')
readline = file.readlines()
file.close()
for i in range(len(readline)):
    #readline[i] = readline[i].replace(' ', '_')
    readline[i] = ViTokenizer.tokenize(readline[i])
    readlines = readline[i].split()
    #print(type(readlines), readlines)
    stopWords += readlines
print(stopWords)

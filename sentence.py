while True:
    text = input('Iveskite sakini: ')
    words = text.split()
    if len(words) < 5:
        print('Iveskite bent 5 žodžius!\n')
        continue
    else:
        break

maxLenWord = words[0]
maxIndex = 0
minLenWord = words[0]
minIndex = 0

for i in words:
    if len(i) > len(maxLenWord):
        maxLenWord = i
        maxIndex = words.index(i)
    if len(i) < len(minLenWord):
        minLenWord = i
        minIndex = words.index(i)

words[maxIndex] = minLenWord
words[minIndex] = maxLenWord

newWord = ' '.join(words)

print('Rezultatas: ' + newWord)
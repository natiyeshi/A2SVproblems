# Enter your code here. Read input from STDIN. Print output to STDOUT


n = int(input())
counter = {}
words = []
for i in range(n):
  word = input()
  
  if word in counter:
    counter[word] += 1
  else:
    counter[word] = 1
    words.append(word)
    
print(len(words))
print (' '.join([str(counter[word]) for word in words]))   

from itertools import product
import string 

min_lenght = int(input("enter minimum lenght :"))
max_lenght = int(input("enter maximum lenght :"))

wordlist_lenght = 0

charater = string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation

folder = open("wordlist.txt" , "w")

for i in range(min_lenght , max_lenght+1):
	for j in product(charater , repeat=i):
		word = "".join(j)
		folder.write(word)
		folder.write("\n")
		wordlist_lenght=  wordlist_lenght + 1

print("wordlist lenght : {}".format(wordlist_lenght))
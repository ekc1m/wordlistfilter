wordlist = input("Which wordlist (use exact path): ")
encodetype = input("Which encoding (you can find the encoding of your file with command 'file foo.txt'): ")
filtered_wordlist = input("New name for the wordlist: ")
length_words = int(input("Length of words: "))

with open(f"{wordlist}", encoding=f"{encodetype}", errors="ignore") as f:
	words = f.readlines()

length = [word.strip() for word in words if len(word.strip()) == length_words]

with open(f"{filtered_wordlist}", "w") as f:
	f.write("\n".join(length))
print(f"{filtered_wordlist} created")
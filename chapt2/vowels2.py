vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Enter a word to find the vowels: ")
found = []
for letter in word:  # iterates through each letter in word
    if letter in vowels:  # if the letter is a vowel
        if letter not in found:  # if that vowel is not in the found list
            found.append(letter)  # add letter to found list
for vowel in found:  # iterate through found list
    print(vowel)  # and print

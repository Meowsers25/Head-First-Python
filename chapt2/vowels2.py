vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Enter a word to find the vowels: ")
found = []
for letter in word:  # iterates through each letter in word
    if letter in vowels:  # if the letter is a vowel
        if letter not in found:  # if that vowel is not in the found list
            found.append(letter)  # add letter to found list
for vowel in found:  # iterate through found list
    print(vowel)  # and print

nums = [1, 2, 3, 4]
print(nums)
nums.remove(4)  # .remove() removes a specific value
print(nums)


nums2 = [1, 2, 3, 4]
# print(nums2.pop())  # can pop() an index value
removed = nums2.pop() + 4  # .pop() can be stored in a variable and reused
print(removed)


nums2.extend([5, 6, 7])  # .extend([]) adds a list wheras .append()
print(nums2)  # takes single value

nums2.insert(0, -1)  # .insert() inserts value at specified location (0 here)
nums2.insert(4, 'four')
print(nums2)

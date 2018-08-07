phrase = "Don't panic!"
plist = list(phrase)  # puts phrase into a list
print(phrase)
print(plist)
for i in range(4):  # iterates 4 times
    plist.pop()  # pops off the last 4 characters ! c i n
# print(plist)
plist.pop(0)  # pops off the first character D
# print(plist)
plist.remove("'")  # removes the apostrophe; note the spacing! Threw an error
# print(plist)
plist.extend([plist.pop(), plist.pop()])  # this pops off the last two characters
# print(plist) # then adds(extends them back on , basically reversed them)
plist.insert(2, plist.pop(3))  # here we pop off the blank space and insert it where we want
# print(plist)
new_phrase = ''.join(plist)  # join the list back into a string;no space between quotations
print(plist)
print(new_phrase)

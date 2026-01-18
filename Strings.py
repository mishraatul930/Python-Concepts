str1 = "String1"
str2 = 'String2'
print(str1)
print(len(str1))
print(str2)

str3 = 'I am "Atul", I am a boy'
print(str3)
print(str1[5])

str4 = '''Loopnig through the strings
using FOR Loops'''

for char in str4:
    print(char)

names = "atul,mandal!!!!"
print(len(names))
print(names[0:4])
print(names[:4])
#below line actually mean names[0:-3]
print(names[0:len(names)-3])
#below line actually means names[len(names)-3:len(names)-1]
print(names[-3:-1])
#Strings are immutable
print(names.upper())
print(names.lower())
print(names.strip("!"))
print(names.replace("Atul", "Ankit"))
print(names.split(","))
print(names.find("Mandal"))
print(names.count("a"))
print(names.startswith("Atu"))
print(names.endswith("!!!!"))
#index method is same as find method but it raises error if substring not found
print(names.index("Mandal"))
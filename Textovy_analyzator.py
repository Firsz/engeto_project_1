'''
author = Mikuláš Marsovszky
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

separator = "-" * 60
graph = "*"
USER = {"bob": 123, "ann": "pass123", "mike": "password123", "liz": "pass123"}

# User and password verification - 3 attempts
for attempt in range(1, 4):
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    if str(USER.get(username)) == password:
        print(
            separator,
            f"Welcome to the app, {username}!".center(len(separator)),
            f"We have 3 texts to be analyzed.".center(len(separator)),
            separator, sep="\n")
        break
    elif attempt == 3:
        print(
            separator,
            f"Wrong password or username! Please contact your support team.".center(len(separator)),
            separator, sep="\n")
        exit()
    elif str(USER.get(username)) != password:
        print(
            separator,
            f"Incorrect password or username. Try again.".center(len(separator)),
            separator, sep="\n")
        continue

# Text selection
select = input("Enter a number btw. 1 and 3 to select: ")
print(separator)
if select.isnumeric() == False or int(select) not in range(1, 4):
    print(f"Incorrect selection.".center(len(separator)),
          separator, sep="\n")
    exit()
else:
    select = TEXTS[int(select) - 1].split()

# Words and numbers search + print
titlecase = []
uppercase = []
lowercase = []
numeric = []

for word in select:
    if word.istitle():
        titlecase.append(word)
    elif word.isupper():
        uppercase.append(word)
    elif word.islower():
        lowercase.append(word)
    elif word.isnumeric():
        numeric.append(int(word))

print(
    f"There are {len(select)} words in the selected text.",
    f"There are {len(titlecase)} titlecase words.",
    f"There are {len(uppercase)} uppercase words.",
    f"There are {len(lowercase)} lowercase words.",
    f"There are {len(numeric)} numeric strings.",
    f"The sum of all the numbers {sum(numeric)}",
    separator, sep="\n")

# Graph
lenght = {}
for word in select:
    word = word.strip(".,-")
    if len(word) not in lenght:
        lenght.setdefault(len(word), 1)
    else:
        lenght[len(word)] += 1

print(
    f"LEN|\tOCCURENCES\t\t|NR.",
    separator, sep="\n")

for printing in range(1, max(lenght) + 1):
    if printing in lenght:
        print(f"{printing: >3}|{graph * lenght[printing]: <20}|{lenght[printing]}")

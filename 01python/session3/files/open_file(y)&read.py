# prin file content lines
with open(r"session3\files\y.py") as ry:
    rd=ry.readlines()
    print(rd)
    print(type(rd))
    print(len(rd))

print("-------------------------------")  

# print file content words
with open(r"session3\files\y.py") as ry:
    rd=ry.read()
    print(rd)
    print(type(rd))
    rd_word=rd.split()
    print(rd_word)
    print(len(rd_word))

with open(r"session3\files\y.py",'w') as ry:
    ls=["#I'm studying at cairo university"]
    rd=ry.write("".join(ls))

    


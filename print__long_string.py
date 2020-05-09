s = "hello this is a really really long string"

strl = list(s)
mystr = str()
myl = []

for i in strl:
    if i != " ":
        mystr += i
    elif i == " ":
        myl.append(mystr)
        mystr = ""
for i in myl:
    print(i)

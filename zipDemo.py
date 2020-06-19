name = ("Saurabh","suman","vipul","Saurabh")
comp = ("Dell","HP","Ms","Dell")

zipped = list(zip(name, comp))
print(zipped)

zipped = set(zip(name, comp))
print(zipped)

zipped = dict(zip(name, comp))
print(zipped)

zipped = zip(name, comp)
for (a,b) in zipped:
    print(a,b)
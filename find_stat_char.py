f = open("stat_char.txt", "r")
for i in range(20):
print(f.readline())
curr = f.readline()
while curr != "Episode 2":
    if curr[:2] != "Ep" and curr != "":
        print (curr)
    curr = f.readline()

f.close()
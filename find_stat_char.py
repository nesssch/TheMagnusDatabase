f = open("stat_char.txt", "r", encoding="utf8")

def format_line(line:str):
    line = line.lstrip()
    comma = line.find(",")
    return line[:comma]

def get_ep_1():
    test_arr = []
    curr = f.readline()
    count = 0
    while curr != "Episode 2\n":
        if curr[:2] != "Ep" and curr != "\n":
            #print (curr)
            count += 1
            test_arr.append(format_line(curr))
        curr = f.readline()
    return test_arr

print(get_ep_1())
# lines = f.readlines()
# print(lines[:20])
f.close()
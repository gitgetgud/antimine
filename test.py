ar=[[' ', ' ', ' ', '1', 'X', 'X', 'X', 'X', 'X'],
[' ', ' ', ' ', '1', 'X', 'X', 'X', 'X', 'X'],
[' ', '1', '1', '2', 'X', 'X', 'X', 'X', 'X'],
[' ', '1', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
[' ', '2', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
[' ', '1', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
[' ', '1', '1', 'X', 'X', 'X', 'X', 'X', 'X'],
[' ', ' ', '1', 'X', 'X', 'X', 'X', 'X', 'X'],
[' ', ' ', '1', 'X', 'X', 'X', 'X', 'X', 'X']]


res = [[0 for x in range(9)] for y in range(9)]

def check(num):
    if num<0 or num>8:
        return False
    return True

def count(x,y):
    res={
        "count":0,
        "coords":[],
        "mine":.0,
        "safe":.0,
    }
    for ysp in range(-1,2):
        for xsp in range(-1,2):
            if check(x+xsp) and check(y+ysp):
                if ar[x+xsp][y+ysp] == "X":
                    res["count"]+=1

    return res


for y in range(0,9):
    for x in range(0,9):
        if ar[x][y] in [" ","X"]:
            continue

from tqdm import tqdm
import time
import random
server_map = open('out.txt').read().replace("g0","  ")
player_map = server_map.replace("^0","$0")
w, l, server_map = server_map.split("/")
w2, l2, player_map = player_map.split("/")
assert w == w2 and l == l2 and len(server_map) == len(player_map)
w, l = int(w), int(l)

grid = [[] for i in range(l)]
for i in tqdm(range(len(server_map)//2), unit="cells"):
    idx = slice(2*i, 2*i+2)
    server, player = server_map[idx], player_map[idx]
#    if server == "^0":
#        assert player_map[2*i:2*i+2] in [";3", "$0"]
#    else:
#        assert player == server
    grid[i//w].append(player)

### BOARDS INITIALIZED ###

values = []
with open('settings.txt','r') as settings:
    for value in settings:
        values.append(int(value))

for i in range(10, len(grid[3]) - 16, 14):
    if values[i//14] == 0:
        grid[3][i] = ";3"
    else:
        grid[3][i] = ";3"

#with open('gatevalues.txt', 'w') as gates:
#    for gate in range(616):
#        for i in range(616):
#            gates.write(str(["  ", ";3"].index(grid[14*i + 16 + gate*7][14 * gate + 8])))
#        gates.write("\n")

### SETTINGS APPLIED ###

print("Grid variable made")
print(f"Dimensions: rows = {len(grid)}, char per row = {len(grid[0])}")
input("Continue to results?")


def neighs(r,c):
    return sum(grid[r-1+i//3][c-1+i%3] == "$0" for i in range(9))

qq = {"$0": "S", ";3": " ", "g0": "."}

align = 'r'
skip = 0

for i in range(l):
    for j in range(w):
        if grid[i][j] == ";3" and neighs(i,j) == 1:
            grid[i][j] = "$0"
    # Below code in loop gives me more control over what I see during the printing of the loop, used for debugging
    if skip==0:
        if align=="r":
            print(i, end="")
            answer = input(grid[i][-45:])
        else:
            print(i,end="")
            answer = input(grid[i][:45])
        if answer:
            if answer=="r":
                align = "r"
            elif answer == "l":
                align = "l"
            else:
                try:
                    skip = int(answer)
                except:
                    continue
    else:
        if align=="r":
            print(i,end="")
            print(grid[i][-45:])
        else:
            print(grid[i][:45]) 
        skip -= 1
                
#with open('default.txt', 'w') as default:
#    default.write("1") #The first row's output is formatted differently and doesn't align with the rest, so I manually added the correct default output
#    for i in range(615):
#        default.write(str([";3", "$0"].index(grid[4344 + 14*i][-11])))

if grid[-4][-4] == "$0":
    bitstring = ""
    for i in range(len(server_map)//2): # shut up i know it's inefficient, deal with it.
        idx = slice(2*i, 2*i+2)
        if server_map[idx] == "^0":
            bitstring += str([";3", "$0"].index(player_map[idx]))
    print("Correct! Your flag is amateursCTF{" + bytes.fromhex(hex(int(bitstring, 2))[2:]).decode() + "}")

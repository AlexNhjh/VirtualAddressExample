virtualAddresses = []
pages = 1

def addToMemory(input: str) -> str:
    global pages
    pageTable = {
        15: ["000", 0],
        14: ["000", 0],
        13: ["000", 0],
        12: ["000", 0],
        11: ["111", 0],
        10: ["000", 0],
        9: ["101", 0],
        8: ["000", 0],
        7: ["000", 0],
        6: ["000", 0],
        5: ["011", 0],
        4: ["100", 0],
        3: ["000", 0],
        2: ["110", 0],
        1: ["001", 0],
        0: ["010", 1],
    }

    res = 0
    multiplier = 3
    for i in range(len(input[0:4])):
        res += int(input[i]) ** multiplier
        multiplier -= 1

    if pages == 8:
        virtualAddresses.pop()
        pages -= 1
    virtualAddresses.append(["page = " + str(pages), pageTable[res][0] + input[4:]])
    pages += 1

addToMemory("00100000000000100")
# addToMemory("11110000000000100")
# addToMemory("10110000000000100")
# addToMemory("10010000000000100")
# addToMemory("10010000000000100")
# addToMemory("10110000000000100")
# addToMemory("11010000000000100")
# addToMemory("00010000000000100")
# addToMemory("00010000000000100")

for address in virtualAddresses:
    print(str(address))
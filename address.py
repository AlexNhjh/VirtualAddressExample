# Hardcoded virtual address
virtual_address = "001000000000100"
# Table to convert virtual memory to physical
page_table = {
    15: ["000", 0],
    14: ["000", 0],
    13: ["000", 0],
    12: ["000", 0],
    11: ["111", 1],
    10: ["000", 0],
    9: ["101", 1],
    8: ["000", 0],
    7: ["000", 0],
    6: ["000", 0],
    5: ["001", 1],
    4: ["100", 1],
    3: ["000", 1],
    2: ["110", 1],
    1: ["001", 1],
    0: ["010", 1],
}

# Creates a string of the first four bits from virtual address
index = virtual_address[0:4]
# Reverse string for the first four bits
index = index[::-1]

# Binary to decimal converter
bin_to_int = 0
for i in range(len(index)):
    if int(index[i]) == 1:
        bin_to_int += pow(2, i)

# Retrieves first three bits of the physical address
if bin_to_int in page_table:
    if page_table[bin_to_int][1] == 1:
        physical_address = page_table[bin_to_int][0] + virtual_address[3:]
        print(f"virtual address: {virtual_address}\nphysical_address: {physical_address}")
    else:
        print("Page not available")










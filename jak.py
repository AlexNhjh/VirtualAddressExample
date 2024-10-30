page_table = {
  15: ("000", 0),
  14: ("000", 0),
  13: ("000", 0),
  12: ("000", 0),
  11: ("111", 1),
  10: ("000", 0),
  9: ("101", 1),
  8: ("000", 0),
  7: ("000", 0),
  6: ("000", 0),
  5: ("011", 1),
  4: ("100", 1),
  3: ("000", 1),
  2: ("110", 1),
  1: ("001", 1),
  0: ("010", 1)
  }
virtual_address = "0010000000000100"
physical_address = ""

page_index = int(virtual_address[:4], 2)  
physical_address = page_table[page_index][0] + virtual_address[4:]
print(f"Physical Address: {physical_address}")
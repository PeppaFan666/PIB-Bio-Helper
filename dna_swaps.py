def swap_dna(m):
  m.lower()
  m = m.split()
  for k in range(len(m)):
    i = m[k]
    if i == "t":
      i = "a"
    elif i == "a":
      i = "t"
    if i == "c":
      i = "g"
    elif i == "g":
      i = "c"
    m[k] = i
    v = ""
  for i in m:
    v += str(i)
  return v
  
def swap_rna(m):
  m.lower()
  m = m.split()
  for k in range(len(m)):
    i = m[k]
    if i == "t":
      i = "a"
    elif i == "a":
      i = "u"
    if i == "c":
      i = "g"
    elif i == "g":
      i = "c"
    m[k] = i
  v = ""
  for i in m:
    v += str(i)
  return v
def start():
  m = input("Please Enter a dna code separated by spaces\nie a t c a g rather than atcag\n")
  y = input("Translate to 1. RNA or 2. DNA?\n")
  v= ""
  if y == "RNA" or y == "1":
    v =swap_rna(m)
  if y == "DNA" or y == "2":
    v = swap_dna(m)
  print("\n\n\nResult:\n" + str(v))

def foil(allel):
  arr = allel.split()
  names = []
  names.append(arr[0] + arr[2])
  names.append(arr[0] + arr[3])
  names.append(arr[1] + arr[2])
  names.append(arr[1] + arr[3])
  return names
def internal_foil(allel):
  arr = allel.split()
  names = []
  names.append(arr[0] +" " + arr[2])
  names.append(arr[0] + " " + arr[3])
  names.append(arr[1] + " " + arr[2])
  names.append(arr[1] +" " +  arr[3])
  return names
def do_calc(allel1,allel2):
  arr = allel1.split()
  arr2 = allel2.split()
  return arr[0] + " " + arr2[0] + " " + arr[1] + " " + arr2[1]
def calculate_cross(genes1,genes2):
  arr = []
  for i in range(len(genes1)):
    for j in range(len(genes2)):
      s = do_calc(genes1[i],genes2[j])
      arr.append(s)
  return arr

def count_ratio(arr):
  dic = {}
  used = []
  for i in range(len(arr)):
    if not arr[i] in used:
      dic[arr[i]] = 1
      used.append(arr[i])
    else:
      dic[arr[i]] += 1
  return dic

def my_sort(arr):
  if arr[0].islower():
    t = arr[0]
    t2 = arr[1]
    arr[0] =t2 
    arr[1] = t
  if arr[2].islower():
    t = arr[2]
    t2 = arr[3]
    arr[2] = t2
    arr[3] = t
  return arr

def order_dominants(arr):
  r = []
  for i in range(len(arr)):
    n = arr[i].split()
    n = my_sort(n)  
    d = ""
    for i in n:
      d += i
    r.append(d)
  return r
      

name = []
name2 = []
internal = []
internal2 = []
result = []

def do():
  t = input("enter the parent allel, add a space between each letter\nie BbEe to B b E e\n\n")
  name = foil(t)
  internal = internal_foil(t)
  #print(name)
  t = input("\n\nenter the parent allel,same convention as last time please\nie BbEe to B b E e\n\n")
  name2 = foil(t)
  internal2 = internal_foil(t)
  #print(name2)
  result = calculate_cross(internal,internal2)
  result = order_dominants(result)
  print("\n\n\n\n\n")
  print(result[0] + " " + result[1] + " " + result[2] +" " + result[3])
  print(result[4] + " " + result[5] + " " + result[6] +" " + result[7])
  print(result[8] + " " + result[9] + " " + result[10] +" " + result[11])
  print(result[12] + " " + result[13] + " " + result[14] +" " + result[15])
  print("\n\n\n\n\n")
  print("ratios:\n\n")
  print(count_ratio(result))

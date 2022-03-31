def square(m,f):
  m = m.split()
  f = f.split()
  arr = []
  arr.append(m[0] +" " +f[0])
  arr.append(m[1] + " "+ f[0])
  arr[0] = my_sort(arr[0])
  arr[1] = my_sort(arr[1])
  arr.append(m[0] + "y")
  arr.append(m[1] + "y")
  return arr


def my_sort(arr):
  arr = arr.split()
  if arr[0].islower():
    t = arr[0]
    t2 = arr[1]
    arr[0] =t2 
    arr[1] = t
  d = ""
  d = arr[0] + arr[1]
  return d

def is_codominant(arr,index):
  male_rec =0
  male_dom =0
  female_rec =0
  female_dom = 0
  codom = 0
  for i in arr:
    if i[0].isupper() and i[1].islower():
      if i[1] == "y":
        male_dom += 1
      else:
        codom += 1
    if i[0].islower() and i[1] == "y":
      male_rec += 1
    if i[0].isupper() and i[0] == i[1]:
      female_dom += 1
    if i[0].islower() and i[0] == i[1]:
      female_rec += 1
    
    l = [female_dom,female_rec,male_dom,male_rec]
    l[index] = codom
  return l

def internal_print_chances(arr):
  male_rec =0
  male_dom =0
  female_rec =0
  female_dom = 0
  for i in arr:
    if i[0].isupper():
      if i[1] == "y":
        male_dom+=1
      else:
        female_dom +=1
    else:
      if i[1] == "y":
        male_rec += 1
      else:
        female_rec +=1
  return [female_dom,female_rec,male_dom,male_rec]
  
    

def print_chances(arr):
  male_rec =0
  male_dom =0
  female_rec =0
  female_dom = 0
  rec = 0
  dom = 0
  for i in arr:
    if i[0].isupper():
      if i[1] == "y":
        male_dom+=1
        dom+=1
      else:
        female_dom +=1
        dom +=1
    else:
      if i[1] == "y":
        male_rec += 1
      else:
        female_rec +=1
      rec+=1
        

  total = rec + dom
  return "Total Dominant Chance: " + str(dom/total * 100) + "%\nTotal Reccesive Chance: " + str(rec/total*100)  + "%\nTotal Male Dominant Chance: " + str(male_dom*2/total*100) + "%\nTotal Male Reccesive Chance: " + str(male_rec/total*2*100) + "%\nTotal Female Dominant Chance: " + str(female_dom/total*2*100)  + "%\nTotal Female Reccesive Chance: " + str(female_rec/total*2*100) + "%"
  

  

def start():
  m= input("Please enter the mothers genes, disregard x's\nie not xr and instead just r\nput spaces between each charected\n ie R R instead of RR\n")
  f = input("enter fathers genes, same format as mothers, do not include Y\n")
  a2 = m
  a3 = a2.split()
  a3.pop(0)
  a3 = a3[0]
  
  a1= f
  v = square(m,f)
  a2.split()
  print("\n\n\nResult:\n  " + str(a2[0]) + "  " + str(a3) +"\n"+ str(a1[0])+ " " + str(v[0]) + " "+ str(v[1]) +"\n" + "y"+ " " + str(v[2])+ " " + str(v[3]))
  print("\n\n\n\n\n" + print_chances(v))
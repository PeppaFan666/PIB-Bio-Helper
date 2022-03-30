def internal_punnet(al1,al2):
  al1 = al1.split()
  al2 = al2.split()
  arr = []
  arr.append(al1[0] + " " + al2[0])
  arr.append(al1[0] + " " + al2[1])
  arr.append(al1[1] + " " + al2[0])
  arr.append(al1[1] + " " + al2[1])
  for i in range(len(arr)):
    j = arr[i]
    arr[i] = my_sort(j.split())
  return arr


def my_sort(arr):
  if arr[0].islower():
    t = arr[0]
    t2 = arr[1]
    arr[0] =t2 
    arr[1] = t
  d =""
  d = arr[0] + arr[1]
  return arr

def count_ratio(arr):
  doms = 0
  recs = 0
  for i in arr:
    #i = i.split()
    if i[0].isupper():
      doms += 1
    else:
      recs += 1
  return [doms,recs]


      
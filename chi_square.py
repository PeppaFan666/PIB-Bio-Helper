import punnets
import dihybrid
import sex_linked

degrees_of_freedom = {
  "1": 3.84,
  "2" : 5.99,
  "3" : 7.81,
  "4" : 9.49
}

tab = [[0 for x in range(3)] for y in range(6)] 


def make_chart(t):
  tab[0].clear()
  t = t.split()
  for m in t:
    tab[0].append(m)
  tab[0].append("total")

def add_observed(t):
  tab[1].clear()
  t = t.split()
  for m in t:
    tab[1].append(m)
  v = 0
  for i in tab[1]:
    v += int(i)
  tab[len(tab[0])][1] = str(v)

def add_expected(ratio):
  tab[2].clear()
  total = int(tab[len(tab[0])][1])
  sum = ratio[0] + ratio[1]
  frac = total / sum
  domsum = frac * ratio[0]
  recsum = frac * ratio[1]
  tab[2].append(domsum)
  tab[2].append(recsum)
  tab[2].append(domsum + recsum)
  
def add_expected_dihybrid(ratio):
  tab[2].clear()
  total = int(tab[len(tab[0])][1])
  sum = ratio[0] + ratio[1] + ratio[2] + ratio[3]
  frac = total / sum
  domdomsum = frac * ratio[0]
  domrecsum = frac * ratio[1]
  recdomsum = frac * ratio[2]
  recrecsum = frac * ratio[3]
  tab[2].append(domdomsum)
  tab[2].append(domrecsum)
  tab[2].append(recdomsum)
  tab[2].append(recrecsum)
  tab[2].append(domdomsum + domrecsum+recdomsum+recrecsum)
  

def OMinusE():
  tab[3].clear()
  for i in range(len(tab[0])-1):
    v = int(tab[1][i]) - int(tab[2][i])
    tab[3].append(str(v))
    
def OMinusESquared():
  tab[4].clear()
  for i in range(len(tab[0])-1):
    tab[4].append(pow(int(tab[3][i]),2))

def finals():
  tab[5].clear()
  for i in range(len(tab[0])-1):
    tab[5].append(str(int(tab[4][i])/int(tab[2][i])))
    v = 0
  for i in range(len(tab[0])-1):
    v += float(tab[5][i])
  tab[5].append(str(v))

def get_print():
  t1 = str(tab[0])
  t2 = str(tab[1])
  t3 = str(tab[2])
  t4 = str(tab[3])
  t5 = str(tab[4])
  t6 = str(tab[5])
  return "Phenotypes: " + t1 + "\nObserved: " + t2 + "\nExpected: " + t3 + "\nO Minus E: " + t4 + "\nO Minus E Squared: " + t5 + "\nO Minus E Square over E: " + t6
    
def start():
  print("\n\n\n\n\n")
  t =input("enter phenotypes, separated by spaces\n ie yellow green\n")
  make_chart(t)
  t = input("enter observations, seperated by spaces\n")
  add_observed(t)
  t = input("enter parent 1 allels(with spaces)\nif trait is codominant make the second dominant lowercase\nie if the trait is BO and its codominant instead make it B o\n")
  al1 = t
  t = input("enter parent 2 allels\nsame convention as last time, only one letter, do not include y chromosome if trait is sex linked\n")
  al2 = t
  t = input("Is the trait sex-linked? Y/N\n")
  ratio = None
  if t == "Y":
    t = input("Is the trait codominant? Y/N\n")
    if t == "Y":
      i = input("What group is the codominant (enter a number)\n")
      ratio = sex_linked.is_codominant(sex_linked.square(al1,al2),int(i)-1)
    else:
      ratio = sex_linked.internal_print_chances(sex_linked.square(al1,al2))
    add_expected_dihybrid(ratio)

  
  elif len(al2.split()) < 3:
    exp = punnets.internal_punnet(al1,al2)
    ratio = punnets.count_ratio(exp)
    add_expected(ratio)
  else:
    ratio = dihybrid.internalcross(al1,al2)
    add_expected_dihybrid(ratio)
  OMinusE()
  OMinusESquared()
  finals()
  dof = len(tab[0]) - 2
  CDOF = degrees_of_freedom[str(dof)]
  print(get_print())
  SDOF = str(CDOF)
  if float(tab[5][len(tab[5])-1]) > CDOF:
    print("\n\n")
    print(SDOF + " < " + tab[5][len(tab[5])-1] + "\nNot a good fit.")
  else:
    print("\n\n")
    print(tab[5][len(tab[5])-1] + " < " + SDOF + "\nGood fit!")
  

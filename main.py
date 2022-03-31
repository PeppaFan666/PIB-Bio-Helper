import chi_square
import dihybrid
import punnets
import dna_swaps
import sex_linked

t = input("What do you want to do\n1. Chi Square\n2. Dihybrid Cross\n3. Punnet Square\n4. Dna Swap\n5. Sex Linked\n")
if t == "Chi Square" or t == "1":
  chi_square.start()
elif t == "Dihybrid Cross" or t == "2":
  dihybrid.do()
elif t == "Punnet Square" or t =="3":
  punnets.start()
elif t == "Dna Swap" or t == "4":
  dna_swaps.start()
elif t == "Sex Linked" or t == "5":
  sex_linked.start()
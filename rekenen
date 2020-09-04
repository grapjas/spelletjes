# reken spel    
import time   # voor stopwatch tussen berekeningen
import random # voor willekeurige getallen

#random.randint(a, b)
#Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
#https://docs.python.org/3.3/library/random.html
#https://realpython.com/python-timer/
#https://www.programiz.com/python-programming/exception-handling
#https://www.programiz.com/python-programming/break-continue

def maak_bewerking(getal1, getal2, bewerking):
  if bewerking == '+':
    return getal1 + getal2 
  elif bewerking == '-':
    return getal1 - getal2 
  elif bewerking == '*':
    return getal1 * getal2 

def neem_input():
  vlag = 0
  while(vlag == 0):
    try:
      speler = input('= ')
      if speler == 's':
        return speler
      speler = int(speler)
      vlag = 1
    except ValueError:
      print("Geef een geldig getal of 's' om te stoppen, stouterik!")
  return speler

intro = "Welkom, liefhebber van rekenen!\n"
intro += "Druk op de 's' toets om te stoppen."
print(intro)

bewerkingen = ['+', '-', '*'] 

juist = 0
fout = 0
totale_tijd = 0

while(1):
  tijd = 0
  start = time.perf_counter()
  bewerking = bewerkingen[random.randint(0,2)]
  if bewerking == '+':
    getal1 = random.randint(1,200)
    getal2 = random.randint(1,200)
  elif bewerking == '-':
    getal1 = random.randint(50,100)
    getal2 = random.randint(0,49)
  elif bewerking == '*':
    getal1 = random.randint(7,20)
    getal2 = random.randint(1,10) 
  print()
  print(getal1, bewerking, getal2)
  speler = neem_input()
  if speler == 's':
    break # ga uit while (naar beneden dus)
  stop = time.perf_counter()
  tijd = round(stop - start,2)
  totale_tijd += tijd
  if (speler == maak_bewerking(getal1, getal2, bewerking)):
    juist += 1
    print("\U00002705 ", tijd , "s")
  else:
    fout += 1
    print("\U0000274C ", tijd , "s")

# print score 
print()
if (juist+fout) != 0:
  print("--------------------------------------------")
  print("Totale speeltijd:     ", totale_tijd)
  print("Gemiddelde speeltijd: ", round(totale_tijd/(juist+fout),2))
  print("\U00002705 :", juist)
  print("\U0000274C :", fout)
else:
  print("Doei? Ging je delen door 0 testen, stouterik?")

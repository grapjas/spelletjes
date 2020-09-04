import os # nodig om scherm leeg te maken 
# int() voor gehele getallen 
# float() voor alle(?) getallen
# ValueError: bijvoorbeeld int('a'), 'a' kan niet tot een geheel getal (integer) omgezet worden
# True en False zijn Booleaanse waarden, 1 en 0 mag ook gebruikt worden 
# van een getal tekst maken tussen de komma's in een print(bla,blabla,blabl) door str(getal)

# to-do: 
#     wat zijn floats?
#       0.1 + 0.2 = 0.30000000000000004 blijkbaar
#     precisie van uitkomsten, juist afronden 
#     

def reset():
  input('Druk op een toets naar keuze om verder te gaan.')
  os.system('clear')

class bcolors: # voor kleurtjes, "How to print colored text in Python?"
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'  # stoppen met kleurtjes
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

while(True):
  intro = '----------------------------\n'
  intro += bcolors.HEADER + 'Rekenmachine voor 2 getallen\n' + bcolors.ENDC
  intro += '   * voor vermenigvuldigen\n'
  intro += '   + voor optellen\n'
  intro += '   - voor aftrekken\n'
  intro += '   / voor delen\n'
  print(intro)

  verkeerd = bcolors.FAIL + '\nDat is geen getal!\n' + bcolors.ENDC
  juist = False

  while(juist==False): # blijven controleren tot een juist getal
    try:
      getal1 = float(input(bcolors.UNDERLINE + 'eerste getal' + bcolors.ENDC + ': '))
      juist = True
    except ValueError:
      print(verkeerd)

  bewerking = input('bewerking: ')

  juist = False # opnieuw False maken, anders start while() niet
  while(juist==False):
    try:
      getal2 = float(input(bcolors.UNDERLINE + 'tweede getal' + bcolors.ENDC + ': '))
      juist = True
    except ValueError:
      print(verkeerd)
  
  # https://stackoverflow.com/questions/6189956/easy-way-of-finding-decimal-places
  naKomma1 = str(getal1)[::-1].find('.')
  naKomma2 = str(getal2)[::-1].find('.')

  # de meeste getallen na de komma voor afronding (float fout beperken, niet significante cijfers ;-) )
  naKomma = naKomma1 
  if naKomma2 > naKomma1:
    naKomma = naKomma2


  if bewerking == '+':
    resultaat = getal1 + getal2
  elif bewerking == '-':
    resultaat = getal1 - getal2
  elif bewerking == '*':
    resultaat = getal1 * getal2
  elif bewerking == '/':
    if getal2 == 0:
      print('\nJe mag niet delen door 0!\n\n')
      reset()
      continue # terug naar boven, nieuwe inputs
    else:
      resultaat = getal1 / getal2 
  else:
    print('\nDie bewerking bestaat niet, stouterik!\n\n')
    continue # terug naar boven, nieuwe inputs

  print('\n', getal1, bcolors.BOLD + bewerking + bcolors.ENDC, getal2, '=', bcolors.OKGREEN + str(round(resultaat,naKomma)) + bcolors.ENDC, '\n\n')
  reset()


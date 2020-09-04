# blad steen schaar (speler vs computer)

# https://stackoverflow.com/questions/3996904/generate-random-integers-between-0-and-9
import random # random (willekeurig) getal voor de computer als ranking in keuzes lijst
import bcolors as b # https://pypi.org/project/bcolors/

keuzes = ["blad", "steen", "schaar"]  # een lijst met 3 string elementen 

def speler_input():
  speler = input("Uw zet: ")
  while(speler not in keuzes):
    speler = input("Kies uit de lijst hierboven, stouterik!: ")
  return speler 

def computer_input():
  computer = keuzes[random.randint(0,2)] # kiest element 0, 1, of 2 in lijst
  return computer

def wie_wint():
  winnaar = 0
  while (winnaar == 0):
    computer = computer_input()
    speler = speler_input()
    if speler == computer:
      winnaar = 0
      print("De computer had ook", computer, ", opnieuw!")
      continue  
    winnaar = 1 
    if speler == "blad" and computer == "steen":
      winnaar = 2
    elif speler == "schaar" and computer == "blad":
      winnaar = 2
    elif speler == "steen" and computer == "schaar":
      winnaar = 2
  return [winnaar, speler, computer]


intro = "Welkom bij blad-steen-schaar, 1v1 de computer 🤖\n"
intro += "Je kan kiezen uit:\n"
intro += "    \U0001F91A  blad\n"
intro += "    \U0001F44A  steen\n" 
intro += "    \U0001F596  schaar\n"
print(intro) 

# kies de winnaar ...
# winnaar = 0 gelijkstand, opnieuw
# winnaar = 1 computer wint  
# winnaar = 2 speler wint 

# emojis["blad"] geeft "\U...."
emojis = {
  "blad": "\U0001F91A",
  "steen": "\U0001F44A", 
  "schaar": "\U0001F596"
}

score_speler = 0
score_computer = 0

while(1):
  winnaar, speler, computer = wie_wint()
  if winnaar == 1:
    print(emojis[speler], b.ERR + " verliest tegen" + b.ENDC, emojis[computer])
    score_computer += 1
  elif winnaar == 2:
    print(emojis[speler], b.OK + " wint tegen" + b.ENDC, emojis[computer])
    score_speler += 1
  extra_spelen = "\n\nDruk op ENTER om te blijven spelen."
  print("🤖 ", score_computer, '-', score_speler, "\U0001F469", extra_spelen)
  input()


""""
 blad verslaat steen 
 schaar verslaat blad 
 steen verslaat schaar 
"""

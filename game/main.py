import random

def choose_options():
  option = ("piedra", "papel", "tijera")
  user_option = (input("pierdra, papel o tijera => ")).lower()
    
  if not user_option in option:
    print ("Opcion incorrecta. Vuelve a intentarlo")
    # continue (ya no esta dentro de "WHILE", por ende no tiene que estar aca)
    return None, None
     
  computer_option = random.choice(option)
    
  print("Computer option =>", computer_option)
  return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == None:
    None
  elif user_option == computer_option:
    print ("EMPATE!")
  elif user_option == "piedra":
    if computer_option == "tijera":
      print ("Piedra le gana a tijera")
      print ("USER WIN")
      user_wins += 1
    else:
      print ("Papel le gana a piedra")
      print ("COMPUTER WIN")
      computer_wins += 1
  elif user_option == "papel":
    if computer_option == "tijera":
      print ("Tijera le gana a papel")
      print ("COMPUTER WIN")
      computer_wins += 1
    else:
      print ("Papel le gana a piedra")
      print ("USER WIN")
      user_wins += 1
  elif user_option == "tijera":
    if computer_option == "papel":
      print ("Tijera le gana a papel")
      print ("USER WIN")
      user_wins += 1
    else:
      print ("Piedra le gana a tijera")
      print ("COMPUTER WIN")
      computer_wins += 1
  return user_wins, computer_wins

def check_winner(user_wins, computer_wins):
  if user_wins == 3:
    print ("***YOU WIN***")
    exit()
  elif computer_wins == 3:
    print ("***YOU LOSE***")
    exit()
  return
  
def run_game():
  user_wins = 0
  computer_wins = 0
  round = 1

  while True:  
    print("·"*40)
    print("ROUND", round)
    print("-"*14)
    print("USER WINS =>", user_wins)
    print("PC WINS   =>", computer_wins)
    print("·"*40)
    round += 1
       
    user_option, computer_option = choose_options()
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
    check_winner(user_wins, computer_wins)

run_game()

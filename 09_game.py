import random

def choose_options():
  option = ("piedra", "papel", "tijera")
  user_option = input("piedra, papel o tijera => ").lower()
  if not user_option in option:
    print("Esta opción no es válida")
    return None, None
    #continue
  computer_opt =  random.choice(option)
  
  print("User option => ", user_option)
  print("Computer option => ", computer_opt)
  return user_option, computer_opt

def check_rules(user_option, computer_opt, win_user, win_computer):
    if(user_option == computer_opt):
      print("Empate")
    elif (user_option == "piedra"):
      if(computer_opt == "tijera"):
        print("Piedra gana a tijera")
        print("User ganó!")
        win_user +=1
      else:
        print("Papel gana a piedra")
        print("Computer gana")
        win_computer+=1
    elif (user_option == "papel"):
      if(computer_opt == "piedra"):
        print("Papel gana a piedra")
        print("User ganó")
        win_user +=1
      else:
        print("Tijera le gana al papel")
        print("Computer gana")
        win_computer+=1
    elif (user_option == "tijera"):
      if(computer_opt == "papel"):
        print("Tijera le gana a papel")
        print("User gana")
        win_user +=1
      else:
        print("Piedra le gana a tijera")
        print("Computer gana")
        win_computer+=1
    return (win_user, win_computer)

def run_game():
  win_user = 0
  win_computer = 0
  rounds = 1  
  
  while True:
    
    print("*" * 10)
    print("ROUND ", rounds)
    print("*" * 10)
  
    print("Puntos Usuarios: ", win_user)
    print("Puntos Computer: ", win_computer)
    
    user_option, computer_opt = choose_options()
    win_user, win_computer = check_rules(user_option, computer_opt, win_user, win_computer )
    
  
        
    if win_computer == 2:
      print("El compu ganó")
      break
    if win_user == 2:
      print("Ganaste")
      break
    rounds+=1

run_game()

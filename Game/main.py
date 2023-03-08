import random
#realizamos la función para elegir las opciones
def choose_options():
  options = ["piedra", "papel", "tijera"]
  user_option = input("Elige piedra, papel o tijera: ").lower()
  
  if user_option not in options:
    print("Esa opcion no es válida")
    # continue
    return None, None
  
  computer_option = random.choice(options)

  print("User option =>", user_option)
  print("Computer Option =>", computer_option)
  return user_option, computer_option

#Realizamos la funcion de las reglas
def check_rules(user_option, computer_option, user_wins, computer_wins):

  if user_option == computer_option:
      print("Empate")
  elif user_option == "piedra":
    if computer_option == "tijera":
      print("piedra gana a tijera")
      print("user gano")
      user_wins += 1
    else:
      print("Papel gana a piedra")
      print("Computer gano")
      computer_wins += 1

  elif user_option == "papel":
    if computer_option == "piedra":
      print("papel gana a piedra")
      print("user gano")
      user_wins +=1
    else:
      print("tijera gana a papel")
      print("computer gano")
      computer_wins +=1
  elif user_option == "tijera":
    if computer_option == "papel":
      print("tijera gana a papel")
      print("user gano")
      user_wins += 1
    else:
      print("piedra gana a tijera")
      print("computer gano")
      computer_wins += 1
  return user_wins, computer_wins

def check_winner(user_wins, computer_wins):
  if computer_wins == 3:
    print("El ganador es la computadora")
    return "Fin" 

  if user_wins == 3:
    print("El ganador es el usuario")
    return "Fin"


def run_game():
  computer_wins = 0
  user_wins = 0
  rounds = 1 

  while True:
    print("*" * 10)
    print("ROUND", rounds)
    print("*" * 10)

    print("Computer_wins", computer_wins)
    print("User_wins", user_wins)
    rounds +=1

        
    user_option, computer_option = choose_options()
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
    result= check_winner(user_wins, computer_wins)

    if result =="Fin":
      break

run_game()
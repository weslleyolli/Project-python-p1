from operationbd import *
from utils import *
conn = abrirBancoDados('localhost','root','Weslley(2021)','systemouvi')


# abc ombudsman menu

print(f"{Colors.blue}Hello, my name is Tron. I am your virtual assistant.{Colors.normal}")
while Functions.options != 7:
  print(f"{Colors.blue}What do you want? {Colors.normal}")
  print()
  print("1) List all manifestations: \n2) List all suggestions: \n3) List all complaints: \n4) List all praise: \n5) Create a new manifestation: \n6) Search protocol by number: \n7) Leave")
  Functions.options = int(input("Enter the number you want: "))
  print()

  while Functions.options < 1 or Functions.options > 7:
    print(f"{Colors.red}Number invalid. Please enter a new number between 1 and 7{Colors.normal}")
    print()
    break

  if Functions.options == 1:
    print(f"{Colors.blue}List of all manifestations:{Colors.normal}")
    sql = "select * from manifestation"
    resultado = listarBancoDados(conn, sql)

    for elemento in resultado:
      print(elemento)

  if Functions.options == 2:
    print(f"{Colors.blue}List of all suggestions:{Colors.normal}")
    sql = "select * from manifestation"
    resultado = listarBancoDados(conn, sql)

    for elemento in resultado:
      if elemento[2] == "suggestion":
        print(elemento)

  if Functions.options == 3:
    print(f"{Colors.blue}List of all complaints:{Colors.normal}")
    sql = "select * from manifestation"
    resultado = listarBancoDados(conn, sql)

    for elemento in resultado:
      if elemento[2] == "complaints":
        print(elemento)

  if Functions.options == 4:
    print(f"{Colors.blue}List of all praise:{Colors.normal}")
    sql = "select * from manifestation"
    resultado = listarBancoDados(conn, sql)

    for elemento in resultado:
      if elemento == "praise":
        print(elemento)
      if elemento != "praise":
        print(f"{Colors.red}list empty{Colors.normal}")
        print()
        break


  if Functions.options == 5:
    # I put 2 zeros on the left in the variable.
    print(f"{Colors.blue}To make a new manifestation I need some information{Colors.normal}")
    name = input('enter your name: ').capitalize()
    type = int(input('enter the type: '))
    description = input('enter the description:  ')

    while type < 1 or type > 3:
      print (f"{Colors.red}Number invalid. Please enter one new number between 1 and 3.{Colors.normal}")
      type = int(input("1) For complaints \n2) For suggestions \n3) For praise \nEnter the type: "))
    if type == 1:
      type = "Complaints"
    elif type == 2:
      type = "Suggestions"
    elif type == 3:
      type = "Praise"
    # I converted the answer to string


    sql = "INSERT INTO manifestation(nome, typed, description) VALUES (%s, %s, %s)"
    dados = (name, type, description)
    protocol_number = insertNoBancoDados(conn, sql, dados)
    print(f"{Colors.blue}The number of your protocol is: {protocol_number}  {Colors.normal}")

    print(f"{Colors.blue}request accepted!!{Colors.normal} ")
    print()

  if Functions.options == 6:
    number_protocol = int(input("Enter the your number of procol: "))
    sql = "select * from manifestation"
    result = listarBancoDados(conn, sql)
    for elemento in result:
      if elemento[0] == number_protocol:
        print(elemento)
print(f"{Colors.blue}Thanks for visiting our website! {Colors.normal} ")
from utils import *
#abc ombudsman menu

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
    printList(List.all_manifestation)
    print()

  if Functions.options == 2:
    print(f"{Colors.blue}List of all suggestions:{Colors.normal}")
    printList(List.list_suggestion)
    print()

  if Functions.options == 3:
    print(f"{Colors.blue}List of all complaints:{Colors.normal}")
    printList(List.list_complaints)
    print()

  if Functions.options == 4:
    print(f"{Colors.blue}List of all praise:{Colors.normal}")
    if not List.list_praise:
      print("Empty list")
    else:
      printList(List.list_praise)
    print()

  if Functions.options == 5:
    protocol = len(List.all_manifestations) + 1
    replace_protocol = str(protocol).zfill(3)
    # I put 2 zeros on the left in the variable.
    print(f"{Colors.blue}To make a new manifestation I need some information{Colors.normal}")
    name = input("Enter your name: ").capitalize()
    type = int(input("1) For complaints \n2) For suggestions \n3) For praise \nEnter the type: "))

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
    description = input("Enter description: ").capitalize()
    protocol_complet = (f"{replace_protocol}#{name}#{type}#{description}")
    # I converted all variables in one string.
    print(f"{Colors.blue}The number of your protocol is: {str(protocol).zfill(3)} {Colors.normal}")
    broken_manifestation = protocol_complet.split("#")
    # And now I will put the protocol in the list it belongs to.
    if type == "Complaints":
      addList(List.list_complaints, protocol_complet)
    elif type == "Suggestions":
      addList(List.list_suggestion, protocol_complet)
    elif type == "Praise":
      addList(List.list_praise)
      protocol += 1
    print(f"{Colors.blue}request accepted!!{Colors.normal} ")
    print()

  if Functions.options == 6:
    number_protocol = int(input("Enter the your number of procol: "))
    # now I'm checking if there is a protocol with that number.
    if (number_protocol > len(List.all_manifestations)) or (number_protocol < 1):
      print(f"{Colors.red}There is no protocol with this number{Colors.normal}")
    else:
      string_protocol = str(number_protocol).zfill(3)
      search_protocol = (List.all_manifestations[number_protocol - 1])
      broken_manifestation = search_protocol.split("#")
      print()
      print(f"{Colors.blue}Details of protocol {Colors.normal}")
      print(f"Number of protocol: {broken_manifestation[0]}")
      print(f"Name: {broken_manifestation[1]}")
      print(f"Type: {broken_manifestation[2]}")
      print(f"Description: {broken_manifestation[3]}")
      print()
print(f"{Colors.blue}Thanks for visiting our website! {Colors.normal} ")
#test1
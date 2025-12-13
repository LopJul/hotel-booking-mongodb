from customers import add_customer, find_customer, list_customers, update_customer, delete_customer
from reservations import add_reservation, find_reservation, list_reservations, update_reservation, delete_reservation

while True:
  collection = input("Valitse yksi (asiakas, varaus, lopeta): ")

  if collection == "lopeta":
    print("Ohjelma lopetetaan")
    break

  if collection == "asiakas":

    print("1. Lisää asiakas")
    print("2. Etsi asiakas")
    print("3. Listaa kaikki asiakkaat")
    print("4. Muokkaa asiakasta")
    print("5. Poista asiakas")

    command = input("Valitse toiminto: ")

    if command == "1":
      add_customer()
    elif command == "2":
      find_customer()
    elif command == "3":
      list_customers()
    elif command == "4":
      update_customer()
    elif command == "5":
      delete_customer()
    else: 
      print("Toimintoa ei löydy")

  elif collection == "varaus":
    print("1. Lisää varaus")
    print("2. Etsi varaus")
    print("3. Listaa kaikki varaukset")
    print("4. Muokkaa varausta")
    print("5. Poista varaus")

    command = input("Valitse toiminto: ")

    if command == "1":
      add_reservation()
    elif command == "2":
      find_reservation()
    elif command == "3":
      list_reservations()
    elif command == "4":
      update_reservation()
    elif command == "5":
      delete_reservation()
    else:
      print("Toimintoa ei löydy")
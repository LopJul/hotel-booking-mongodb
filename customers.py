from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["hotel_booking_db"]

def add_customer():

  name = input("Anna nimi: ")
  email = input("Anna sähköpostiosoite: ")
  phone = input("Anna puhelinnumero: ")
  street = input("Anna katuosoite: ")
  postal_code = input("Anna postinumero: ")
  city = input("Anna kaupunki: ")
  country = input("Anna maa: ")

  customer = {"name": name,
              "email": email,
              "phone": phone,
              "address": 
                  {"street": street,
                   "postal_code": postal_code,
                   "city": city,
                  "country": country}}
  x = db.customers.insert_one(customer)
  print("Asiakas lisätty ID: ", x.inserted_id)

def find_customer():
  email = input("Anna asiakkaan sähköposti:")
  customer = db.customers.find_one({"email": email})

  if customer:
    print(customer)
  else:
    print("Asiakasta ei löydy")

def list_customers():

  for customer in db.customers.find():
    print(customer)

def update_customer():

  email = input("Anna asiakkaan nykyinen sähköposti: ")
  customer = db.customers.find_one({"email": email})

  if not customer:
    print("Asiakasta ei löydy")
    return

  print("Mitä tietoja haluat muokata?")
  option = input("Valitse yksi: nimi, sähköposti, puhelinnumero, osoite: ")

  if option == "nimi":
    new_value = input("Anna uusi nimi: ")
    db.customers.update_one(
      {"email": email},
      {"$set": {"name": new_value}}
    )
    print("Nimi päivitetty onnistuneesti")
  elif option == "sähköposti":
    new_value = input("Anna uusi sähköposti: ")
    db.customers.update_one(
      {"email": email},
      {"$set": {"email": new_value}}
    )
    print("Sähköposti päivitetty onnistuneesti")
  elif option == "puhelinnumero":
    new_value = input("Anna uusi puhelinnumero: ")
    db.customers.update_one(
      {"email": email},
      {"$set": {"phone": new_value}}
    )
    print("Puhelinnumero päivitetty onnistuneesti")
  elif option == "osoite":
    street = input("Anna uusi katuosoite: ")
    postal_code = input("Anna uusi postinumero: ")
    city = input("Anna uusi kaupunki: ")
    country = input("Anna uusi maa: ")
    db.customers.update_one(
      {"email": email},
      {"$set": {
        "address.street": street,
        "address.postal_code": postal_code,
        "address.city": city,
        "address.country": country
      }}
    )
    print("Osoite päivitetty onnistuneesti")
  else:
    print("Ei löydy")
  
def delete_customer():

  email = input("Anna asiakkaan sähköposti: ")
  customer = db.customers.find_one({"email": email})

  if not customer:
    print("Asiakasta ei löydy")
    return
  
  print("Löytyi asiakas: ", customer)

  confirm = input("Haluatko varmasti poistaa kyseisen asiakkaan? (k/e): ")

  if confirm == "k":
    delete = db.customers.delete_one({"email": email})
    if delete.deleted_count > 0:
      print("Asiakas poistettu onnistuneesti")
    else:
      print("Poistaminen ei onnistunut")
  else:
    print("Poisto peruutettu")

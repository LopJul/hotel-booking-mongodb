from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["hotel_booking_db"]

def add_reservation():

  customer_email = input("Anna asiakkaan sähköposti: ")
  customer = db.customers.find_one({"email": customer_email})
  if not customer:
    print("Asiakasta ei löydy")
    return
  room_number = input("Anna huomeen numero: ")
  room = db.rooms.find_one({"room_number": room_number})
  if not room:
    print("Huonetta ei löydy")
    return
  
  check_in_str = input("Anna sisäänkirjautumispäivä (YYYY-MM-DD): ")
  check_out_str = input("Anna uloskirjautumispäivä (YYYY-MM-DD): ")
  check_in = datetime.strptime(check_in_str, "%Y-%m-%d")
  check_out = datetime.strptime(check_out_str, "%Y-%m-%d")

  status = "confirmed"

  reservation = {
    "customer_id": customer["_id"],
    "room_id": room["_id"],
    "check_in": check_in,
    "check_out": check_out,
    "status": status
}

  new_doc = db.reservations.insert_one(reservation)
  print("Varaus lisätty onnistuneesti, ID: ", new_doc.inserted_id)

def find_reservation():

  customer_email = input("Anna asiakkaan sähköposti: ")

  customer = db.customers.find_one({"email": customer_email})
  if not customer:
    print("Asiakasta ei löydy")
    return

  reservation = db.reservations.find_one({"customer_id": customer["_id"]})
  if reservation:
    print(reservation)
  else:
    print("Varausta ei löydy")


def list_reservations():
  for reservation in db.reservations.find():
    print(reservation)
  
def update_reservation():
  customer_email = input("Anna asiakkaan sähköposti: ")

  customer = db.customers.find_one({"email": customer_email})
  if not customer:
    print("Asiakasta ei löydy")
    return

  reservation = db.reservations.find_one({"customer_id": db.customers.find_one({"email": customer_email})["_id"]})

  if not reservation:
    print("Varausta ei löytynyt")
    return

  print("Nykyiset päivämäärät:")
  print("Sisäänkirjautuminen:", reservation["check_in"].strftime("%Y-%m-%d"))
  print("Uloskirjautuminen:", reservation["check_out"].strftime("%Y-%m-%d"))

  new_check_in_str = input("Anna uusi sisäänkirjautumispäivä (YYYY-MM-DD): ")
  new_check_out_str = input("Anna uusi uloskirjautumispäivä (YYYY-MM-DD): ")
    
  new_check_in = datetime.strptime(new_check_in_str, "%Y-%m-%d")
  new_check_out = datetime.strptime(new_check_out_str, "%Y-%m-%d")

  new_dates = db.reservations.update_one(
    {"_id": reservation["_id"]},
    {"$set": {"check_in": new_check_in, "check_out": new_check_out}}
    )
  
  if new_dates.modified_count > 0:
    print("Varaus päivitetty onnistuneesti")
  else:
    print("Päivitys ei onnistunut")

def delete_reservation():

  customer_email = input("Anna asiakkaan sähköposti: ")

  customer = db.customers.find_one({"email": customer_email})
  if not customer:
    print("Asiakasta ei löydy")
    return

  reservation = db.reservations.find_one({"customer_id": customer["_id"]})
  if not reservation:
    print("Varausta ei löydy")
    return
  
  print(f"Huone ID: {reservation['room_id']}")
  print(f"Sisään: {reservation['check_in'].strftime('%Y-%m-%d')}, Ulos: {reservation['check_out'].strftime('%Y-%m-%d')}")

  confirm = input("Haluatko varmasti poistaa kyseisen varauksen? (k/e): ")

  if confirm == "k":
    delete_doc = db.reservations.delete_one({"_id": reservation["_id"]})
    if delete_doc.deleted_count > 0:
      print("Varaus poistettu onnistuneesti")
    else:
      print("Poistaminen ei onnistunut")
  else:
    print("Poisto peruutettu")
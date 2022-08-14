import phonenumbers
from phonenumbers import timezone, geocoder, carrier

number = input("Enter your no. with your country code (+--) : ")

phone = phonenumbers.parse(number)

time = timezone.time_zones_for_number(phone)

carr = carrier.name_for_number(phone, "en")

registration = geocoder.description_for_number(phone, "en")

print(phone)
print("Time Zone : ", time)
print("Sim Card provider : ", carr)
print("Country : ", registration)
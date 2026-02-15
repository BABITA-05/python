#stores as key value pairs
customer = {
    "name":"Babita Bhandari",
    "age":20,
    "is_verified":True
}
for key, value in customer.items():
    print(key, ":" , value)


#wap to get input from user and translate it into english alphabet

phone = input("Enter your phone number:")
digits_mapping = {
    "1":"one",
    "2":"two",
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
    print(output)


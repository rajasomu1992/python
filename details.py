n = "NAME"
a = "Age"
add = "Address"
b = ":"

firstname = str(input("First Name:"))
lastname = str(input("Last Name:"))
age = input("Age:")
area = input("Area:")
city = input("City:")
state = input("State:")
zip = input("Zip:")

print(n.ljust(15," "),b.ljust(15," "), firstname.capitalize(), lastname.capitalize())
print(a.ljust(15," "),b.ljust(15," "), age)
print(add.ljust(15," "),b.ljust(15," "), area.capitalize(), ",", city.capitalize(), ",", state.capitalize(), "-", zip.capitalize())

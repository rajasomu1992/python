n = "NAME"
a = "Age"
add = "Address"
b = ":"

firstname = input("Please enter your first name:")
lastname = input("Please enter your last name:")
age = input("Please enter your age:")
city = input("Please enter your city:")
state = input("Please enter your state:")
zip = input("Please enter your zip code:")

print(n.ljust(15," "),b.ljust(15," "), firstname.capitalize(), lastname.capitalize())
print(a.ljust(15," "),b.ljust(15," "), age)
print(add.ljust(15," "),b.ljust(15," "), city.capitalize(), ",", state.upper(), "-", zip.capitalize())

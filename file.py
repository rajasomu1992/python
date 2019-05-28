n = "NAME"
a = "Age"
add = "Address"
b = ":"
c = ","
d = "-"

firstname = (input("First Name:"))
lastname = (input("Last Name:"))
age = input("Age:")
area = input("Area:")
city = input("City:")
state = input("State:")
zip = input("Zip:")


f = open("C:\\Users\\RAJ\\Desktop\\python tasks\\test.txt", "w")



# f.write(f"{n.ljust(15," ")}{b.ljust(15," ")}{firstname.capitalize()}{lastname.capitalize()}")
# print(a.ljust(15," "),b.ljust(15," "), age)
# print(add.ljust(15," "),b.ljust(15," "), area.capitalize(), ",", city.capitalize(), ",", state.capitalize(), "-", zip.capitalize())
f.write(f'{n:<15}{b:<15}{firstname.capitalize()} {lastname.capitalize()}' '\n')
f.write(f'{a:<15}{b:<15}{age}' '\n')
f.write(f'{add:<15}{b:<15}{area.capitalize()}{c:<1}{city.capitalize()}{c:<1}{state.capitalize()}{d:<1}{zip.capitalize()}')
f.close()


# f = open("C:\\Users\\RAJ\\Desktop\\python tasks\\test.txt", "w")


#String Methods
#upper()
str="harsh Dhiman !!"
print(str.upper())
#lower()
print(str.lower())
#strip() - removes any white spaces before and after the string
print(str.strip())
#rstrip() -  removes any trailing characters.
print(str.rstrip("!"))
#replace()
print(str.replace("Harsh","Happy"))
#split()
print(str.split(" ")) #Splits the string at the whitespace " "
#capitalize()
print(str.capitalize())
#center()
print(str.center(50,"."))
#count()
print(str.count("a"))
#endswith()
print(str.endswith("n"))
print(str.endswith("!"))
#find()
print(str.find("a"))
print(str.find("z"))
#index()
print(str.index("n"))
# print(str.index("z"))  Throws error

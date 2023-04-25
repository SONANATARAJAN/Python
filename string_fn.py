s = "sona anos"

print(s)
print(type(s))
print(s.capitalize())
print(s.upper())
print(s.title())
print(s.count('s'))
print(s.endswith('os'))
print(s.find('o'))
print(s.find('o',6))
print(s.replace('o','0'))

a = " sona143"
print("Is Upper", a.isupper())
print("Is Lower", a.islower())
print("is Alpha numeric", a.isalnum())
print("Is Alpha",a.isalpha())


s="he\nis\ngood"
print(s)
print(s.splitlines())
print(s.splitlines(True))


a= "Sona Electronics Engineer"
print(a.split(' '))


a= "Sona,Electronics,Engineer"
print(a.split(','))




d="          sona        "
print(len(d))
print(len(s.strip()))
print(len(s.rstrip()))
print(len(s.lstrip()))


s='12-03-2020'
print(s.partition('-'))
          

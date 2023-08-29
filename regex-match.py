import  re

nombre1="Sandra Lopez"

nombre2="Antonio Gomez"

nombre3="Maria Lopez"

if re.match("Sandra", nombre1, re.IGNORECASE):

    print("Hemos encontrado el nombre")

else: 

    print("No lo hemos encontrado")


if re.match(".ara", nombre1, re.IGNORECASE):

    print("Hemos encontrado el nombre")

else: 

    print("No lo hemos encontrado")

if re.match("\d", nombre1, re.IGNORECASE):

    print("Hemos encontrado el nombre")

else: 

    print("No lo hemos encontrado")
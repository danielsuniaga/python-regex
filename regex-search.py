import re

cadena ="Vamos a aprender expresiones regulares"

print(re.search("aprender", cadena))

textoBuscar="aprender"

if re.search(textoBuscar, cadena) is not None: 

    print("He encontrado el texto")

else: 

    print("No he encontrado el texto")
#expresiones regulares
#search
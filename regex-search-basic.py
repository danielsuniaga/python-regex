import re

cadena ="Vamos a aprender expresiones regulares, aprender"

print(re.search("aprender", cadena))

textoBuscar="aprender"

textoEncontrado=re.search(textoBuscar, cadena)

print(textoEncontrado.start())

print(textoEncontrado.end())

print(textoEncontrado.span())

print(re.findall(textoBuscar, cadena))

#start
#end
#span
#findall
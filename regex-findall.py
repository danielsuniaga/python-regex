import re

lista_nombres=['Ana gomez','Maria martin','Sandra lopez','Santigo martin']

for elemento in lista_nombres:

    if re.findall('^Sandra',elemento):

        print(elemento)

for elemento in lista_nombres:

    if re.findall('Martín$', elemento):

        print(elemento)

for elemento in lista_nombres:

    if re.findall('[ñ]', elemento):

        print(elemento)

for elemento in lista_nombres:

    if re.findall('niñ[oa]s', elemento):

        print(elemento)
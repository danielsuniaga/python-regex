import re

lista_nombres=[
    'Ana gomez',
    'Maria martin',
    'Sandra lopez',
    'Santigo martin'
]

for elemento in lista_nombres:

    if re.findall('[o-t]', elemento):#DEVUELVE LOS REGISTROS ENTRE LOS RANGOS INDICADOS

        print(elemento)

for elemento in lista_nombres:

    if re.findall('[^O-T]', elemento):#DEVUELVE LOS REGISTROS ENTRE LOS RANGOS INDICADOS SIN EMBARGO SOLO EVALUA LA LETRA INICIAL

        print(elemento)

for elemento in lista_nombres:

    if re.findall('[O-T]$', elemento):#DEVUELVE LOS REGISTROS ENTRE LOS RANGOS INDICADOS SIN EMBARGO SOLO EVALUA LA LETRA INICIAL

        print(elemento)


lista_nombres=[
    'Ma1',
    'Se1',
    'Ba1',
    'Ma3'
]

for elemento in lista_nombres: 

    if re.findall('Ma[0-3]',elemento):

        print(elemento)
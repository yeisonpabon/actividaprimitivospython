#tipos de datos 

#lista de numeros
numeros = range(11)
#generacion de cuadrados de los numeros 
cuadrados = [num**2 for num in numeros ]
#impresion de resultados 
print(cuadrados)


#actividad 2 formateo de cadenas(str, int )

name = 'yeison'
age = 22

mensaje = f'hola, mi nombre es {name} y  tengo {age} de edad'
print ( mensaje)

#Actividad 3: uso de condicionales con booleanos 

#definicion de variables 
edad= 22
#condicion para la mayoria de eadad
if edad >= 18:
    print('eres mayor de edad' )

else :
    print('eres menor de edad ')

#actividad 4: uso de ciclos while y flotantes (float)
#definicion de una variable con valor flotante

saldo = 100.0 

# simulaion de un ciclo de retiros de saldo 
while saldo > 10:
    retiro = 15.0
    saldo -=retiro
    print( f'sea ha retirado{retiro}, saldo actual: {saldo}')

#atvida 5
#uso de diccionarios 
# definimos un diccionario 

persona = {
    'nombre': 'caro',
    'edad':'30',
    'ciudad':'sevilla'
}

#iteramos sobre las claves y valores del diccionario
for clave ,valor in persona.items():
    print(f'{clave.capitalize()}:{valor}')
    
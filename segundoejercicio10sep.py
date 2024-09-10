#ejercicio 2 laboratorio
#uso avanzado de de float con manejo de dicimal

from decimal import Decimal,getcontext

#establecemos un contexto de precision alta
getcontext().prec = 50
#realizmos una operacion matematicas precisas
numero1= Decimal('1.123456789123456789') 
numero2= Decimal('2.987654321987654321')
resultado = numero1*numero2
#mostramos el reultado con alta precision
print(f'resultado preciso : {resultado}')
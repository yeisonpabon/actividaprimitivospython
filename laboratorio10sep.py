#laboratorio 
#usamos recursion con memorizacion para calcular numeros de fibonocci
#memo es la habrieviatura de memorizar 
def fibonacci(n,memo={}):
    if n in memo :
        return memo[n]
    if n<=1:
        return n
    memo[n]= fibonacci(n-1,memo)+fibonacci(n-2,memo)
    return memo[n]
#calcular suceion de fibonacci de 50
resutado = fibonacci(50)

print(",".join(str (e) for e in resutado))



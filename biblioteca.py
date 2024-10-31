#function that calculates a factorial of a number
def fatorial(number):
    result = 1
    for i in range(1, number + 1):
        result = result * i
    return result
    
#Function that show the factorial
def mostrarfatorial(number):
     print('O fatorial de {} é: {} '.format(number, fatorial(number)))
    
#function that calculates a sum of a number
def somatorio(number, pares):
    result = 0 
    inicio = 0 
    if pares:
        inicio = 0
    else:
        inicio = 1
    for i in range(inicio, number + 1, 2):
       result = result + i
    return result
    
#Function that show the Even
def mostrarSomatorio(number, pares):
    if pares:
        print('Agora vamos fazer a somátoria dos números pares! ')
        print('A soma dos pares é: {} '.format(somatorio(number, pares))) 
        
    else:
        print('Agora vamos fazer a somátoria dos números ímpares! ')
        print('A soma dos ímpares é: {} '.format(somatorio(number, pares))) 
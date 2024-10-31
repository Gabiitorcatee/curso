from biblioteca import  mostrarfatorial, mostrarSomatorio

#main program
while True:
    user_input = input('Digite um número ou digite "fim": ')
    if user_input.lower() == 'fim': 
        print('Obrigada por utilizar meu programa, espero que tenha gostado!')
        break
    number = int(user_input)
    mostrarfatorial(number)
    mostrarSomatorio(number, True)
    mostrarSomatorio(number, False)
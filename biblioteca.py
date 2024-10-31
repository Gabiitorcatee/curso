from rich import print
from rich.prompt import Prompt

def fatorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result

def mostrarfatorial(number):
    print(f'[blue]O fatorial de {number} é: {fatorial(number)}[/blue]')

def somatorio(number, pares):
    result = 0
    inicio = 0 if pares else 1
    for i in range(inicio, number + 1, 2):
        result += i
    return result

def mostrarSomatorio(number, pares):
    tipo = "pares" if pares else "ímpares"
    print(f'[green]A soma dos {tipo} até {number} é: {somatorio(number, pares)}[/green]')

# Programa principal
while True:
    user_input = Prompt.ask('[bold]Digite um número ou digite "fim"[/bold]')
    if user_input.lower() == 'fim': 
        print('[red]Obrigada por utilizar meu programa![/red]')
        break
    try:
        number = int(user_input)
        mostrarfatorial(number)
        mostrarSomatorio(number, True)
        mostrarSomatorio(number, False)
    except ValueError:
        print("[red]Por favor, insira um número válido.[/red]")

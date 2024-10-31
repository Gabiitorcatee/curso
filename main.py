from rich import print
from rich.prompt import Prompt
from rich.console import Console

console = Console()

while True:
    user_input = Prompt.ask('Digite um número ou digite "fim"')
    if user_input.lower() == 'fim': 
        print('[green]Obrigada por utilizar meu programa, espero que tenha gostado![/green]')
        break
    try:
        number = int(user_input)
        mostrarfatorial(number)
        mostrarSomatorio(number, True)
        mostrarSomatorio(number, False)
    except ValueError:
        print("[red]Por favor, insira um número válido.[/red]")

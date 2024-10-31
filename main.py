from planetas import planetas
#programa principal
while True:
    user_input = input('Gostaria de acessar o banco de dados dos planetas? "Sim" ou "Não": ')
    if user_input.lower() == 'não': 
        print('Obrigada por utilizar meu programa, espero que tenha gostado!')
        break
    else:
      print('\nDicionário de Planetas')
      print('1. Adicionar planeta')
      print('2. Remover planeta')
      print('3. Lista planetas')
      print('4. Buscar planetas')
      print('5. Editar planeta')
      print('fim. Sair')
    
    number = (user_input) # muda a entrada de dados para números
    opcao = input('Digite a opção desejada: ')
    
    if opcao == '1':
        adicionar_planetas()
    elif opcao == '2':
        remover_planetas()
    elif opcao == '3':
        listar_planetas()
    elif opcao == '4':
        buscar_planetas()
    elif opcao == '5':
        editar_planetas()
    else:
        print('Opção desejada não existe')
            
            



from planetas import planetas

#adiciona um item
def adicionar_planetas():
    nome = input('Digite o nome do planeta que deseja adicionar: ')
    apelido = input('Digite o apelido do planeta: ')
    tamanho = input('Digite o tamanho do planeta: ')
    distancia = input('Digite a distância entre o Sol e o planeta: ')
    planetas[nome] = {'tamanho': tamanho, 'distancia': distancia, 'apelido': apelido}
    print(f'O planeta {nome} foi adicionado com sucesso!.')
    print('-' * 20)

#remove um dado soliciado
def remover_planetas():
    nome = input('Digite o nome do planeta a ser removido: ')
    if nome in planetas:
        del planetas [nome]
        print(f'O planeta {nome} foi removido.')
        print('-' * 20)
    else:    
        print('Não é possível remover este planeta.')

#lista todos os dados
def listar_planetas():
    if not planetas:
        print('Não há planetas cadastrados, volte mais tarde!')
    else:
        for planeta, info in planetas.items():
            print(f'Planeta: {planeta}')
            print(f'Tamanho: {info["tamanho"]}')
            print(f'Distância do Sol: {info["distancia"]}')
            print(f'Apelido: {info["apelido"]}')
            print('-' * 20)
        
#Busca e apresenta o dado selecionado        
def buscar_planetas():
    nome = input('Digite o nome do planeta a ser buscado: ')
    if nome in planetas:
        print(f'Planeta: {nome}')
        print(f'Tamanho: {planetas[nome]["tamanho"]}')
        print(f'Distância do Sol: {planetas[nome]["distancia"]}')
        print(f'Apelido: {planetas[nome]["apelido"]}')
        print('-' * 20)
    else:    
        print('Planeta não foi encontrado.')

def editar_planetas():
    nome = input('Digite o nome do planeta que deseja editar: ')
    if nome in planetas:
      novo_apelido = input('Digite o novo apelido do planeta: ')
      novo_tamanho = input('Digite o novo tamanho do planeta: ')
      nova_distancia = input('Digite a nova distância entre o Sol e o planeta: ')
      planetas[nome]['tamanho'] = novo_tamanho 
      planetas[nome]['apelido'] = novo_apelido
      planetas[nome]['distancia'] = nova_distancia
      print(f'O planeta {nome} foi editado com sucesso!.')
      print('-' * 20)  
    else:
      print('O planeta não foi encontrado')



from os import system
system('cls')
from entrada_dados import pega_str_vazia, pega_int_positivo

#----------- Dict Jogadores -----------
'''
def cabecalho (texto):
    print(texto)
    
    print(f"{'Nome':<20} {'Idade':<4} {'Cidade':<20} {'Profissão':<20}")
def adicionar_ou_atualizar_jogadores(nome, idade nacionalidade, posicao):
    jogadores[nome] = {'idade':idade, 'nacionalidade':nacionalidade, 'posicao':posicao}
    print(f'Dados do Jogador {nome} foram Adionados/Atualizados com Sucesso\n')
    
def listar_jogadores(jogadores):
    print('============ Dicionario de Jogadores ===========')
    print(f"{'Nome':<20} {'Idade':<4} {'Cidade':<20} {'Profissão':<20}")
    for nome, info in jogadores.items():
        print(f"{nome:<20} {info['idade']:<5} {info['nacionalidade']:<20} {info['posicao']:<20}")
        
def buscar_ou_remover_jogador(jogador, nome, booleano):
    if booleano == True:
        if nome in jogador:
            print(f"Nome: {nome}\n"
                  f"idade: {jogador[nome]['idade']}\n"
                  f"nacionalidade: {jogador[nome]['nacionalidade']}\n"
                  f"posição: {jogador[nome]['posicao']}\n")
        else:
            if nome in jogador:
                del jogador[nome]
                print(f'Jogador {nome} foi removido da lista.\n')
            else:
                print(f'Jogador {nome} não encontrado.\n')
            
def menu():
    print('\n1.Adicionar ou Atualizar Jogador\n'
          '2.Listar jogadores Cadastrados\n'
          '3.Mostrar os Dados de um Jogador\n'
          '4.Remover um Jogador\n'
          '5.Sair\n')
                
#------- Programa Principal -------

jogadores = {
    'Cristiano Ronaldo': {'idade': 36, 'nacionalidade': 'Portugal', 'posicao': 'Atacante'},
    'Lionel Messi': {'idade': 34, 'nacionalidade': 'Argentina', 'posicao': 'Atacante'}
}

while True:
    menu()
    op = input('Explore uma Função')
    match op:
        case '1':
            nome = input('Digite o Nome do Jogador: ')
            idade = int(input('Idade do Jogador: '))
            nacionalidade = input('Nacionalidade do Jogador: ')
            posicao = input('Posicao de Jogo: ')
            adicionar_ou_atualizar_jogadores(nome, idade nacionalidade, posicao)
        case '2':
            listar_jogadores(jogadores)
        case '3':
            nome=input('Nome do Jogador: ')
            buscar_ou_remover_jogador(jogadores, nome, True)
        case '4':
            nome=input('Nome do Jogador: ')
            buscar_ou_remover_jogador(jogadores, nome, False)
        case '5':
            print('Até Breve!')
            break
        case _:
            print('Opção Invalida')
           
'''     
# ----------- Cad Alunos ----------
''' 
def dados_alunos(dict_cadastro):
    nome_candidato = input('Nome do Candidato: ').capitalize()
    idade_candidato = int(input('Idade do Candidato: '))
    nota1 = float(input('Nota da Primeira Prova: '))
    nota2 = float(input('Nota da Segunda Prova: '))
        
    cadastrar_alunos(nome_candidato, idade_candidato, nota1, nota2, dict_cadastro)
        
def validar_aluno(nome, idade, nota1, nota2):
    if not nome:
        return "Nome não pode ser vazio."
    elif idade < 17:
        return "Idade deve ser maior ou igual a 17."
    elif not (0 <= nota1 <= 10) or not (0 <= nota2 <= 10):
        return "Notas devem estar entre 0 e 10."
    return None

def cadastrar_alunos(nome_candidato, idade_candidato, nota1, nota2, dict_cadastro):
    
    validacao=validar_aluno(nome_candidato, idade_candidato, nota1, nota2)
    if validacao:
        print(validacao)
        return
    dict_cadastro[nome_candidato] = {'idade': idade_candidato, 'notas': [nota1, nota2]}
    print("Candidato aluno cadastrado com sucesso! Bem-vindo à faculdade.")
        
def remover_alunos(nome_aluno, dict_cadastro):
    if nome_aluno in dict_cadastro:
        del dict_cadastro[nome_aluno]
        print(f'O Aluno {nome_aluno} foi removido da lista.\n')
    else:
        print(f'O Aluno {nome_aluno} não encontrado.\n')
                     
def  listar_alunos(dict_cadastrados):

    dicionario_filtrado = dict(sorted(dict_cadastrados.items()))
    print('============ Lista de Alunos Cadastrados ===========')
    print(f"{'Nome':<20} {'Idade':<5} {'Primeira Prova':<5} {'Segunda Prova':<5}  {'Média':<5}")

    for nome_aluno, info in dicionario_filtrado.items():   
        primeira_prova = info['notas'][0]
        segunda_prova = info['notas'][1]
        media = (primeira_prova + segunda_prova) / 2 
        print(f"{nome_aluno:<22} {info['idade']:<10} {primeira_prova:<13.2f} {segunda_prova:<9.2f} {media:<5.2f}")

def pesquisar_alunos (nome_aluno, dict_cadastrados):
    if nome_aluno in dict_cadastrados:
        primeira_prova = dict_cadastrados[nome_aluno]['notas'][0]
        segunda_prova = dict_cadastrados[nome_aluno]['notas'][1]
        print(f"idade: {dict_cadastrados[nome_aluno]['idade']}\n"
        f"Primeira Fase: {primeira_prova}\n"
        f"Segunda Fase: {segunda_prova}\n")

def menu():
    print(f'\nMenu\n'
          f'1.Adicionar ou Atualizar\n'
          f'2.Listar todos os alunos\n'
          f'3.Pesquisar os dados de um aluno\n'
          f'4.Remover os dados de um aluno do dicionário\n'
          f'5.sair do programa\n')
          
#------- Programa Principal -------

dict_cadastro_alunos = {
    'Carlos': {'idade': 17, 'notas': [7.5, 8.0]},
    'Fernanda': {'idade': 18, 'notas': [9.0, 9.3]},
    'Ricardo': {'idade': 20, 'notas': [6.0, 7.5]},
    'Juliana': {'idade': 19, 'notas': [8.8, 9.1]},
    'Lucas': {'idade': 18, 'notas': [9.6, 9.7]},
    'Patrícia': {'idade': 17, 'notas': [5.5, 6.0]},
    'Gustavo': {'idade': 21, 'notas': [10.0, 10.0]},
    'Sofia': {'idade': 19, 'notas': [8.0, 7.5]},
    'Leonardo': {'idade': 22, 'notas': [6.5, 6.0]},
    'Camila': {'idade': 18, 'notas': [9.5, 9.8]}
}

while True:
    menu()
    op = input('Opção: ').strip()
    
    match op:
        
        case '1':
            while True:
                dados_alunos(dict_cadastro_alunos)
                op = input('Deseja cadastrar mais Alunos? 1.Sim ou 2.Não').strip()      
                if op == '1':
                    continue
                elif op == '2':
                    print('Retornando ao Menu')
                    break
                else:
                    print("Opção Invalida! Verifique o campo e tente novamente")
            
        case '2':
            if dict_cadastro_alunos:
                listar_alunos(dict_cadastro_alunos)
        
        case '3':
            nome_aluno = input("Nome do Aluno: ").strip().capitalize()
            if nome_aluno:
                pesquisar_alunos(nome_aluno, dict_cadastro_alunos)
            else:
                print("Opção Invalida! Verifique o campo e tente novamente")
                
        case '4':
            while True:
                nome_aluno = input("Nome do Aluno: ").strip().capitalize()
                if nome_aluno:
                    remover_alunos(nome_aluno, dict_cadastro_alunos)
                else:
                    print("Opção Invalida! Verifique o campo e tente novamente")
                     
                op = input('Deseja Excluir mais Alunos? 1.Sim ou 2.Não').strip()
                if op == '1':
                    continue
                elif op == '2':
                    print('Retornando ao Menu')
                    break
                else:
                    print("Opção Invalida! Verifique o campo e tente novamente")
        case '5':
            print("Até Breve!")
            
        case _:
            print("Opção invalida! Verifique o campo e tente novamente")
''' 
#------ cadastro atleta 
'''
def cabecalho (texto):
    print(texto)
    print(f"{'Nome':<20} {'Idade':<4} {'Nacionalidade':<10} {'Rancking'}")

def dados_atletas(dict_modalidades):
    nome_atleta = pega_str_vazia('Nome do Atleta: ').capitalize()
    idade_atleta = pega_int_positivo('Idade: ')
    nacionalidade = pega_str_vazia('Nacionalidade: ').capitalize()
    modalidade = pega_str_vazia('Modalidade: ').capitalize()
    rancking = pega_int_positivo('Posição no Rancking da Modalidade: ')
        
    cadastrar_atualizar_atleta(nome_atleta, idade_atleta, nacionalidade, modalidade, rancking, dict_modalidades)

def cadastrar_atualizar_atleta(nome_atleta, idade_atleta, nacionalidade, modalidade, rancking, dict_modalidades):
    if modalidade not in dict_modalidades:
        dict_modalidades[modalidade]={}
    
    dict_modalidades[modalidade][nome_atleta] = {'idade': idade_atleta, 'nacionalidade': nacionalidade, 'rancking': rancking}
    print(f'Atleta: {nome_atleta} Adicionado a Base de Dados.')

def listar_atletas(modalidade,dict_modalidades):
    cabecalho(f'============ Lista de Atletas - {modalidade} ===========')
    if modalidade in dict_modalidades:
        for nome_atleta, dados in dict_modalidades[modalidade].items():
            print(f"{nome_atleta:<22} {dados['idade']:<10} {dados['nacionalidade']:<13} {dados['rancking']:<4}")    
    else:
        print('Lista de Atletas ainda não foi preenchida')
            
def pesquisar_atleta (nome_atleta, modalidade, dict_modalidades):
    if modalidade in dict_modalidades and nome_atleta in dict_modalidades[modalidade]:
        info = dict_modalidades[modalidade][nome_atleta]
        cabecalho(f'============ Atleta - {nome_atleta} ===========')
        print(f"Nome: {nome_atleta} "
              f"Idade: {info['idade']} "
              f"Nacionalidade: {info['nacionalidade']} "
              f"Modalidade: {modalidade} "
              f"Rancking: {info['idade']} ")
    else:
        print('Atleta não encontrado')

def menu():
    print(f'\nMenu\n'
          f'1.Adicionar ou Atualizar\n'
          f'2.Listar todos os atletas de uma Modalide Especifica\n'
          f'3.Pesquisar os dados de um Atleta\n'
          f'4.Remover os dados de um Atleta do dicionário\n'
          f'5.Sair do programa\n')
    
#-------------- Programa principal ------------
dict_modalidades={}

while True: 
    menu()
    op = pega_str_vazia('Opção: ')
    
    match op:
        
        case '1':
            while True:
                dados_atletas(dict_modalidades)
                op = input('Deseja cadastrar mais Alunos? 1.Sim ou 2.Não').strip()      
                if op == '1':
                    continue
                elif op == '2':
                    print('Retornando ao Menu')
                    break
                else:
                    print("Opção Invalida! Verifique o campo e tente novamente")
            
        case '2':
            modalidade = pega_str_vazia('Qual modalidade será Listada? ')
            if dict_modalidades:
                listar_atletas(modalidade,dict_modalidades)
        
        case '3':
            nome_atleta = pega_str_vazia("Nome do Atleta: ").strip().capitalize()
            modalidade = pega_str_vazia("Modalidade: ").strip().capitalize()
            pesquisar_atleta(nome_atleta, modalidade, dict_modalidades)

        case '4':
            while True:
                nome_atleta = input("Nome do Aluno: ").strip().capitalize()
                if nome_atleta:
                    # remover_aleta(nome_atleta, dict_modalidades)
                # else:
                    print("Opção Invalida! Verifique o campo e tente novamente")
                     
                op = input('Deseja Excluir mais Alunos? 1.Sim ou 2.Não').strip()
                if op == '1':
                    continue
                elif op == '2':
                    print('Retornando ao Menu')
                    break
                else:
                    print("Opção Invalida! Verifique o campo e tente novamente")
        case '5':
            print("Até Breve!")
'''
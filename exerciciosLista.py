from os import system
system('cls')
import math
#-------- Média de Notas -----------
'''
lista_de_notas=[]
cont = 1
while True:
    nota=float(input(f'Nota {cont}: '))
    if nota==-1:
        break
    else:
        lista_de_notas.append(nota)
    cont+=1
    
if lista_de_notas:
    media=sum(lista_de_notas)/len(lista_de_notas)        
    print(f'Notas do aluno: {lista_de_notas}')
    print(f'Media do aluno: {media}')
else:
    print('Lista vazia')
'''
#--------- Lista de Compras ------------
'''
cont=1
lista_compras = []
print('Passe o produto pelo leitor: ')
while True:
    produto=input(f'Produto {cont}: ')
    if not produto.strip():  # .strip() remove espaços em branco extras
        print("Produto vazio. Por favor, insira um nome válido.")
        continue
    if produto.lower()=='fim':
        break
    cont+=1
    lista_compras.append(produto)
    
if lista_compras:
    print('Lista finalizada:')
    for item in lista_compras:
        print(item)
else:
    print('item vazio. Verifique e dicione o produto novamente')
'''
#-------- Estatistica de Acidentes entre Cidades------------
'''
lista_de_cidades = ['araraquara', 'campinas', 'sao carlos', 'ribeirao preto','sao jose do rio preto']
lista_de_acidentes= [20, 80, 80, 15, 15]
lista_cidades_com_mais_acidentes = []
lista_cidades_com_menos_acidentes = []

total_acidentes = sum(lista_de_acidentes)
print(f'Total de acidentes na região é de: {total_acidentes}')
media_acidentes_total = sum(lista_de_acidentes)/len(lista_de_acidentes)
print(f'Media entre todas as cidades: {media_acidentes_total:.2f}')  

maior_num_acidentes = max(lista_de_acidentes)
for i in range(len(lista_de_acidentes)):
    if lista_de_acidentes[i] == maior_num_acidentes:
        lista_cidades_com_mais_acidentes.append((lista_de_cidades[i], lista_de_acidentes[i]))
print(f'Cidade(s) com mais acidentes: {lista_cidades_com_mais_acidentes}')

menor_num_acidentes=min(lista_de_acidentes)
for i in range(len(lista_de_acidentes)):
    if menor_num_acidentes == lista_de_acidentes[i]:
        lista_cidades_com_menos_acidentes.append((lista_de_cidades[i], lista_de_acidentes[i]))
print(f'Cidade(s) com menos acidentes: {lista_cidades_com_menos_acidentes}')
'''
#----------------- Aula de Funções --------------------
'''
def somar(a, b):
    print('O resultado da soma é de: ', a+b)

def subtrair(a, b):
    print('O resultado da subtração é de: ', a-b)

def multiplicar(a,b):
    print('O resultado da multiplicação é de: ', a*b)

def dividir(a ,b):
    if b==0:
        print('Não é possivel a dividir por 0')
    print('O resultado da Divisão é de: ', a/b)

def menu():
        print('Escolha uma operação:\n1:Soma \n2:Subtração \n3:Multiplicação \n4:Divisão \n5:Sair')
            
#-------- programa principal
while True:
    menu()
    op=input()
    a=int(input('Valor de a: '))
    b=int(input('Valor de b: '))
    
    match op:
        case '1':
            somar(a,b)
            print('\n')
        case '2':
            subtrair(a,b)
            print('\n')
        case '3':
            multiplicar(a,b)
            print('\n')
        case '4': 
            dividir(a,b)
            print('\n')
        case '5':
            print('Até breve!')
            break
        case _ :
            print('Operação invalida')
            print('\n')
'''
#-------------- Calc Area de FIguras--------------
'''
def AreaQuadrado():
    lado=float(input('Lado: '))
    print('Area de quadrado é de: ', lado*lado)
    
def AreaCirculo():
    raio=float(input('Raio: '))
    area=math.pi*(raio**2)
    print(f'Area de Circulo é de: {area:.2f}')
    
def AreaTriangulo():
    base=float(input('Base: '))
    altura=float(input('Altura: '))
    print('Area de TRiangulo é de: ', base*altura)

def AreaTrapezio():
    base_maior=float(input('Base maior: '))
    base_menor=float(input('Base menor: '))
    altura=float(input('Altura: '))
    print('Area de quadrado é de: ', ((base_maior+base_menor)*altura)/2)
    
def menu():
    print('Escolha uma figura:\n'
          '1:Quadrado, 2:Circulo, 3:Triangulo, 4:Trapezio, 5:Sair')

#---- Programa Principal

while True:
    menu()
    op=input()
    match op:
        case '1':
            AreaQuadrado()
        case '2':
            AreaCirculo()
        case '3':
            AreaTriangulo()
        case '4':
            AreaTrapezio()
        case '5':
            print('Até breve!')
            break
        case _:
            print('Operação invalida')
            
'''
#--------- Carrinho de Conpra ----------
'''
def showList(list):
    if list:
        for i, item in enumerate(list,1):
            print(f'{i:{item}}')
    else:
        print('Carrinho Vazio')
            
def addItem(list):
    while True:
        item=input('Qual item iremos Adicionar: ').strip()
        if item != "":
            list.append(item)
            break
        else:
            print('Produto Invalido, linha vazia')

def remvItem(list):
    while True:
        print(lista_de_produtos)
        item=input('Qual item iremos Adicionar: ').strip()
        if item != "":
            list.remove(item)
            break
        else:
            print('Produto Invalido, Linha vazia')
            
def options():
    print('1:Exibir carrinho de compras:'
          '\n2:Adicionar produtos ao Carrinho'
          '\n3:Remosver item: '
          '\n4:Abandonar Carrinho')

#---- Programa Principal
lista_de_produtos = []
cont_item=0
while True:
    options()
    carrinho=input().strip()
    match carrinho:
        case '1':
            showList(lista_de_produtos)
        case '2':
            addItem(lista_de_produtos)
            print(f'Produto Adicionado com Sucesso: {lista_de_produtos}')         
        case '3':
            remvItem(lista_de_produtos)
            print(f'Produto Removido com Sucesso: {lista_de_produtos}')
        case '4':
            lista_de_produtos.clear
            print('Carrinho de Compras esvaziado. Até breve!')
            break
'''
#--------- Gerenciador de Tarefas --------
'''
def opcoes():
    print('1.Adicionar tarefa \n'
          '2.Remover tarefa\n'
          '3.Listar tarefas\n'
          '4.Marcar tarefa como Concluida\n'
          '5.Listas tarefas Concluidas\n'
          '6.Listas tarefas Pendentes\n'
          '7.Sair')
    
def adicionar_tarefa(list, tarefa): 
    while True:
            list.append([tarefa, 'false'])
            print('Tarefa Adicionada com Sucesso!\n')
            while True:
                add=input('Deseja Add outra tarefa? S ou N: ').strip().upper()
                if add == 'S':
                    tarefa=input('Qual a nova tarefa? ').strip()
                    if tarefa != "":
                        list.append([tarefa, 'false'])
                    break
                elif add == 'N':
                    return
                else:
                    print('Opção invalida')

def remover_tarefa(list, tarefa):
    for item in list:
        if item[0]==tarefa:
            list.remove(item)
            print('Tarefa Removida com Sucesso!\n')
            return
        else:
            print('Tarefa não encontrada')
        while True:
            add=input('Deseja Remover outra tarefa? S ou N: ').strip().upper()
            if add == 'S':
                tarefa=input('Qual a nova tarefa? ').strip()
                if tarefa != "":
                    list.remove(tarefa)
                    print('Tarefa Removida com Sucesso!\n')
                break
            elif add == 'N':
                return
            else:
                print('Opção invalida')
            
def listar_tarefas(list):  
    for i,item in enumerate(list,1):
        if item[1] == 'true':
            status = "realizada"
        else:
            status = "tarefa não realizada"
    print(f"{i}.{item[0]: <20} {status: <20} ")   
         
def concluir_tarefa(list, tarefa): 
    for item in list:
        if item[0] == tarefa:
            if item[1]== 'false':
                item[1] = 'true'
                print('Status da Tarefa alterado com Sucesso!\n')
                break
            else:
                print('Tarefa ja realizda')
                break
        else:
            print('Tarefa não encontrada')

# def exibir_tarefas_conclidas(list):
#     for i, item in enumerate(list,1):
#          if item[1] == 'true':
#             print(f'{i}:{item[0]}')
                
# def exibir_tarefas_pendentes(list):
#     for i, item in enumerate(list,1):
#          if item[1] == 'false':
#             print(f'{i}:{item[0]}') 
def exibir_tarefas_filtradas(list,situacao):
    lista_filtrada=[]
    for item in list:
        if item[0]==situacao:
            lista_filtrada.append(item)
    if situacao==True:
        print('-- Tarefas Realizadas --')
    else:
        print('-- Tarefas Pendentes --')
    for i,item in enumerate(lista_filtrada,1):
        print(f'{i}:{item[0]}')
    
#---------- Programa Principal -----------
lista_de_tarefas = []

while True:
    opcoes()
    op=input()
    match op:
        case '1':
            tarefa=input('Qual a nova tarefa? ').strip()
            if tarefa != "":
                adicionar_tarefa(lista_de_tarefas, tarefa)
            else:
                print('Linha vazia')
        case '2':
            tarefa=input('Qual tarefa será removida? ').strip()
            if tarefa != "":
                remover_tarefa(lista_de_tarefas, tarefa)
            else:
                print('Linha vazia')
        case '3':
            if lista_de_tarefas:
                listar_tarefas(lista_de_tarefas)
            else:
                print("Sem Tarefas Planejadas\n")
        case '4':
            tarefa=input('Qual tarefa foi concluida? ').strip()
            if tarefa!="":
                concluir_tarefa(lista_de_tarefas, tarefa)
            else:
                print('Linha vazia')
        case '5': 
            if lista_de_tarefas:
                #exibir_tarefas_conclidas(lista_de_tarefas)
                exibir_tarefas_filtradas(lista_de_tarefas, True)
        case '6': # Tarefas Pendentes
            if lista_de_tarefas:
                #exibir_tarefas_pendentes(lista_de_tarefas)
                exibir_tarefas_filtradas(lista_de_tarefas, False)
        case '7': 
            print('Até Breve!')
            break

'''        
#------- Estatistica de Acidentes 2.0 ------
''' 
def adicionar_dados(list,city,acident):
    sub_list=[city,acident]
    list.append(sub_list)
    print(f'{city} Adicionada com Sucesso!')
    while True:
        add=input('Deseja Adicionar dados de oitras Cidades? ').strip().lower()
        try:
            if add == 's':
                cidade=input('Cidade a ser Relacionada: ').strip()
                acidentes=int(f'Numero de Acidentes de {cidade}: ').strip()
                sub_list=[cidade,acidentes]
                list.append(sub_list)
                print(f'{cidade} Adicionada com Sucesso!')
                break
            elif add =='n':
                return
            else:
                print('Opção Invalida')        
        except:
            print('Dados Incongruentes, Verifique linhas Vazias')
        
def remover_dados(list, city):
    for item in list:
        if item[0]==city:
            list.remove(item)
            print(f'{item} Foi removida da relação com Sucesso')
    while True:
        remover=input('Deseja Remover dados de outras Cidades? ').strip().lower()
        try:
            if remover == 's':
                cidade=input('Cidade a ser Relacionada: ').strip()
                for item in list:
                    if item[0]==cidade:
                        list.remove(item)
                        print(f'{item} Foi removida da relação com Sucesso')
                        break
            elif remover =='n':
                return
            else:
                print('Opção Invalida')
        except:
            print('Dados Incongruentes, Verifique linhas Vazias')
            
def calc_dados(list, Boleano, list_filtered_bigger, list_filtered_smaller):
    if Boleano==True:
        total_acidentes=sum(item[1] for item in list)
        print(f'O Numero de Acientes Somados é de: {total_acidentes}')
        
        media_acidentes=sum(item[1] for item in list)/len(list)
        print(f'o Numero médio entre as cidades é de: {media_acidentes}')
    else:
        maior_numero=max(sub_list[1] for sub_list in list)
        menor_numero=min(sub_list[1] for sub_list in list)
        for item in list:
            if maior_numero == item[1]:
                list_filtered_bigger.append(item)
            elif menor_numero == item[1]:
                list_filtered_smaller.append(item)
                
        print('----- Maior Numero de Acidentes -----')       
        for i, item in enumerate(list_filtered_bigger):
            print(f'{i}:{item[0]} - {item[1]}')
        
        print('----- Menor Numero de Acidentes -----')       
        for i, item in enumerate(list_filtered_smaller):
            print(f'{i}:{item[0]} - {item[1]}')

def exibir_cidades(list):
    for i, item in enumerate(list,1):
        print(f'{i}:{item[0]} - {item[1]}')

def menu():
    print('\nMenu de opções\n'
          '1.Adicionar dados do acidente\n'
          '2.Remover dados da cidade\n'
          '3.Calcular total e média de acidentes\n'
          '4.Encontrar o maior e o menor número de acidentes e as respectivas cidades\n'
          '5.Listar todas as cidades\n'
          '6.Sair')

#--------- programa principal---------
lista_dados_cidades=[["Araraquara", 150],["Brotas", 75],["São Carlos", 150],["Matão", 90 ]]
lista_maiores_filtro=[]
lista_menores_filtro=[]
print('Bem vindo ao App de Controle e Estatisca de Acidentes')
while True:
    menu()
    op=input('Qual opção iremos Tabalhar? ')
    match op:
            case '1': #Adicionar
                while True:
                    try:
                        cidade=input('Cidade a ser Relacionada: ').strip().title()
                        for item in lista_dados_cidades:
                            if cidade == item[0]:
                                print('Cidade ja Cadastrada')
                                break
                        else:
                            acidentes=int(input(f'Numero de Acidentes de {cidade}: '))
                    
                        adicionar_dados.append(lista_dados_cidades, cidade, acidentes)
                        break
                    except:
                        print('Dados Incongruentes, Verifique Linhas Vazias')
            
            case '2': # Remover
                while True:
                    try:
                        cidade=input('Qual Cidade será retirada: ').strip()
                        remover_dados(lista_dados_cidades, cidade)
                        break
                    except:
                        print('Dados Incongruentes, Verifique Linhas Vazias')
                
            case '3': #Calcular Media e Total
                if lista_dados_cidades:
                    calc_dados(lista_dados_cidades, True)
                else:
                    print('Sem Dados Relatados')
                    
            case '4': #Pegar Max e Min
                if lista_dados_cidades:
                    calc_dados(lista_dados_cidades, False, lista_maiores_filtro, lista_menores_filtro)
                else:
                    print('Sem Dados Relatados')
            case '5': # Exibir Cidades
                if lista_dados_cidades:
                    exibir_cidades(lista_dados_cidades)
                else:
                    print('Sem Dados Relatados')
                
            case '6': # Sair
                print('Até Breve')
                break
                
            case _:
                print('Opção invalida')

#----- Controle de Estoque -----

def adicionar_produto(cod, product, qntd, list):
    sub_list=[cod, product, qntd]
    list.append(sub_list)
    print(f'{product} Adicionado com Sucesso ao Estoque')

def exibir_estoque(list):
    for i, item in enumerate(list,1):
        print(f'Cod:{item[0]}: {item[1]} - Qntd: {item[2]} ')
        
def remover_produto(cod, descript, list, booln):
    if booln == True:  
        for item in list:
            if item[0] == cod:
                print(f'Produto {item[1]} Removido com Sucesso')
                list.remove
            else:
                print('Produto não encontrado')
    else:
        for item in list:
            if item[1] == descript:
                print(f'Produto {item[1]} Removido com Sucesso')
                list.remove
            else:
                print('Produto não encontrado')
            
def manipular_produto(cod, descript, list, booln):
    qntd=int(input('Quantidade: '))
    if booln == True:
        for item in list:
            if item[0] == cod:
                item[2] = qntd
                print(f'A Quantidade em Estoque do Produto: {item[1]}, foi alterada para: {item[2]}')
    else:
        for item in list:
            if item[1] == descript:
                item[2] = qntd
                print(f'A Quantidade em Estoque do Produto: {item[1]}, foi alterada para: {item[2]}')
                
def menu():
    print('\nMenu de Opções\n'
          '1. Cadastrar Produto\n'
          '2. Exibir Estoque\n'
          '3. Remover Cadastro do Produto\n'
          '4. Registrar Entrada de Produto\n'
          '5. Registrar Saida de Produto\n'
          '6. Fechar o Programa\n')
                   
#---- Programa Principal
lista_estoque=[[1, 'Arroz', 40], [2, 'Feijao', 120], [3, 'Espaguete',30], [4, 'Linguine', 35], [5, 'fusili', 40]]

while True:
    maior_numero_registro=max(sub_list[0] for sub_list in lista_estoque)+1
    menu()
    op=input('Qual Ação irá ser Executada:')   
    match op:
        case '1': # Cadastrar Nomvo Produto
            produto=input('Informe o produto a ser Cadastrado no Estoque: ').strip().title()
            if produto !="":
                for produtos in lista_estoque:
                    if produto == produtos[1]:
                        print('Produto ja Cadastradado.\n'
                                'Com o Numero de Registro: ', produtos[0])
                else:
                    num_registro=maior_numero_registro
                    qntd=int(input('Informe a quantidade da Entrada: '))
                    adicionar_produto(num_registro, produto, qntd, lista_estoque)
            else:
                print('Informação Invalida')        
        case '2': # Exibir Lista
            if lista_estoque:
                exibir_estoque(lista_estoque)
            else:
                print('Sem Produtos Cadastrados')            
        case '3': # Remover
            opt=input('Vamos produrar pelo 1.Cod ou pela 2.Descrição:').strip()
            if opt !="":
                if opt == '1':
                    cod_produto=input('Digite o Codigo do Produto: ').strip
                    int(cod_produto)
                    if not opt == "":
                        remover_produto(cod_produto, lista_estoque, True)
                    else:
                        print('Dados Incongruentes')
                elif opt == '2':
                    nome_produto=input('Informe o Nome do Produto: ').strip().title      
                    if not opt == "":
                        remover_produto(nome_produto, lista_estoque, False)
                    else:
                        print('Dados Incongruentes')
                else:
                    print('Dados Incongruentes')
            else:
                print('Dados Incongruentes')
        case '4': # Entrada de Estoque
            opt=input('Vamos procurar pelo 1.Cod ou pela 2.Descrição:').strip()
            if opt !="":
                if opt == '1':
                    cod_produto=input('Digite o Codigo do Produto: ').strip
                    int(cod_produto)
                    if not opt == "":
                        manipular_produto(cod_produto, lista_estoque, True)
                    else:
                        print('Dados Incongruentes')
                else:
                    nome_produto=input('Informe o Nome do Produto: ').strip().title      
                    if not opt == "":
                        manipular_produto(nome_produto, lista_estoque, False)
                    else:
                        print('Dados Incongruentes')
        case '5': # Saida de Estoque
            opt=input('Vamos produrar pelo 1.Cod ou pela 2.Descrição:').strip()
            if opt !="":
                if opt == '1':
                    cod_produto=input('Digite o Codigo do Produto: ').strip
                    int(cod_produto)
                    if not opt == "":
                        manipular_produto(cod_produto, lista_estoque, True)
                    else:
                        print('Dados Incongruentes')
                else:
                    opt=input('Informe o Nome do Produto: ').strip().title      
                    if not opt == "":
                        manipular_produto(nome_produto, lista_estoque, False)
                    else:
                        print('Dados Incongruentes')
        case '6': # Encerrar
            print('Até Breve')
            break      
        case _:
            print('Opção Invalida')
'''

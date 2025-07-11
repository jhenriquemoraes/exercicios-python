import os
limpar_tela = lambda: os.system("cls")
limpar_tela()
from entrada_dados import pega_int_positivo, pega_str_vazia

#---------- Inventario de Produtos

nome_arquivo = "Inventario.txt"

def adicionar_produto(nome_produto, qntd_produto):
    try:
        with open(nome_arquivo, 'a') as arquivo:
            arquivo.write(f"{nome_produto}:{qntd_produto}\n")
            print(f'Produto Adicionado com sucesso')
    except IOError:
        print("Erro: no acesso e ou abertura do Arquivo")
    except PermissionError:
        print("Erro: Permissão de acesso ao Arquivo")
    except Exception as e:
        print(f"Erro: inesperado {e}")
        
def listar_inventario():
    try:
        with open(nome_arquivo,'r') as arquivo:
            print('--------Inventario de Produtos--------')
            print(f"{'Produtos': <30}{'Quantidade':10}")
            for linha in arquivo:
                produto, quantidade = linha.strip().split(":")
                print(f"{produto: <30}{quantidade:10}")
                
    except FileNotFoundError:
        print("Erro: arquivo não encontrado")
    except IOError:
        print("Erro: no acesso e ou abertura do Arquivo")
    except PermissionError:
        print("Erro: Permissão de acesso ao Arquivo")
    except Exception as e:
        print(f"Erro: inesperado {e}")
        
def atualizar_produto(nome_produto):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
    
    except IOError:
        print("Erro: no acesso e ou abertura do Arquivo")
    except PermissionError:
        print("Erro: Permissão de acesso ao Arquivo")
    except Exception as e:
        print(f"Erro: inesperado {e}")
    try:
        with open(nome_arquivo,'w') as arquivo:
            achou_produto = False
            for linha in linhas:
                if linha.startswith(f"{nome_produto}"):
                    quantidade_produto=pega_int_positivo("Digite a Quantidade")
                    arquivo.write(f"{nome_produto}:{quantidade_produto}\n")
                    achou_produto = True
                else:
                    arquivo.write(linha)            
        print(f"Produto: {nome_produto} atualizado com sucesso" if achou_produto else f"Produto: {nome_produto} não encontrado")
    except IOError:
        print("Erro: no acesso e ou abertura do Arquivo")
    except PermissionError:
        print("Erro: Permissão de acesso ao Arquivo")
    except Exception as e:
        print(f"Erro: inesperado {e}")
               
def remover_produto(nome_produto):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
    
    except IOError:
        print("Erro: no acesso e ou abertura do Arquivo")
    except PermissionError:
        print("Erro: Permissão de acesso ao Arquivo")
    except Exception as e:
        print(f"Erro: inesperado {e}")
        
    try:
        with open(nome_arquivo,'w') as arquivo:
            achou_produto = False
            for linha in linhas:
                if linha.startswith(f"{nome_produto}"):
                    achou_produto = True
                    #Apagar um informação no arquivo, é iteralo, e não reescrever
                else:
                    arquivo.write(linha)            
        print(f"Produto: {nome_produto} foi Excluido com sucesso" if achou_produto else f"Produto: {nome_produto} não encontrado")
        
    except IOError:
        print("Erro: no acesso e ou abertura do Arquivo")
    except PermissionError:
        print("Erro: Permissão de acesso ao Arquivo")
    except Exception as e:
        print(f"Erro: inesperado {e}")
        
def bucar_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                produto, quantidade = linha.strip().split(":")
                if nome_produto == produto:
                    print('--------Inventario de Produtos--------')
                    print(f"{'Produtos': <30}{'Quantidade':10}")
                    print(f"{produto: <30}{quantidade:10}")
                    return
            print(f"Produto: {nome_produto} não encontrado")
            
    except IOError:
        print("Erro: no acesso e ou abertura do Arquivo")
    except PermissionError:
        print("Erro: Permissão de acesso ao Arquivo")
    except Exception as e:
        print(f"Erro: inesperado {e}")
        
def menu():
    print(f"Menu de Opçãoes\n"
          f"1.Adicionar um produto\n"
          f"2.Listar o inventario\n"
          f"3.Atualizar um produto\n"
          f"4.Remover um produto\n"
          f"5.Bucar um produto\n"
          f"6.Sair\n")

# ---- programa primcipal -----

while True:
    limpar_tela()
    menu()
    
    op = input("Explore uma opção: ")
    
    match op:
        case '1': #Adicionar produto
            nome_produto=pega_str_vazia("Digite o Nome do Produto: ")
            qntd_produto=pega_int_positivo("Digite a Quantidade do Produto: ")
            
            adicionar_produto(nome_produto,qntd_produto)
            
            input("Enter para continuar")
            
        case '2': #listar produto
            try:
                if os.path.getsize(nome_arquivo)>0:
                    listar_inventario()
                else:
                    print("Inventario de produtos vazio")
            except FileNotFoundError:
                print("Arquivo não encontrado")
            input("Enter para continuar")
            
        case '3': #Atualizar quantidade produto
            try:
                if os.path.getsize(nome_arquivo)>0:
                    nome_produto = pega_str_vazia("Digite o Nome do produto: ")
                    atualizar_produto(nome_produto)
                else:
                    print("Imventario de produtos vazio")
            except FileNotFoundError:
                print("Arquivo não encontrado")
            input("Enter para continuar")
            
        case '4': #Remover produto
            try:
                if os.path.getsize(nome_arquivo)>0:
                    nome_produto = pega_str_vazia("Digite o Nome do produto: ")
                    remover_produto(nome_produto)
                else:
                    print("Imventario de produtos vazio")
            except FileNotFoundError:
                print("Arquivo não encontrado")
            input("Enter para continuar")
            
        case '5': #Bucar produto
            try:
                if os.path.getsize(nome_arquivo)>0:
                    nome_produto = pega_str_vazia("Digite o Nome do produto: ")
                    remover_produto(nome_produto)
                else:
                    print("Imventario de produtos vazio")
            except FileNotFoundError:
                print("Arquivo não encontrado")
            input("Enter para continuar")
            
        case '6': #Sair
            input("Enter para continuar")
            limpar_tela()
            break
            
        case '_': 
            input("Opção invalida")
def pega_str_vazia(texto):
    while True:
        valor=input(texto).strip()
        if texto != "":
            return valor
        else:
            print("Erro: Campo não pode ser Vazio!")

def pega_int_positivo(texto):
    while True:
        try:
            valor = int(input(texto))
            if valor>0:
                return valor
            else:
                print("O campo não pode ser Negativo")
        except ValueError:
            print("O Campo não pode ser Vazio!")
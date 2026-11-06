def menu_vis():
    """Visualização do menu de opções"""

    print("="*50)
    print("| PROGRAMA DE INVENTÁRIO SOUL X |\n")
    print("Selecione uma opção:")
    print("1) Entrada")
    print("2) Saída")
    print("3) Visualizar")
    print("4) Alterar")
    print("5) Sair")
    print("="*50)
    return True

def user_menu_input():
    """Loop de selecao de processo atraves de entradas"""

    input_entry = int(input("Escolha uma opção: "))

    match input_entry:
        case 1:
            print("Entrada")
        case 2:
            print("Saída")
        case 3:
            #Visualizar
            pass
        case 4:
            #Alterar
            pass
        case 5:
            return False
    return True
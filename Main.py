import Menu
import Armazenamento

inventario = Armazenamento.carregar_inventario()

while True:

    Menu.menu_vis()

    if Menu.user_menu_input() == False:
        print("Encerrando programa!")
        break


print(inventario)
import Menu

while True:

    Menu.menu_vis()

    if Menu.user_menu_input() == False:
        print("Encerrando programa!")
        break
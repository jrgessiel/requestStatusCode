from title import title
from clear import clear
from request_ import request_

def menu():
    title()
    print('##01 | Começar')
    print('##02 | Créditos')
    print('##00 | Fechar progama')
    try:
        choice_menu = int(input('\n| '))

        if choice_menu == 1:
            clear()
            title()
            request_()
        elif choice_menu == 2:
            clear()
            title()
            print('- Me chamo Gessiel Júnior e este projeto faz parte do meu portfólio pessoal.')
            print('- Ficarei feliz se você puder fornecer algum feedback sobre o projeto, \ncódigo, estrutura ou qualquer relato que possa me tornar um desenvolvedor melhor!\n')
            menu()
        elif choice_menu == 0:
            clear()
            title()
            input('- Clique em qualquer lugar para encerrar.')

        else:
            clear()
            print('Insira um número dentro do alcance permitido!\n')
            menu()
    except ValueError as error:
        clear()
        print('Por favor insira apenas um dos números esperado.\n')
        menu()
menu()

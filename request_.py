import requests
from clear import clear
from title import title

def m_request_():
    change = str(input('\nDeseja verificar outros sites? (S | N) ')).lower()
    if change == 's':
        clear()
        title()
        request_()

    elif change == 'n':
        clear()
        title()
        print('Okay. Obrigado por usar o aplicativo.')
    else:
        clear()
        title()
        print('Insira um valor dentro do alcance permitido! (S | N)\n')
        m_request_()

def request_():
    print('- Insira as URLs dos sites para verificar o seu status.')
    urls = str(input()).lower().split(',')
    for url in urls:
        url = url.strip()
        if '.' not in url:
            print(url, '| Esta URL é inválida e/ou desconhecida. \n')
        else:
            if 'http' not in url:
                url = f'http://{url}'
            try:
                r_url = requests.get(url)
                if r_url.status_code == 200:
                    print(f'\n{url} | O site está ligado.')
                else:
                    print(f'{url} | O site está desligado.')
                    print('')
            except:
                print(f'\n{url} | Erro inesperado, por favor refaça a verificação.')
    m_request_()

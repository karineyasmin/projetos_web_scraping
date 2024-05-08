# version 1.0
# Autor: Karine Yasmin

import requests
from bs4 import BeautifulSoup

html = requests.get('https://www.scrapethissite.com/pages/simple/').text

html_parsed = BeautifulSoup(html, 'html.parser')
html_parsed.find(class_ = 'country-name').text.strip()
html_parsed.find(class_ = 'country-capital').text.strip()

lista_paises = [pais.text.strip() for pais in html_parsed.find_all(class_ = 'country-name')]
lista_capitais = [capital.text.strip() for capital in html_parsed.find_all(class_ = 'country-capital')]
dicionario_paises_capitais = dict(zip(lista_paises, lista_capitais))


entrada_usuario =  ''
while True:
    
    entrada_usuario = input('''\n== Você gostaria de saber a capital de qual país? ==
                            
    O nome deve estar em inglês, alguns exemplos:

    Brazil
    Spain
    United Kingdom
    Japan
    United States
    Morocco
    
    Digite 'q' para sair
    
    >> ''').title()
    
    if entrada_usuario == 'Q':
        print('\nEncerrando...')
        break
    
    elif entrada_usuario in dicionario_paises_capitais.keys():
        print(f'\n=== A capital é {dicionario_paises_capitais[entrada_usuario]} ===\n')
        input('Aperte qualquer tecla para voltar ao menu')
        
    else:
        print('\nPaís não encontrado, por favor, verifique a ortografia\n')
        input('Aperte qualquer tecla para voltar ao menu')



    

    
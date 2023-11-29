from funcs import *
from informacao import *

def main():
    while True:
        print('-------------MENU-------------')
        print('1. Funcionalidades')
        print('0. Sair')
        print('------------------------------')

        choice = int(input('Escolha um: '))
        if choice == 0:
            break
        elif choice == 1:
            funcs()

def funcs():
    while True:
        print('---------------------------------------------------------PHASE----------------------------------------------------------')
        # Funcionalidades que vamos ter que implementar
        options = [
            'Consultar o estafeta que utilizou mais vezes um meio de transporte mais ecológico.',
            'Consultar os estafetas que entregaram determinada(s) encomenda(s) a um determinado cliente.',
            'Consultar os clientes servidos por um determinado estafeta.',
            'Calcular o valor faturado pela Green Distribution num determinado dia.',
            'Consultar quais as zonas (e.g., rua ou freguesia) com maior volume de entregas por parte da Green Distribution.',
            'Calcular a classificação média de satisfação de cliente para um determinado estafeta.',
            'Consultar o número total de entregas pelos diferentes meios de transporte, num determinado intervalo de tempo.',
            'Consultar o número total de entregas pelos estafetas, num determinado intervalo de tempo.',
            'Calcular o número de encomendas entregues e não entregues pela Green Distribution, num determinado período de tempo.',
            'Calcular o peso total transportado por estafeta num determinado dia.',
            'Consultar o cliente que fez mais encomendas.',
            'Consultar os estefetas menos pontuais a fazer as suas entregas.',
            'Gerar os circuitos de entrega, caso existam, que cubram um determinado território.',
            'Representar os diversos pontos de entrega (freguesias) disponíveis em forma de grafo.',
            'Identificar quais os circuitos com maior número de entregas (por volume e peso).',
            'Comparar circuitos de entrega tendo em conta os indicadores de produtividade.',
            'Escolher o circuito mais rápido para entregar uma dada encomenda, utilizado um algoritmo de pesquisa.',
            'Escolher o circuito mais ecológico para entregar uma dada encomenda, utilizado um algoritmo de pesquisa.',
            'Identificar quais os circuitos com maior número de entregas.'
        ]

        for i, option in enumerate(options, 1):
            print(f'{i}. {option}')
        print('0. Sair')
        print('-----------------------------------------------------------------------------------------------------------------------')

        user_input = input('Escolha um: ')
        if user_input == '0':
            break
        else:
            print('-----------------------------------------------------------------------------------------------------------------------')
            print(f'Funcionalidade {user_input}')
            funcionalidade()
        

# Function to check if a point is a delivery point
def pontoEntrega(grafo, Input):
    return Input in grafo

# Para já, apenas mostra os caminhos possíveis para um ponto de entrega
def funcionalidade():
    
    print('Territórios disponíveis: ')
    print(grafo.keys())
    print('-----------------------------------------------------------------------------------------------------------------------')
    
    Input = input("Indique o território a consultar: \n")
    
    if pontoEntrega(grafo, Input):
        L = all_paths_to_goal(grafo, Input)
        print(L)
    else:
        print('Não existem informações sobre este território.')

        
if __name__ == "__main__":
    main()

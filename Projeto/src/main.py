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
            'Calcular o valor faturado pela Health Planet num determinado dia.',
            'Consultar quais as zonas (e.g., rua ou freguesia) com maior volume de entregas por parte da Health Planet.',
            'Calcular a classificação média de satisfação de cliente para um determinado estafeta.',
            'Consultar o número total de entregas pelos diferentes meios de transporte, num determinado intervalo de tempo.',
            'Consultar o número total de entregas pelos estafetas, num determinado intervalo de tempo.',
            'Calcular o número de encomendas entregues e não entregues pela Health Planet, num determinado período de tempo.',
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
            funcionalidade(user_input)
        

# Function to check if a point is a delivery point
def pontoEntrega(grafo, Input):
    return Input in grafo

def funcionalidade(option):
    
    def func1():
        print('-----------------------------------------------------------------------------------------------------------------------')
        print('Estafeta que utilizou mais vezes um meio de transporte mais ecológico: ')
        print(get_most_ecological_courier())
        print('-----------------------------------------------------------------------------------------------------------------------')
    
    def func2():
        #'Consultar os estafetas que entregaram determinada(s) encomenda(s) a um determinado cliente.',
        print('Insira o id do cliente: ')
        client_id = int(input())
        print(get_couriers_by_client(client_id))
        print('-----------------------------------------------------------------------------------------------------------------------')
    def func3():
        #'Consultar os clientes servidos por um determinado estafeta.',
        print('Insira o id do estafeta: ')
        estafeta_id = int(input())
        print(get_clientes_by_estafeta(estafeta_id))
        print('-----------------------------------------------------------------------------------------------------------------------')
    def func4():
        #'Calcular o valor faturado pela Health Planet num determinado dia.',
        print('Insira o ano: ')
        ano = int(input())
        print('Insira o mês: ')
        mes = int(input())
        print('Insira o dia: ')
        dia = int(input())
        print(faturamento_diario(ano, mes, dia))
        print('-----------------------------------------------------------------------------------------------------------------------')
    def func5():
        #'Consultar quais as zonas (e.g., rua ou freguesia) com maior volume de entregas por parte da Health Planet.',
        print(freguesiasMaisFrequentes())
        print('-----------------------------------------------------------------------------------------------------------------------')
        
    def func6():
        #'Calcular a classificação média de satisfação de cliente para um determinado estafeta.',
        print('Insira o id do estafeta: ')
        estafeta_id = int(input())
        print(classificacao_media(estafeta_id))
        print('-----------------------------------------------------------------------------------------------------------------------')
        
    def func7():
        #'Consultar o número total de entregas pelos diferentes meios de transporte, num determinado intervalo de tempo.',
        print('Insira a data de início no formato (ano, mês, dia, horas, minutos): ')
        data_inicio = eval(input())
        print('Insira a data de fim no formato (ano, mês, dia,horas, minutos): ')
        data_fim = eval(input())
        print(numeroTotalEntregasTransporte(data_inicio, data_fim))
        
        print('-----------------------------------------------------------------------------------------------------------------------')
    def func13():
        print('-----------------------------------------------------------------------------------------------------------------------')
        print('Territórios disponíveis: ')
        print(grafo.keys())
        print('-----------------------------------------------------------------------------------------------------------------------')
        
        Input = input("Indique o território a consultar: \n")
        
        if pontoEntrega(grafo, Input):
            L = all_paths_to_goal(grafo, Input)
            print(L)
        else:
            print('Não existem informações sobre este território.')

    def func14():
        print('-----------------------------------------------------------------------------------------------------------------------')
        print('Mapa de pontos de entrega: ')
        show_graph(grafo)
        print('-----------------------------------------------------------------------------------------------------------------------')
    #'Identificar quais os circuitos com maior número de entregas (por volume e peso).',
    def func15():
        print('-----------------------------------------------------------------------------------------------------------------------')
        print('Para calcular o circuito com maior número de entregas, escolha uma das opções abaixo: ')
        print('0. Peso')
        print('1. Volume')
        print('-----------------------------------------------------------------------------------------------------------------------')
        weight_or_volume = int(input('Escolha um: '))

        print('Circuito com maior número de entregas: ')
        print(circuit_with_max_deliveries(weight_or_volume, grafo))
        print('-----------------------------------------------------------------------------------------------------------------------')
    case = {
         '1': func1,
         '2': func2,
         '3': func3,
         '4': func4,
         '5': func5,
         '6': func6,
         '7': func7,
        # '8': func8,
        # '9': func9,
        # '10': func10,
        # '11': func11,
        # '12': func12,
        '13': func13,
        '14': func14,
        '15': func15,
        # '16': func16,
        # '17': func17,
        # '18': func18,
        # '19': func19,
        # '20': func20
    }
    
    # Execute a função baseada na opção escolhida
    if option in case:
        case[option]()
    else:
        print("Opção inválida.")
        
if __name__ == "__main__":
    main()

# Import necessary libraries
from auxiliares import *
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

#----------------------------------------Funcionalidade 1----------------------------------------


def most_ecological_courier(couriers):
    max_orders = 0
    max_ids = []

    for courier in couriers:
        order_count = orders_by_bike(courier[0])

        if order_count > max_orders:
            max_orders = order_count
            max_ids = [courier[0]]
        elif order_count == max_orders:
            max_ids.append(courier[0])

    return max_ids

def get_most_ecological_courier():
    couriers = get_all_estafetas()
    most_ecological = most_ecological_courier(couriers)
    
    return most_ecological

#----------------------------------------Funcionalidade 2----------------------------------------
#'Consultar os estafetas que entregaram determinada(s) encomenda(s) a um determinado cliente.',
# Encomenda: #IdEnc, #IdCliente, Peso, Volume, Prazo, DataInicio, DataFim
# Data: #Ano, Mês, Dia, Hora, Minuto
# IdEnc: #12 dígitos

def get_couriers_by_client(client_id):
    lista_de_encomendas = get_encomenta_by_client(client_id)
    lista_de_estafetas = get_estafeta_by_encomenda(lista_de_encomendas)
    
    # Remove duplicates from the list by converting it to a set and then back to a list.
    lista_de_estafetas_unicos = list(set(lista_de_estafetas))
    
    return sorted(lista_de_estafetas_unicos)

#----------------------------------------Funcionalidade 3----------------------------------------
 #'Consultar os clientes servidos por um determinado estafeta.',
 # Encomenda: #IdEnc, #IdCliente, Peso, Volume, Prazo, DataInicio, DataFim
def get_clientes_by_estafeta(estafeta_id):
    lista_de_encomendas = get_encomenda_by_estafeta(estafeta_id)
    lista_de_clientes = get_cliente_from_encomenda(lista_de_encomendas)
    
    # Remove duplicates from the list by converting it to a set and then back to a list.
    lista_de_clientes_unicos = list(set(lista_de_clientes))
    
    return sorted(lista_de_clientes_unicos)

#----------------------------------------Funcionalidade 4----------------------------------------
#'Calcular o valor faturado pela Health Planet num determinado dia.',
def faturamento_diario(ano, mes, dia):
    # Obter todas as encomendas para o dia especificado
    encomendas_do_dia = obter_encomendas_por_dia(ano, mes, dia)

    # Calcular os preços para todas as encomendas do dia
    precos = precos_lista_encomendas(encomendas_do_dia)

    # Retornar o total (faturamento do dia)
    return sum(precos)
 
#----------------------------------------Funcionalidade 5----------------------------------------
#'Consultar quais as zonas (e.g., rua ou freguesia) com maior volume de entregas por parte da Health Planet.',
def freguesiasMaisFrequentes():
    lista_encomendas_dos_estafetas = [estafeta[1] for estafeta in estafetas]
    listaTodasFreg = todasAsFreguesias_da(lista_encomendas_dos_estafetas)
    listaMaisFrequentes = freguesiasMaisFrequentes_da(listaTodasFreg)
    return listaMaisFrequentes

#----------------------------------------Funcionalidade 6----------------------------------------
#Calcular a classificação média de satisfação de cliente para um determinado estafeta.

def classificacao_media(estafeta_id):
    classificacoes = []
    for estafeta in estafetas:
        if estafeta[0] == estafeta_id:
            for order in estafeta[1]:
                if order[1] != None:
                    classificacoes.append(order[1])
    if len(classificacoes) == 0:
        return None
    return sum(classificacoes) / len(classificacoes)

#----------------------------------------Funcionalidade 7----------------------------------------
#'Consultar o número total de entregas pelos diferentes meios de transporte, num determinado intervalo de tempo.',
from datetime import datetime
# Encomenda: #IdEnc, #IdCliente, Peso, Volume, Prazo, DataInicio, DataFim
# Data: #Ano, Mês, Dia, Hora, Minuto
# IdEnc: #12 dígitos
# Estafeta: #IdEstaf, [ (#IdEnc,Nota,Transporte,Freguesia) | T]
def numeroTotalEntregasTransporte(start_date, end_date):
    # calcular o numero total de entregas pelos diferentes meios de transporte

    # obter todas as encomendas no intervalo de tempo especificado
    encomendas_no_intervalo = obter_encomendas_por_intervalo(start_date, end_date)
    
    # obter os transportes de todas as encomendas no intervalo de tempo especificado
    transportes = [get_transporte_by_encomenda(encomenda[0]) for encomenda in encomendas_no_intervalo]
    
    # contar o numero de transportes de cada tipo
    transportes_contados = {}
    for transporte in transportes:
        if transporte in transportes_contados:
            transportes_contados[transporte] += 1
        else:
            transportes_contados[transporte] = 1
            
    return transportes_contados

#----------------------------------------Funcionalidade 8----------------------------------------
#'Consultar o número total de entregas pelos estafetas, num determinado intervalo de tempo.',

def numeroTotalEntregasEstafeta(start_date, end_date):
    # obter todas as encomendas no intervalo de tempo especificado
    encomendas_no_intervalo = obter_encomendas_por_intervalo(start_date, end_date)
    
    # obter os estafetas de todas as encomendas no intervalo de tempo especificado
    estafetas = [get_estafeta_by_encomenda(encomenda) for encomenda in encomendas_no_intervalo]
    
    # contar o numero de estafetas de cada tipo
    estafetas_contados = {}
    for estafeta in estafetas:
        if estafeta in estafetas_contados:
            estafetas_contados[estafeta] += 1
        else:
            estafetas_contados[estafeta] = 1
            
    return estafetas_contados
#----------------------------------------Funcionalidade 9----------------------------------------
#Calcular o número de encomendas entregues e não entregues pela Health Planet, num determinado período de tempo.

def numeroEncomendasEntreguesNaoEntregues(start_date, end_date):
    # obter todas as encomendas no intervalo de tempo especificado
    encomendas_no_intervalo = obter_encomendas_por_intervalo(start_date, end_date)
    
    # contar o numero de encomendas entregues
    encomendas_entregues = 0
    for encomenda in encomendas_no_intervalo:
        if encomenda[6] != (0,0,0,0,0):
            encomendas_entregues += 1
            
    return (encomendas_entregues, len(encomendas_no_intervalo) - encomendas_entregues)

#----------------------------------------Funcionalidade 10----------------------------------------
#Calcular o peso total transportado por estafeta num determinado dia.

def pesoTotalTransportadoPorEstafeta( ano, mes, dia):
    encomendas_do_dia = obter_encomendas_por_dia(ano, mes, dia)
     
    pesos = {}
    for encomenda in encomendas_do_dia:
        estafeta = get_estafeta_by_encomenda(encomenda)
        peso = encomenda[2]
        if estafeta in pesos:
            pesos[estafeta] += peso
        else:
            pesos[estafeta] = peso
    return pesos
    
#----------------------------------------Funcionalidade 11---------------------------------------- 
#Consultar o cliente que fez mais encomendas.

def clienteQueFezMaisEncomendas():
    lista_de_clientes = [order[1] for order in encomendas]
    return clienteQueFezMaisEncomendas_da(lista_de_clientes)
       
#----------------------------------------Funcionalidade 12----------------------------------------
#Consultar os estefetas menos pontuais a fazer as suas entregas.
def estafetas_menos_pontuais():
    estafetas_id = [estafeta[0] for estafeta in estafetas]
    r = encomendas_nao_entregues_e_atrasadas()
    ratios = {estaf: racio_estafeta(estaf, r) for estaf in estafetas_id}
    max_ratio = max(ratios.values())
    l = [estaf for estaf, ratio in ratios.items() if ratio == max_ratio]
    return (l, max_ratio)

#----------------------------------------Funcionalidade 13----------------------------------------

# def all_paths_to_goal(graph, goal):
#     all_paths = []
#     for start in graph.keys():
#         paths = list(dfs_paths(graph, start, goal))
#         if paths:
#             all_paths.extend(paths)
#     return all_paths

#----------------------------------------Funcionalidade 14----------------------------------------
# Representar os diversos pontos de entrega (freguesias) disponíveis em forma de grafo.

def show_graph(grafo):
    G = nx.Graph()

    for node, edges in grafo.items():
        for edge, weight in edges:
            G.add_edge(node, edge, weight=weight)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.show()
    
#----------------------------------------Funcionalidade 15----------------------------------------

# def circuit_with_max_deliveries(weight_or_volume, grafo):
#     paths = all_paths(grafo)
    
#     if weight_or_volume == 0:
#         max_path = max_deliveries_by_weight(paths, grafo)
#     elif weight_or_volume == 1:
#         max_path = max_deliveries_by_volume(paths, grafo)
        
#     return max_path

#----------------------------------------Funcionalidade 16----------------------------------------

 # 1 - DFS
 # 2 - BFS
 # 3 - Limitada em Profundidade
 # 4 - Gulosa
 # 5 - A*
def produtividade(enc_id, metodo):
    # Obter a encomenda

    encomenda = get_encomenda_por_entregar_by_id(enc_id)


    if metodo == 1:
        caminho = (resolveDFS(encomenda[0]), resolveDFSTempo(encomenda[0]))
    elif metodo == 2:
        caminho = (resolveBFS(encomenda[0]), resolveBFSTempo(encomenda[0]))
    elif metodo == 3:
        caminho = (resolveDLS(encomenda[0],5), resolveDLSTempo(encomenda[0],5))
    elif metodo == 4:
        caminho = (resolveGulosa(encomenda[0]), resolveGulosaTempo(encomenda[0]))
    elif metodo == 5:
        caminho = (resolveAStar(encomenda[0]), resolveAStarTempo(encomenda[0]))
    
    # obter distancia e tempo do caminho
    distancia = caminho[0][1]
    tempo = caminho[1][1]
    return (distancia, tempo)

#----------------------------------------Funcionalidade 16----------------------------------------
# obter os caminhos de uma encomenda para um determinado metodo de pesquisa

def caminhos_encomenda(enc_id, metodo):
    # Obter a encomenda

    encomenda = get_encomenda_por_entregar_by_id(enc_id)


    if metodo == 1:
        caminho = resolveDFS(encomenda[0])
    elif metodo == 2:
        caminho = resolveBFS(encomenda[0])
    elif metodo == 3:
        caminho = resolveDLS(encomenda[0],5)
    elif metodo == 4:
        caminho = resolveGulosa(encomenda[0])
    elif metodo == 5:
        caminho = resolveAStar(encomenda[0])
    
    return caminho

#----------------------------------------Funcionalidade 18----------------------------------------

# comparaçao entre os metodos de pesquisa, correr todos os metodos para todas as encomendas e obter todas todas as estatisticas, como tempo de execuçao, distancia percorrida, numero de nos expandidos, etc

import time

def comparacao_metodos():
    
    mapa_metodos = {1: "DFS", 2: "BFS", 3: "DLS", 4: "Gulosa", 5: "A*"}
    resultados = []
    for metodo in mapa_metodos.keys():
        for encomenda in encomendas_por_entregar:
            # obter tempo de execuçao
            start_time = time.time()
            print (f"Encomenda: {encomenda[0]}")
            prod = produtividade(encomenda[0], metodo)
            resultados.append(prod)
            end_time = time.time()
            execution_time = end_time - start_time
            print("--------------------------------------------------")
            print(f"Tempo de execução para a encomenda {encomenda[0]} e método {mapa_metodos[metodo]}: {execution_time} segundos")
            print(f"Caminho percorrido: {prod[0]} Kms")
            print(f"Tempo de entrega: {prod[1]} horas")
            print("--------------------------------------------------")

    return resultados

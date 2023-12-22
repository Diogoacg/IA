from informacao import *
# Estafeta: #IdEstaf, [ (#IdEnc,Nota,Transporte,Freguesia) | T]
def get_all_estafetas():
    return estafetas

def get_all_encomendas():
    return encomendas

def get_encomenda_by_id(id_enc):
    for order in encomendas:
        if order[0] == id_enc:
            return order
        
def get_encomenda_por_entregar_by_id(id_enc):
    for order in encomendas_por_entregar:
        if order[0] == id_enc:
            return order
# Estafeta: #IdEstaf, [ (#IdEnc,Nota,Transporte,Freguesia) | T]

# Encomenda: #IdEnc, #IdCliente, Peso, Volume, Prazo, DataInicio, DataFim
# Data: #Ano, Mês, Dia, Hora, Minuto
# IdEnc: #12 dígitos

def get_transporte_by_encomenda(id_enc):
    for estafeta in estafetas:
        for order in estafeta[1]:
            if order[0] == id_enc:
                return order[2]
    return None
def obter_encomendas_por_intervalo(start_date, end_date):
    lista_de_encomendas = []
    for order in encomendas:
        if start_date <= order[5] <= end_date:
            lista_de_encomendas.append(order)
    return lista_de_encomendas

def contaEntregasIntervalo(start_date, end_date):
    count = 0
    for order in encomendas:
        if start_date <= order[6] <= end_date:
            count += 1
    return count


def orders_by_bike(estafeta_id):
    orders = 0
    for estafeta in estafetas:
        if estafeta[0] == estafeta_id:
            for order in estafeta[1]:
                if order[2] == 'Bicicleta':
                    orders += 1
    return orders

def get_encomenta_by_client(client_id):
    lista_de_encomendas = []
    for order in encomendas:
        if order[1] == client_id:
            lista_de_encomendas.append(order[0])
    return lista_de_encomendas

def get_estafeta_by_encomenda(lista_de_encomendas):
    estafeta_id = 0
    lista_de_estafetas = []
    for encomenda in lista_de_encomendas:
        for estafeta in estafetas:
            for order in estafeta[1]:
                if order[0] == encomenda:
                    estafeta_id = estafeta[0]
                    lista_de_estafetas.append(estafeta_id)
                    
    return lista_de_estafetas

def get_encomenda_by_estafeta(estafeta_id):
    lista_de_encomendas = []
    for estafeta in estafetas:
        if estafeta[0] == estafeta_id:
            for order in estafeta[1]:
                lista_de_encomendas.append(order[0])
    return lista_de_encomendas

def get_cliente_from_encomenda(lista_de_encomendas):
    lista_de_clientes = []
    for encomenda in lista_de_encomendas:
        for order in encomendas:
            if order[0] == encomenda:
                lista_de_clientes.append(order[1])
    return lista_de_clientes

def obter_encomendas_por_dia(ano, mes, dia):
    lista_de_encomendas = []
    for order in encomendas:
        if order[5][0] == ano and order[5][1] == mes and order[5][2] == dia:
            lista_de_encomendas.append(order)
    return lista_de_encomendas

def todasAsFreguesias_da(listaEstaf):
    lista_de_freguesias = []
    for encomendas in listaEstaf:
        for encomenda in encomendas:
            lista_de_freguesias.append(encomenda[3])
    return lista_de_freguesias
        

def freguesiasMaisFrequentes_da(lista_de_freguesias):
    from collections import Counter

    contagem = Counter(lista_de_freguesias)
    maximo = max(list(contagem.values()))
    modas = [k for k,v in contagem.items() if v == maximo]

    return modas

def clienteQueFezMaisEncomendas_da(lista_de_clientes):
    from collections import Counter

    contagem = Counter(lista_de_clientes)
    maximo = max(list(contagem.values()))
    modas = [k for k,v in contagem.items() if v == maximo]

    return modas #retorna uma lista para caso de empate

# se a data for 2023-06-24 20:30 e o prazo for 8 horas, a data máxima de entrega é 2023-06-25 4:30
def data_maxima_de_entrega(data , prazo):
    ano, mes, dia, hora, minuto = data
    if prazo == 'Imediato':
        return (ano, mes, dia, hora, minuto + 30)
    else:
        n, s = prazo.split(' ')
        if s == 'horas':
            if hora + int(n) > 23:
                return (ano, mes, dia + 1, hora + int(n) - 24, minuto)
            else:
                return (ano, mes, dia, hora + int(n), minuto)
        else:
            return (ano, mes, dia + int(n) + 1 , 0, 0)
    
#   def estafetas_menos_pontuais():
#     estafetas_id = [estafeta[0] for estafeta in estafetas]
#     r = encomendas_nao_entregues_e_atrasadas()
#     ratio = racio_estafetas_aux(estafetas_id, r)
#     l = estafetas_maior_ratio(ratio, r)
#     return l  
    
def encomendas_nao_entregues_e_atrasadas():
    lista_de_encomendas = []
    for order in encomendas:
        if order[6] == (0,0,0,0,0) or order[6] > data_maxima_de_entrega(order[5], order[4]):
            lista_de_encomendas.append(order)
    return lista_de_encomendas

def racio_estafeta(id_estaf, l):
    encomendas_do_estafeta = get_encomenda_by_estafeta(id_estaf) #lista de encomendas_id
    c = len(encomendas_do_estafeta)
    e = [encomenda[0] for encomenda in l if encomenda[0] in encomendas_do_estafeta]
    t = len(e)
    return t/c


def preco_encomenda(id_enc):

    encomenda = get_encomenda_by_id(id_enc)
    transporte = get_transporte_by_encomenda(id_enc)


    peso = encomenda[2]
    vol = encomenda[3]
    prazo = encomenda[4]

    pt = calcula_preco_por_transporte(transporte)
    horas = get_prazo_encomenda_horas(prazo)
    pp = calcula_preco_por_prazo(horas)

    return 3*peso + 2*vol + pt + pp

def get_prazo_encomenda_horas(prazo):
    if prazo == 'Imediato':
        return 0
    else:
        n, s = prazo.split(' ')
        return int(n) if s == 'horas' else int(n)*24

def calcula_preco_por_prazo(prazo_h):
    if prazo_h < 7:
        return calcula_preco_ate7_horas(prazo_h)
    elif prazo_h < 13:
        return 8
    elif prazo_h < 25:
        return 5
    elif prazo_h < 73:
        return 4
    elif prazo_h < 121:
        return 3
    else:
        return 2

def calcula_preco_ate7_horas(horas):
    return [25, 20, 18, 16, 14, 12, 10][horas]

def calcula_preco_por_transporte(transporte):
    if transporte == 'Bicicleta':
        return 5
    elif transporte == 'Mota':
        return 10
    elif transporte == 'Carro':
        return 15

def precos_lista_encomendas(lista_de_encomendas):
    return [preco_encomenda(id_enc[0]) for id_enc in lista_de_encomendas]


# # Gerar os circuitos de entrega, caso existam, que cubram um determinado território. 
# def dfs_paths(graph, start, goal):
#     stack = [(start, [start])]
#     while stack:
#         (vertex, path) = stack.pop()
#         if vertex in graph:  # Verifique se a chave existe no dicionário
#             for next in set([neighbor[0] for neighbor in graph[vertex]]) - set(path):
#                 if next == goal:
#                     yield path + [next]
#                 else:
#                     stack.append((next, path + [next]))


# #devolve todos os caminhos possiveis do grafo
# def all_paths(grafo):
#     all_paths = []
#     for start in grafo.ge
#         paths = list(dfs_paths(grafo, start, start))
#         if paths:
#             all_paths.extend(paths)
#     return all_paths

#maximo de entregas por peso

# def max_deliveries_by_weight(paths, grafo):
#     max_weight = 0
#     max_path = []
#     for path in paths:
#         weight = sum([grafo[path[i]][path[i + 1]][0][1] for i in range(len(path) - 1)])
#         if weight > max_weight:
#             max_weight = weight
#             max_path = path
#     return max_path

# def max_deliveries_by_volume(paths, grafo):
#     max_volume = 0
#     max_path = []
#     for path in paths:
#         volume = sum([grafo[path[i]][path[i + 1]][0][2] for i in range(len(path) - 1)])
#         if volume > max_volume:
#             max_volume = volume
#             max_path = path
#     return max_path

# algoritmos de pesquisa

# # We will also need a function for DFS traversal
# def dfs_path(graph, start, goal):
#     stack = [(start, [start], 0)]
#     while stack:
#         (vertex, path, distance) = stack.pop()
#         if vertex in graph:  # Check if the key exists in the dictionary
#             for next in graph[vertex]:
#                 new_distance = distance + next[1]
#                 if next[0] == goal:
#                     return path + [next[0]], new_distance
#                 else:
#                     stack.append((next[0], path + [next[0]], new_distance))
#     return None, None

# # BFS algorithm que retorna o caminho mais curto encontrado
# def bfs_path(graph, start, goal):
#     queue = [(start, [start], 0)]
#     while queue:
#         (vertex, path, distance) = queue.pop(0)
#         if vertex in graph:  # Check if the key exists in the dictionary
#             for next in graph[vertex]:
#                 new_distance = distance + next[1]
#                 if next[0] == goal:
#                     return path + [next[0]], new_distance
#                 else:
#                     queue.append((next[0], path + [next[0]], new_distance))
#     return None, None



#encontra o destino de uma encomenda pelo id
def find_destination(id_enc):
    for order in encomendas_por_entregar:
        if order[0] == id_enc:
            
            return order[4]
        
def find_peso(id_enc):
    for order in encomendas_por_entregar:
        if order[0] == id_enc:
            return order[2]

# Now we can define our main functions
def resolveDFS(id_enc):
    start_node = 'Health Planet'
    goal_node = find_destination(id_enc)
    path, distance = grafo.procura_DFS(start_node, goal_node)
    if path is None:  # No path found
        return None, float('inf')
    # Double the distance because it's a round trip
    return path + path[::-1], distance * 2

def resolveDFSTempo( id_enc):
    start_node = 'Health Planet'
    goal_node = find_destination(id_enc)

    result = grafo.procura_DFS(start_node, goal_node)
    if result is None:  # No path found
        return None, float('inf')
    else:
        path, distance = result

    # Calculate delivery time based on some function tempoEntregaEncomenda
    time = tempoEntregaEncomenda(id_enc, distance)

    return path + path[::-1], time



def resolveBFS(id_enc):
    start_node = 'Health Planet'
    goal_node = find_destination(id_enc)
    path, distance = grafo.procura_BFS(start_node, goal_node)
    if path is None:  # No path found
        return None, float('inf')
    # Double the distance because it's a round trip
    return path + path[::-1], distance * 2

def resolveBFSTempo(id_enc):
    start_node = 'Health Planet'
    goal_node = find_destination(id_enc)

    result = grafo.procura_BFS(start_node, goal_node)
    if result is None:  # No path found
        return None, float('inf')
    else:
        path, distance = result

    # Calculate delivery time based on some function tempoEntregaEncomenda
    time = tempoEntregaEncomenda(id_enc, distance)

    return path + path[::-1], time

def resolveDLS(id_enc, limit):
    start_node = 'Health Planet'
    goal_node = find_destination(id_enc)
    result = grafo.procura_DLS(start_node, goal_node, limit)
    if result is None:  # No path found
        return None, float('inf')
    else:
        path, distance = result
    # Double the distance because it's a round trip
    return path + path[::-1], distance * 2

def resolveDLSTempo(id_enc, limit):
    start_node = 'Health Planet'
    goal_node = find_destination(id_enc)

    result = grafo.procura_DLS(start_node, goal_node, limit)
    if result is None:  # No path found
        return None, float('inf')
    else:
        path, distance = result

    # Calculate delivery time based on some function tempoEntregaEncomenda
    time = tempoEntregaEncomenda(id_enc, distance)

    return path + path[::-1], time

def resolveGulosa(id_enc):
    start_node = 'Health Planet'
    goal_node = find_destination(id_enc)
    result = grafo.procura_gulosa(start_node, goal_node)
    if result is None:  # No path found
        return None, float('inf')
    else:
        path, distance = result
    # Double the distance because it's a round trip
    return path + path[::-1], distance * 2

def resolveGulosaTempo(id_enc):
    start_node = 'Health Planet'
    goal_node = find_destination(id_enc)

    result = grafo.procura_gulosa(start_node, goal_node)
    if result is None:  # No path found
        return None, float('inf')
    else:
        path, distance = result

    # Calculate delivery time based on some function tempoEntregaEncomenda
    time = tempoEntregaEncomenda(id_enc, distance)

    return path + path[::-1], time

def resolveAStar(id_enc):
    start_node = 'Health Planet'
    goal_node = find_destination(id_enc)
    result = grafo.a_star_search(start_node, goal_node)

    if result is None:  # No path found
        return None, float('inf')
    else:
        path, distance = result
    # Double the distance because it's a round trip
    return path + path[::-1], distance * 2

def resolveAStarTempo(id_enc):
    start_node = 'Health Planet'
    goal_node = find_destination(id_enc)

    result = grafo.a_star_search(start_node, goal_node)
    
    if result is None:  # No path found
        return None, float('inf')
    else:
        path, distance = result

    # Calculate delivery time based on some function tempoEntregaEncomenda
    time = tempoEntregaEncomenda(id_enc, distance)

    return path + path[::-1], time

# Define a function to get the appropriate transportation method based on total weight
def meioDeTransporteUsado(peso_total):
    if peso_total <= 5:
        return 'Bicicleta'
    elif peso_total <= 20:
        return 'Mota'
    elif peso_total <= 100:
        return 'Carro'
    else:
        return None

# Define a function to calculate delivery speed based on transportation method and weight
def velocidadeEntrega(transporte, peso):
    if transporte == 'Bicicleta':
        return 10 - peso * 0.6
    elif transporte == 'Mota':
        return 35 - peso * 0.5
    elif transporte == 'Carro':
        return 50 - peso * 0.1
    else:
        return None

# Define a function to calculate delivery time based on distance and speed
def tempoEntregaEncomenda(id_enc, d):
    velocidade = velocidadeEncomenda(id_enc)
    return d / velocidade if velocidade else float('inf')

# Define a function to calculate delivery speed based on id and weight
def velocidadeEncomenda(id_enc):
    peso = find_peso(id_enc)
    transporte = meioDeTransporteUsado(peso)
    return velocidadeEntrega(transporte, peso)

    
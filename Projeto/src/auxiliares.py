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
        if start_date <= order[6] <= end_date:
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
    lista_de_estafetas = []
    for encomenda in lista_de_encomendas:
        for estafeta in estafetas:
            for order in estafeta[1]:
                if order[0] == encomenda:
                    lista_de_estafetas.append(estafeta[0])
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


    

def preco_encomenda(id_enc):
    print(id_enc)
    encomenda = get_encomenda_by_id(id_enc)
    transporte = get_transporte_by_encomenda(id_enc)
    print(transporte)

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
 

# Gerar os circuitos de entrega, caso existam, que cubram um determinado território. 
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex in graph:  # Verifique se a chave existe no dicionário
            for next in set([neighbor[0] for neighbor in graph[vertex]]) - set(path):
                if next == goal:
                    yield path + [next]
                else:
                    stack.append((next, path + [next]))


#devolve todos os caminhos possiveis do grafo
def all_paths(grafo):
    all_paths = []
    for start in grafo.keys():
        paths = list(dfs_paths(grafo, start, start))
        if paths:
            all_paths.extend(paths)
    return all_paths

#maximo de entregas por peso

def max_deliveries_by_weight(paths, grafo):
    max_weight = 0
    max_path = []
    for path in paths:
        weight = sum([grafo[path[i]][path[i + 1]][0][1] for i in range(len(path) - 1)])
        if weight > max_weight:
            max_weight = weight
            max_path = path
    return max_path

def max_deliveries_by_volume(paths, grafo):
    max_volume = 0
    max_path = []
    for path in paths:
        volume = sum([grafo[path[i]][path[i + 1]][0][2] for i in range(len(path) - 1)])
        if volume > max_volume:
            max_volume = volume
            max_path = path
    return max_path
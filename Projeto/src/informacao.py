import heapq


# ---------------------------Encomenda---------------------------

# Encomenda: #IdEnc, #IdCliente, Peso, Volume, Prazo, DataInicio, DataFim
# Data: #Ano, Mês, Dia, Hora, Minuto
# IdEnc: #12 dígitos
encomendas = [
    (100000000001,1,10,20,'6 horas',(2023,7,25,10,0),(2023,7,25,15,30)),
    (123456789000,4,16,15,'Imediato',(2023,8,1,12,30),(2023,8,1,12,35)),
    (300145999366,3,5,30,'2 horas',(2023,4,10,17,20),(0,0,0,0,0)),  # não entregue
    (411188745632,3,30,25,'3 horas',(2023,5,29,13,10),(2023,5,29,16,0)),
    (512200534686,4,1,25,'6 horas',(2023,6,30,9,0),(2023,6,30,16,45)), # entregue com atraso
    (611111154895,2,70,40,'1 dia',(2023,4,16,15,40),(2023,4,18,15,0)), # entregue com atraso
    (792555468332,2,4,10,'3 horas',(2023,2,28,16,12),(0,0,0,0,0)), # não entregue
    (800000000234,5,97,52,'12 horas',(2023,6,24,8,30),(2023,6,24,20,0)), 
    (910928382779,4,8,10,'4 horas',(2023,8,1,14,0),(2023,8,1,17,10)), 
    (100910101098,6,4,17,'1 horas',(2023,1,31,12,27),(2023,1,31,12,45)), 
    (113364968333,2,18,67,'1 dia',(2023,12,19,21,29),(2023,12,20,20,23)), 
    (121203928222,7,10,28,'Imediato',(2023,10,13,11,43),(2023,10,14,8,33)), # entregue com atraso
    (136666733413,5,20,41,'6 horas',(2023,3,28,12,12),(2023,3,28,15,53)), 
    (142019203922,2,7,21,'3 horas',(2023,6,12,18,49),(0,0,0,0,0)), # não entregue
    (150393815151,8,30,77,'12 horas',(2023,1,31,12,27),(2023,1,31,21,7)), 
    (169998372344,4,87,87,'1 dia',(2023,2,13,0,0),(2023,2,14,13,0)), 
    (172123212430,9,9,18,'2 horas',(2023,11,7,12,12),(2023,11,7,13,45)), 
    (154268745963,10,33,12,'7 horas',(2023,12,14,9,0),(2023,12,14,16,0)), 
    (774951266458,9,10,13,'10 horas',(2023,10,10,8,30),(2023,10,10,18,30)), 
    (122457456652,11,72,40,'1 dia',(2023,9,20,12,45),(2023,9,21,13,0)), 
    (901230054687,12,4,5,'5 horas',(2023,6,1,9,0),(2023,6,1,14,0)), 
    (758846125940,10,6,21,'13 horas',(2023,4,10,11,0),(2023,4,10,21,9)), 
    (214568744021,13,3,20,'2 horas',(2023,3,14,13,0),(2023,3,14,15,0)), 
    (115542001235,12,61,35,'4 horas',(2023,9,21,11,0),(2023,9,21,15,0)), 
    (125489652311,14,8,5,'Imediato',(2023,11,3,10,0),(2023,11,3,10,0)), 
    (812485569441,13,46,52,'6 horas',(2023,2,16,14,0),(2023,2,16,20,0)), 
    (122145875630,15,15,12,'1 hora',(2023,8,7,17,0),(2023,8,7,18,0)), 
    (124562335601,16,85,54,'1 dia',(2023,7,23,15,0),(2023,7,24,15,0)), 
    (458751021235,14,8,10,'2 horas',(2023,5,29,12,1),(2023,5,29,13,34)), 
    (124501236889,16,3,4,'5 horas',(2023,2,7,17,0),(2023,2,7,22,0)), 
    (214501239987,11,26,9,'12 horas',(2023,5,21,9,0),(2023,5,21,21,0)), 
    (723100045791,3,45,36,'Imediato',(2023,12,6,16,0),(2023,12,6,18,0)), # entregue com atraso
    (312450012994,15,76,81,'4 horas',(2023,1,31,12,27),(2023,1,31,15,27)), 
    (124568790122,12,8,24,'16 horas',(2023,4,3,22,0),(2023,4,5,14,0)), 
    (154200113287,16,32,17,'3 horas',(2023,2,25,17,0),(2023,2,25,20,0)), 
    (890125440127,10,47,30,'9 horas',(2023,3,26,9,0),(2023,3,26,18,0)), 
    (125400133654,4,15,41,'7 horas',(2023,7,14,16,0),(2023,7,14,23,0)), 
    (124578512366,14,84,95,'10 horas',(2023,6,11,9,0),(2023,6,11,18,50)), 
    (125004357899,7,16,24,'8 horas',(2023,6,24,8,30),(2023,6,24,15,10)) 
    
]

#----------------------------Cliente----------------------------
# Cliente: #IdCliente

clientes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

#---------------------------Estafeta---------------------------
# Estafeta: #IdEstaf, [ (#IdEnc,Nota,Transporte,Freguesia) | T]
# Nota: 0-5
# Transporte: Bicicleta, Carro, Mota
# Freguesia: Celeirós, Real, Vimieiro, Panoias, Pedralva, Arentim, Sequeira, Merelim, Ferreiros, Padim da Graça, Nogueira, Santa Tecla, São João do Souto, São Paio, Navarra
# usar ids de encomendas que estao a cima com transportes diferentes para testar, sem ser constantes

estafetas = [
    (1,[(792555468332,0,'Bicicleta','Arentim')]),
    (2,[(300145999366,0,'Bicicleta','Ferreiros'),(100910101098,4.2,'Bicicleta','Arentim'),(100000000001,4.7,'Bicicleta','Ferreiros')]),
    (3,[(123456789000,4.7,'Mota','Arentim'),(169998372344,4.7,'Carro','Real')]),
    (4,[(512200534686,3.9,'Bicicleta','Nogueira'),(910928382779,4.3,'Mota','Nogueira'),(113364968333,5.0,'Mota','Ferreiros'),(136666733413,5.0,'Mota','Santa Tecla'),(411188745632,4.3,'Carro','Nogueira')]),
    (5,[(611111154895,2.8,'Bicicleta','São João do Souto'),(150393815151,4.8,'Carro','São Paio')]),
    (6,[(800000000234,4.9,'Carro','Arentim'),(172123212430,4.9,'Carro','Nogueira'),(142019203922,0,'Bicicleta','Arentim')]),
    (7,[(121203928222,2.9,'Bicicleta','Nogueira')]),
    (8,[(154268745963,4.5,'Carro','Celeirós'),(774951266458,1.2,'Mota','Sequeira')]),
    (9,[(122457456652,2.3,'Carro','Arentim')]),
    (10,[(901230054687,3.0,'Bicicleta','Vimieiro'),(758846125940,3.9,'Bicicleta','Merelim'),(214568744021,3.6,'Bicicleta','Celeirós'),(125004357899,4.3,'Mota','Padim da Graça')]),
    (11,[(115542001235,2.5,'Carro','Real'),(125489652311,4.1,'Bicicleta','Santa Tecla')]),
    (12,[(812485569441,3.7,'Carro','Navarra')]),
    (13,[(122145875630,4.0,'Mota','Ferreiros'),(124562335601,3.1,'Carro','Nogueira'),(458751021235,2.6,'Bicicleta','Merelim'),(124501236889,4.2,'Bicicleta','Sequeira')]),
    (14,[(214501239987,3.3,'Carro','Panoias'),(723100045791,2.8,'Carro','São Paio')]),
    (15,[(312450012994,3.4,'Carro','Vimieiro'),(124568790122,2.7,'Bicicleta','Ferreiros'),(154200113287,3.5,'Carro','Celeirós')]),
    (16,[(890125440127,4.3,'Carro','Pedralva')]),
    (17,[(125400133654,3.8,'Mota','Navarra'),(124578512366,4.1,'Carro','Ferreiros')]),
    # ... add more estafetas here ...
]
#IdEnc, IdEstafeta, Peso, Volume, Freguesia
encomendas_por_entregar = [
    (300145999366,1,5,30,'Arentim'),
    (142019203922,2,7,21,'Ferreiros'),
    (723100045791,3,15,36,'Real'),
    (214501239987,4,26,9,'Nogueira'),
    (124501236889,5,35,4,'Santa Tecla'),
    (124578512366,6,45,95,'São João do Souto'),
    (124562335601,7,55,10,'São Paio'),
    (124568790122,8,65,24,'Celeirós'),
    (124568790123,9,75,24,'Sequeira'),
    (124568790124,10,85,24,'Vimieiro'),
    (124568790125,11,95,24,'Merelim'),
    (124568790126,12,54,24,'Padim da Graça'),
    (124568790127,13,12,24,'Navarra'),
    (124568790128,14,3,24,'Panoias'),
    (124568790129,15,45,24,'Pedralva'),
    (124568790130,16,67,24,'Arentim'),
    (124568790131,17,12,24,'Ferreiros'),
    (124568790132,18,20,24,'Real'),
    (124568790133,19,17,24,'Nogueira'),
    (124568790134,20,18,24,'Santa Tecla'),
    (124568790135,21,19,24,'São João do Souto'),
    (124568790136,22,20,24,'São Paio'),
    (124568790137,23,21,24,'Celeirós'),
    (124568790138,24,22,24,'Sequeira'),
    (124568790139,25,23,24,'Vimieiro'),
    (124568790140,26,24,24,'Merelim'),
    (124568790141,27,5,24,'Padim da Graça'),
    (124568790142,28,6,24,'Navarra'),
    (124568790143,29,75,24,'Panoias'),
    (124568790144,30,85,24,'Pedralva'),
]



# -----------------------------Grafo--------------------------------
# Aresta: #Inicio, Fim, Distância

import math
from queue import Queue

import networkx as nx  # biblioteca de tratamento de grafos necessária para desnhar graficamente o grafo
import matplotlib.pyplot as plt  # idem

# Classe nodo para definiçao dos nodos
# cada nodo tem um nome e um id
class Node:
    def __init__(self, name, id=-1):     #  construtor do nodo....."
        self.m_id = id
        self.m_name = str(name)


    def __str__(self):
        return "node " + self.m_name

    def setId(self, id):
        self.m_id = id

    def getId(self):
        return self.m_id

    def getName(self):
        return self.m_name

    def __eq__(self, other):
        return self.m_name == other.m_name

    def __hash__(self):
        return hash(self.m_name)

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]


# Constructor
# Methods for adding edges
# Methods for removing edges
# Methods for searching a graph
# BFS, DFS
# Other interesting methods


class Graph:

    def __init__(self, directed=False):
        self.m_nodes = []
        self.m_directed = directed
        self.m_graph = {}  # dicionario para armazenar os nodos e arestas
        #self.m_h = {}  # dicionario para posterirmente armazenar as heuristicas para cada nodo -< pesquisa informada

    #############
    #    escrever o grafo como string
    #############
    def __str__(self):
        out = ""
        for key in self.m_graph.keys():
            out = out + "node" + str(key) + ": " + str(self.m_graph[key]) + "\n"
        return out

    ################################
    #   encontrar nodo pelo nome
    ################################

    def get_node_by_name(self, name):
        search_node = Node(name)
        for node in self.m_nodes:
            if node == search_node:
                return node
        return None

    ##############################3
    #   imprimir arestas
    ############################333333

    def imprime_aresta(self):
        listaA = ""
        lista = self.m_graph.keys()
        for nodo in lista:
            for (nodo2, custo) in self.m_graph[nodo]:
                listaA = listaA + nodo + " ->" + nodo2 + " custo:" + str(custo) + "\n"
        return listaA

    ################
    #   adicionar   aresta no grafo
    ######################

    def add_edge(self, node1, node2, weight):
        n1 = Node(node1)
        n2 = Node(node2)
        if (n1 not in self.m_nodes):
            n1_id = len(self.m_nodes)  # numeração sequencial
            n1.setId(n1_id)
            self.m_nodes.append(n1)
            self.m_graph[node1] = []

        if (n2 not in self.m_nodes):
            n2_id = len(self.m_nodes)  # numeração sequencial
            n2.setId(n2_id)
            self.m_nodes.append(n2)
            self.m_graph[node2] = []

        self.m_graph[node1].append((node2, weight))  # poderia ser n1 para trabalhar com nodos no grafo

        if not self.m_directed:
              self.m_graph[node2].append((node1, weight))


    #############################
    # devolver nodos
    ##########################

    def getNodes(self):
        return self.m_nodes
    
    #############################
    # heuristica
    ##########################
    def heuristic(a, b):
        return estima[b]

    #######################
    #    devolver o custo de uma aresta
    ##############3

    def get_arc_cost(self, node1, node2):
        custoT = math.inf
        a = self.m_graph[node1]  # lista de arestas para aquele nodo
        for (nodo, custo) in a:
            if nodo == node2:
                custoT = custo

        return custoT

    ##############################
    #  dado um caminho calcula o seu custo
    ###############################

    def calcula_custo(self, caminho):
        # caminho é uma lista de nodos
        teste = caminho
        custo = 0
        i = 0
        while i + 1 < len(teste):
            custo = custo + self.get_arc_cost(teste[i], teste[i + 1])
            i = i + 1
        return custo
    
    ################################################################################
    #     gerar todos os caminhos entre dois nodos
    ####################################################################################
    
    def generate_all_paths_from_to(self, start_node, end_node):
        visited = {node: False for node in self.m_graph}

        # Call the recursive helper function from the start_node
        path = [start_node]
        self.generate_all_paths_util(start_node, end_node, visited, path)

    def generate_all_paths_util(self, current_node, end_node, visited, path):
        visited[current_node] = True

        if current_node == end_node:
            print(' -> '.join(path))
        else:
            for neighbour, _ in self.m_graph[current_node]:
                if not visited[neighbour]:
                    path.append(neighbour)
                    self.generate_all_paths_util(neighbour, end_node, visited, path)
                    path.pop()

        visited[current_node] = False

        

    ################################################################################
    #     procura DFS
    ####################################################################################

    def procura_DFS(self, start, end, path=None, visited=None):
        if path is None:
            path = []
        if visited is None:
            visited = set()

        path = path + [start]
        visited.add(start)

        if start == end:
            # calcular o custo do caminho funçao calcula custo.
            custoT = self.calcula_custo(path)
            return (path, custoT)
        for (adjacente, peso) in self.m_graph[start]:
            if adjacente not in visited:
                resultado = self.procura_DFS(adjacente, end, path, visited)
                if resultado is not None:
                    return resultado
        return None



    #####################################################
    # Procura BFS
    ######################################################

    def procura_BFS(self, start, end):
        # definir nodos visitados para evitar ciclos
        visited = set()
        fila = Queue()
        custo = 0
        # adicionar o nodo inicial à fila e aos visitados
        fila.put(start)
        visited.add(start)

        # garantir que o start node nao tem pais...
        parent = dict()
        parent[start] = None

        path_found = False
        while not fila.empty() and path_found == False:
            nodo_atual = fila.get()
            if nodo_atual == end:
                path_found = True
            else:
                for (adjacente, peso) in self.m_graph[nodo_atual]:
                    if adjacente not in visited:
                        fila.put(adjacente)
                        parent[adjacente] = nodo_atual
                        visited.add(adjacente)

        # reconstruir o caminho

        path = []
        if path_found:
            path.append(end)
            while parent[end] is not None:
                path.append(parent[end])
                end = parent[end]
            path.reverse()
            # funçao calcula custo caminho
            custo = self.calcula_custo(path)
        return (path, custo)
    
    ###########################
    # Procura Limitada em Profundidade
    #########################
    
    def procura_DLS(self, start, end, limit, path=None, visited=None):
        if path is None:
            path = []
        if visited is None:
            visited = set()

        path = path + [start]
        visited.add(start)

        # Verificar se atingimos o limite de profundidade
        if len(path) > limit:
            return None

        if start == end:
            # calcular o custo do caminho funçao calcula custo.
            custoT = self.calcula_custo(path)
            return (path, custoT)
        for (adjacente, peso) in self.m_graph[start]:
            if adjacente not in visited:
                resultado = self.procura_DLS(adjacente, end, limit, path, visited)
                if resultado is not None:
                    return resultado
        return None
    ###########################
    # Gulosa - pesquisa informada
    #########################
    
  
    def procura_gulosa(self, start, end, path=None, visited=None):
        if path is None:
            path = []
        if visited is None:
            visited = set()

        path = path + [start]
        visited.add(start)

        if start == end:
            # calcular o custo do caminho funçao calcula custo.
            custoT = self.calcula_custo(path)
            return (path, custoT)

        # Criar uma lista prioritária para armazenar os nós adjacentes
        adjacentes = []

        for (adjacente, peso) in self.m_graph[start]:
            if adjacente not in visited:
                # Adicionar o nó adjacente e a estimativa para o final à lista prioritária
                heapq.heappush(adjacentes, (estima[adjacente], adjacente))

        # Enquanto houver nós na lista prioritária
        while adjacentes:
            # Obter o nó com a menor estimativa
            (_, proximo_nodo) = heapq.heappop(adjacentes)

            resultado = self.procura_gulosa(proximo_nodo, end, path, visited)
            if resultado is not None:
                return resultado

        return None
    
    ###########################
    # A* - pesquisa informada
    #########################
    
    def a_star_search(self, start, goal):
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0
        
        while not frontier.empty():
            current = frontier.get()
            
            if current == goal:
                break
            
            for next in self.m_graph[current]:
                new_cost = cost_so_far[current] + self.get_arc_cost(current, next[0])
                if next[0] not in cost_so_far or new_cost < cost_so_far[next[0]]:
                    cost_so_far[next[0]] = new_cost
                    priority = new_cost + estima[next[0]]
                    frontier.put(next[0], priority)
                    came_from[next[0]] = current

        # Reconstruct the path
        path = []
        current = goal
        while current is not None:
            path.append(current)
            current = came_from[current]
        path.reverse()

        return path, cost_so_far[goal]

        
    
    
    

    ###########################
    # desenha grafo  modo grafico
    #########################

    def desenha(self):
        ##criar lista de vertices
        lista_v = self.m_nodes
        lista_a = []
        g = nx.Graph()
        for nodo in lista_v:
            n = nodo.getName()
            g.add_node(n)
            for (adjacente, peso) in self.m_graph[n]:
                lista = (n, adjacente)
                # lista_a.append(lista)
                g.add_edge(n, adjacente, weight=peso)

        pos = nx.spring_layout(g)
        nx.draw_networkx(g, pos, with_labels=True, font_weight='bold')
        labels = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

        plt.draw()
        plt.show()




grafo = Graph()

edges = {
    'Health Planet': [('Celeirós', 4.9), ('Real', 4.5), ('Vimieiro', 2.7), ('São Vicente', 5)],
    'Celeirós': [('Panoias', 2.5), ('Pedralva', 2.6), ('Arentim', 3.2), ('São Vitor', 3)],
    'Panoias': [('Pedralva', 2.2), ('São José de São Lázaro', 4)],
    'Pedralva': [('Arentim', 2.1), ('São Paio de Arcos', 3)],
    'Arentim': [('Sequeira', 6.4), ('Cividade', 2)],
    'Vimieiro': [('Merelim', 1.3), ('Ferreiros', 3.4), ('Maximinos', 3)],
    'Merelim': [('Ferreiros', 2.8), ('Padim da Graça', 2.9), ('Cabreiros', 4)],
    'Ferreiros': [('Padim da Graça', 2.8), ('Esporões', 2)],
    'Real': [('Nogueira', 3.7), ('Santa Tecla', 3.9), ('Gualtar', 5)],
    'Nogueira': [('Santa Tecla', 4.3), ('Navarra', 4.8), ('Lamaçães', 3)],
    'Santa Tecla': [('São João do Souto', 2.15), ('Frossos', 2)],
    'São João do Souto': [('São Paio', 3.8), ('Ruães', 4)],
    'São Vicente': [('São Vitor', 2), ('São José de São Lázaro', 3)],
    'São Vitor': [('São Paio de Arcos', 2), ('Cividade', 3)],
    'São José de São Lázaro': [('Maximinos', 2), ('Cabreiros', 3)],
    'São Paio de Arcos': [('Esporões', 2), ('Gualtar', 3)],
    'Cividade': [('Lamaçães', 2), ('Frossos', 3)],
    'Maximinos': [('Ruães', 2)]
}

for node1, edges in edges.items():
    for edge in edges:
        node2, weight = edge
        grafo.add_edge(node1, node2, weight)


ponto_entrega = ['Arentim', 'Ferreiros', 'Real', 'Nogueira', 'Santa Tecla', 'São João do Souto', 'São Paio', 'Celeirós', 'Sequeira', 'Vimieiro', 'Merelim', 'Padim da Graça', 'Navarra', 'Panoias', 'Pedralva']


ponto_entrega.extend(['São Vicente', 'São Vitor', 'São José de São Lázaro', 'São Paio de Arcos', 'Cividade', 'Maximinos', 'Cabreiros', 'Esporões', 'Gualtar', 'Lamaçães', 'Frossos', 'Ruães'])

#heuristica 
#Essas estimativas foram calculadas adicionando a menor distância entre o nó atual e seus vizinhos à estimativa heurística do vizinho. Por exemplo, para 'Celeirós', pegamos a menor distância entre 'Celeirós' e seus vizinhos (que é 2.5 para 'Panoias') e adicionamos à estimativa heurística de 'Panoias' (que é 4.9), resultando em 7.4.
# apenas estimativas para os pontos de entrega
estima = {
    'Health Planet': 0,
    'Celeirós': 4.9,
    'Panoias': 7.4,
    'Pedralva': 7.5,
    'Arentim': 8.1,
    'Vimieiro': 2.7,
    'Merelim': 4,
    'Ferreiros': 6.4,
    'Real': 4.5,
    'Nogueira': 8.2,
    'Santa Tecla': 8.4,
    'São João do Souto': 10.55,
    'São Vicente': 5,
    'São Vitor': 7,
    'São José de São Lázaro': 8,
    'São Paio de Arcos': 9,
    'Cividade': 10,
    'Maximinos': 5,
    'Ruães': 7,
    'Sequeira': 14.5,
    'Padim da Graça': 9.7,
    'Cabreiros': 11,
    'Esporões': 11.4,
    'Gualtar': 12,
    'Navarra': 13.1,
    'Lamaçães': 13,
    'Frossos': 10.15,
    'São Paio': 14.35
}

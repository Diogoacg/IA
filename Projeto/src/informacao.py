# ---------------------------Encomenda---------------------------
# Encomenda: #IdEnc, #IdCliente, Peso, Volume, Prazo, DataInicio, DataFim
# Data: #Ano, Mês, Dia, Hora, Minuto
# IdEnc: #12 dígitos

encomendas = [
    (200000000001,1,15,25,'6 horas',('2023',7,25,10,0),('2023',7,25,15,30)),
    (223456789000,4,20,18,'Imediato',('2023',8,1,12,30),('2023',8,1,12,35)),
    # ... add more encomendas here ...
]

#----------------------------Cliente----------------------------
# Cliente: #IdCliente

clientes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

#---------------------------Estafeta---------------------------
# Estafeta: #IdEstaf, [ (#IdEnc,Nota,Transporte,Freguesia) | T]

estafetas = [
    (1,[(792555468332,0,'Bicicleta','Celeirós')]),
    (2,[(300145999366,0,'Bicicleta','Panoias'),(100910101098,4.2,'Bicicleta','Merelim'),(100000000001,4.7,'Bicicleta','Ferreiros')]),
    # ... add more estafetas here ...
]

# -----------------------------Grafo--------------------------------
# Aresta: #Inicio, Fim, Distância

grafo = {
    'Green Distribuition': [('Celeirós', 4.9), ('Real', 4.5), ('Vimieiro', 2.7)],
    'Celeirós': [('Panoias', 2.5), ('Pedralva', 2.6), ('Arentim', 3.2)],
    'Panoias': [('Pedralva', 2.2)],
    'Pedralva': [('Arentim', 2.1)],
    'Arentim': [('Sequeira', 6.4)],
    'Vimieiro': [('Merelim', 1.3), ('Ferreiros', 3.4)],
    'Merelim': [('Ferreiros', 2.8), ('Padim da Graça', 2.9)],
    'Ferreiros': [('Padim da Graça', 2.8)],
    'Real': [('Nogueira', 3.7), ('Santa Tecla', 3.9)],
    'Nogueira': [('Santa Tecla', 4.3), ('Navarra', 4.8)],
    'Santa Tecla': [('São João do Souto', 2.15)],
    'São João do Souto': [('São Paio', 3.8)]
}

ponto_entrega = ['Arentim', 'Ferreiros', 'Real', 'Nogueira', 'Santa Tecla', 'São João do Souto', 'São Paio', 'Celeirós', 'Sequeira', 'Vimieiro', 'Merelim', 'Padim da Graça', 'Navarra', 'Panoias', 'Pedralva']

estima = {
    'Green Distribuition': 0,
    'Vimieiro': 2.7,
    'Celeirós': 4.5,
    'Real': 4.5,
    'Nogueira': 7.5,
    'Navarra': 9,
    'Santa Tecla': 6.5,
    'São João do Souto': 8,
    'São Paio': 4,
    'Panoias': 6.7,
    'Pedralva': 7,
    'Arentim': 6.2,
    'Sequeira': 11,
    'Merelim': 2,
    'Padim da Graça': 5.7,
    'Ferreiros': 5
}
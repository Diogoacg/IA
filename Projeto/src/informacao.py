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

# -----------------------------Grafo--------------------------------
# Aresta: #Inicio, Fim, Distância

grafo = {
    'Health Planet': [('Celeirós', 4.9), ('Real', 4.5), ('Vimieiro', 2.7)],
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
    'Health Planet': 0,
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
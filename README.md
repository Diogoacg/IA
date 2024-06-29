# Health Planet Delivery System

## Descrição do Projeto

Este projeto consiste em um sistema de consulta de dados e estatísticas relacionados às entregas feitas pela empresa Health Planet. A aplicação permite aos usuários acessar diversas informações sobre as entregas, os estafetas (couriers), clientes, meios de transporte utilizados, entre outros dados, através de um menu interativo.

## Estrutura do Projeto

O projeto está organizado em dois módulos principais:

- `funcs.py`: Contém as funções que implementam as diversas funcionalidades oferecidas pelo sistema.
- `informacao.py`: Contém as funções que lidam com os dados e estatísticas relacionadas às entregas.

## Funcionalidades Implementadas

O sistema oferece as seguintes funcionalidades:

1. **Consultar o estafeta que utilizou mais vezes um meio de transporte mais ecológico.**
2. **Consultar os estafetas que entregaram determinada(s) encomenda(s) a um determinado cliente.**
3. **Consultar os clientes servidos por um determinado estafeta.**
4. **Calcular o valor faturado pela Health Planet num determinado dia.**
5. **Consultar quais as zonas (rua ou freguesia) com maior volume de entregas por parte da Health Planet.**
6. **Calcular a classificação média de satisfação de cliente para um determinado estafeta.**
7. **Consultar o número total de entregas pelos diferentes meios de transporte, num determinado intervalo de tempo.**
8. **Consultar o número total de entregas pelos estafetas, num determinado intervalo de tempo.**
9. **Calcular o número de encomendas entregues e não entregues pela Health Planet, num determinado período de tempo.**
10. **Calcular o peso total transportado por estafeta num determinado dia.**
11. **Consultar o cliente que fez mais encomendas.**
12. **Consultar os estafetas menos pontuais a fazer as suas entregas.**
13. **Gerar os circuitos de entrega, caso existam, que cubram um determinado território.**
14. **Representar os diversos pontos de entrega (freguesias) disponíveis em forma de grafo.**
15. **Comparar circuitos de entrega tendo em conta os indicadores de produtividade.**
16. **Mostrar o circuito obtido por um algoritmo de pesquisa.**
17. **Comparar os algoritmos de pesquisa em termos de tempo de execução e eficiência.**

## Estrutura do Código

### `main.py`

O arquivo principal que contém o menu interativo e chama as funções apropriadas com base na escolha do usuário.

### `funcs.py`
Contém as definições das funções específicas para cada funcionalidade.

### `informacao.py`
Contém as funções auxiliares que recuperam e processam os dados necessários para as funcionalidades.

# Execução
Para executar o projeto, siga os seguintes passos:

Certifique-se de que todas as dependências necessárias estão instaladas.
Execute o arquivo principal main.py:
```bash
python main.py
```
Utilize o menu interativo para acessar as funcionalidades desejadas.

# Conclusão

Este projeto fornece uma ferramenta completa para consultar e analisar dados relacionados às entregas feitas pela Health Planet. Ele utiliza uma abordagem modular, permitindo fácil expansão e manutenção das funcionalidades.

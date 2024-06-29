# Health Planet Delivery System (AI Project (UM))

## Project Description

This project consists of a system for querying data and statistics related to deliveries made by the company Health Planet. The application allows users to access various information about deliveries, couriers, clients, transportation means used, among other data, through an interactive menu.

## Project Structure

The project is organized into two main modules:

- `funcs.py`: Contains functions that implement various functionalities offered by the system.
- `informacao.py`: Contains functions that handle data and statistics related to deliveries.
- `auxiliares.py`: Contains auxiliary functions for the `informacao.py` file.

## Implemented Functionalities

The system offers the following functionalities:

1. **Query the courier who most often used an eco-friendly mode of transportation.**
2. **Query the couriers who delivered specific order(s) to a particular client.**
3. **Query the clients served by a specific courier.**
4. **Calculate the amount billed by Health Planet on a specific day.**
5. **Query the areas (street or district) with the highest volume of deliveries by Health Planet.**
6. **Calculate the average customer satisfaction rating for a specific courier.**
7. **Query the total number of deliveries by different means of transportation within a specified time interval.**
8. **Query the total number of deliveries by couriers within a specified time interval.**
9. **Calculate the number of orders delivered and undelivered by Health Planet within a specified time period.**
10. **Calculate the total weight transported by a courier on a specific day.**
11. **Query the client who placed the most orders.**
12. **Query the least punctual couriers in making their deliveries.**
13. **Generate delivery routes, if any, that cover a specific territory.**
14. **Represent the various delivery points (districts) as a graph.**
15. **Compare delivery routes based on productivity indicators.**
16. **Display the route obtained by a search algorithm.**
17. **Compare search algorithms in terms of execution time and efficiency.**

# Execution
To run the project, follow these steps:

Make sure all necessary dependencies are installed.
Run the main file `main.py`:

```bash
python main.py
```
Use the interactive menu to access the desired functionalities.

# Conclusion
This project provides a comprehensive tool for querying and analyzing data related to deliveries made by Health Planet. It uses a modular approach, allowing for easy expansion and maintenance of functionalities.

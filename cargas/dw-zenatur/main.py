from config.database_connection import DatabaseConnection
import pandas as pd

def main():
    db_connection = DatabaseConnection()

    print("-----------------------------------")
    print("# Versões das bibliotecas")
    print("PANDAS:", pd.__version__)
    print("-----------------------------------")

    # Exemplo de execução de consulta
    print("# Exemplo de execução de consulta")

    query = "SELECT 'Olá Mundo'"
    result = db_connection.execute_query(query)
    if result:
        for row in result:
            print(row)

    db_connection.close_connection()
    print("-----------------------------------")

if __name__ == '__main__':
    main()

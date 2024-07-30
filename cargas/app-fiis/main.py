from config.database_connection import DatabaseConnection
from selenium import webdriver
from time import sleep
import sqlalchemy
import pandas as pd
import selenium
import sqlalchemy

def main():

    db_connection = DatabaseConnection()

    #Testando frameworks instalados
    print(" ")
    print("----------------- INSTALADOS --------------------")
    print(" ")
    print(f"Selenium: {selenium.__version__}")
    print(f"Pandas: {pd.__version__}")  # Modificamos a importação para 'pd'
    print(f"SQLAlchemy: {sqlalchemy.__version__}")
    print(" ")

    # Conexão com Banco de dados
    print("-------- Testando conexão com SQL Server --------")    
    
    print("# Exemplo de execução de consulta")
    query = "SELECT vwgdm.siglaCliente,vwgdm.numeroPedido,vwgdm.codigoItemZenatur,vwgdm.descricaoItem,vwgdm.quantidadeItem,vwgdm.grupoItem,vwgdm.subgrupoItem,vwgdm.DataEntrega ,vwgdm.PrevisaoEntrega,vwgdm.DataEntrega,vwgdm.modalidadeEntrega,vwgdm.ValorTotal,vwgdm.cidadePedido,vwgdm.UFPedido FROM DB_PWBI.dbo.vw_EnviosGDM AS vwgdm WHERE  vwgdm.siglaCliente = 'GDM'"
    
    result = db_connection.execute_query(query)

    if result:
        # Crie um DataFrame Pandas com os resultados da consulta
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
        print(df)

       # Salvar em um arquivo .xlsx na pasta "C:\_projetos\_exports"
        df.to_excel("C:\\_projetos\\_exports\\resultado.xlsx", index=False)

        #Salvar em um arquivo .csv na pasta "C:\_projetos\_exports"
        df.to_csv("C:\\_projetos\\_exports\\resultado.csv", index=False)

    db_connection.close_connection()

    print(" ")
    print("-------------- Testando Selenium ---------------")
    print(" ")

    driver = webdriver.Chrome()

    driver.get("https://sistema.zenatur.com.br/Zenatur/login.asp")
    sleep(10)
    print(driver.title)
    driver.quit()

    print(" ")
    print("--------------------- FIM ----------------------")
    print(" ")

if __name__ == "__main__":
    main()
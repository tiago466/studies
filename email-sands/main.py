from config.test import Test

def main():
    # Execute os testes
    Test.test_database_connection()
    Test.test_email_connection()

if __name__ == "__main__":
    main()
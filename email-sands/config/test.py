from config.settings import DATABASE_CONNECTION_STRING, EMAIL_HOST, EMAIL_PORT, EMAIL_USER, EMAIL_PASSWORD
from sqlalchemy import create_engine
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib  # Importe a biblioteca para envio de e-mail

class Test:
    def test_database_connection():
        try:
            # Crie uma instância do mecanismo SQLAlchemy
            engine = create_engine(DATABASE_CONNECTION_STRING)

            # Tente estabelecer uma conexão
            connection = engine.connect()

            # Se não houver erros, a conexão foi bem-sucedida
            print("Conexão ao banco de dados bem-sucedida!")

            # Não se esqueça de fechar a conexão
            connection.close()
        except Exception as e:
            # Em caso de erro, imprima a mensagem de erro
            print(f"Erro na conexão ao banco de dados: {str(e)}")

    def test_email_connection():
        try:
            # Tente conectar ao servidor de e-mail e enviar um e-mail de teste
            server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASSWORD)

            # Crie a mensagem de e-mail
            subject = "Teste de e-mail"
            message = "Este é um teste de e-mail, envaido pelo python"
            sender_email = EMAIL_USER
            receiver_email = ""

            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg['Subject'] = subject

            # Conteúdo do e-mail com codificação UTF-8
            body = MIMEText(message, 'plain', 'utf-8')
            msg.attach(body)

            server.sendmail(sender_email, receiver_email, msg.as_string())

            # Encerre a conexão com o servidor de e-mail
            server.quit()

            # Se não houver erros, o e-mail foi enviado com sucesso
            print("E-mail de teste enviado com sucesso!")
            
        except Exception as e:
            # Em caso de erro, imprima a mensagem de erro
            print(f"Erro ao enviar e-mail de teste: {str(e)}")
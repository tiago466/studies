from decouple import config

# Acesso as configurações do banco de dados
DATABASE_CONNECTION_STRING = config("DB_CONNECTION_STRING")

# Acesso as configurações de e-mail
EMAIL_HOST = config("EMAIL_HOST")
EMAIL_PORT = config("EMAIL_PORT")
EMAIL_USER = config("EMAIL_USER")
EMAIL_PASSWORD = config("EMAIL_PASSWORD")
# TODO: migrar pra variáveis de ambiente
#  pesquisar como fazer isso com o Heroku

username = 'telefoniaapi'
password = '7ptkrqtp2l2ELWmi'
db_name = 'telefoniaapi_db'
connection_string = f'mongodb+srv://telefoniaapi:{password}@cluster-telefonia-api-mqzcw.mongodb.net/{db_name}?' \
                    f'retryWrites=true&w=majority'

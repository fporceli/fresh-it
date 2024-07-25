import mysql.connector
con = mysql.connector.connect(
    host='localhost',
    database='db_tcc',
    user='root',
    password='Felipe789')

"""if con.is_connected():
        db_info = con.get_server_info
        print("Conectado ao servidor com êxito!! Versão ",db_info)
        cursor = con.cursor()
        cursor.execute("SELECT database();")
        linha = cursor.fetchone()
        print("Conectado ao banco de dados {} ".format(linha))
else:
    print('Não foi possível realizar a conexão ao banco!')
if con.is_connected():
        cursor.close()
        con.close()
        print('Conexão ao banco foi encerrado!')"""

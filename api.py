import pyodbc
from flask import Flask, jsonify

app = Flask(__name__)

# Defina os detalhes de conexão
server = 'hal9000.database.windows.net'  # Nome do seu servidor no Azure
database = 'HAL9000DB'                   # Nome do seu banco de dados
username = 'adm-sqldb-hal9000'           # Seu nome de usuário
password = '76153Ab#'                    # Sua senha
driver = '{ODBC Driver 17 for SQL Server}'  # Verifique o nome correto do driver instalado

# String de conexão
conn_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

@app.route('/teste/', methods=['GET'])
def teste():
    try:
        # Tentar conectar
        conn = pyodbc.connect(conn_string)
        cursor = conn.cursor()
        
        # Executar a consulta para obter a versão
        cursor.execute("SELECT @@VERSION;")
        row = cursor.fetchone()
        
        # Fechar a conexão
        conn.close()

        if row:
            # Retornar a versão do SQL Server como resposta JSON
            return jsonify({'version': row[0]}), 200
        else:
            return jsonify({'error': 'Nenhuma versão encontrada'}), 500

    except Exception as e:
        # Em caso de erro, retornar uma mensagem de erro
        return jsonify({'error': str(e)}), 500



@app.route('/teste2/', methods=['GET'])
def teste2():
      return jsonify({'messge': 'Testou'}), 200
if __name__ == '__main__':
    app.run(debug=True)

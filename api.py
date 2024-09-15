import pyodbc
from flask import Flask, jsonify, request

app = Flask(__name__)

# Defina os detalhes de conexão
server = 'hal9000.database.windows.net'
database = 'HAL9000DB'
username = 'adm-sqldb-hal9000'
password = '76153Ab#'
driver = '{ODBC Driver 17 for SQL Server}'

conn_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

def get_db_connection():
    conn = pyodbc.connect(conn_string)
    return conn

@app.route('/logins/', methods=['POST'])
def create_login():
    try:
        data = request.get_json()
        conn = get_db_connection()
        cursor = conn.cursor()
        
        query = '''
        INSERT INTO Logins (Username, PasswordHash, Email)
        VALUES (?, ?, ?)
        '''
        cursor.execute(query, 
                       data['Username'], 
                       data['PasswordHash'], 
                       data['Email'])
        conn.commit()
        conn.close()
        return jsonify({'message': 'Login criado com sucesso!'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/logins/', methods=['GET'])
def get_logins():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM Logins")
        rows = cursor.fetchall()
        conn.close()

        logins = []
        for row in rows:
            logins.append({
                'LoginID': row.LoginID,
                'Username': row.Username,
                'PasswordHash': row.PasswordHash,
                'Email': row.Email,
                'CreatedAt': row.CreatedAt.isoformat()
            })
        
        return jsonify(logins), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/logins/<int:login_id>/', methods=['GET'])
def get_login(login_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM Logins WHERE LoginID = ?", (login_id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            login = {
                'LoginID': row.LoginID,
                'Username': row.Username,
                'PasswordHash': row.PasswordHash,
                'Email': row.Email,
                'CreatedAt': row.CreatedAt.isoformat()
            }
            return jsonify(login), 200
        else:
            return jsonify({'error': 'Login não encontrado'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/logins/<int:login_id>/', methods=['PUT'])
def update_login(login_id):
    try:
        data = request.get_json()
        conn = get_db_connection()
        cursor = conn.cursor()

        query = '''
        UPDATE Logins
        SET Username = ?, PasswordHash = ?, Email = ?
        WHERE LoginID = ?
        '''
        cursor.execute(query, 
                       data['Username'], 
                       data['PasswordHash'], 
                       data['Email'], 
                       login_id)
        conn.commit()
        conn.close()
        
        if cursor.rowcount:
            return jsonify({'message': 'Login atualizado com sucesso!'}), 200
        else:
            return jsonify({'error': 'Login não encontrado'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/logins/<int:login_id>/', methods=['DELETE'])
def delete_login(login_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM Logins WHERE LoginID = ?", (login_id,))
        conn.commit()
        conn.close()

        if cursor.rowcount:
            return jsonify({'message': 'Login removido com sucesso!'}), 200
        else:
            return jsonify({'error': 'Login não encontrado'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/auth/', methods=['POST'])
def authenticate_user():
    try:
        data = request.get_json()
        conn = get_db_connection()
        cursor = conn.cursor()
        
        query = '''
        SELECT * FROM Logins 
        WHERE Username = ? AND PasswordHash = ?
        '''
        cursor.execute(query, (data['Username'], data['PasswordHash']))
        row = cursor.fetchone()
        conn.close()

        if row:
            return jsonify({'message': 'Autenticação bem-sucedida!'}), 200
        else:
            return jsonify({'error': 'Credenciais inválidas'}), 401

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/pedidos_completos/', methods=['GET'])
def get_pedidos_completos():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = '''
        SELECT 
    c.ClienteID, 
    c.Nome, 
    p.PedidoID, 
    p.DataPedido, 
    p.Valor
FROM Clientes c
LEFT JOIN Pedidos p ON c.ClienteID = p.ClienteID;
        '''
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()

        pedidos = []
        for row in rows:
            pedidos.append({
                'ClienteID': row.ClienteID,
                'Nome': row.Nome,
                'PedidoID': row.PedidoID,
                'DataPedido': row.DataPedido.isoformat(),
                'Valor': row.Valor
            })
        
        return jsonify(pedidos), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500




























































@app.errorhandler(404)
def page_not_found(e):
    return jsonify({
        'error': 'Rota não encontrada',
        'message': f'A rota {request.path} não existe.'
    }), 404

if __name__ == '__main__':
    app.run(debug=True)

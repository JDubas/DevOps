# Requisitos 📜
## Criar um Web App,
- Stack: ``Python``
- Major version: ``Python 3``
- Minor Version ``3.12``

- Starup Command:
``gunicorn --bind 0.0.0.0:8000 api:app``

## Testando com o Postman ![Postman](https://img.shields.io/badge/-Postman-FF6C37?style=flat&logo=postman&logoColor=white)

### Listar logins </br>
  URL: ``http://testeapidubas.azurewebsites.net/logins/`` </br>
  Metodo: ``GET``

### Criar Login </br>
URL: ``http://testeapidubas.azurewebsites.net/logins/`` </br>
Metodo: ``POST``</br>
Json: ``` {
    "Username": "teste.teste",
    "PasswordHash": "teste",
    "Email": "teste.teste@example.com"
      }```



### Atualizar Login </br>
URL: ``http://testeapidubas.azurewebsites.net/logins/<login_id>/`` </br>
Metodo: ``PUT``</br>
Json: ``` {
    "Username": "novoTeste.teste",
    "PasswordHash": "teste",
    "Email": "Novoteste.teste@example.com"
      }```
      </br>


### Deletar Login </br>
URL: ``http://testeapidubas.azurewebsites.net/logins/<login_id>/`` </br>
Metodo: ``DELETE``</br>
      </br>


### Verificar login </br>
URL: ``http://testeapidubas.azurewebsites.net/auth/`` </br>
Metodo: ``PUT``</br>
Json: ``` {
  {
        "PasswordHash": "Nova_senha",
        "Username": "joao.dubas.atualizado"
}```
      </br>


### Tabelas relacionadas </br>
  URL: ``http://testeapidubas.azurewebsites.net/pedidos_completos/`` </br>
  Metodo: ``GET``

      

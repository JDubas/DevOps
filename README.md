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
Json: ```Json {
    "Username": "teste.teste",
    "PasswordHash": "teste",
    "Email": "teste.teste@example.com"
      }```
      </br>


 ### Listar logins </br>
 URL: ``http://testeapidubas.azurewebsites.net/logins/`` </br>
 Metodo: ``GET``

 ### Listar logins </br>
 URL: ``http://testeapidubas.azurewebsites.net/logins/`` </br>
  Metodo: ``GET``

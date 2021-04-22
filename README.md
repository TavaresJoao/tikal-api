# tikal-api

## RUN THE API

Before running the server for the first time, execute the steps described on Setup

### Setup
```bash
docker-compose build
docker-compose run tikalpoc python manage.py makemigrations
docker-compose run tikalpoc python manage.py migrate
```

### Run the Server
```bash
docker-compose up -d
```

### Stop Server
```bash
docker-compose down
```

## ENDPOINTS

### `http://localhost:8080/api/clientes`
#### GET
List all Clientes on database

#### POST
Create a Cliente on database. Send a POST request with the following body:
```JSON
{
  "nome": "colocar o nome aqui",
  "rg": "colocar o rg aqui",
  "cpf": "colocar o cpf aqui",
  "data_nasc": "2021-04-22",
  "sexo": "male",
  "telefone": 1,
  "email": 2
}
```

### `http://localhost:8080/api/clientes/<str:queryparams>`
#### GET
Here we have 4 options to make the query:
- `http://localhost:8080/api/clientes/1` will return the Client which id is `1`
- `http://localhost:8080/api/clientes/id=1` will return the Client which id is `1`
- `http://localhost:8080/api/clientes/telefone=123456789` will return the Client which telefone number is `123456789`
- `http://localhost:8080/api/clientes/email=joao@email.com` will return the Client which email email is `joao@email.com`

#### PUT
Using this method on `http://localhost:8080/api/clientes/1` will edit the Client which id is `1`. Send a body like the one to create.

#### DELETE
Using this method on `http://localhost:8080/api/clientes/1` will delete the Client which id is `1`

### `http://localhost:8080/api/telefones`
#### GET
List all Telefones on database

#### POST
Create a Telefone on database. Send a POST request with the following body:
```JSON
{
  "ddd": "011",
  "numero": "123456789",
  "tipo": "Celular"
}
```

### `http://localhost:8080/api/telefones/<str:id>`
#### GET
Using this method on `http://localhost:8080/api/telefones/1` will return the Telefone which id is `1`.

#### PUT
Using this method on `http://localhost:8080/api/telefones/1` will edit the Telefone which id is `1`. Send a body like the one to create.

#### DELETE
Using this method on `http://localhost:8080/api/telefones/1` will delete the Telefone which id is `1`.

### `http://localhost:8080/api/emails`
#### GET
List all Emails on database

#### POST
Create a Email on database. Send a POST request with the following body:
```JSON
{
  "email": "joao@email.com"
}
```

### `http://localhost:8080/api/emails/<str:id>`
#### GET
Using this method on `http://localhost:8080/api/emails/1` will return the Email which id is `1`.

#### PUT
Using this method on `http://localhost:8080/api/emails/1` will edit the Email which id is `1`. Send a body like the one to create.

#### DELETE
Using this method on `http://localhost:8080/api/emails/1` will delete the Email which id is `1`.

# Telefonia API Rest com Flask

No contexto de um Agente Virtual de Telefonia, é utilizada uma base de telefones para a realização
de acionamentos. Dessa forma, neste cenário, é necessário inibir alguns casos, ou seja, não discar
para telefones de clientes específicos.

Esse projeto representa uma API REST para o gerenciamento do bloqueio de números em acionamentos
telefônicos, utilizando **Python 3.8** e **Flask**.

### Configurando

Após clonar este repositório e ter a versão do Python compatível instalada, é necessário ativar o _virtualenv_.

Em seguida, execute o comando abaixo para instalar as bibliotecas necessárias:

```
pip install -r requirements.txt
```

O _pip_ se encarregará de instalar as bibliotecas nas versões especificadas pelo arquivo _requirements.txt_.

### Executando

Você utilizará dois terminais - um para rodar a API com o Flask, e outro para enviar requisições HTTP para testar o recebimento pela API.

Lembre-se: em ambos é necessário ter o `virtualenv` habilitado.

Execute na sequência.

```
Terminal 1:

python app.py
```

Ao rodar, deve aparecer o seguinte:

```
Terminal 1:

python app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

O arquivo `requesting.py` possui quatro requisições HTTP: um GET e um POST para a url `http://127.0.0.1:5000/`, e um
GET e um POST para a url `http://127.0.0.1:5000/1` (final customizado).

```
Terminal 2:

python requesting.py
```

Você poderá ver no Terminal 1 as requisições recebidas.

```
Terminal 1:

python app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

127.0.0.1 - - [18/Dec/2019 16:52:58] "GET / HTTP/1.1" 200 -
GET request
127.0.0.1 - - [18/Dec/2019 16:53:03] "POST / HTTP/1.1" 200 -
POST request
127.0.0.1 - - [18/Dec/2019 16:53:08] "GET /1 HTTP/1.1" 200 -
GET response on /1
127.0.0.1 - - [18/Dec/2019 16:53:13] "POST /1 HTTP/1.1" 200 -
POST response on /1
```

#### Mais informações

- [Flask](https://www.palletsprojects.com/p/flask/)
- [Requests](https://requests.readthedocs.io/pt_BR/latest/user/quickstart.html)
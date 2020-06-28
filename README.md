# Telefonia API Rest com Flask

No contexto de um Agente Virtual de Telefonia, é utilizada uma base de telefones para a realização
de acionamentos. Dessa forma, neste cenário, é necessário inibir alguns casos, ou seja, não discar
para telefones de clientes específicos.

Esse projeto representa uma API REST para o gerenciamento do bloqueio de números em acionamentos
telefônicos, utilizando **Python 3.8.3** e **Flask**.

## Fazendo funcionar

Para rodar a API em seu ambiente local, siga os tópicos abaixo.

### Configurando

Após clonar este repositório e ter a versão do Python compatível instalada, é necessário ativar o _venv_.

Em seguida, execute o comando abaixo para instalar as bibliotecas necessárias:

```
pip install -r requirements.txt
```

O _pip_ se encarregará de instalar as bibliotecas nas versões especificadas pelo arquivo _requirements.txt_.

### Executando

Para rodar a API, você deverá executar os seguintes comandos no seu terminal, sequencialmente.

Lembre-se: é necessário ter o `venv` habilitado.

```
Terminal 1:

python app.py
```

Ao rodar, deve aparecer o seguinte:

```
Terminal 1:

> python app.py
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
```

Para a utilização da API, você pode conferir as requisições possíveis e como utilizar cada uma delas acessando
o Swagger, ferramenta visual e interativa instalada junto à API, através da URL do 
[Swagger dessa API](http://127.0.0.1:5000/swagger).

## Sobre a solução

A construção da presente API se deu pelos seguintes requisitos básicos:

- Consultar 1 ou n telefones para verificar se é válido para discagem.
- Cadastrar 1 ou n telefones na lista de bloqueio.
- Remover 1 ou n telefones na lista de bloqueio.
- Consultar todos os telefones.

Com base nessas informações e nas necessidades apresentadas, foi possível pensar em uma solução que se 
comportasse como uma _blocklist_, um armazenamento de números telefônicos que deveriam ser inibidos de
acionamento, ao invés de armazenar todos os números telefônicos de uma base original e no banco dessa API 
tivessem um _status de bloqueio_, definido entre estar ou não bloqueado.

### Escolha do banco de dados

Por isso, uma opção que facilita o desenvolvimento e cumpre de forma mais prática esse modelo esperado foi
a adoção do MongoDB, especialmente pelo MongoDB Atlas. Para saber mais sobre, veja o link para a plataforma 
em [Mais informações](#mais-informações).

A _collection_ foi planejada conforme o seguinte modelo:

```
{
    'phone_number': '1432323232 
}
```

Nela, `phone_number` é uma string, de presença obrigatória nas requisições. O _schema_ da collection também
está documentado através do Swagger.

Cada _document_, elemento da _collection_, também possui um `ObjectID`, com uma chave de identificação 
única para cada _document_. Porém, na API básica, que se norteia pelas quatro necessidades básicas listadas 
acima, o _id_ do _document_ não foi levado em consideração, e o `phone_number` é a propriedade utilizada 
para as operações (consultas, leituras, inserções e deleções).

### Estrutura do projeto

Para a estrutura de projeto, a solução encontrada foi a divisão do escopo em três arquivos principais:

- app.py para representar o Flask
- manager.py para implementação das regras de negócio
- database.py para integração com o banco de dados

Para possibilitar futuros desenvolvimentos de URLs e funcionalidades novas para a API, manteve-se os 
`errorhandler` em `app.py` e as rotas foram separadas no arquivo `routes/api_routes.py`.

Todas as integrações entre as requisições HTTP e a comunicação com o banco de dados são intermediados pelo 
`manager.py`, que se ocupa com as validações e permite o acréscimo prático de novas regras que se façam 
necessárias, além das já implementadas, como a validação de duplicidade/existência do número de telefone 
no banco.

Por fim, o `database.py` faz efetivamente a comunicação com o banco de dados, utilizando a biblioteca 
`pymongo`. Optou-se por ela, ao invés da utilização de alguma biblioteca que atuasse como _wrapper_ do 
`pymongo` e que eventualmente permitisse um ORM justamente pela solução mais simples da API atuando como 
uma `blocklist`, evitando o armazenamento de muitas informações.

### Testes unitários

O projeto também conta com testes unitários, estruturados separadamente em três TestCases, um arquivo para 
cada classe. Eles podem ser executados com o seguinte comando na raiz do projeto:

`python -m unittest discover -s <directory_path>/tests -t <directory_path>/tests`

Substitua a tag `<directory_path>` pelo caminho do diretório raiz do projeto clonado e, para a execução dos 
testes, certifique-se de que o `venv` está habilitado.

### Deploy

Para o deploy, foi utilizado o [Heroku](https://www.heroku.com/), ferramenta de cloud para deploy (manual 
e/ou automatizado), principalmente pela fácil integração e deploy automático de repositórios do GitHub.

Os arquivos `Procfile` e `runtime.txt` foram adicionados ao projeto para que o deploy pudesse ser realizado 
pelo Heroku, e foi adicionado o `gunicorn` no arquivo `requirements.txt` como o WSGI HTTP Server.

Para conferir o projeto, que está em produção, pode-se acessar: https://telefonia-api.herokuapp.com/. Por ele, 
é possível também acessar a (documentação da API pelo Swagger)[https://telefonia-api.herokuapp.com/swagger].

#### Mais informações

- [Flask](https://www.palletsprojects.com/p/flask/)
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
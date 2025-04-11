# Minha API em REST

Pequeno projeto para implementação do MVP da disciplina **Desenvolvimento Full Stack Avançado** 

O objetivo é apresentar uma API seguindo o estilo REST.

Principais tecnologias utilizadas:

 - [Flask](https://flask.palletsprojects.com/en/2.3.x/)
 - [SQLAlchemy](https://www.sqlalchemy.org/)
 - [OpenAPI3](https://swagger.io/specification/)
 - [SQLite](https://www.sqlite.org/index.html)

---
### Instalação


Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas descritas no arquivo `requirements.txt`.

---
### Executando o servidor


Para executar a API  basta rodar o comando:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

---
### Acesso no browser

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.

---

## Executando através do Docker

Certifique-se de ter o [Docker](https://docs.docker.com/engine/install/) instalado e em execução em sua máquina.

Navegue até o diretório que contém o Dockerfile e o requirements.txt no terminal. Execute **como administrador** o seguinte comando para construir a imagem Docker:

```
$ docker build -t rest-api
```

Uma vez criada a imagem, para executar o container basta rodar o seguinte comando **como administrador** :

```
$ docker run -p 5000:5000 rest-api
```

Uma vez executando, para acessar a API, basta abrir o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador.


### Comandos úteis do Docker

**Verificar se a imagem foi criada**

```
$ docker images
```

**Remover uma imagem**

```
$ docker rmi <IMAGE ID>
```

**Verificar se o container está em execução**

```
$ docker container ls --all
```

**Parar um container**

```
$ docker stop <CONTAINER ID>
```

**Destruir um container**

```
$ docker rm <CONTAINER ID>
```

**Documentação do Docker** [documentação do docker](https://docs.docker.com/engine/reference/run/).

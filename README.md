# CRM Parceiro

Sistema CRM Parceiro

## Dependencias do projeto

- 3.11 <= Python < 3.12
- Node.js >= 14 (LTS)
- Poetry (NPM do Python)
- Docker >= 20

## Guia de instalação

### Instalar server (Python)

Na raiz do projeto, criar o ambiente virtual e instalar as dependencias com o comando:

```sh
poetry install
```

### Instalar client (Node.js)

Na pasta `./client`, executar o comando:

```sh
npm install
```

### Executar build do client (Node.js)

```sh
npm run build
```

### Executar watch do client (Node.js)

```sh
npm run vite
```

## Iniciar servidor (Python)

A aplicação contem uma dependencia do Redis para executar.

```sh
poetry run redis_start
```

| Abaixo contem comandos do Redis no Projeto.

Assim que o Redis for iniciado, iniciar o servidor:

```sh
poetry run server
```

## Redis

Redis é um banco de dados NoSQL de apoio para a aplicação.
Ele funciona em diversas camadas da aplicação, como: cache de parametros da AWS, cache de aplicação, gerenciador de fila e tarefas do Celery.  
Sugestão de IDE: [Another Redis Desktop Manager](https://goanother.com/)

### Iniciar o Redis

```sh
poetry run redis_start
```

### Parar o Redis (sem remover o container)

Essa opção não remove o conteudo do Redis:

```sh
poetry run redis_stop
```

### Parar o Redis (removendo o container)

Essa opção remove o conteudo do Redis.

```sh
poetry run redis_down
```

### Log do Redis

Com o Redis ativo:

```sh
poetry run redis_log
```

# DEV DOCS

## Exemplos de rotas
GET    https://parceiro.ape11.com.br/api/imoveis/v1/imoveis     -> Listar imoveis
GET    https://parceiro.ape11.com.br/api/imoveis/v1/imoveis/123 -> Consulta imovel pelo ID
POST   https://parceiro.ape11.com.br/api/imoveis/v1/imoveis     -> Criar post
PUT    https://parceiro.ape11.com.br/api/imoveis/v1/imoveis/123 -> Atualizar
PATCH  https://parceiro.ape11.com.br/api/imoveis/v1/imoveis/123 -> Atualizar
DELETE https://parceiro.ape11.com.br/api/imoveis/v1/imoveis/123 -> Deletar


## Exemplos de payload e body 
GET    https://parceiro.ape11.com.br/api/imoveis/v1/imoveis/123 -> Consulta imovel pelo ID
body
{
    "data": {
        "id_imovel": 1,
        ...
    }
}

GET    https://parceiro.ape11.com.br/api/imoveis/v1/imoveis?pessoa=juridica    -> Lista imoveis referente casa
body
{
    "data": [
        ...
    ],
    total: 10,
    pagination: {
        next: 3
        current: 2
        previous: 1
    }
}

POST   https://parceiro.ape11.com.br/api/imoveis/v1/imoveis     -> Criar post
payload
{
    "logradouro": "Rua ..."
}

## Estrutura de uma URL de API REST
GET  https://parceiro.ape11.com.br/api/imoveis/v1/imoveis    -> Lista imoveis
^    ^- host                      ^- rota
|
metodo

/imoveis/v1/imoveis
^        ^  ^- recurso
|        versao
dominio no plural


POST /imoveis/v1.1/imoveis

## Exemplos de URLs para APIs REST

GET https://parceiro.ape11.com.br/api/parceiros/v1/parceiros             -> Lista parceiros
GET https://parceiro.ape11.com.br/api/parceiros/v1/parceiros/1           -> Obter parceiro 1
GET https://parceiro.ape11.com.br/api/parceiros/v1/parceiros/1/imoveis   -> Listar imoveis do parceiro 1
GET https://parceiro.ape11.com.br/api/parceiros/v1/parceiros/1/imoveis/1 -> Obter imovel 1 do parceiro 1


## Exemplos de Status-Code
200 - OK
201 - OK para CREATE ou POST
204 - Não encontrou na pesquisa
400 - Payload invalido
404 - Não encontrou recurso 
403 - Sem permissão
422 - Erro de negocio

## Site - Exemplos de rotas
GET e POST apenas
OK - 200

GET  https://parceiro.ape11.com.br/captacao?pessoa=juridica&limit=50
GET  https://parceiro.ape11.com.br/captacao/cadastrar  <- devolve a pagina
POST https://parceiro.ape11.com.br/captacao/cadastrar  -> insere os dados da pagina
GET  https://parceiro.ape11.com.br/captacao/imoveis

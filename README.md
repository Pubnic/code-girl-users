# Avant Microservices Boilerplate

<p align="center">
  <a href="#-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-projeto">Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#como-usar">Como usar</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#adicionando-um-usuário">Usuários</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#rodando-os-testes">Testes</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
</p>

## Motivação
Padronizar os projetos de microserviços da Avant e evitar *copy and paste*.

## Tecnologias

- [Python](https://www.python.org/)
- [Node.js](https://nodejs.org/en/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Django ORM](https://docs.djangoproject.com/en/4.0/topics/db/)
- [PynamoDB](https://github.com/pynamodb/PynamoDB)
- [Doppler](https://doppler.com/)

## Como usar

Para clonar, rodar e realizar deploy dessa aplicação, você irá precisar de [Git](https://git-scm.com), [Docker](https://www.docker.com/) e [Docker-Compose](https://docs.docker.com/compose/)

## Recomendamos a instalação e configuração do seu ambiente baseado na [Documentação](https://zapay-pagamentos.github.io/avant-microservices-boilerplate)

### Configurar VSCode

Configure o conda do projeto

```sh
conda create -n avant-microservices python=3.10
```

### Adicione variáveis de ambiente

```sh
touch .env
echo <seu-doppler-token> > .env
```

### Executar o Projeto

No seu terminal:

```sh
sudo docker-compose up
```

## Instalando novas libs

```sh
# Tenha certeza que tem todas as libs instaladas
pip install -r requirements.txt

# Instale a nova lib
pip install novalib

# Para a lib ser instalada no seu container será necessário rebuildar
docker-compose stop
docker-compose up --build
```

## Testando

- Rodar os testes
- `docker-compose exec avant-microservices bash`
- `doppler run -- pytest`

- Simular uma requisição na API, basta adicionar `client: TestClient` no parâmetro do método

```python
from pytest.test_client import TestClient
def test_nome_da_funcao(client: TestClient):
    response = client.get('/auth/status/)
    print(response.status_code)
    print(response.json())
```

## Acessando o banco de dados pelos pgadmin

- Subir o docker
- Acessar http://localhost:8080/
- Preencher
    - username: `mystique@usezapay.com.br`
    - password: `zapay_pass`
- Em `Servers` clique com o direito do mouse -> Create -> Server
    - Em `Name` coloque `Mystique`
    - Na Aba `Connection`
        - Em `Host` coloque `mystique-postgres`
        - Em `Maintenance database` coloque `mystique_db`
        - Em `Username` coloque `zapay`
        - Em `Password` coloque `zapay`
            - Clique em `Save password`
    - Agora clique em `Save`
- Vai aparecer dentro de `Servers` o BD `Mystique`
    - Dentro dele terá o nosso BD `mystique_db`
    - Para acessar as tabelas dentro de `mystique_db` faça
        - Abra `Schemas` -> `public` -> `Tables`

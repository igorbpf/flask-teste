## Flask-teste

### Seguir os seguintes passos

#### Criar ambiente virtual com o pipenv
`pipenv --python 3.6`

#### Ativar ambiente
`pipenv shell`

#### Instalar pacotes
`pip install -r requirements.txt`

#### Criar container
`bash run_container.sh` (talvez tenha que usar sudo por conta do docker)

#### Executar os comandos que estão dentro de docker_instructions.txt

#### Popular o banco de dados com registros
`python populate_db.py`

#### Destruir e remover container do banco quando quiser parar de usar (Este comando é necessário porque não é possível criar seguidamente o mesmo container. É preciso remover para criar de novo.
`bash destroy_container.sh` (talvez tenha que usar sudo por conta do docker)

## Dependências:
python3;
sqlite3;
pip;
Flask, MysqlAlchemy, Flask Rest JSONAPI;

Caso não houver o pip configurado, executar esses comandos:

`curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
`python get-pip.py`

As dependências do Flask podem ser configuradas por meio de:

`pip install flask-rest-jsonapi flask-sqlalchemy`

Depois de extraído/clonado, basta executar *diretório-do-projeto/application.py* por meio do python3.

Com isso será aberto um servidor local com o endereço: http://127.0.0.1:5000/entries

Esse endereço listará todos os registros cadastrados, enquanto http://127.0.0.1:5000/entries/id irá mostrar somente o registro com o id respectivo.

Para realizar um registro, basta executar:

`curl -i -X POST -H 'Content-Type: application/json' -d '{"data":{"type":"entry", "attributes":{"name":"Nome do registro"}}}' http://localhost:5000/entries`

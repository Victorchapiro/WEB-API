from flask import Flask, make_response, jsonify, request
from bd import Produtos
app = Flask(__name__)

@app.route('/produtos',methods=['GET'])
def retornar_produtos():
    return make_response(
        jsonify(Produtos)
        )

@app.route('/cadastro',methods=['POST'])
def cadastrar_produto():
    newproduto = request.json
    Produtos.append(newproduto)
    return make_response(
        jsonify(mensagen = "Produto cadastrado com sucesso"
        )
    )
    

app.run()    
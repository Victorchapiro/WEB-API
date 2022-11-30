from flask import Flask, make_response, jsonify, request
from bd import Produtos
app = Flask(__name__)

@app.route('/produtos',methods=['GET'])
def retornar_produtos():
    return make_response(
        jsonify(Produtos)
        )

@app.route('/produtos',methods=['POST'])
def cadastrar_produto():
    newproduto = request.json
    Produtos.append(newproduto)
    return make_response(
        jsonify( produto = newproduto,
            mensagen = "Produto cadastrado com sucesso"
        )
    )

@app.route('/produtos',methods=['DELETE'])
def deletar():
    apagar()    
    return make_response(
        jsonify(mensagen = "Produto deletado")
    )


@app.route('/produtos',methods=['PUT'])
def atualizar():
    atualizarproduto()    
    return make_response(
        jsonify(mensagen = "Produto atualizado")
    )

def apagar():     
     for i in range(len(Produtos)):
        for v in Produtos[i].values():
            if(v==2):
                Produtos.pop(i)

def atualizarproduto():
    novoproduto = request.json

    for i in range(len(Produtos)):
        for v in Produtos[i].values():
            if(v==1):
                Produtos[i] = novoproduto
                

app.run()    
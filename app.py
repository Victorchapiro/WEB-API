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

@app.route('/deletar',methods=['DELETE'])
def deletar():
    apagar()    
    return make_response(
        jsonify(mensagen = "Produto deletado")
    )


@app.route('/atualizar',methods=['PUT'])
def atualizar():
    atualizarproduto()    
    return make_response(
        jsonify(mensagen = "Produto atualizado")
    )

def apagar():
    for i in range(len(Produtos)):
        for k,v in Produtos[i].items():
            if(v==2):
                Produtos.pop(i)

def atualizarproduto():
    novoproduto =  {
        'id':14,
        'nome': 'Notebook',
        'preço': 45000
    }

    for i in range(len(Produtos)):
        for k,v in Produtos[i].items():
            if(v==2):
                Produtos[i] = novoproduto
                

app.run()    
from bd import Produtos
buscar()

def buscar():
    for i in range(len(Produtos)):
        for k,v in Produtos[i].items():
            if(v==2):
                print(Produtos[i].items())
            else:
                print("não deu") 
           
       
def buscar():
    valor = id_produto.value()
    for i in range(len(Produtos)):
        for k,v in Produtos[i].items():
            if(v==2):
                print("deun certo")
            else:
                print("não deu") 

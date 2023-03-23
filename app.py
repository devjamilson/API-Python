from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
      'id':1,
       'título':'O Pequeno Príncipe',
       'autor':'Antoine de Saint-Exupéry' 
    },
    {
      'id':2,
       'título':'Romeu E Julieta',
       'autor':'William Shakespeare' 
    },
    {
      'id':3,
       'título':'1984',
       'autor':'George Orwell' 
    },
    {
      'id':4,
       'título':'Dom Quixote De La mancha',
       'autor':'Miguel de Cervantes' 
    },
    {
       'id':5,
       'título':'Os Miseráveis',
       'autor':'Victor Hugo' 
    },
]

#Consultar(todos)
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)
#Consultar(id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livros_por_id(id):
    for livro in livros:
       if livros.get('id') == id:
           return jsonify(livros)
#Editar
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livros_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if  livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
#Criar
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)
#Excluir
@app.route('/livros', methods=['POST'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)

app.run(port=5000, host='localhost', debug=True)
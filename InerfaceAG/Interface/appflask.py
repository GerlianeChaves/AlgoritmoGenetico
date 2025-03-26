from flask import Flask, request, jsonify, render_template
from ag_funcional import ag_caixeiroviajante  # Importa a função do AG

app = Flask(__name__)

# Rota para carregar a página inicial
@app.route("/")
def index():
    return render_template("index.html")

# Rota para processar o formulário
@app.route("/solve", methods=["POST"])
def solve():
    # Obter os dados enviados pelo formulário
    data = request.get_json()
    num_cities = int(data["numCities"])
    distances_input = data["distances"]

    # Converter a matriz de distâncias em uma lista de listas
    try:
        distances = [
            list(map(float, line.split(",")))
            for line in distances_input.strip().split("\n")
        ]
    except ValueError:
        return jsonify({"error": "Formato inválido para a matriz de distâncias."})

    # Garantir que a matriz seja válida
    if len(distances) != num_cities or any(len(row) != num_cities for row in distances):
        return jsonify({"error": "A matriz de distâncias não corresponde ao número de cidades."})

    # Rodar o algoritmo genético
    try:
        result = ag_caixeiroviajante(distances)
    except Exception as e:
        return jsonify({"error": f"Erro ao executar o algoritmo: {str(e)}"})

    # Retornar o resultado como JSON
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)

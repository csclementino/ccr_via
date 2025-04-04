from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime  # Adicione esta importação

app = Flask(__name__)
CORS(app)

metro_data = {
    "ultima_atualizacao": None,
    "dados_trem": {}
}

@app.route('/api/trem', methods=['POST'])
def receber_dados_trem():
    try:
        dados = request.get_json()  # Alterado para get_json()
        
        if not dados:
            return jsonify({"erro": "Dados inválidos"}), 400
            
        metro_data["ultima_atualizacao"] = datetime.now().isoformat()
        metro_data["dados_trem"] = dados
        
        print("Dados recebidos:")  # Log para debug
        print(dados)  # Mostra os dados recebidos
        
        return jsonify({"mensagem": "Dados recebidos com sucesso"}), 200
        
    except Exception as e:
        app.logger.error(f"Erro interno: {str(e)}")  # Log detalhado
        return jsonify({"erro": "Erro interno do servidor"}), 500

@app.route('/api/trem', methods=['GET'])
def obter_dados_trem():
    primeiro = metro_data["dados_trem"][0]
    return jsonify({"hora_previsto_chegada": primeiro["hora_previsto_chegada"]})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
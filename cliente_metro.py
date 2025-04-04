import requests
from datetime import datetime
import time

def get_next_train():
    url = "https://apim-proximotrem-prd-brazilsouth-001.azure-api.net/api/v1/lines/L8/stations/BFU/next-train"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
        
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição do metrô: {e}")
        return None
    
def get_status_linha():
    url = "https://webapi.grupoccr.com.br/v1/mobility/public/line-status/current/state/SP"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
        
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição do metrô: {e}")
        return None

def send_status_to_flask_api(data):
    flask_api_url = "http://localhost:5000/api/linhas"
    
    try:
        response = requests.post(
            flask_api_url,
            json=data
        )
        response.raise_for_status()
        print("Dados enviados para a API Flask com sucesso!")
        return response.json()
        
    except requests.exceptions.RequestException as e:
        print(f"Erro ao enviar para API Flask: {e}")
        return None
    
def send_train_to_flask_api(data):
    flask_api_url = "http://localhost:5000/api/trem"
    
    try:
        response = requests.post(
            flask_api_url,
            json=data
        )
        response.raise_for_status()
        print("Dados enviados para a API Flask com sucesso!")
        return response.json()
        
    except requests.exceptions.RequestException as e:
        print(f"Erro ao enviar para API Flask: {e}")
        return None    

if __name__ == "__main__":
    while True:
        dados_trem = get_next_train()
        if dados_trem:
            print("Dados obtidos da API do metrô:")
            print(dados_trem)
            
            # Envia para a API Flask
            resultado_envio = send_train_to_flask_api(dados_trem)
            
            if resultado_envio:
                print("Resposta da API Flask:")
                print(resultado_envio)
        else:
            print("Falha ao obter dados do proximo trem")
        
        dados_linhas = get_status_linha()
        if dados_linhas:
            print("Dados obtidos da API do metrô:")
            print(dados_linhas)
            
            # Envia para a API Flask
            resultado_envio = send_status_to_flask_api(dados_linhas)
            
            if resultado_envio:
                print("Resposta da API Flask:")
                print(resultado_envio)
        else:
            print("Falha ao obter dados das linhas")
        time.sleep(30)

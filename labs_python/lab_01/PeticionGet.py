import requests

def get_request():
    url = "https://www.google.com/"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return f"Respuesta del servidor:\n{response.text}"
        else:
            return f"Error: Código HTTP {response.status_code}"

    except requests.exceptions.RequestException as e:
        return f"Error en la conexión: {e}"

print(get_request())
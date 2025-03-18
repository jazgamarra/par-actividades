import requests

def check_urls():
    try:
        test_url1 = "http://www.pol.una.py"
        test_url2 = "http://grado.pol.una.py/index.html"
        
        def print_url_details(url):
            response = requests.get(url)
            return f"Protocolo: {response.url.split(':')[0]} | Host: {response.url.split('/')[2]} | Archivo: {url.split('/')[-1]}"

        result1 = print_url_details(test_url1)
        result2 = print_url_details(test_url2)

        return f"Resultados:\n{result1}\n{result2}"

    except requests.exceptions.MissingSchema as e:
        return f"Error: URL mal formada - {e}"
    except requests.exceptions.RequestException as e:
        return f"Error de conexión - {e}"

print(check_urls())
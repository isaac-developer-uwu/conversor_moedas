from flask import Flask, render_template, request
import requests


app = Flask(__name__)

@app.route('/')
def main():
	return render_template('home.html')
@app.route('/buscar', methods=['POST'])
def buscar():
	endpoint = request.form.get('moeda').upper()
	url = "https://economia.awesomeapi.com.br/json/last/"
	url_completa = url + endpoint
	resposta = requests.get(url_completa, timeout=10)
	dados = resposta.json()
	endp_formatado = endpoint.replace('-', '')

	valor = dados[endp_formatado]['ask']
	if endp_formatado == "USDBRL":
		valor_float = float(valor)
		valor_inteiro = round(valor_float)
		return render_template('result.html', resultado=valor_inteiro)
	elif endp_formatado == "BTCBRL":
		valor_float = float(valor)
		return render_template('result.html', resultado=valor_float)

if __name__ == '__main__':
	import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
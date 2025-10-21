from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/consultar_cnpj", methods=["POST"])
def consultar_cnpj():
    try:
        data = request.get_json()
        cnpj = data.get("cnpj")

        if not cnpj:
            return jsonify({"error": "CNPJ não fornecido"}), 400

        url = f"https://api.cnpja.com/office/{cnpj}?simples=true"
        headers = {
            "Authorization": "4ccafc18-17bb-470b-ace1-05dce7620705-563854f9-edbf-43fb-b290-9b71c0a0d912"
        }

        response = requests.get(url, headers=headers)
        return jsonify(response.json()), response.status_code

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "Servidor da Valentina Online ✅"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

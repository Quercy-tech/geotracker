from flask import Flask, request, jsonify

app = Flask(__name__)
received_coords = []

@app.route("/coords", methods=['POST'])
def receive_coords():
    data = request.get_json()
    received_coords.append(data)
    return jsonify({"status": "ok"})

@app.route("/map", methods=['GET'])
def show_coords():
    return jsonify(received_coords)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3030, debug=True)
from flask import Flask, jsonify, request

app = Flask(__name__)

payments = []

@app.route('/payments', methods=['GET'])
def get_payments():
    return jsonify(payments)

@app.route('/payments', methods=['POST'])
def create_payment():
    payment = request.json
    payment["id"] = len(payments) + 1
    payments.append(payment)
    return jsonify(payment), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/books', methods=['GET'])
def get_books():
    books = [
        {"id": 1, "title": "Book A", "author": "Author A"},
        {"id": 2, "title": "Book B", "author": "Author B"}
    ]
    return jsonify(books)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

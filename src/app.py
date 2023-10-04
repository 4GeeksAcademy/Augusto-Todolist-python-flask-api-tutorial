from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    try:
        new_todo = request.get_json()
        todos.append(new_todo)
        return jsonify(todos)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    try:
        if 0 <= position < len(todos):
            del todos[position]
            return jsonify(todos)
        else:
            return jsonify({"error": "Posición no válida"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
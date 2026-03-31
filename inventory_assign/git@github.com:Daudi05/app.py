from flask import Flask, request, jsonify
from external_api import fetch_product

app = Flask(__name__)

# Mock database
inventory = []
current_id = 1


@app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify(inventory), 200


@app.route("/inventory/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = next((i for i in inventory if i["id"] == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item), 200


@app.route("/inventory", methods=["POST"])
def add_item():
    global current_id
    data = request.get_json()

    if not data.get("product_name"):
        return jsonify({"error": "Product name required"}), 400

    new_item = {
        "id": current_id,
        "product_name": data.get("product_name"),
        "price": data.get("price", 0),
        "stock": data.get("stock", 0)
    }

    inventory.append(new_item)
    current_id += 1

    return jsonify(new_item), 201

@app.route("/inventory/<int:item_id>", methods=["PATCH"])
def update_item(item_id):
    data = request.get_json()
    item = next((i for i in inventory if i["id"] == item_id), None)

    if not item:
        return jsonify({"error": "Item not found"}), 404

    item.update(data)
    return jsonify(item), 200


@app.route("/inventory/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    global inventory
    inventory = [i for i in inventory if i["id"] != item_id]
    return "", 204


@app.route("/external/<barcode>", methods=["GET"])
def get_external_product(barcode):
    product = fetch_product(barcode)

    if not product:
        return jsonify({"error": "Product not found"}), 404

    return jsonify(product), 200


if __name__ == "__main__":
    app.run(debug=True)
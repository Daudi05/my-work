import requests

def fetch_product(barcode):
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"

    try:
        response = requests.get(url)
        if response.status_code != 200:
            return None

        data = response.json()

        if data["status"] == 0:
            return None

        product = data["product"]

        return {
            "product_name": product.get("product_name"),
            "brand": product.get("brands"),
            "ingredients": product.get("ingredients_text")
        }

    except Exception:
        return None
# tests/retractable_banners/utils/price_utils.py
import json
from pathlib import Path

def load_data():
    path = Path("tests/retractable_banners/utils/getDetailsFixture.json")
    if not path.exists():
        raise FileNotFoundError(f" JSON fixture not found at {path}")
    with open(path) as f:
        return json.load(f)

def get_base_price():
    data = load_data()
    material = next((a for a in data["accessories"] if a["name"] == "Material"), None)
    default_option = next((opt for opt in material["accessoryOptions"] if opt["isDefault"]), None)
    return default_option["optionPrice"] if default_option else 0

def get_roll_up_options() -> list[dict]:
    data = load_data()
    roll_up = next((a for a in data['accessories'] if a['name'] == 'Roll up Stand'), None)
    if roll_up:
        return [{'name': opt['optionName'], 'price': opt['optionPrice']} for opt in roll_up['accessoryOptions']]
    return []

def get_discount_percent(quantity: int) -> float:
    data = load_data()
    matches = [d for d in data['discount'] if quantity >= d['count']]
    matches.sort(key=lambda x: x['count'], reverse=True)
    return matches[0]['percent'] if matches else 0

def calculate_total(base_price: float, quantity: int, stand_price: float = 0) -> float:
    discount = get_discount_percent(quantity)
    subtotal = (base_price + stand_price) * quantity
    discounted = subtotal * (1 - discount / 100)
    return round(discounted, 2)

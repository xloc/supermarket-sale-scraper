import json
from pprint import pprint
from dataclasses import dataclass


@dataclass(repr=True, eq=True)
class FlyerItem:
    name: str
    description: str
    image_url: str

    price: float
    pre_price_text: str
    price_text: str

    valid_from: str
    valid_to: str

    def __init__(self, item_dict):
        self.name = item_dict['display_name']
        self.description = item_dict['description']
        self.image_url = item_dict['x_large_image_url']
        try:
            self.price = float(item_dict['current_price'])
        except:
            self.price = None
        self.pre_price_text = item_dict['pre_price_text']
        self.price_text = item_dict['price_text']
        self.valid_from = item_dict['valid_from']
        self.valid_to = item_dict['valid_to']


def parse_json_as_items(json_bytes):
    flyer = json.loads(json_bytes)
    items = [FlyerItem(d) for d in flyer['items']]
    return items


def main():
    with open('flyer_data.json', 'rb') as f:
        flyer = json.loads(f.read())

    items = flyer['items']
    print(len(items))

    # pprint(items[0])

    # fi = FlyerItem(items[0])
    # pprint(fi)

    for d in flyer['items']:
        try:
            FlyerItem(d)
        except:
            pprint(d)
            break


if __name__ == "__main__":
    main()

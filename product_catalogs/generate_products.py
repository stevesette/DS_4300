import random
import string
from random import randrange

categories = ['Watches', 'Couches', 'Kitchen', 'Rugs', 'Appliances', 'Pants', 'Shoes']

product_catalog = []
for i in range(70):
    attributes = {}
    product_id = i
    product_name = "".join([random.choice(string.ascii_letters + string.digits) for n in range(20)])
    brand = "".join([random.choice(string.ascii_letters) for n in range(10)])
    all_colors = ["blue", "black", "brown", "red", "yellow", "green", "orange", "beige", "turquoise", "pink"]
    random.shuffle(all_colors)
    color = all_colors[0]
    price = randrange(200)
    category = categories[int(i/10)]
    attributes['product_id'] = product_id
    attributes['product_name'] = product_name
    attributes['brand'] = brand
    attributes['color'] = color
    attributes['price'] = price
    attributes['category'] = category
    if category == 'Watches':
        attributes['diameter'] = randrange(30,50)
        random.shuffle(all_colors)
        dial_color = all_colors[0]
        attributes['dial_color'] = dial_color
    product_catalog.append(attributes)

searched_attr = {'product_id': 71, 'product_name': 'johnson', 'brand': 'Tommy Hilfiger', 'color': 'beige',
                 'price': 6870, 'category': 'Watches', 'diameter': 40, 'dial_color': 'beige'}
product_catalog.append(searched_attr)


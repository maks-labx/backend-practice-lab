def sort_products_by_price(products):
    return sorted(products, key=lambda product: product["price"])


def sort_products_by_name(products):
    return sorted(products, key=lambda product: product["name"].lower())


def get_product_names(products):
    return list(map(lambda product: product["name"], products))

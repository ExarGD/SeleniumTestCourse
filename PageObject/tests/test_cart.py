def test_cart(app):
    old_qty = app.get_quantity()

    app.add_items_to_cart()
    new_qty = app.get_quantity()
    assert old_qty != new_qty

    app.remove_items_from_cart()

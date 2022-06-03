from . import db

# ___________________Product Class______________________


class Product(db.Model):
    __tablename__ = 'product'
    unique_product_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(60), nullable=False)
    dimension = db.Column(db.String(160), nullable=False)
    material = db.Column(db.String(160), nullable=False)
    category = db.Column(db.String(160), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        str = "Product ID: {}, Product Title/Name: {}, Product Description: {}, Image: {}, Product Dimension: {}, Product Material: {}, Product Category: {}, Product Price: {} \n"
        str = str.format(self.unique_product_id, self.title, self.description,
                         self.image, self.dimension, self.material, self.category, self.price)
        return str


# ___________________Secondary table connecting products to other tables______________________
orderdetails = db.Table('orderdetails',
                        db.Column('order_id', db.Integer, db.ForeignKey(
                            'orders.id'), nullable=False),
                        db.Column('product_id', db.Integer, db.ForeignKey(
                            'product.unique_product_id'), nullable=False),
                        db.PrimaryKeyConstraint('order_id', 'product_id'))


# ___________________ShoppingCart Class______________________
class ShoppingCart(db.Model):
    __tablename__ = 'shoppingCart'
    cart_id = db.Column(db.Integer, primary_key=True)
    order_place_status = db.Column(db.Boolean, default=False)
    cart_product_title = db.Column(db.String(64), nullable=False)
    cart_product_description = db.Column(db.String(500), nullable=False)
    cart_product_image = db.Column(db.String(60), nullable=False)
    cart_product_price = db.Column(db.Float, nullable=False)
    cart_individual_product_count = db.Column(
        db.Integer, default=1, nullable=False)
    cart_total_product_price = db.Column(db.Float)
    cart_net_total_price = db.Column(db.Float)
    shipping_charges = db.Column(db.Float)

    # proceed to checkOut Form details
    buyerFullName = db.Column(db.String(64))
    shippingHomeAddressDetails = db.Column(db.String(500))
    city = db.Column(db.String(128))
    state = db.Column(db.String(132))
    postCode = db.Column(db.String(20))

    unique_product_id = db.Column(db.Integer, db.ForeignKey(
        'product.unique_product_id'))

    products = db.relationship(
        "Product", secondary=orderdetails, backref="shoppingCart")

    def __repr__(self):
        str = "Cart ID : {}, is Order Placed From this cart {}, Cart Product Title : {}, Cart Product Description : {}, Cart Product Image : {}, Cart Product Price : {}, Cart Individual Product Count : {}, Total Product Price : {}, Net Total Price : {}, Product Shipping Charges : {}, Buyer FullName: {}, ShippingHome Address: {}, State: {}, City: {}, postcode: {}\n"
        str = str.format(self.cart_id, self.order_place_status, self.cart_product_title, self.cart_product_description,
                         self.cart_product_image, self.cart_product_price, self.cart_individual_product_count, self.cart_total_product_price, self.cart_net_total_price, self.shipping_charges, self.buyerFullName, self.shippingHomeAddressDetails, self.state, self.city, self.postCode)
        return str


# ___________________WishList Class______________________
class WishList(db.Model):
    __tablename__ = 'whishList'
    wishList_id = db.Column(db.Integer, primary_key=True)
    wishList_product_title = db.Column(db.String(64), nullable=False)
    wishList_product_description = db.Column(db.String(500), nullable=False)
    wishList_product_image = db.Column(db.String(60), nullable=False)
    wishList_product_price = db.Column(db.Float, nullable=False)
    individual_product_count = db.Column(db.Integer, nullable=False)

    unique_product_id = db.Column(db.Integer, db.ForeignKey(
        'product.unique_product_id'))

    products = db.relationship(
        "Product", secondary=orderdetails, backref="wishList")

    def __repr__(self):
        str = "WishList ID : {}, WishList Product Title : {}, WishList Product Description : {}, WishList Product Image : {}, WishList Product Price : {}, WishList Product Count : {} \n"
        str = str.format(self.wishList_id, self.wishList_product_title, self.wishList_product_description,
                         self.wishList_product_image, self.wishList_product_price, self.individual_product_count)
        return str

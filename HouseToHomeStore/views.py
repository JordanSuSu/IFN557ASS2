from flask import Blueprint, render_template, url_for, request, session, flash, redirect
from .models import Product, ShoppingCart, WishList
from datetime import datetime
from .forms import ProceedToCheckoutForm
from .login import LogInForm
from . import db


bp = Blueprint('main', __name__, template_folder='templates')


@bp.route('/houseToHome')
def index():
    # todo: correct folder in template________________ add flask and jinja
    return render_template('index.html')


@bp.route('/houseToHome/kitchenproducts/')
def kitchenproducts():
    kitchensP = Product.query.filter(Product.category == 'kitchen')
    # todo: correct folder in template________________ add flask and jinja
    return render_template('kitchenIndex.html', kitchensP=kitchensP)


@bp.route('/houseToHome/livingproducts/')
def livingproducts():
    livingsP = Product.query.filter(Product.category == 'living')
    # todo: correct folder in template________________ add flask and jinja
    return render_template('livingIndex.html', livingsP=livingsP)


@bp.route('/houseToHome/bathroomproducts/')
def bathroomproducts():
    bathroomsP = Product.query.filter(Product.category == 'bathroom')
    # todo: correct folder in template________________ add flask and jinja
    return render_template('bathRoomIndex.html', bathroomsP=bathroomsP)


@bp.route('/houseToHome/outdoors/')
def outdoors():
    outdoorsP = Product.query.filter(Product.category == 'outdoors')
    # todo: correct folder in template________________ add flask and jinja
    return render_template('kitchenIndex.html', outdoorsP=outdoorsP)


@bp.route('/houseToHome/bedroomproducts/')
def bedroomproducts():
    bedroomsP = Product.query.filter(Product.category == 'bedroom')
    # todo: correct folder in template________________ add flask and jinja
    return render_template('badRoomIndex.html', bedroomsP=bedroomsP)


@bp.route('/houseToHome/commonproducts/')
def commonproducts():
    commonP = Product.query.filter(Product.category == 'commonones')
    # todo: correct folder in template________________ add flask and jinja
    return render_template('commonOnesIndex.html', commonP=commonP)


# !!!!!_________________main Content above

# !!!!!_________________main Content below
# Referred to as "Basket" to the user

# Referred to as "Basket" to the user
@bp.route('/houseToHome/cart', methods=['POST', 'GET'])
def placeOrder():
    product_id = request.values.get('product_id')

    # retrieve order if there is one
    if 'order_id' in session.keys():
        order = ShoppingCart.query.get(session['order_id'])
        # order will be None if order_id stale
    else:
        # there is no order
        order = None

    # create new order if needed
    # str = str.format(self.cart_id, self.order_place_status, self.cart_product_title, self.cart_product_description,
    # self.cart_product_image, self.cart_product_price, self.cart_individual_product_count, self.cart_total_product_price, self.cart_net_total_price, self.shipping_charges
    if order is None:
        order = ShoppingCart(order_place_status=False, cart_product_title='', cart_product_description='', cart_product_image='',
                             cart_product_price='', cart_net_total_price=0, shipping_charges=0, cart_total_product_price=0)
        try:
            db.session.add(order)
            db.session.commit()
            #!____________???Not table or class object
            session['order_id'] = order.cart_id
        except:
            print('failed at creating a new order')
            order = None

    # calcultate totalprice
    # self.cart_total_product_price, self.cart_net_total_price, self.shipping_charges
    total_product_price = 0
    net_total_price = 0
    shipping_charges = 15.00
    if order is not None:
        for products in order.products:
            #totalprice = totalprice + tour.price
            total_product_price = total_product_price + \
                (products.cart_product_price *
                 products.cart_individual_product_count)
    net_total_price = net_total_price + total_product_price + shipping_charges

    # are we adding an item?
    if product_id is not None and order is not None:
        product = Product.query.get(product_id)
        if product not in order.products:
            try:
                order.products.append(product)
                db.session.commit()
            except:
                return 'There was an issue adding the item to your basket'
            return redirect(url_for('main.order'))
        else:
            products.cart_individual_product_count = products.cart_individual_product_count + 1
            order.products.append(product)
            db.session.commit()
            #flash('item already in basket')
            # return redirect(url_for('main.order'))

    return render_template('cartIndex.html', order=order, total_product_price=total_product_price, net_total_price=net_total_price)


# Delete specific basket items
@bp.route('/houseToHome/deletecartproduct', methods=['POST'])
def deletecartproduct():
    id = request.form['id']  # !_______________
    if 'order_id' in session:
        order = ShoppingCart.query.get_or_404(session['order_id'])
        product_to_delete = ShoppingCart.query.get(id)
        try:
            order.products.remove(product_to_delete)
            db.session.commit()
            return redirect(url_for('main.order'))  # !______
        except:
            return 'Problem deleting item from order'
    return redirect(url_for('main.order'))


#!-----------------------WishList methods

# Scrap basket
@bp.route('/houseToHome/emptycart')
def deleteorder():
    if 'order_id' in session:
        del session['order_id']
        flash('All items deleted')
    return redirect(url_for('main.index'))  # !-----------------


@bp.route('/houseToHome/proceedtocheckout', methods=['POST', 'GET'])
def proceedtocheckout():
    form = ProceedToCheckoutForm()
    if 'order_id' in session:
        order = ShoppingCart.query.get_or_404(session['order_id'])

        if form.validate_on_submit():
            order.order_place_status = True
            order.buyerFullName = form.buyerFullName.data
            order.shippingHomeAddressDetails = form.shippingHomeAddressDetails.data
            order.city = form.city.data
            order.state = form.state.data
            order.postCode = form.postCode.data

            try:
                db.session.commit()
                del session['order_id']
                flash(
                    'Thank you! One of for shopping with us. Your order is ready. Please make the final payment transaction...')
                return redirect(url_for('main.index'))  # !___________________
            except:
                return 'There was an issue completing your order'
    return render_template('checkout.html', form=form)  # !____________________

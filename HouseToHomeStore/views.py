from asyncio.log import logger
from flask import Blueprint, render_template, url_for, request, session, flash, redirect
from .models import Product, ShoppingCart, WishList
from datetime import datetime
from .forms import ProceedToCheckoutForm
from .login import LogInForm
from . import db
import logging


bp = Blueprint('main', __name__, template_folder='templates')


# todo: 1. create databse for models
# todo: 2. load products from data base to the 6 different products page
# todo: 3. delete product from cart
# todo: 4. delete allllll the products from cart
# todo: 5. delete products from wishlist
# todo: 6. add products to cart
# todo: 7. add products to wishList both from products page and cart
# todo: 8. make login form work in modal if possible
# todo: 9. check houseToHome Database content
# todo: 10. delete extra folders in project as of sir ..........comment properly and add details
# todo: 11. Make final test and prepare vedio

#! COMPLETED TASKS:
#! 1. displayed routes for products page


@bp.route('/houseToHome')
def index():
    return render_template('index.html')


@bp.route('/houseToHome/cart/')
def cart():
    return render_template('cartIndex.html')


@bp.route('/houseToHome/wishlist/')
def wishlist():
    return render_template('wishListIndex.html')


@bp.route('/houseToHome/kitchenproducts/')
def kitchenproducts():
    kitchensP = Product.query.filter(Product.category == 'Kitchen')
    # logging.info(kitchensP)
    return render_template('kitchenIndex.html', kitchensP=kitchensP)
    # return render_template('kitchenIndex.html')


@bp.route('/houseToHome/livingproducts/')
def livingproducts():
    livingsP = Product.query.filter(Product.category == 'LivingRoom')
    return render_template('livingIndex.html', livingsP=livingsP)


@bp.route('/houseToHome/bathroomproducts/')
def bathroomproducts():
    bathroomsP = Product.query.filter(Product.category == 'BathRoom')
    return render_template('bathRoomIndex.html', bathroomsP=bathroomsP)


@bp.route('/houseToHome/outdoors/')
def outdoors():
    outdoorsP = Product.query.filter(Product.category == 'Outdoor')
    return render_template('outDoorsIndex.html', outdoorsP=outdoorsP)


@bp.route('/houseToHome/bedroomproducts/')
def bedroomproducts():
    bedroomsP = Product.query.filter(Product.category == 'BedRoom')
    return render_template('bedRoomIndex.html', bedroomsP=bedroomsP)


@bp.route('/houseToHome/commonproducts/')
def commonproducts():
    commonP = Product.query.filter(Product.category == 'Common')
    return render_template('commonOnesIndex.html', commonP=commonP)


# Referred to as "Cart" to the user
@bp.route('/houseToHome/placeOrder', methods=['POST', 'GET'])
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
    if order is None:
        order = ShoppingCart(order_place_status=False, cart_product_title='', cart_product_description='', cart_product_image='',
                             cart_product_price='', cart_net_total_price=0, shipping_charges=0, cart_total_product_price=0)
        try:
            db.session.add(order)
            db.session.commit()
            session['order_id'] = order.cart_id
        except:
            print('failed at creating a new order')
            order = None

    # calcultate totalprice
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
            return redirect(url_for('main.index'))
        else:
            products.cart_individual_product_count = products.cart_individual_product_count + 1
            order.products.append(product)
            db.session.commit()
            return redirect(url_for('main.index'))

    return render_template('cartIndex.html', order=order, total_product_price=total_product_price, net_total_price=net_total_price)


# Delete specific basket items
@bp.route('/houseToHome/deletecartproduct', methods=['POST'])
def deletecartproduct():
    id = request.form['id']
    if 'order_id' in session:
        order = ShoppingCart.query.get_or_404(session['order_id'])
        product_to_delete = ShoppingCart.query.get(id)
        try:
            order.products.remove(product_to_delete)
            db.session.commit()
            return redirect(url_for('main.index'))
        except:
            return 'Problem deleting item from order'
    return redirect(url_for('main.index'))


# Scrap basket
@bp.route('/houseToHome/emptycart')
def deleteorder():
    if 'order_id' in session:
        del session['order_id']
        flash('All items deleted')
    return redirect(url_for('main.index'))


# Referred to as "Add Product To WishList" by the user
@bp.route('/houseToHome/addProductToWishList', methods=['POST', 'GET'])
def addProductToWishList():
    product_id = request.values.get('product_id')

    # retrieve order if there is one
    if 'order_id' in session.keys():
        requestByUser = WishList.query.get(session['order_id'])
        # order will be None if order_id stale
    else:
        # there is no order
        requestByUser = None

    # create new request if needed
    if requestByUser is None:
        requestByUser = WishList(wishList_product_title='', wishList_product_description='', wishList_product_image='',
                                 wishList_product_price='', individual_product_count=0)
        try:
            db.session.add(requestByUser)
            db.session.commit()
            session['order_id'] = requestByUser.wishList_id
        except:
            print('failed at add product to wishlist')
            requestByUser = None

    # are we adding an item?
    if product_id is not None and requestByUser is not None:
        product = Product.query.get(product_id)
        if product not in requestByUser.products:
            try:
                requestByUser.products.append(product)
                db.session.commit()
            except:
                return 'There was an issue adding the item to your basket'
            return redirect(url_for('main.index'))
        else:
            product.individual_product_count = product.individual_product_count + 1
            requestByUser.products.append(product)
            db.session.commit()
            return redirect(url_for('main.index'))

    return render_template('wishListIndex.html', requestByUser=requestByUser)


# Delete specific WishList items
@bp.route('/houseToHome/deletewishListproduct', methods=['POST'])
def deletewishListproduct():
    id = request.form['id']
    if 'order_id' in session:
        requestByUser = WishList.query.get_or_404(session['order_id'])
        product_to_delete = WishList.query.get(id)
        try:
            requestByUser.products.remove(product_to_delete)
            db.session.commit()
            return redirect(url_for('main.index'))
        except:
            return 'Problem deleting item from order'
    return redirect(url_for('main.index'))


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
                return redirect(url_for('main.index'))
            except:
                return 'There was an issue completing your order'
    return render_template('checkout.html', form=form)  # !____________________

'''
CREATING A NEW DATABASE
-----------------------
Read explanation here: https://flask-sqlalchemy.palletsprojects.com/en/2.x/contexts/

In the terminal navigate to the project folder just above the miltontours package
Type 'python' to enter the python interpreter. You should see '>>>'
In python interpreter type the following (hitting enter after each line):
    from miltontours import db, create_app
    db.create_all(app=create_app())
The database should be created. Exit python interpreter by typing:
    quit()
Use DB Browser for SQLite to check that the structure is as expected before 
continuing.

ENTERING DATA INTO THE EMPTY DATABASE
-------------------------------------

# Option 1: Use DB Browser for SQLite
You can enter data directly into the cities or tours table by selecting it in
Browse Data and clicking the New Record button. The id field will be created
automatically. However be careful as you will get errors if you do not abide by
the expected field type and length. In particular the DateTime field must be of
the format: 2020-05-17 00:00:00.000000

# Option 2: Create a database seed function in an Admin Blueprint
See below. This blueprint needs to be enabled in __init__.py and then can be 
accessed via http://127.0.0.1:5000/admin/dbseed/
Database constraints mean that it can only be used on a fresh empty database
otherwise it will error. This blueprint should be removed (or commented out)
from the __init__.py after use.

Use DB Browser for SQLite to check that the data is as expected before 
continuing.
'''

from flask import Blueprint
from . import db
from .models import Product, WishList, ShoppingCart
import datetime


bp = Blueprint('admin', __name__, url_prefix='/admin/')

# function to put some seed data in the database


@bp.route('/dbseed/')
def dbseed():
    # Naming rule of unique_product_id: (category_id)+(item number in each category)
    # category_id: 1->kitchen products,  2->living room products,  3->bath room products
    #              4->bed room products,  5->common products,  6->outdoors products

    # Create data of kitchen products and add them in to DB
    product_kitchen_1 = Product(unique_product_id=101,
                                title='''CHEF'S APRON''',
                                description='Lemon print, yellow & white',
                                image='ChefsApron.png',
                                dimension='Adult',
                                material='Cotton',
                                category='Kitchen',
                                price=14.40)
    product_kitchen_2 = Product(unique_product_id=102,
                                title='BLUE MELAMINE DINNER SET',
                                description='set of 4 big plates, 4 small plates, 4 bowls',
                                image='cabo-melamine-dinnerware-set-of-4-blue-c.jpeg',
                                dimension='Standard Dishware Size',
                                material='Melamine',
                                category='Kitchen',
                                price=150.00)
    product_kitchen_3 = Product(unique_product_id=103,
                                title='KITCHEN TOWELS',
                                description='Set of 12, vibrant color prints',
                                image='Kitchen_Towels.jpg',
                                dimension='35 Centimeters * 35 Centimeters',
                                material='Textured Cotton',
                                category='Kitchen',
                                price=40.00)
    product_kitchen_4 = Product(unique_product_id=104,
                                title='SPOON AND FORK SET',
                                description='Matte Gold finish, black handles, set of 3 each',
                                image='Spoon&ForkSet.png',
                                dimension='Standard Adult Spoon Size',
                                material='Steel With Gold Coating',
                                category='Kitchen',
                                price=60.00)
    product_kitchen_5 = Product(unique_product_id=105,
                                title='OVEN MITTS',
                                description='Spring Floral print',
                                image='OvenMitts2.png',
                                dimension='Standard Size For Adult Hands',
                                material='Thick Cotton',
                                category='Kitchen',
                                price=8.00)
    product_kitchen_6 = Product(unique_product_id=106,
                                title='TEA TOWELS',
                                description='Fruit print - set of 3',
                                image='TeaTowels.png',
                                dimension='30 Centimeters * 30 Centimeters',
                                material='Durable Cotton',
                                category='Kitchen',
                                price=18.60)
    product_kitchen_7 = Product(unique_product_id=107,
                                title='KITCHEN DOOR HERB POTS',
                                description='Blue color with White hue',
                                image='HerbPotters.jpeg',
                                dimension='Small(Height 20 Cms)',
                                material='Ceramic',
                                category='Kitchen',
                                price=24.99)
    product_kitchen_8 = Product(unique_product_id=108,
                                title='BLUE SCALLOPED DISH SET',
                                description='Set of 4 each - small plate, large plate, small bowl, large bowl',
                                image='NavyScallopedDishSet16.png',
                                dimension='Standard Dish Ware Size',
                                material='Bone China',
                                category='Kitchen',
                                price=544.44)
    try:
        db.session.add(product_kitchen_1)
        db.session.add(product_kitchen_2)
        db.session.add(product_kitchen_3)
        db.session.add(product_kitchen_4)
        db.session.add(product_kitchen_5)
        db.session.add(product_kitchen_6)
        db.session.add(product_kitchen_7)
        db.session.add(product_kitchen_8)
        db.session.commit()
    except:
        return 'There was an issue adding the kitchen_products in dbseed function'

    # Create data of living room products and add them in to DB
    product_livingroom_1 = Product(unique_product_id=201,
                                   title='CUSHIONS',
                                   description='Set of 4, Plush Comfortable, grey & yellow shades',
                                   image='Pillow.png',
                                   dimension='40 Cm * 40 Cm',
                                   material='Cotton, Machine Washable',
                                   category='LivingRoom',
                                   price=50.40)
    product_livingroom_2 = Product(unique_product_id=202,
                                   title='TASSELED THROW BLANKET',
                                   description='Set of 4, KNITTED, Common shades as in picture',
                                   image='Throw_Blanket.jpg',
                                   dimension='2 Meters * 2 Meters',
                                   material='Polyester, Machine Washable',
                                   category='LivingRoom',
                                   price=56.00)
    product_livingroom_3 = Product(unique_product_id=203,
                                   title='ARTIFICIAL INDOOR PLANT',
                                   description='Green, ceramic vase underneath',
                                   image='Plant_Artificial.jpg',
                                   dimension='2 Meters, Green',
                                   material='Resin And Plastic',
                                   category='LivingRoom',
                                   price=90.40)
    product_livingroom_4 = Product(unique_product_id=204,
                                   title='OTTOMAN',
                                   description='Tan color',
                                   image='ottoman_Jpeg.jpg',
                                   dimension='2 Feet Hieght, 0.5 Meter Radius',
                                   material='TEDDY BEAR FABRIC',
                                   category='LivingRoom',
                                   price=18.50)
    product_livingroom_5 = Product(unique_product_id=205,
                                   title='LIVING SOFA',
                                   description='Three seater, with plush pillows for back',
                                   image='Sofa.jpeg',
                                   dimension='2.5 Meters * 0.8 Meters',
                                   material='Velvet Fabric With Customisable Colour Option',
                                   category='LivingRoom',
                                   price=140.40)
    product_livingroom_6 = Product(unique_product_id=206,
                                   title='TULIP FLOWER VASE',
                                   description='Shades of pink, red & yellow',
                                   image='FlowerVase.jpeg',
                                   dimension='Vase-1 Feet, Flowers-30 Cms',
                                   material='Ceramic Vase, Plastic Flowers',
                                   category='LivingRoom',
                                   price=28.89)
    product_livingroom_7 = Product(unique_product_id=207,
                                   title='COFFEE TABLE',
                                   description='Dark brown finish, natural wood',
                                   image='Coffee Table.jpeg',
                                   dimension='Face Radius-0.5 Meters',
                                   material='Teak Wood, Durable Chocolate Poslish',
                                   category='LivingRoom',
                                   price=289.40)
    try:
        db.session.add(product_livingroom_1)
        db.session.add(product_livingroom_2)
        db.session.add(product_livingroom_3)
        db.session.add(product_livingroom_4)
        db.session.add(product_livingroom_5)
        db.session.add(product_livingroom_6)
        db.session.add(product_livingroom_7)
        db.session.commit()
    except:
        return 'There was an issue adding the livingroom_products in dbseed function'

    # Create data of bath room products and add them in to DB
    product_bathroom_1 = Product(unique_product_id=301,
                                 title='KIDS BATH DUCK',
                                 description='Yellow small duck with squeezy noise',
                                 image='Bath_Duck.jpeg',
                                 dimension='Medium',
                                 material='Rubber',
                                 category='BathRoom',
                                 price=10.90)
    product_bathroom_2 = Product(unique_product_id=302,
                                 title='BATH MAT',
                                 description='Orange theme, machine washable',
                                 image='Bath_Mats.jpeg',
                                 dimension='70 Centimeters * 30 Centimeters',
                                 material='Cotton Jute + Polyester',
                                 category='BathRoom',
                                 price=26.00)
    product_bathroom_3 = Product(unique_product_id=303,
                                 title='SET OF SEVEN TOWELS',
                                 description='Set of 7 in vibrant colors',
                                 image='body_Towel.jpeg',
                                 dimension='Large',
                                 material='Cotton With Ruffle Texture',
                                 category='BathRoom',
                                 price=240.40)
    product_bathroom_4 = Product(unique_product_id=304,
                                 title='SHAMPOO/SOAP/CONDITIONER CONTAINER',
                                 description='Set of - 3, Amber glass colored, pump bottles',
                                 image='Containers.jpeg',
                                 dimension='Standard Size',
                                 material='High Quality Glass',
                                 category='BathRoom',
                                 price=80.99)
    product_bathroom_5 = Product(unique_product_id=305,
                                 title='FACE TOWELS',
                                 description='Set of 8, ruffled texture, common vibrant colors',
                                 image='face_towels.jpeg',
                                 dimension='30 Centimeters * 20 Centimeters',
                                 material='Thick Cotton Jute Texture',
                                 category='BathRoom',
                                 price=100.40)
    product_bathroom_6 = Product(unique_product_id=306,
                                 title='HAND TOWELS',
                                 description='Set of 2, ruffled texture, Blush Color',
                                 image='hand_towel.jpeg',
                                 dimension='40 Centimeters * 30 Centimeters',
                                 material='Thick Cotton Jute Texture',
                                 category='BathRoom',
                                 price=56.40)
    try:
        db.session.add(product_bathroom_1)
        db.session.add(product_bathroom_2)
        db.session.add(product_bathroom_3)
        db.session.add(product_bathroom_4)
        db.session.add(product_bathroom_5)
        db.session.add(product_bathroom_6)
        db.session.commit()
    except:
        return 'There was an issue adding the bathroom_products in dbseed function'

    # Create data of bed products and add them in to DB
    product_bedroom_1 = Product(unique_product_id=401,
                                title='KING BED',
                                description='''Made out of durable teak wood, retan net at the Head & Foot boards''',
                                image='bed_King.jpg',
                                dimension='198 Centimeter * 208 Centimeters',
                                material='Teak Wood, Dark Cholcolate Polish',
                                category='BedRoom',
                                price=1000.90)
    product_bedroom_2 = Product(unique_product_id=402,
                                title='FLORAL KING BEDSHEET',
                                description='''Orange theme, machine washable''',
                                image='BedSheets.jpg',
                                dimension='250 Centemeters * 300 Centimeters',
                                material='Polyester, Machine Washable',
                                category='BedRoom',
                                price=89.00)
    product_bedroom_3 = Product(unique_product_id=403,
                                title='QUILT SET OF 7',
                                description='Flamingo print on teal background',
                                image='quilt_set_7.jpeg',
                                dimension='Suitable For KING Size Bed',
                                material='Thick Cotton Fabric',
                                category='BedRoom',
                                price=100.99)
    product_bedroom_4 = Product(unique_product_id=404,
                                title='BED THROW PILLOW',
                                description='''Set of 2, cream colour with multi colored crochet embroidery''',
                                image='ThrowPillow.jpg',
                                dimension='60 Centimeters * 60 Centimeters',
                                material='Thick Cotton Jute Texture',
                                category='BedRoom',
                                price=100.40)
    try:
        db.session.add(product_bedroom_1)
        db.session.add(product_bedroom_2)
        db.session.add(product_bedroom_3)
        db.session.add(product_bedroom_4)
        db.session.commit()
    except:
        return 'There was an issue adding the bedroom_products in dbseed function'

    # Create data of common products and add them in to DB
    product_common_1 = Product(unique_product_id=501,
                               title='CURTAINS',
                               description='Large Door light floral curtain set',
                               image='Curtains.jpeg',
                               dimension='2.5 M * 50 Cm Door',
                               material='Cotton, Machine Washable',
                               category='Common',
                               price=150.40)
    product_common_2 = Product(unique_product_id=502,
                               title='CANDEL',
                               description='3-Wicked Vanilla Aroma',
                               image='candels.jpg',
                               dimension='7 Cm Hieght',
                               material='Plant Based Wax',
                               category='Common',
                               price=56.00)
    product_common_3 = Product(unique_product_id=503,
                               title='AROMA DIFFUSER',
                               description='Grey',
                               image='Aroma_Diffuser.jpg',
                               dimension='15 Cm Height',
                               material='Marble Carved',
                               category='Common',
                               price=180.40)
    product_common_4 = Product(unique_product_id=504,
                               title='SCONCES',
                               description='General sconces',
                               image='Sconces.jpg',
                               dimension='Variable Sizes - Customisable',
                               material='Matte Metallic Gold, Glass',
                               category='Common',
                               price=18.50)
    product_common_5 = Product(unique_product_id=505,
                               title='WALLPEPER',
                               description='Floral white background',
                               image='wallpaper.png',
                               dimension='Set Of Single Role For 500 Sq Feet Wall Coverage',
                               material='Semi Permanent Thick Paper Base',
                               category='Common',
                               price=670.00)
    product_common_6 = Product(unique_product_id=506,
                               title='LAMP',
                               description='Cream Color shade',
                               image='Lamp.jpeg',
                               dimension='2 Feet Height',
                               material='Canvas Shade, Jute',
                               category='Common',
                               price=128.89)
    product_common_7 = Product(unique_product_id=507,
                               title='RUG',
                               description='Tasseled, multi colored, light base',
                               image='Rug.jpg',
                               dimension='8 Feet * 6 Feet',
                               material='Ruggable Muterial',
                               category='Common',
                               price=899.40)
    try:
        db.session.add(product_common_1)
        db.session.add(product_common_2)
        db.session.add(product_common_3)
        db.session.add(product_common_4)
        db.session.add(product_common_5)
        db.session.add(product_common_6)
        db.session.add(product_common_7)
        db.session.commit()
    except:
        return 'There was an issue adding the common_products in dbseed function'

    # Create data of outdoors products and add them in to DB
    product_outdoor_1 = Product(unique_product_id=601,
                                title='FLOWER SEEDS',
                                description='Set of 25, common gardening beautiful flowers, types as in image',
                                image='Flower_seeds.jpeg',
                                dimension='Packet Dimensions-15cm * 10 Cm',
                                material='Natural Original Seeds',
                                category='Outdoor',
                                price=125.00)
    product_outdoors_2 = Product(unique_product_id=602,
                                 title='ARTIFICIAL INDOOR PLANT POTS',
                                 description='Set of 5, beige & shades',
                                 image='Outside_Pots_Set_of_5.jpeg',
                                 dimension='Different Ranging From 30 Cm - 50 Cm',
                                 material='Cement, Jute, Ceramic',
                                 category='Outdoor',
                                 price=144.40)
    product_outdoors_3 = Product(unique_product_id=603,
                                 title='OUTSIDE CLIMATE RESISTANT FURNITURE SET',
                                 description='Natural Soft white color, Coffee table, 2 side sofas, main sofa, ottoman, pillows',
                                 image='OutDoorFurniture_set.jpeg',
                                 dimension='Fit For Porch/Balcony Or Backyard Of 4 Meters * 3.5 Meters',
                                 material='Jute, Retan, Bamboo Sheets',
                                 category='Outdoor',
                                 price=500.50)
    try:
        db.session.add(product_outdoor_1)
        db.session.add(product_outdoors_2)
        db.session.add(product_outdoors_3)
        db.session.commit()
    except:
        return 'There was an issue adding the outdoors_products in dbseed function'

    return 'DATA LOADED'

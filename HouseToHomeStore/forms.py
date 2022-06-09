from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField
from wtforms.validators import InputRequired, email
# form used in cart


class ProceedToCheckoutForm(FlaskForm):
    buyerFullName = StringField(
        "Your Full Name ", validators=[InputRequired()])
    shippingHomeAddressDetails = StringField(
        "Your Home Address", validators=[InputRequired()])
    city = StringField("Your City ", validators=[InputRequired()])
    state = StringField("Your State ", validators=[InputRequired()])
    postCode = StringField("Your Area PostCode ", validators=[InputRequired()])
    contactDetails = StringField(
        "Your Contact Details ", validators=[InputRequired()])
    submit = SubmitField("Proceed to Final Payment Transaction ")

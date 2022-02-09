# from flask import Flask 
# from flask_sqlalchemy import SQLAlchemy 
# import os

# app = Flask(__name__) # Declare Flask object

# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI") # Set the connection string to connect to a database
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
# db = SQLAlchemy(app) # Declare SQLAlchemy object

# class Countries(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(30), nullable=False)
#     cities = db.relationship('Cities', backref='countries') 

# class Cities(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(30), nullable=False)
#     country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=False)

# if __name__=='__main__':
#     app.run(debug==True, host='0.0.0.0')

# #Exercise
# class Orders(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     address = db.Column(db.String(30), nullable=False)
#     orders_products = db.relationship('Orders_Products', backref='orders')
    
# class Products(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(30), nullable=False)
#     orders_products = db.relationship('Orders_Products', backref='products')
# class Orders_Products(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
#     product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
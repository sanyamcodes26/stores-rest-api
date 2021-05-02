from flask_jwt import jwt_required
from db import db

class ItemModel(db.Model):

    __tablename__='items' #telling sqlalchemy about our database so as to establish relationship between model and database
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(20))
    price= db.Column(db.Float(precision=3))
    store_id= db.Column(db.Integer, db.ForeignKey('stores.id'))
    store= db.relationship('StoreModel')

    def __init__(self,name,price,store_id):
        self.name=name
        self.price=price
        self.store_id=store_id

    def json(self):
        return {
            "id":self.id,
            "name": self.name,
            "price": self.price
        }

    @classmethod
    def find_by_name(cls, item_name):
        # select * from items where name = item_name and returns ItemModel object
        return ItemModel.query.filter_by(name=item_name).first()

        # select * from items where name = item_name limit 1
        #return ItemModel.query.filter_by(name=item_name).first()

    def save_to_db(self): #it also updates in a sense   
        db.session.add(self)
        db.session.commit()

    @jwt_required()
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        
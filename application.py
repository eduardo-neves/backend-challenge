from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_rest_jsonapi import Api, ResourceDetail, ResourceList
from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/entries.db'
db = SQLAlchemy(app)

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

db.create_all()

class EntrySchema(Schema):
    class Meta:
        type_ = 'entry'
        self_view = 'entry_one'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'entry_many'

    id = fields.Integer()
    name = fields.Str(required=True)

class EntryMany(ResourceList):
    schema = EntrySchema
    data_layer = {'session': db.session,
                  'model': Entry}

class EntryOne(ResourceDetail):
    schema = EntrySchema
    data_layer = {'session': db.session,
                  'model': Entry}

api = Api(app)
api.route(EntryMany, 'entry_many', '/entries')
api.route(EntryOne, 'entry_one', '/entries/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
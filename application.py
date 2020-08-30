from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_rest_jsonapi import Api, ResourceDetail, ResourceList
from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields

# Create a new Flask application
app = Flask(__name__)

# Set up SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/entries.db'
db = SQLAlchemy(app)

# Define a class for the Entry table
class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

# Create the table
db.create_all()

# Create data abstraction layer
class EntrySchema(Schema):
    class Meta:
        type_ = 'entry'
        self_view = 'entry_one'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'entry_many'

    id = fields.Integer()
    name = fields.Str(required=True)

# Create resource managers and endpoints

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

# main loop to run app in debug mode
if __name__ == '__main__':
    app.run(debug=True)
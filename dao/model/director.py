from marshmallow import Schema, fields

from setup_db import db


class Director(db.Model):
    __tablename__ = 'director'
    # __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Colomn(db.String(255))


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()

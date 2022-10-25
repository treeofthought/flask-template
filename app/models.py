from . import db


class ExampleModel(db.Model):
  __tablename__ = 'example_models'
  id = db.Column(db.Integer, primary_key=True)
  string_attribute = db.Column(db.String(2))

  def __repr__(self):
    return '<ExampleModel %r>' % self.string_attribute

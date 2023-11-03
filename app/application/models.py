from application import db
from datetime import datetime

class myList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(128), nullable = False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    user_score = db.Column(db.Integer, default=0)
    text_submissions = db.relationship('TextSubmission', backref='author', lazy='dynamic')

class TextSubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    language = db.Column(db.String(120))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    sentence_list = db.Column(db.PickleType)
    word_list = db.Column(db.PickleType)
    popularity = db.Column(db.Integer, default=0)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f'<TextSubmission {self.title}>'

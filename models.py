from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from datetime import datetime
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now() )

    def __repr__(self) -> str:
        return '<TASK %r>' % self.id
from connections.dbconnection import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    post = db.relationship("Post", back_populates="user")

    def __repr__(self) -> str:
        return self.name
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500))
    body = db.Column(db.String(1000))
    user_id = db.Column(db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User", back_populates="post")
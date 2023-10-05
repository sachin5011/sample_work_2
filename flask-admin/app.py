from flask import Flask
from connections.dbconnection import db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models.user_model import User, Post

app = Flask(__name__)

# Creating Admin object
admin = Admin()

app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///admin.db"
app.config["SECRET_KEY"] = "secret"
# Database Initilization
db.init_app(app)
# admin object initilization
admin.init_app(app)

with app.app_context():
    db.create_all()

class PostView(ModelView):
    can_delete = True
    form_columns = ["title", "body", "user"]
    column_list = ["title", "body", "user"]

admin.add_view(ModelView(User, db.session))
admin.add_view(PostView(Post, db.session))


if __name__ == "__main__":
    app.run(debug=True)


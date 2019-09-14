from app import db


class User(db.Model):
    __tablename__ = 'users'
    username = db.Column(db.String(255), unique=False)
    password = db.Column(db.String(255), unique=True)

    def save(self):
        pass

    def delete(self):
        pass

    def generate_password(self):
        pass

    def check_password(self):
        pass

from webapp import db


# Создаем класс User для возможности хранения данных пользователей
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)  # Пароли обычно хранятся в зашифрованном виде

    def __repr__(self):
        return f'<User {self.login}>'
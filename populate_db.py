from app import db, User


# Cria tabelas no banco
try:
    db.create_all()
except Exception:
    pass

# popular banco
user1 = User(username="fernando", email="nando@gmail.com")
db.session.add(user1)
user2 = User(username="Rafael", email="rafa@gmail.com")
db.session.add(user2)
user3 = User(username="Gustavo", email="gustavo@gmail.com")
db.session.add(user3)
user4 = User(username="Camila", email="camila@gmail.com")
db.session.add(user4)

db.session.commit()



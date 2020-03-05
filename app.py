from flask import Flask, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


# Criando aplicacao
app = Flask(__name__)

# Setando algumas configuracoes da aplicacao
app.config['SECRET_KEY'] = 'super_secret' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:lulalivre@localhost:5432/flask_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

# Configurando as extensoes
admin = Admin(app, name="flask-teste", template_mode="bootstrap3")
CORS(app)
db = SQLAlchemy(app)

# Criando modelos (tabelas)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return "User {}".format(self.username)

# Cria pagina no admin referente as tabelas
# A pagina do admin fica em localhost:5000/admin
admin.add_view(ModelView(User, db.session))

# Criando as rotas
@app.route('/')
def index():
    users = User.query.all()
    return render_template("index.html", users=users)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

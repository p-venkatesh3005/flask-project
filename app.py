from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///venky.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
class Venky(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'{self.id} - {self.name}'

@app.route('/')
def hello():
    venky=Venky(name="ism6art",id="165605",email="12544463@gmail.com")
    db.session.add(venky)
    db.session.commit()
    return render_template('index.html')

@app.route('/hii')
def hell():
    return "welcome"
if __name__=="__main__":
    app.run(debug=True)

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_details.db'  # SQLite database file
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"User(name='{self.name}', email='{self.email}', phone='{self.phone}')"

@app.route('/', methods=['GET', 'POST'])
def capture_user_details():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')

        new_user = User(name=name, email=email, phone=phone)
        db.session.add(new_user)
        db.session.commit()

        return 'User details captured successfully!'
    return '''
        <form method="POST">
            <label for="name">Name:</label>
            <input type="text" name="name" id="name" required><br>

            <label for="email">Email:</label>
            <input type="email" name="email" id="email" required><br>

            <label for="phone">Phone:</label>
            <input type="tel" name="phone" id="phone" required><br>

            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)

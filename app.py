from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes import main
from instance.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

# db = SQLAlchemy(app)

# if __name__ == "__main__":
#     app.run(debug=True)

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# import os

# app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")

# db = SQLAlchemy(app)

# if __name__ == "__main__":
#     app.run(debug=True)
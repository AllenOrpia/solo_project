from flask_app import app
from flask_app.controllers import trainers
from flask_app.controllers import reviews
from flask_app.controllers import berries

if __name__ == '__main__':
    app.run(debug=True)

from flask_app import app
from flask import request, render_template, jsonify, redirect, session

from flask_app.models.trainer import Trainer


@app.route('/flavors/<string:flavor>') 
def berryFlavor(flavor):
    email = session['trainer_email']
    user = Trainer.get_by_email(email)
    return render_template('berryFlavors.html', user = user, flavor = flavor)
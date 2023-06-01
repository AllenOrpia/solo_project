from flask_app import app
from flask import request, render_template, jsonify,redirect,session, flash
from flask_app.models.trainer import Trainer
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)



@app.route('/')
def index():
    return redirect('/register')

@app.route('/register')
def login_register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login_trainer', methods =['POST'])
def login_trainer():
    if not Trainer.validate_login(request.form):
        return redirect('/login')
    else:
        log_trainer = Trainer.get_by_email(request.form['email'])
        if not log_trainer.password == request.form['password']:
            flash('Invalid password')
            return redirect('/login')
    session['trainer'] = log_trainer.id
    email = request.form["email"]
    session['trainer_email'] = email
    return redirect('/dashboard')


@app.route('/register_trainer', methods =['POST'])
def register_trainer():
    if not Trainer.validate_register(request.form):
        return redirect('/')
    data = {
        'trainer_name': request.form['trainer_name'],
        'email': request.form['email'],
        'password': request.form['password']
    }
    log_trainer = Trainer.createTrainer(data)
    session['trainer'] = log_trainer
    return redirect('/login')


@app.route('/dashboard')
def dashboard():
    if 'trainer' not in session:
        return redirect('/log_out')
    email = session['trainer_email']
    user = Trainer.get_by_email(email)
    return render_template('index.html', user = user)

@app.route('/user_account')
def account():
    if 'trainer' not in session:
        return redirect('/log_out')
    user = Trainer.get_by_email(session['trainer_email'])
    reviews = Trainer.get_trainer_with_reviews(session['trainer_email'])
    return render_template('user_account.html', reviews = reviews, user = user)

@app.route('/log_out')
def log_out():
    session.clear()
    return redirect('/login')








from flask_app.models import review
from flask_app.controllers import trainers


from flask_app import app
from flask import request, render_template, jsonify, redirect, session
from flask_app.models.trainer import Trainer


# @app.route('/berry/<int:id>')
# def get_One_Berry_By_Id(id):
#     email = session['trainer_email']
#     trainer = Trainer.get_by_email(email)
#     berry = Review.get_one_by_berry_api_id(id)
#     reviews = Review.get_all_reviews_by_berry_id(id)
#     return render_template('berry.html', id = id, trainer = trainer , reviews = reviews, berry = berry ) 



@app.route('/search', methods = ['POST'])
def search_Berry_By_Name():
    name = request.form['searchInput']
    return redirect(f'/berry/{name}') 

@app.route('/berry/<string:name>')
def get_One_Berry_By_Name(name):
    if 'trainer' not in session:
        return redirect('/log_out')
    reviews = review.Review.get_all_reviews_by_berry_name(name)
    email = session['trainer_email']
    trainer = Trainer.get_by_email(email)
    return render_template('berry.html', name = name, trainer = trainer, reviews = reviews) 

@app.route('/create-berry-review',methods=['POST'])
def createBerryReview():
    review.Review.create_review(request.form)
    return redirect(f'/berry/{request.form["berry_name"]}')

@app.route('/delete/<int:id>')
def delete(id):
    if 'trainer' not in session:
        return redirect('/log_out')
    one_review = review.Review.get_one_by_id(id)
    
    review.Review.delete_by_id(id)
    return redirect(f'/berry/{one_review.berry_name}')

@app.route('/user-delete/<int:id>')
def userDelete(id):
    if 'trainer' not in session:
        return redirect('/log_out')
    review.Review.delete_by_id(id)
    return redirect('/user_account')

@app.route('/edit-review/<int:id>')
def editReview(id):
    if 'trainer' not in session:
        return redirect('/log_out')
    return render_template('edit.html', id = id, review = review.Review.get_one_by_id(id))

@app.route('/review-update' , methods =['POST'])
def updateReview():
    if 'trainer' not in session:
        return redirect('/log_out')
    review.Review.update_review_id(request.form)
    return redirect(f'/berry/{request.form["berry_name"]}')

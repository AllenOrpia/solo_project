

from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Trainer:
    db = 'berrydex'
    def __init__(self,data):
        self.id = data['id']
        self.trainer_name = data['trainer_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.reviews = []
        

    @staticmethod
    def validate_register(data):
        is_valid = True
        query = 'SELECT * FROM trainers WHERE email = %(email)s;'
        results = connectToMySQL(Trainer.db).query_db(query,data)
        if len(results) > 0:
            flash('email already exists!')
            is_valid = False
        if len(data['trainer_name']) < 3:
            if data['trainer_name'] == '':
                flash('Trainer name must be atleast 3 characters')
            else:
                flash('Trainer name must be atleast 2 characters')
            is_valid = False
        if len(data['password']) < 8:
            if data['password'] == '':
                flash('Invalid password')
            else: 
                flash('Password must be atleast 8 characters')
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            if data['email'] == '':
                flash('Email cannot be empty')
                is_valid = False
            else:
                flash('invalid email address')
                is_valid = False
        if not data['password'] == data['confirm']:
            flash('Passwords must match!')
            is_valid = False
        return is_valid
        
    @staticmethod
    def validate_login(data):
        is_valid = True
        if not EMAIL_REGEX.match(data['email']):
            if data['email'] == '':
                flash('Invalid email address')
                is_valid = False
        if not Trainer.get_by_email(data['email']):
            flash('Email does not exist')
            is_valid = False
        if data['password'] == '':
            flash('Invalid password')
            is_valid = False
        return is_valid


    @classmethod
    def createTrainer(cls,data):
        query = '''INSERT INTO trainers (trainer_name, email, password, created_at, updated_at)
                VALUES(%(trainer_name)s,%(email)s, %(password)s, NOW(), NOW());'''
        
        hashed_data = {
            'trainer_name': data['trainer_name'],
            'email': data['email'],
            'password': data['password'],
        }
        results = connectToMySQL(cls.db).query_db(query, hashed_data)

        return results
    

    @classmethod
    def get_by_email(cls, email):
        query = '''SELECT * FROM trainers WHERE email = %(email)s;'''
        results = connectToMySQL(cls.db).query_db(query, {'email':email})   
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod
    def get_by_id(cls, id):
        query = '''SELECT * FROM trainers WHERE id = %(id)s;'''
        results = connectToMySQL(cls.db).query_db(query, {'id':id})   
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod
    def get_trainer_with_reviews(cls,email):
        query = '''SELECT * FROM trainers LEFT JOIN reviews ON trainers.id = reviews.trainer_id WHERE trainers.email = %(email)s;'''
        results = connectToMySQL(cls.db).query_db(query, {'email': email})
        return results
# from flask_app.config.mysqlconnection import connectToMySQL

# class Review:
#     db = 'berrydex'
#     def __init__(self,data):
#         self.id = data['id']
#         self.trainer_id = data['trainer_id']
#         self.berry_api_id = data['berry_api_id']
#         self.berry_name = data['berry_name']
#         self.review_post = data['review_post']
#         self.created_at = data['created_at']
#         self.updated_at = data['updated_at']


#     @classmethod
#     def create_review(cls,data):
#         query = '''INSERT INTO reviews (trainer_id, berry_api_id,berry_name,review_post,created_at,updated_at)
#                     VALUES(trainer_id, berry_api_id,berry_name,review_post,NOW(), NOW());''' 
#         results = connectToMySQL(cls.db).query_db(query,data)
#         return cls(results)
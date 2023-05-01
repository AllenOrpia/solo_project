from flask_app.config.mysqlconnection import connectToMySQL

class Review:
    db = 'berrydex'
    def __init__(self,data):
        self.id = data['id']
        self.trainer_id = data['trainer_id']
        self.berry_name = data['berry_name']
        self.review_post = data['review_post']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def create_review(cls,data):
        query ='''INSERT INTO reviews (trainer_id,berry_name,review_post,created_at,updated_at)
                    VALUES(%(trainer_id)s,%(berry_name)s,%(review_post)s,NOW(), NOW());'''
        results = connectToMySQL(cls.db).query_db(query,data)
        return results

    # @classmethod
    # def get_one_by_berry_api_id(cls,berry_api_id):
    #     query = '''SELECT * FROM reviews WHERE berry_api_id = %(berry_api_id)s;'''
    #     results = connectToMySQL(cls.db).query_db(query,{'berry_api_id':berry_api_id})
    #     if not results: 
    #         return False
    #     return cls(results[0])
    
    # @classmethod
    # def get_one_by_berry_name(cls,berry_name):
    #     query = '''SELECT * FROM reviews WHERE berry_name = %(berry_name)s;'''
    #     results = connectToMySQL(cls.db).query_db(query,{'berry_name':berry_name})
    #     if not results: 
    #         return False  
    #     return cls(results[0])
    @classmethod
    def get_one_by_id(cls,id):
        query = '''SELECT * FROM reviews WHERE id = %(id)s;'''
        results = connectToMySQL(cls.db).query_db(query, {'id':id})
        return cls(results[0])

    @classmethod
    def get_all_reviews_by_berry_name(cls,berry_name):
        query = '''SELECT * FROM reviews WHERE berry_name = %(berry_name)s;'''
        results = connectToMySQL(cls.db).query_db(query,{'berry_name': berry_name})
        return results

    

    @classmethod
    def get_all_reviews_by_trainer_id(cls,trainer_id):
        query = '''SELECT * FROM reviews WHERE trainer_id = %(trainer_id)s;'''
        results = connectToMySQL(cls.db).query_db(query, {'trainer_id': trainer_id})
        if not results:
            return False
        return cls(results)
    
    @classmethod
    def delete_by_id(cls,id):
        query = '''DELETE FROM reviews WHERE id = %(id)s;'''
        results = connectToMySQL(cls.db).query_db(query,{'id':id})
        return results
    
    @classmethod
    def update_review_id(cls,data):
        query = '''UPDATE reviews
                    SET review_post =%(review_post)s, updated_at = NOW() WHERE id = %(id)s;'''
        results = connectToMySQL(cls.db).query_db(query,data)
        return results



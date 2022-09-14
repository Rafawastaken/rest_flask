from typing_extensions import Required
from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__) # App obj
db = SQLAlchemy(app) # Database obj
api = Api(app) # Api obj

##### * Config Geral * #####
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db" 


##### * Create db * #####

# Database models
class Video(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False, unique = True)
    nome = db.Column(db.String(200), nullable = False, unique = False)
    likes = db.Column(db.Integer, nullable = False, unique = False)
    views = db.Column(db.Integer, nullable = False, unique = False)

    def __repr__(self):
        return f"Video ({video_id}): {nome}, {likes}, {views}"

db.create_all()


##### * Arguments required * #####
video_args = reqparse.RequestParser()
video_args.add_argument("nome", type=str, help="Inserir nome do video", required=True)
video_args.add_argument("likes", type=int, help="Inserir número de gostos", required=True)
video_args.add_argument("views", type=int, help="Inserir visualizações do video", required=True )


##### * Abort funcitons * #####~

"""
# Check if video exists
def check_video(video_id):
    if video_id not in videos: # Se video nao encontrado, aborta
        abort(404, message = f"Video {video_id} not foud")

# Check if video doesn't exist
def video_exists(video_id):
    if video_id in videos: # Se video registado, aborta
        abort(409, message = "Video already exists") 
"""


########## * API * ##########
class Video(Resource):
    # Get request
   def get(self, video_id):
    video = Video.query.get(id = video_id)

api.add_resource(Video, "/video/<int:video_id>")

if __name__ == '__main__':
    app.run(debug = True)
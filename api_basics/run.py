from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, marshal_with, fields
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__) # App obj
db = SQLAlchemy(app) # Database obj
api = Api(app) # Api obj

##### * Config Geral * #####
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db" 


##### * Create db * #####

# Database models
class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(200), nullable = False)
    likes = db.Column(db.Integer, nullable = False)
    views = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return f"Video(nome = {nome}, likes = {likes}, views = {views})"
db.create_all()


##### * Arguments required * #####
video_args = reqparse.RequestParser()
video_args.add_argument("nome", type=str, help="Inserir nome do video", required=True)
video_args.add_argument("likes", type=int, help="Inserir número de gostos", required=True)
video_args.add_argument("views", type=int, help="Inserir visualizações do video", required=True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("nome", type=str, help="Inserir nome do video")
video_update_args.add_argument("likes", type=int, help="Inserir número de gostos")
video_update_args.add_argument("views", type=int, help="Inserir visualizações do video")

##### * Resources Fields * #####
resources_fields = {
    'id': fields.Integer,
    'nome': fields.String,
    'likes': fields.Integer,
    'views': fields.Integer
}

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
    @marshal_with(resources_fields)
    def get(self, video_id):
        video = VideoModel.query.get(video_id)  
        if not video:
            abort(404, message = "Couldn't find video requested")
        return video

    # Add video to database
    @marshal_with(resources_fields)
    def put(self, video_id):
        args = video_args.parse_args()
        if VideoModel.query.filter_by(id = video_id).first():
            abort(409, message = "Video already registered")

        new_video = VideoModel(
            id = video_id, 
            nome = args['nome'],
            likes = args['likes'],
            views = args['views']
        )

        db.session.add(new_video)
        db.session.commit()
        return new_video, 201

    # Update video
    @marshal_with(resources_fields)
    def patch(self, video_id):
        args = video_update_args.parse_args()
        video = VideoModel.query.filter_by(id = video_id).first()

        # If can't find video
        if not video: 
            abort(404, message = "Couldn't find video required")

        # Check fields to update
        if args['nome']:
            video.nome = args['nome'] 
        if args['likes']:
            video.likes = args['likes']
        if args['views']:
            video.views = args['views']

        db.session.commit()
        return video

api.add_resource(Video, "/video/<int:video_id>")

if __name__ == '__main__':
    app.run(debug = True)
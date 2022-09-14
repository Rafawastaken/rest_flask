from typing_extensions import Required
from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

video_args = reqparse.RequestParser()

# Arguments required
video_args.add_argument("nome", type=str, help="Inserir nome do video", required=True)
video_args.add_argument("likes", type=int, help="Inserir número de gostos", required=True)
video_args.add_argument("views", type=int, help="Inserir visualizações do video", required=True )

videos = {}

class Video(Resource):
    def get(self, video_id):
        try:
            video = videos[video_id]
            if not video: return {"data":"Video not found"}
            else: return videos[video_id]
        except Exception as e:
            return {"error": str(e)}

    def put(self, video_id):
        args = video_args.parse_args()
        return {video_id: args}

api.add_resource(Video, "/video/<int:video_id>")

if __name__ == '__main__':
    app.run(debug = True)
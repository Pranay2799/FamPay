from flask import Blueprint, jsonify
from app.models import Video

api_bp = Blueprint('api', __name__)

@api_bp.route('/videos', methods=['GET'])
def get_videos():
    videos = Video.query.all()
    video_list = []
    for video in videos:
        video_dict = {
            'id': video.id,
            'title': video.title,
            'description': video.description,
            'publish_datetime': video.publish_datetime.isoformat(),
            'thumbnail_url': video.thumbnail_url
        }
        video_list.append(video_dict)
    return jsonify(video_list)
from app import db

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.Text)
    publish_datetime = db.Column(db.DateTime)
    thumbnail_url = db.Column(db.String(255))

    def __repr__(self):
        return f'<Video {self.title}>'
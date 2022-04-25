from flask import Flask,request 
from flask_restful import Api, Resource, reqparse,abort,fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)
api=Api(app)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
db=SQLAlchemy(app)

class ViewModel(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    views=db.Column(db.Integer)
    likes=db.Column(db.Integer)
    
# db.create_all()

video_put_args=reqparse.RequestParser()
video_put_args.add_argument('name',type=str,help='Name of the video',location='form', required=True)
video_put_args.add_argument('likes',type=int,help='likes of the video',location='form', required=True)
video_put_args.add_argument('views',type=int,help='views of the video',location='form', required=True)



videos={}

resource_fields={
    'id':fields.Integer,
    'name': fields.String,
    'likes':fields.Integer,
    'views': fields.Integer
}

names={'jess':{'age':10,'gender':'female'},
        'bill':{'age':56,'gender':'male'}}

def abort_if_exists(video_id):
    if video_id in videos:
        abort(404,message='Already added')

def abort_video_not_exists(video_id):
    if video_id not in videos:
        abort(404,message='Not Found')

class HelloWorld(Resource):
    def get(self,name):
        return names[name]
    def post(self):
        return{'data':'Post request'}    

class Video(Resource):
    @marshal_with(resource_fields)
    def get(self,video_id):
        result=ViewModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404,message='Not Found')
        # abort_video_not_exists(video_id)
        # return videos[video_id]
        return result

    @marshal_with({})
    def put(self,video_id):
        # abort_if_exists(video_id)
        args=video_put_args.parse_args()
        video=ViewModel(name=args['name'],views=args['views'],likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        # videos[video_id]=args
        # return videos[video_id]
        return video

    def delete(self,video_id):
        abort_video_not_exists(video_id)
        del videos[video_id]
        return '',204

# api.add_resource(HelloWorld,'/hello','/world')
api.add_resource(HelloWorld,'/helloworld/<string:name>')

api.add_resource(Video,'/video/<int:video_id>')

if __name__=='__main__':
    app.run(debug=True)
from flask import Flask
from flask_restful import Api

from config import Config
from db_utils import prepare_tables
from views import ListCreateUsers, GetUser

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)


api.add_resource(ListCreateUsers, '/users')
api.add_resource(GetUser, '/users/<int:user_id>')


if __name__ == '__main__':
    prepare_tables()

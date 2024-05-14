from flask_restful import Resource, abort, reqparse
from werkzeug.security import generate_password_hash

from db_utils import get_db_connection


class ListCreateUsers(Resource):

    def get(self):
        users = self._get_users_from_db()
        return users, 200

    # def post(self):
    #     parser = reqparse.RequestParser()
    #     parser.add_argument('first_name', type=str, required=True, help='first_name is required')
    #     parser.add_argument('last_name', type=str, required=True, help='last_name is required')
    #     parser.add_argument('date_of_birth', type=str)
    #     parser.add_argument('gender', type=str)
    #     parser.add_argument('interests', type=str)
    #     parser.add_argument('city', type=str)
    #     parser.add_argument('profile_page', type=str)
    #     parser.add_argument('password', type=str, required=True, help='last_name is required')
    #     args = parser.parse_args()
    #
    #
    #
    #     return {'message': 'User created successfully'}, 201

    def _get_users_from_db(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = (
            "SELECT user_id, first_name, last_name, to_char(date_of_birth, 'YYYY-MM-DD'), gender, interests, city, profile_page FROM users")  # NoQA
        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()

        users = []
        for row in result:
            user_data = {
                'id': row[0],
                'first_name': row[1],
                'last_name': row[2],
                'date_of_birth': row[3],
                'gender': row[4],
                'interests': row[5],
                'city': row[6],
                'profile_page': row[7],
            }
            users.append(user_data)

        return users


class GetUser(Resource):

    def get(self, user_id):
        user = self._get_user_by_id(user_id)
        if user is None:
            abort(404, message="User {} doesn't exist".format(user_id))
        return user, 200

    def _get_user_by_id(self, user_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = (
            "SELECT user_id, first_name, last_name, to_char(date_of_birth, 'YYYY-MM-DD'), gender, interests, city, profile_page " # NoQA
            "FROM users WHERE user_id = %s"
        )  # NoQA
        cursor.execute(query, (user_id,))
        result = cursor.fetchall()
        conn.close()

        if result:
            for row in result:
                user_data = {
                    'id': row[0],
                    'first_name': row[1],
                    'last_name': row[2],
                    'date_of_birth': row[3],
                    'gender': row[4],
                    'interests': row[5],
                    'city': row[6],
                    'profile_page': row[7],
                }
                return user_data
        else:
            return None

import time
import jwt
import json
from meigens.settings import SECRET_KEY
from rest_framework.authentication import (BaseAuthentication, get_authorization_header)
from rest_framework import exceptions

from meigen_app.models import User

class NormalAuthentication(BaseAuthentication):
    def authenticate(self, request):
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        user_obj = User.objects.filter(name=username).first()
        if not user_obj:
            raise exceptions.AuthenticationFailed('ユーザが存在しません')
        elif user_obj.hspw != password:
            raise exceptions.AuthenticationFailed('パスワードが間違っています')
        
        token = generate_jwt(user_obj)
        return (token, None)
    
    def authenticate_header(self, request):
        pass

def generate_jwt(user):
    return jwt.encode(
        {'userid': user.pk, 'username': user.name},
        key = SECRET_KEY,
        algorithm = 'HS256',
    ).decode('utf-8')


class JWTAuthentication(BaseAuthentication):
    keyword = 'JWT'
    model = None

    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None
        
        if len(auth) == 1:
            raise exceptions.AuthenticationFailed('Authorization invalid')

        try:
            jwt_token = auth[1]
            jwt_info = jwt.decode(jwt_token, SECRET_KEY)
            userid = jwt_info.get('userid')
            try:
                user = User.objects.get(pk=userid)
                user.is_authenticated = True
                return (user, jwt_token)
            except:
                raise exceptions.AuthenticationFailed('ユーザが存在しません')
        except:
            raise exceptions.AuthenticationFailed('トークンがタイムアウトしました')
        
    
    def authenticate_header(self, request):
        pass

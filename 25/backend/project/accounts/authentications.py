from cmath import exp
from datetime import datetime
import jwt
from rest_framework import authentication, exceptions

from django.contrib.auth import get_user_model
from django.conf import settings

class JWTAuthentication(authentication.BaseAuthentication):

    
    def authenticate(self, request):
        access_token = request.headers.get('Authorization')
        if not access_token:
            return None
        return self.authenticate_credentials(access_token)
    
    def authenticate_credentials(self, token):
        User = get_user_model()

        if isinstance(token, bytes):
            token = token.decode('ascii')
        try:
            data = jwt.decode(token, settings.SECRET_KEY, algorithms="HS256")
            user_id = data['user_id']
            expired_at = data['expired_at']
            user = User.objects.get(id=user_id)
        
        except jwt.DecodeError:
            print(1)
            raise exceptions.AuthenticationFailed("DecodeError: Invalid Token")
        except jwt.InvalidAlgorithmError:
            print(2)
            raise exceptions.AuthenticationFailed("InvalidAlgorithmError: Invalid Token")
        except AttributeError as e:
            print(e)
            raise exceptions.AuthenticationFailed("AttributeError: Invalid Token")
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed("No Such User")
        
        if expired_at:
            expired_at = datetime.strptime(expired_at, "%Y-%m-%d %H:%M:%S")
            if datetime.now() >= expired_at:
                raise exceptions.AuthenticationFailed("Expired Token")
        return user, None
    
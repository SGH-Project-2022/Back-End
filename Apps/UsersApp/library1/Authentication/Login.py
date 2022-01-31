from Apps.UsersApp.models import User
import datetime
import jwt


class Login:

    def check_email(self, email: str) -> bool:
        user = User.get_user_by_email(email)
        if user is None:
            return False
        return True

    def login_with_email(self, email: str, password: str) -> bool:

        if not self.check_email(email):
            return False

        user = User.get_user_by_email(email)

        if not user.check_password(password):
            return False

        return True

    def generate_JWT_token(user: User) -> str:
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        return token

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import UserSerializer
from .models import User

from Library import jwt_token
from Library.api_response import ApiResponse

# Create your views here.
api_response = ApiResponse()
# https://www.youtube.com/watch?v=Wq6JqXqOzCE


class RegisterView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        api_response.__init__()

        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return api_response.set_status_code(400).set_data("errors", serializer.errors).reponse()

        user = serializer.save()

        token = jwt_token.generate_JWT_token(user)

        return api_response.set_status_code(code=200).set_data(
            "user", serializer.data).set_token(token).reponse()


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):

        api_response.__init__()

        email = request.data['email']
        password = request.data['password']

        user = User.get_user_by_email(email=email)

        if user is None:
            return api_response.set_status_code(401).set_data("message", "User not found !").reponse()

        if not user.check_password(password):
            return api_response.set_status_code(401).set_data("message", "Incorrect password !").reponse()

        token = jwt_token.generate_JWT_token(user)

        response = api_response.set_status_code(code=200).set_data(
            "user", UserSerializer(user).data).set_token(token).reponse()

        response.set_cookie(key='user-token', value=token, httponly=True)

        return response


# class UserView(APIView):
#     def get(self, request):
#         token = request.COOKIES.get('jwt')

#         if not token:
#             raise AuthenticationFailed('Unauthenticated!')

#         try:
#             payload = jwt.decode(token, 'secret', algorithm=['HS256'])
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed('Unauthenticated!')

#         user = User.objects.filter(id=payload['id']).first()
#         serializer = UserSerializer(user)
#         return Response(serializer.data)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    # def _check_loggedin(request):
    #     token = request.COOKIES.get('user-token')

    #     if not token:
    #         raise AuthenticationFailed('Unauthenticated!')

    #     try:
    #         payload = jwt.decode(token, 'secret', algorithm=['HS256'])
    #     except jwt.ExpiredSignatureError:
    #         raise AuthenticationFailed('Unauthenticated!')

    def post(self, request):

        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return

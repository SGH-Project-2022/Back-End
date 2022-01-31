import jwt


def login_check(request, cookie_name):
    token = request.COOKIES.get(cookie_name)

    if not token:
        return False

    try:
        payload = jwt.decode(token, 'secret', algorithm=['HS256'])
    except jwt.ExpiredSignatureError:
        return False

    return True

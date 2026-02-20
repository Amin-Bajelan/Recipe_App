from serializers.serializer import GetUserSerializer
from recipe_app.serializer_error import SerializersError


def get_user_by_id(data,id):
    ok = False
    data = None
    errores = {}
    
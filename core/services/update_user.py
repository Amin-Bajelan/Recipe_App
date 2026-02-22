# services.py

from core.models import User
from recipe_app.serializer_error import SerializersError
from core.serializers import UserSerializer  

def update_user_services(user_id, data):
    updated = False
    errors = {}

    try:
        user = User.objects.get(id=user_id)
        serializer = UserSerializer(user, data=data, partial=True)  
        if serializer.is_valid():
            serializer.save()  
            updated = True
        else:
            errors = serializer.errors
    except User.DoesNotExist:
        errors["error"] = "User not found"
    
    return updated, serializer.data, errors



# from rest_framework import status
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from src.apps.user.services import update_user_services  # سرویس ویرایش کاربر
# from src.utils.exceptions import BadRequestException  # برای ارورهای سفارشی

# class UpdateUserAPIView(APIView):
#     permission_classes = [IsAuthenticated]

#     def put(self, request, *args, **kwargs):
#         user_id = request.user.id  # کاربری که وارد شده است
#         data = request.data  # داده‌های جدید که از کاربر آمده‌اند
        
#         updated, user_data, errors = update_user_services(user_id=user_id, data=data)
        
#         if errors:
#             raise BadRequestException(
#                 message="Invalid data",
#                 error_type=errors,
#             )
        
#         return Response(
#             data={
#                 "updated": updated,
#                 "data": user_data,
#                 "status": status.HTTP_200_OK,
#             },
#             status=status.HTTP_200_OK,
#         )
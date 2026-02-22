# services.py

from core.serializers import CreateUserSerializer
from recipe_app.serializer_error import SerializersError


def create_user_services(data):
    created = False
    data = None
    errors = {}

    errors_dict = SerializersError.UserError.errores  

    serializer = CreateUserSerializer(data=data)  
    if serializer.is_valid():
        instance = serializer.save()
        data = serializer.data
        created = True
    else:
   
        error_types = []
        errors = serializer.errors
        for error in errors.keys():
            error_type = errors_dict.get(error)
            error_types.append(error_type)
        errors["errors"] = errors
        errors["error_type"] = error_types

    return created, data, errors



# from rest_framework import status
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.views import APIView

# from src.apps.user.services import create_user_services  # سرویس ایجاد کاربر
# from src.utils.exceptions import BadRequestException  # برای ارورهای اختصاصی

# class CreateUserAPIView(APIView):
#     permission_classes = [IsAuthenticated]  # فقط کاربران احراز هویت شده می‌توانند ثبت‌نام کنند

#     def post(self, *args, **kwargs):
#         # گرفتن داده‌ها از درخواست
#         data = self.request.data
        
#         # فراخوانی سرویس برای ایجاد کاربر
#         created, user, errs = create_user_services(data=data)
        
#         # اگر خطا وجود داشت، استثنای BadRequestException پرتاب می‌شود
#         if errs:
#             raise BadRequestException(
#                 message=errs.get("errors"),
#                 error_type=errs.get("error_type"),
#             )
        
#         # در صورت موفقیت، داده‌های کاربر جدید به همراه وضعیت ارسال می‌شود
#         return Response(
#             data={
#                 "created": created,
#                 "data": user,  # داده‌های کاربر جدید
#                 "status": status.HTTP_201_CREATED,
#             },
#             status=status.HTTP_201_CREATED,
#         )
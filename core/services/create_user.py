from core.serializers import CraeteUSerSerializer
from recipe_app.serializer_error import SerializersError


def create_user_services(data):
    created = False
    data = None
    errors = {}
    
    errors_dict = SerializersError.UserError.errores
    
    serializer = CraeteUSerSerializer()
    if serializer.is_valid():
        instance = serializer.save()
        data = create_user_services(instance=instance, many = False)
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
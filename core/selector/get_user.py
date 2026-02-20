import uuid
from typing import Optional, Union
from models import User


def get_user_id(id: Union[str,uuid.UUID])-> Optional[User]:
    try: 
        return User.objects.get()
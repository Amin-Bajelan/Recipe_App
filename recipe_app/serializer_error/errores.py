from django.utils.translation import gettext_lazy as _


class SerializersError():
    class UserError():
        errores = {
            "id": _("INVALID ID FOR USER"),
            "email": _("THIS DATA FOR EMAIL IS INVALID"),
            "name": _("THIS NAME IS INVALID"),
        } 
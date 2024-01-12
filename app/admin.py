from django.contrib import admin
from .models import CustomUser
from app.models import AllProducts, RelaxedFit, RegularFit
admin.site.register(CustomUser)
admin.site.register(AllProducts)
admin.site.register(RelaxedFit)
admin.site.register(RegularFit)
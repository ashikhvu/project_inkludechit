from django.contrib import admin
from .models import User,UserProfileModel,NomineeModel,ProductModel,PaymentModel

# Register your models here.
admin.site.register(User)
admin.site.register(UserProfileModel)
admin.site.register(NomineeModel)
admin.site.register(ProductModel)
admin.site.register(PaymentModel)
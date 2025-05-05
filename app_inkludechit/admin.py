from django.contrib import admin
from .models import User,UserProfileModel,NomineeModel,ProductModel,PaymentModel

# Register your models here.

class userprof(admin.ModelAdmin):
    list_display=["first_name","email","mobile","current_address"]

admin.site.register(User)
admin.site.register(UserProfileModel,userprof)
admin.site.register(NomineeModel)
admin.site.register(ProductModel)
admin.site.register(PaymentModel)
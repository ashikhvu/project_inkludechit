from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.IndexView.as_view(),name='indexview'),
    path('mymodelview',views.MymodelView.as_view(),name='mymodelview'),
    path('mymodelsingleview/<int:pk>',views.MymodelSingleView.as_view(),name='mymodelsingleview'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bert_classifier/', include('bert_classifier.urls')),
]

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bert_classifier/', include('bert_classifier.urls')),
    path('dialog_bot/', include('dialog_bot.urls')),
    path('', include('bert_classifier.urls')),
]
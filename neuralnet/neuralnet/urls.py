from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bert_classifier/', include('bert_classifier.urls')),
    path('dialog_bot/', include('dialog_bot.urls')),
    path('image_classification/', include('image_classification.urls')),
    path('', include('bert_classifier.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
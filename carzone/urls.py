from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # This line routes requests starting with 'admin/' to the Django admin site.
    # When a user accesses 'http://yourdomain.com/admin/', they will be directed to the Django admin interface.
    path('admin/', admin.site.urls),
    
    # This line includes the URLs defined in the 'pages' app's 'urls.py' file when the path is empty.
    # This means that if a user accesses the root URL 'http://yourdomain.com/', Django will further route the request
    # based on the URLs defined in the 'pages' app.
    path('', include('pages.urls')),
] 

# This part is used to serve media files during development.
# It appends a URL pattern for serving media files uploaded by users.
# 'settings.MEDIA_URL' specifies the URL path to serve the media files from,
# and 'settings.MEDIA_ROOT' specifies the directory on the filesystem where the uploaded media files are stored.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

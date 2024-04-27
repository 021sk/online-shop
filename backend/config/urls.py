from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # / => base
    path("", include("apps.accounts.urls")),
    path("", include("apps.home.urls")),
    # /profile/
    # /notification
    # /(search)/product/<key>
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += (
        [path("admin/", admin.site.urls)]
        + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )

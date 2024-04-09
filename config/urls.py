from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('apps.user.urls')),
    path('user/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('palette/', include('apps.palette.urls')),
    path('color/', include('apps.color.urls')),
    path('docs/swagger', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
    path('docs/schema', SpectacularAPIView.as_view(), name='schema'),
]

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]

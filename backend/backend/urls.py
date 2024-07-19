from django.contrib import admin
from django.urls import path
from django.urls import path, include
from api.views import CreateUserView, UploadCSVView, GenerateChartView, UserEntriesView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/user/register/", CreateUserView.as_view(), name="register"),    
    path("api/token/", TokenObtainPairView.as_view(), name ="get_token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("api-auth/", include("rest_framework.urls")),
    path('api/upload/', UploadCSVView.as_view(), name='upload_csv'),
    path('api/generate_chart/', GenerateChartView.as_view(), name='generate_chart'),
    path('api/user_entries/', UserEntriesView.as_view(), name='user_entries'),

]   
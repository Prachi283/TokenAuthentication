from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter
# from api.auth import CustomAuthToken


# Createing Router Object
router= DefaultRouter()

# Register EmployeeViewSet with Router
router.register('employeeapi',views.EmployeeModelViewSet,basename='employee')
# router.register('readonlyapi',views.EmployeeReadOnlyModelViewSet,basename='employeeapi')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('employee/',include('rest_framework.urls',namespace='rest_framework')),
    path('gettoken/',CustomAuthToken.as_view())
    ]

from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly


# Model View Set 
class EmployeeModelViewSet(viewsets.ModelViewSet):
	queryset=Employee.objects.all()
	serializer_class=EmployeeSerializer
	authentication_classes=[TokenAuthentication]
	permission_classes=[IsAuthenticated]
	permission_classes=[IsAuthenticatedOrReadOnly]



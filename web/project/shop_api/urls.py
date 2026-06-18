from .views import *
from rest_framework import routers

urlpatterns = []

router = routers.SimpleRouter()
router.register('category', CategoryViewSet, basename='category')
router.register('collection', CollectionViewSet, basename='collection')
router.register('aquarium', AquariumViewSet, basename='aquarium')
router.register('product', ProductViewSet, basename='product')
router.register('inhabitant', InhabitantViewSet, basename='inhabitant')
router.register('schedule-event', ScheduleEventViewSet, basename='schedule-event')
router.register('employee', EmployeeViewSet, basename='employee')
router.register('ticket', TicketViewSet, basename='ticket')

urlpatterns += router.urls
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

# router.register(r'djangoadminlog', DjangoAdminLogViewSet)
# router.register(r'djangocontenttype', DjangoContentTypeViewSet)
# router.register(r'djangomigrations', DjangoMigrationsViewSet)
# router.register(r'djangosession', DjangoSessionViewSet)

router.register(r'addressbook', AddressBookViewSet)
router.register(r'categories', CategoriesViewSet)
router.register(r'farmbatches', FarmBatchesViewSet)
router.register(r'farms', FarmsViewSet)
router.register(r'favorites', FavoritesViewSet)
router.register(r'messages', MessagesViewSet)
router.register(r'orderitems', OrderItemsViewSet)
router.register(r'orders', OrdersViewSet)
router.register(r'productavailability', ProductAvailabilityViewSet)
router.register(r'productcategory', ProductCategoryViewSet)
router.register(r'productstatistic', ProductStatisticViewSet)
router.register(r'products', ProductsViewSet)
router.register(r'reports', ReportsViewSet)
router.register(r'reviews', ReviewsViewSet)
router.register(r'statusorder', StatusOrderViewSet)
router.register(r'typefarm', TypeFarmViewSet)
router.register(r'userroles', UserRolesViewSet)
router.register(r'users', UsersViewSet)
router.register(r'weathertips', WeatherTipsViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

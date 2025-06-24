from rest_framework import viewsets
from .models import *
from .serializers import *


# class DjangoAdminLogViewSet(viewsets.ModelViewSet):
#     queryset = DjangoAdminLog.objects.all()
#     serializer_class = DjangoAdminLogSerializer


# class DjangoContentTypeViewSet(viewsets.ModelViewSet):
#     queryset = DjangoContentType.objects.all()
#     serializer_class = DjangoContentTypeSerializer


# class DjangoMigrationsViewSet(viewsets.ModelViewSet):
#     queryset = DjangoMigrations.objects.all()
#     serializer_class = DjangoMigrationsSerializer


# class DjangoSessionViewSet(viewsets.ModelViewSet):
#     queryset = DjangoSession.objects.all()
#     serializer_class = DjangoSessionSerializer



class AddressBookViewSet(viewsets.ModelViewSet):
    queryset = AddressBook.objects.all()
    serializer_class = AddressBookSerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer



class FarmBatchesViewSet(viewsets.ModelViewSet):
    queryset = FarmBatches.objects.all()
    serializer_class = FarmBatchesSerializer


class FarmsViewSet(viewsets.ModelViewSet):
    queryset = Farms.objects.all()
    serializer_class = FarmsSerializer


class FavoritesViewSet(viewsets.ModelViewSet):
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer


class MessagesViewSet(viewsets.ModelViewSet):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer


class OrderItemsViewSet(viewsets.ModelViewSet):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer


class ProductAvailabilityViewSet(viewsets.ModelViewSet):
    queryset = ProductAvailability.objects.all()
    serializer_class = ProductAvailabilitySerializer


class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductStatisticViewSet(viewsets.ModelViewSet):
    queryset = ProductStatistic.objects.all()
    serializer_class = ProductStatisticSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class ReportsViewSet(viewsets.ModelViewSet):
    queryset = Reports.objects.all()
    serializer_class = ReportsSerializer


class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer


class StatusOrderViewSet(viewsets.ModelViewSet):
    queryset = StatusOrder.objects.all()
    serializer_class = StatusOrderSerializer


class TypeFarmViewSet(viewsets.ModelViewSet):
    queryset = TypeFarm.objects.all()
    serializer_class = TypeFarmSerializer


class UserRolesViewSet(viewsets.ModelViewSet):
    queryset = UserRoles.objects.all()
    serializer_class = UserRolesSerializer


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class WeatherTipsViewSet(viewsets.ModelViewSet):
    queryset = WeatherTips.objects.all()
    serializer_class = WeatherTipsSerializer

from rest_framework import serializers

from .models import *


# class DjangoAdminLogSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DjangoAdminLog
#         fields = '__all__'


# class DjangoContentTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DjangoContentType
#         fields = '__all__'


# class DjangoMigrationsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DjangoMigrations
#         fields = '__all__'


# class DjangoSessionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DjangoSession
#         fields = '__all__'

class AddressBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressBook
        fields = '__all__'


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


class FarmBatchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmBatches
        fields = '__all__'


class FarmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farms
        fields = '__all__'


class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = '__all__'


class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = '__all__'


class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = '__all__'


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'


class ProductAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAvailability
        fields = '__all__'


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class ProductStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductStatistic
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class ReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = '__all__'


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'


class StatusOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusOrder
        fields = '__all__'


class TypeFarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeFarm
        fields = '__all__'


class UserRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRoles
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class WeatherTipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherTips
        fields = '__all__'
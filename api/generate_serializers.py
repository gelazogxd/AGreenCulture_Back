from django.apps import apps
from rest_framework import serializers

for model in apps.get_models():
    print(f"class {model.__name__}Serializer(serializers.ModelSerializer):")
    print("    class Meta:")
    print(f"        model = {model.__name__}")
    print("        fields = '__all__'\n")

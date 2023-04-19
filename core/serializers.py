from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Sales, Type, Size, Category


class UserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "password", "email", "first_name", "last_name"]

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data.get("email", ""),
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        password = validated_data.get("password")
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class TypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"

class SizeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = "__all__"

class SalesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = "__all__"


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

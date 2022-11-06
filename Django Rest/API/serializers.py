from rest_framework import serializers
from .models import Character, Category

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["title"]

class Serializers(serializers.ModelSerializer):

    category = CategorySerializers()

    class Meta:
        model = Character
        exclude = ["date_create", "date_update"]
        depth = 1





class SerializersNotModel(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    age = serializers.IntegerField()
    content = serializers.CharField()
  

    def create(self, validated_data):
        return Character.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.age = validated_data.get("age", instance.age)
        instance.content = validated_data.get("content", instance.content)
        instance.save()
        return instance





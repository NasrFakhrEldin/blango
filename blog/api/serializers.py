from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        readonly = ["modified_at", "created_at"]
    
#     def validate(self, data):
#         if not data.get("slug"):
#             if data["autogenerate_slug"]:
#                 data["slug"] = slugify(data["title"])
#             else:
#                 raise serializers.ValidationError("slug is required if autogenerate_slug is not set")
#         del data["autogenerate_slug"]
#         return data

        

# class UserSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     email = serializers.EmailField(required=False)
#     first_name = serializers.CharField(
#     max_length=20,
#     required=False,
#     validators=[is_capitalized]
#     )
#     last_name = serializers.CharField(
#     max_length=20,
#     required=False,
#     validators=[is_capitalized]
#     )
#     password = serializers.CharField(write_only=True,
#     required=False)
#     join_date = serializers.DateTimeField(read_only=True)
    
#     def create(self, validated_data):
#         return User(**validated_data)
    
#     def update(self, instance, validated_data):
#         for key, value in validated_data.items():
#             setattr(instance, key, value)
#         return instance
    
#     def validate_email(self, value):
#         value = value.lower()
#         domain = value.split("@")[1] # safe to do since we know value is valid email address
#         if domain != "example.com":
#             raise serializers.ValidationError("domain must be example.com")
#         return value
        
#         def validate(self, data):
#             if (not data.get("first_name")) != (not data.get("last_name")):
#                 raise serializers.ValidationError("first_name and last_name must be provided together")
#             return data

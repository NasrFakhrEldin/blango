from rest_framework import serializers
from blog.models import Post, Tag, Comment
from blango_auth.models import User



# def is_capitalized(value):
#     if value[0].lower() == value[0]:
#         raise serializers.ValidationError("Value must be capitalized") 

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
        
#     def validate(self, data):
#         if (not data.get("first_name")) != (not data.get("last_name")):
#             raise serializers.ValidationError("first_name and last_name must be provided together")
#         return data

class TagField(serializers.SlugRelatedField):
    def to_internal_value(self, data):
        try:
            return self.get_queryset().get_or_create(value=data.lower())[0]
        except (TypeError, ValueError):
            self.fail(f"Tag value {data} is invalid")




class PostSerializer(serializers.ModelSerializer):
    tags = TagField(
        slug_field="value", many=True, queryset=Tag.objects.all()
    )

    author = serializers.HyperlinkedRelatedField(
        queryset=User.objects.all(), view_name="api_user_detail", lookup_field="email"
    )

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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    creator = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "creator", "content", "modified_at", "created_at"]
        readonly = ["modified_at", "created_at"]


class PostDetailSerializer(PostSerializer):
    comments = CommentSerializer(many=True)

    def update(self, instance, validated_data):
        comments = validated_data.pop("comments")

        instance = super(PostDetailSerializer, self).update(instance, validated_data)

        for comment_data in comments:
            if comment_data.get("id"):
                # comment has an ID so was pre-existing
                continue
            comment = Comment(**comment_data)
            comment.creator = self.context["request"].user
            comment.content_object = instance
            comment.save()

        return instance






'''
    if we wanted to allow access to Posts for a particular author,
    we might have a URL path
    like /api/v1/<author_email>/posts/<post_id>. In this case,
    we’d need to provide both the author’s email and a Post ID
    to generate the URL.
'''
# https://www.django-rest-framework.org/api-guide/relations/#custom-hyperlinked-fields

# from rest_framework.reverse import reverse

# class CustomerHyperlink(serializers.HyperlinkedRelatedField):
#     # We define these as class attributes, so we don't need to pass them as arguments.
#     view_name = 'post-detail'
#     queryset = Post.objects.all()

#     def get_url(self, obj, view_name, request, format):
#         url_kwargs = {
#             'author_email': obj.User.email,
#             'post_pk': obj.pk
#         }
#         return reverse(view_name, kwargs=url_kwargs, request=request, format=format)

#     def get_object(self, view_name, view_args, view_kwargs):
#         lookup_kwargs = {
#            'author__email': view_kwargs['author_email'],
#            'pk': view_kwargs['post_pk']
#         }
#         return self.get_queryset().get(**lookup_kwargs)
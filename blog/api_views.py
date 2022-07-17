# import json

# from http import HTTPStatus
# from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed
# from django.shortcuts import get_object_or_404
# from django.urls import reverse
# from django.views.decorators.csrf import csrf_exempt

# from blog.models import Post
# from blog.api.serializers import PostSerializer

# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# # def post_to_dict(post):
# #     return {
# #         "pk": post.pk,
# #         "author_id": post.author_id,
# #         "created_at": post.created_at,
# #         "modified_at": post.modified_at,
# #         "published_at": post.published_at,
# #         "title": post.title,
# #         "slug": post.slug,
# #         "summary": post.summary,
# #         "content": post.content,
# #     }


# # @csrf_exempt
# @api_view(["GET", "POST"])
# def post_list(request, format=None):
#     if request.method == "GET":

#         posts = Post.objects.all()
#         # posts_as_dict = [post_to_dict(p) for p in posts]

#         # return JsonResponse({"data": posts_as_dict})
#         # return JsonResponse({"data": PostSerializer(posts, many=True).data})
#         return Response({"data": PostSerializer(posts, many=True).data})
    
#     elif request.method == "POST":

#         # post_data = json.loads(request.body)
#         # post = Post.objects.create(**post_data)
#         # serializer = PostSerializer(data=post_data)

#         # serializer = PostSerializer(data=request.data)
#         # serializer.is_valid(raise_exception=True)
#         # post = serializer.save()

#         # return HttpResponse(
#         #     status=HTTPStatus.CREATED,
#         #     headers={"Location": reverse("api_post_detail", args=(post.pk,))},
#         # )
#     # return HttpResponseNotAllowed(["GET", "POST"])

#       serializer = PostSerializer(data=request.data)
#       if serializer.is_valid():
#         post = serializer.save()
#         return Response(
#           status = HTTPStatus.CREATED,
#           headers = {"Location": reverse("api_post_detail", args=(post.pk,))}
#         )
#       return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)

# # @csrf_exempt
# @api_view(["GET", "PUT", "DELETE"])
# def post_detail(request, pk, format=None):

#     try:
#       post = Post.objects.get(pk=pk)
#     except Post.DoesNotExist:
#       return Response(status = HTTPStatus.NOT_FOUND)
#     # post = get_object_or_404(Post, pk=pk)

#     if request.method == "GET":
#         # return JsonResponse(post_to_dict(post))
#         # return JsonResponse(PostSerializer(post).data)
#         return Response(PostSerializer(post).data)

#     elif request.method == "PUT":

#         # post_data = json.loads(request.body)
#         # for field, value in post_data.items():
#         #     setattr(post, field, value)
#         # post.save()
#         # serializer = PostSerializer(post, data=post_data)
#         # serializer = PostSerializer(post, data=request.data)
#         # serializer.is_valid(raise_exception=True)
#         # serializer.save()
#         # return HttpResponse(status=HTTPStatus.NO_CONTENT)

#         serializer = PostSerializer(post, data = request.data)
#         if serializer.is_valid():
#           serializer.save()
#           return Response(status = HTTPStatus.NO_CONTENT)
#         return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)
    
#     elif request.method == "DELETE":
#         post.delete()
#         # return HttpResponse(status=HTTPStatus.NO_CONTENT)
#         return Response(status=HTTPStatus.NO_CONTENT)

#     # return HttpResponseNotAllowed(["GET", "PUT", "DELETE"])


# # from rest_framework import mixins
# # from rest_framework import generics


# # class PostList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
# #     queryset = Post.objects.all()
# #     serializer_class = PostSerializer

# #     def get(self, request, *args, **kwargs):
# #         return self.list(request, *args, **kwargs)

# #     def post(self, request, *args, **kwargs):
# #         return self.create(request, *args, **kwargs)



# # class PostDetail(APIView):
# #     @staticmethod
# #     def get_post(pk):
# #         return get_object_or_404(Post, pk=pk)

# #     def get(self, request, pk, format=None):
# #         post = self.get_post(pk)
# #         return Response(PostSerializer(post).data)

# #     def put(self, request, pk, format=None):
# #         post = self.get_post(pk)
# #         serializer = PostSerializer(post, data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(status=HTTPStatus.NO_CONTENT)
# #         return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)

# #     def delete(self, request, pk, format=None):
# #         post = self.get_post(pk)
# #         post.delete()
# #         return Response(status=HTTPStatus.NO_CONTENT)


# # class PostDetail(
# #     mixins.RetrieveModelMixin,
# #     mixins.UpdateModelMixin,
# #     mixins.DestroyModelMixin,
# #     generics.GenericAPIView,
# #   ):
# #     queryset = Post.objects.all()
# #     serializer_class = PostSerializer

# #     def get(self, request, *args, **kwargs):
# #         return self.retrieve(request, *args, **kwargs)

# #     def put(self, request, *args, **kwargs):
# #         return self.update(request, *args, **kwargs)

# #     def delete(self, request, *args, **kwargs):
# #         return self.destroy(request, *args, **kwargs)

'''
  YOU CAN END UP WITH THIS
  ^_0
'''

# class PostList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
'''
  MOVED TO api/views.py
'''

# Refernces
# https://www.django-rest-framework.org/api-guide/generic-views/
# https://github.com/encode/django-rest-framework/blob/master/rest_framework/mixins.py
# https://github.com/encode/django-rest-framework/blob/master/rest_framework/generics.py

"""
______ _____ _____ _____    __
| ___ \  ___/  ___|_   _|  / _|                                           | |
| |_/ / |__ \ `--.  | |   | |_ _ __ __ _ _ __ ___   _____      _____  _ __| |__
|    /|  __| `--. \ | |   |  _| '__/ _` | '_ ` _ \ / _ \ \ /\ / / _ \| '__| |/ /
| |\ \| |___/\__/ / | |   | | | | | (_| | | | | | |  __/\ V  V / (_) | |  |   <
\_| \_\____/\____/  \_/   |_| |_|  \__,_|_| |_| |_|\___| \_/\_/ \___/|_|  |_|\_|

"""
# ^_^
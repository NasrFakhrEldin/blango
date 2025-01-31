from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

class AnonSustainedThrottle(AnonRateThrottle):
    scope = "anon_sustained"


class AnonBurstThrottle(AnonRateThrottle):
    scope = "anon_burst"


class UserSustainedThrottle(UserRateThrottle):
    scope = "user_sustained"


class UserBurstThrottle(UserRateThrottle):
    scope = "user_burst"


# import random

# class RandomRateThrottle(throttling.BaseThrottle):
#     def allow_request(self, request, view):
#         return random.randint(1, 10) != 1


'''
https://github.com/encode/django-rest-framework/blob/master/rest_framework/throttling.py
https://www.django-rest-framework.org/api-guide/throttling/#custom-throttles
'''
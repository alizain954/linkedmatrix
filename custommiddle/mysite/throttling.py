from rest_framework.throttling import UserRateThrottle

class Goldthrottlin(UserRateThrottle):
    scope = "gold"

class Silverthrottlin(UserRateThrottle):
    scope = "silver"

class Bronzethrottlin(UserRateThrottle):
    scope = "bronze"
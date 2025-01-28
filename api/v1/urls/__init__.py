from .landing import urlpatterns as landing
from .market import urlpatterns as market
from .product import urlpatterns as product
from .user import urlpatterns as user

urlpatterns = landing + market + product + user

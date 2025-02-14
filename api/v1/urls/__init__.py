from .landing import urlpatterns as landing
from .market import urlpatterns as market
from .product import urlpatterns as product
from .user import urlpatterns as user
from .payment import urlpatterns as payment

urlpatterns = landing + market + product + user + payment

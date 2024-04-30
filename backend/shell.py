import os
from django.contrib.auth import get_user_model
import django

# from utils import catche, mail
from django.core.cache import cache

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()
#
User = get_user_model()
#
# user = User.objects.create(username="ali", email="shahaab.kabiri@gmail.com", password="177038sk", phone="09121710325")
# # user.set_password("177038sk"
user = User.objects.get(username="ali")

token_in_cache = cache.get(f"activate_token_user_{user.username}")
print(token_in_cache)

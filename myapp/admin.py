from django.contrib import admin

# Register your models here.
from .models.user import User
from .models.address import Address
from .models.company import Company
from .models.post import Post
from .models.comment import Comment
from .models.album import Album
from .models.photo import Photo
from .models.todo import Todo

# Modelleri admin paneline ekliyoruz
admin.site.register(User)
admin.site.register(Address)
admin.site.register(Company)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Album)
admin.site.register(Photo)
admin.site.register(Todo)
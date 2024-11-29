from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from .models.user import User
from .models.address import Address
from .models.company import Company
from .models.post import Post
from .models.comment import Comment
from .models.album import Album
from .models.photo import Photo
from .models.todo import Todo
from rest_framework import serializers

# Modellerin Serializer'ları
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'catch_phrase', 'bs']

        
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'street', 'suite', 'city', 'zipcode', 'geo_lat', 'geo_lng']
class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    company = CompanySerializer()

    class Meta:
        model = User
        fields = ['id', 'name', 'username', 'email', 'phone', 'website', 'address', 'company']

    def create(self, validated_data):
        # Address ve company verisini ayırıyoruz
        address_data = validated_data.pop('address')
        company_data = validated_data.pop('company')

        # Kullanıcıyı oluşturuyoruz
        user = User.objects.create(**validated_data)

        # Address ve Company nesnelerini kullanıcıyla ilişkilendirerek oluşturuyoruz
        address = Address.objects.create(user=user, **address_data)
        company = Company.objects.create(user=user, **company_data)
        
        user.address = address
        user.company = company
        user.save()

        return user

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


# from .serializers import UserSerializer, AddressSerializer, CompanySerializer, PostSerializer, CommentSerializer, AlbumSerializer, PhotoSerializer, TodoSerializer


# User ViewSet
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()  
        self.perform_destroy(instance)  
        return Response({"message": "Kullanıcı başarıyla silindi!"}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def posts(self, request, pk=None):
        """
        Kullanıcının tüm paylaşımlarını döndüren özel bir action
        """
        user = self.get_object()  # Kullanıcıyı al
        posts = Post.objects.filter(user=user)  # Kullanıcının paylaşımlarını al
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

# Address ViewSet
class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    @action(detail=True, methods=['get'])
    def user_address(self, request, pk=None):
        """
        Kullanıcının adresini döndüren özel bir action
        """
        address = self.get_object()  # Adresi al
        serializer = AddressSerializer(address)
        return Response(serializer.data)

# Company ViewSet
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(detail=True, methods=['get'])
    def user_company(self, request, pk=None):
        """
        Kullanıcının şirket bilgilerini döndüren özel bir action
        """
        company = self.get_object()  # Şirketi al
        serializer = CompanySerializer(company)
        return Response(serializer.data)

# Post ViewSet
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()  
        self.perform_destroy(instance)  
        return Response({"message": "Post başarıyla silindi!"}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'], url_path='comments', url_name='post_comments')
    def get_comments(self, request, pk=None):
        try:
            post = Post.objects.get(pk=pk)  # İlgili gönderiyi alıyoruz
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=404)

        comments = Comment.objects.filter(post=post)  # Gönderiye ait yorumları filtreliyoruz
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

# Comment ViewSet
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()  
        self.perform_destroy(instance)  
        return Response({"message": "Yorum başarıyla silindi!"}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        """
        Yorum onaylama action'ı
        """
        comment = self.get_object()  # Yorumu al
        comment.is_approved = True  # Yorumun onay durumunu değiştir
        comment.save()
        return Response({"message": "Yorum başarıyla onaylandı!"}, status=status.HTTP_200_OK)

# Album ViewSet
class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()  
        self.perform_destroy(instance)  
        return Response({"message": "Album başarıyla silindi!"}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def user_albums(self, request, pk=None):
        user_albums = Album.objects.filter(user_id=pk)
        serializer = self.get_serializer(user_albums, many=True)
        return Response(serializer.data)

# Photo ViewSet
class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()  
        self.perform_destroy(instance)  
        return Response({"message": "Resim başarıyla silindi!"}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def album_photos(self, request, pk=None):
        album_photos = Photo.objects.filter(album_id=pk)
        serializer = self.get_serializer(album_photos, many=True)
        return Response(serializer.data)


# Todo ViewSet
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()  
        self.perform_destroy(instance)  
        return Response({"message": "Todo başarıyla silindi!"}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def completed_todos(self, request):
        completed = Todo.objects.filter(completed=True)
        serializer = self.get_serializer(completed, many=True)
        return Response(serializer.data)

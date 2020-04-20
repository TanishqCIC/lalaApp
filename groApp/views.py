from django.http import HttpResponse
from .models import Articles, ShopDetails, Users
from .serializers import ArticlesSerializer, ShopsSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class ArticleList(APIView):
    def get(self, request):
        articles = Articles.objects.all()
        serializer = ArticlesSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        print('req', request)
        print('req', request.data.get('name'))
        shop = ShopDetails.objects.first()
        new_entry = Articles(name=request.data.get('name'), shop_id=shop)
        new_entry.save()
        return HttpResponse('request')

class ShopList(APIView):
    def get(self, request):
        shops = ShopDetails.objects.all()
        serializer = ShopsSerializer(shops, many=True)
        return Response(serializer.data)

    def post(self, request):
        print('req', request)
        print('req', request.data.get('name'))
        print('req', request.data.get('address'))
        new_entry = ShopDetails(name=request.data.get('name'), address=request.data.get('address'))
        new_entry.save()
        return HttpResponse('request')

class User(APIView):
    def get(self, request):
        request = request.data
        username = request.get('username')
        password = request.get('password')
        users = Users.objects.filter(username=username, password=password).first()
        user = UserSerializer(users)
        if(users):
            return Response(user.data)
        else:
            return HttpResponse('User not found')

    def post(self, request):
        request = request.data
        username = request.get('username')
        password = request.get('password')
        name = request.get('name')
        address = request.get('address')
        contact = request.get('contact')
        new_user = Users(
            name=name,
            address=address,
            contact=contact,
            username=username,
            password=password
        )
        new_user.save()
        return HttpResponse('request successful')

def index(request):
    query = Articles.objects.all()
    return HttpResponse(query)


def add(request):
    return HttpResponse("Add")

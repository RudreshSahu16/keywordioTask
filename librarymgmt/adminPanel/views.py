from ast import Return
from django import http
from django.shortcuts import render,redirect
import requests
from django.http.response import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .serializers import AddBooksSerializer
from .models import AddBooks
# Create your views here.
class Home(APIView):
    def get(self,request):
        try:
            bookdata=AddBooks.objects.all()
            param={'books':bookdata}
            return render(request,'homescreen.html',param)
        except Exception as e:
            return HttpResponse(e,status=400)

class ShowBook(APIView):
    def get(self,request,bId):
        try:
            book=AddBooks.objects.filter(bookId=bId)
            param={'book':book}
            return render(request,'viewbook.html',param)
        except Exception as e:
            return HttpResponse(e,status=400)

    def put(self,request,bId):
        try:
            myDict = request.data
            bookdata = AddBooks.objects.get(bookId=bId)
            bookdata.bookName=myDict['bookName']
            bookdata.bookAuthor=myDict['bookAuthor']
            bookdata.bookZone=myDict['bookZone']
            bookdata.bookYear=myDict['bookYear']
            bookdata.save()
            messages.success(request,'successfully Updated')
            pass
        except Exception as e:
            return HttpResponse(e,status=400)
        
    def delete(self,request,bId):
        try:
            bookdata = AddBooks.objects.get(bookId=bId)
            bookdata.delete()
            messages.success(request,'successfully Deleted')
            pass
        except Exception as e:
            return HttpResponse(e,status=400)
    def post(self,request,bId):
        try:
            method=request.POST.get('_method')
            if(method =='update'):
                self.put(request,bId)
            
            if(method == 'delete'):
                self.delete(request,bId)
            return redirect('home')
        except Exception as e:
            return HttpResponse(e,status=400)


class AddBook(APIView):
    def get(self,request):
        try:
            return render(request,'addbook.html')
        except Exception as e:
            return HttpResponse(e,status=400)
    def post(self,request):
        try:
            serializerdata = AddBooksSerializer(data=request.data)
            if serializerdata.is_valid():
                serializerdata.save()
                myDict={}
                myDict = serializerdata.data
                bookId=myDict['bookId']
                bookName=myDict['bookName']
                bookAuthor=myDict['bookAuthor']
                bookZone=myDict['bookZone']
                bookYear=myDict['bookYear']
                bookDetails=AddBooks(bookId=bookId,bookName=bookName,bookAuthor=bookAuthor,bookZone=bookZone,bookYear=bookYear)
                bookDetails.save()
                return redirect('home')
        
        except Exception as e:
            return HttpResponse(e,status=400)
        
def basicwork(request):
    try:
        return render(request,'home.html')
    except Exception as e:
        return HttpResponse(e,status=400)

class Register(APIView):
    def get(self,request):
        try:
            return render(request,'register.html')
        except Exception as e:
            return HttpResponse(e,status=400)
    def post(self,request):
        try:
            if request.method=='POST':
                username=request.POST['userName']
                email=request.POST['email']
                firstname=request.POST['firstName']
                lastname=request.POST['lastName']
                password=request.POST['password']
                password1=request.POST['confirmPassword']

                if(password != password1):
                    messages.error(request,'Password is not Matched please Confirm The Password.')
                    # return HttpResponse({'Password is not Matched please Confirm The Password'},status=401)
                user=User.objects.create_user(username,email,password)
                user.first_name=firstname
                user.last_name=lastname
                user.save()
                messages.success(request,'Thanks for Register.Please login into your account')
                return render(request,'home.html')
        except Exception as e:
            return Response("account already exist or there may be some issue with your details")

class Login(APIView):
    def get(self,request):
        try:
            return render(request,'login.html')
        except Exception as e:
            return HttpResponse(e,status=400)
    def post(self,request):
        try:
            if request.method=='POST':
                email=request.POST.get('email')
                password=request.POST.get('password')
                username = User.objects.get(email=email.lower()).username
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request,user)
                    messages.success(request,"login successfully")
                else:
                    messages.error(request,"invalid Credentials")
                    return redirect('/')
               
                return redirect('home')
        except Exception as e:
             return Response("Check Your Credentials")

class Logout(APIView):
    def get(self,request):
        try:
            logout(request)
            messages.success(request,"logout successfully")
            return redirect('/')
        except Exception as e:
            return HttpResponse(e,status=400)

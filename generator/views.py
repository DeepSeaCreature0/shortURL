from urllib import response
from django.http import Http404, JsonResponse,HttpResponse
from django.shortcuts import redirect,render
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


from rest_framework.views import View ,APIView
from rest_framework.response import Response
from rest_framework import viewsets 
from rest_framework import status
from django.conf import settings
from yaml import serialize


from .models import link
from .serializer import LinkSerializers

from django.conf import settings

# default page/main page
def index(request):
    return render(request,'generator/index.html')

# Creating and Reading links
class linkshorter(viewsets.ReadOnlyModelViewSet):
    queryset=link.objects.all()
    serializer_class=LinkSerializers
    
    def getLastID(self):
        if link.objects.exists():
            id=link.objects.last().id
        else:
            id=0
        return id
    
    def generateHashValue(self,id):
        row_id=id
        # string of supported characters
        supported_characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

        hash_value=""

        while(row_id>0):
            ind=row_id % 62
            hash_value= supported_characters[ind] + hash_value
            row_id //=62
        
        return settings.HOST_URL+'/' + hash_value
    
    
    def isValidURL(self, url_string):
        validate_url = URLValidator()

        try:
            validate_url(url_string)
        except ValidationError as e:
            try:
                validate_url("https://"+url_string)
            except ValidationError as e:
                return False

        return True
    
    def create(self,request,*args,**kwargs):
        link_data = request.data

        id=self.getLastID()+1
        actual_url=request.POST.get('actual_url')

        # Check if the URL is valid or not
        if self.isValidURL(actual_url) == False:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        short_url=self.generateHashValue(id)

        new_link=link.objects.create(id=id,actual_url=actual_url,short_url=short_url)
        new_link.save()
        context={
            "short_url":short_url
        }
        return render(request,'generator/link.html',context)
        # serialize_data=LinkSerializers(new_link)

        # return JsonResponse(data=serialize_data.data)
    

# Redirecting the user to actual URL when the user uses short URL
class Redirector(View):

    def getIDfromHash(self,hash_value):
        
        id=0
        hash_value_length=len(hash_value)

        for i in range(hash_value_length):
            if(ord(hash_value[i]) >= ord('a') and ord(hash_value) <= ord('z')):
                ind= ord(hash_value[i]) - ord('a')
            elif(ord(hash_value[i]) >= ord('A') and ord(hash_value[i]) <= ord('Z')):
                ind= 26 + ord(hash_value[i]) - ord('A')
            else:
                ind= 52 + ord(hash_value[i]) - ord('0')

            id+=pow(62,hash_value_length-1-i)*ind

        return id
    
    def get(self,request,hash_value):
        id=self.getIDfromHash(hash_value)

        try:
            filtered_data = link.objects.get(pk=id)
        except:
            return render(request,'generator/404.html')
        

        redirect_link=filtered_data.actual_url

        if filtered_data.expired == True:
            return render(request,'generator/expire.html')

        filtered_data.hit_count=filtered_data.hit_count + 1

        if filtered_data.hit_count == 5:
            filtered_data.expired=True

        filtered_data.save()
            

        return redirect(redirect_link,)


    
    

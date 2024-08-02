from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def GetData(request):
    driver = {'name':'Marcel', 'age':30}
    return Response(driver)
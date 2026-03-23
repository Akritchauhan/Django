from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_list(request):
    
    if request.method == 'GET':
        return Response({"message": "GET request - public access"})
    
    elif request.method == 'POST':
        return Response({"message": "POST request - only authenticated users"})
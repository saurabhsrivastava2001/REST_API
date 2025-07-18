from rest_framework.response import Response
from watchlist_app.models import Movie
from rest_framework.decorators import api_view
from watchlist_app.api.serializers import MovieSerializer

@api_view(['GET']) # This decorator allows us to specify the HTTP methods that this view can handle
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True) #many=True indicates that we are serializing a queryset(list of objects)
    return Response(serializer.data) #serializer.data returns a list of serialized movie data
@api_view(['GET'])
def movie_detail(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response({'error': 'Movie not found'}, status=404)
    
    serializer = MovieSerializer(movie)
    return Response(serializer.data)
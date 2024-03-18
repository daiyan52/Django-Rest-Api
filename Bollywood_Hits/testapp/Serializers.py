from rest_framework.serializers import ModelSerializer
from testapp.models import Actor,Movie

class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        
class ActorSerializer(ModelSerializer):
    lead_actor = MovieSerializer(read_only=True,many=True)
    class Meta:
        model = Actor
        fields = '__all__'

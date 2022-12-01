from rest_framework.serializers import ModelSerializer, SlugRelatedField

from core.models import Livro
from media.models import Image



class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    
        
class LivroDetailSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1
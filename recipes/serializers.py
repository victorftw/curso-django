from rest_framework import serializers

from recipes.models import Recipe
from tag.serializers import TagSerializer


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = [
            'id', 'title', 'description', 'author',
            'category', 'tags', 'public', 'preparation',
            'tag_objects', 'tag_links'
        ]

    public = serializers.BooleanField(
        source='is_published',
        read_only=True,
    )
    preparation = serializers.SerializerMethodField(
        method_name='any_method_name',
        read_only=True,
    )
    category = serializers.StringRelatedField(read_only=True)
    tag_objects = TagSerializer(
        many=True,
        source='tags',
        read_only=True,
    )
    tag_links = serializers.HyperlinkedRelatedField(
        many=True,
        source='tags',
        view_name='recipes:recipes_api_v2_tag',
        read_only=True,
    )

    def any_method_name(self, recipe):
        return f'{recipe.preparation_time} {recipe.preparation_time_unit}'

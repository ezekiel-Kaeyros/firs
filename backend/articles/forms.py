from articles.models import Article
from django import forms


class NewArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = (
            "titre",
            "content",
            "description",
            "image",
        )

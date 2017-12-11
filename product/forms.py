from django.forms import ModelForm, Textarea
from product.models import Comment, Like


class CommentModelForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['author', 'text']
        widgets = {
            'text': Textarea(attrs={'rows': 3}),
        }


class LikeModelForm(ModelForm):

    class Meta:
        model = Like
        fields = ['user', 'product']

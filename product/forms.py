from django.forms import ModelForm, Textarea
from product.models import Comment


class CommentModelForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['author', 'text']
        widgets = {
            'text': Textarea(attrs={'rows': 3}),
        }

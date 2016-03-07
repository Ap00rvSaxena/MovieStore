from datetime import timezone
from haystack import indexes
from newsletter.models import SignUp

class SignUpIndex(indexes.SearchIndex):
    text = indexes.CharField(document=True, use_template=True)
    first_name = indexes.CharField(model_attr='first_name')

    def get_model(self):
        return SignUp

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        # return self.get_model().objects.filter(timestamp__lte=timezone.now())
        return self.get_model().objects.all()

from django.test import TestCase
from blog.models import Post

class PostTests(TestCase):

    def test_str(self):

        phrase = "This is a basic title for a basic test case"
        my_title = Post(title=phrase)
        self.assertEquals(str(my_title), phrase)
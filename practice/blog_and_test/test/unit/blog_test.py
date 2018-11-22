from unittest import TestCase


from practice.blog_and_test.test.blog import Blog

class BlogTest(TestCase):

    def test_create_blog(self):

        b = Blog("title", "author")
        self.assertEqual(b.title,"title")
        self.assertEqual('author', b.author)
        self.assertListEqual([],b.post)


    def test_repr(self):
        b = Blog("test", "author")

        self.assertEqual(b.__repr__(),"test by test and author 0 post")

    def test_repr_multiple_posts(self):
        b = Blog("test", "author")
        b.post = ['one']
        self.assertEqual(b.__repr__(),"test by test and author 1 post")
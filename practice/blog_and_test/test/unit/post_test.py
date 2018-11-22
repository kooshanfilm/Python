from unittest import TestCase
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from post import Post



class PostTest(TestCase):


    def test_create_post(self):
        p = Post("test_title","test_content")

        self.assertEqual (p.title,"test_title")
        self.assertEqual(p.content, "test_content")

    def test_json(self):
        p = Post("test_title", "test_content")
        expected = {'title':'test_title','content':'test_content'}
        self.assertDictEqual(expected,p.json())
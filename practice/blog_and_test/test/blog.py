from unittest import TestCase

from practice.blog_and_test.test.post import Post


class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.post = []


    def __repr__(self):
        return "test by {} and {} {} post".format(self.title,self.author,len(self.post))



    def create_post(self, title, content):
        pass


    # def create_post(self,title,content):
    #     self.post.append(Post(title,content))
    #



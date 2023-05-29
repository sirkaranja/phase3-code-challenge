import Article

class Author:
    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)

    def articles(self):
        return [article for article in Article.all() if article.author() == self]

    def magazines(self):
        return list(set([article.magazine() for article in self.articles()]))

    def topic_areas(self):
        return list(set([magazine.category() for magazine in self.magazines()]))

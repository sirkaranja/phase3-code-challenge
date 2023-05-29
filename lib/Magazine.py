import Article
class Magazine:
    _all = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []
        Magazine._all.append(self)

    def name(self):
        return self._name

    def category(self):
        return self._category

    @classmethod
    def all(cls):
        return cls._all

    @classmethod
    def find_by_name(cls, name):
        for magazine in cls._all:
            if magazine.name() == name:
                return magazine
        return None

    def add_article(self, author, title):
        article = Article(author, self, title)
        self._articles.append(article)

    def article_titles(self):
        return [article.title() for article in self._articles]

    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            author = article.author()
            if author in author_counts:
                author_counts[author] += 1
            else:
                author_counts[author] = 1
        return [author for author, count in author_counts.items() if count > 2]

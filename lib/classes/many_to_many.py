class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("author must be a Author class")
        self._author = author
        if not isinstance(magazine, Magazine):
            raise ValueError("magazine must be a Magazine class")
        self._magazine = magazine
        if not isinstance(title, str):
            raise ValueError("title must be a string")
        if len(title) < 5 or len(title) > 50:
            raise ValueError("title must be between 5 and 50 chars")
        self._title = title
        
        Article.add_new_article(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
      raise ValueError("Title cannot be changed once it is set.")
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, new_author):
        # if not isinstance(new_author, Author):
        #     raise ValueError("author must be a Author class")
        self._author = new_author

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise ValueError("magazine must be a Magazine class")
        self._magazine = new_magazine

    @classmethod
    def add_new_article(cls, new_artcle):
        cls.all.append(new_artcle)
        
class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Author name must be a string")
        if len(name) == 0:
            raise ValueError("Author name must be longer than 0 characters")
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
      raise ValueError("Author name cannot be changed once it is set.")

    def articles(self):
        return list(set(article for article in Article.all if article.author == self))

    def magazines(self):
        return list(set(article.magazine for article in Article.all if article.author == self))

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        Article.add_new_article(new_article)
        return new_article

    def topic_areas(self):
        topics = list(set(article.magazine.category for article in Article.all if article.author == self))
        if len(topics) > 0: 
            return topics
        else:
            return None

class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str):
            raise ValueError("Magazine name must be a str")
        if (len(name) < 2) or (len(name) > 16):
            raise ValueError("Magazine name must be 2-16 characters.")
        self._name = name

        if not isinstance(category, str):
            raise ValueError("Category must be a str")
        if len(category) == 0:
            raise ValueError("Category must be more than 0 char.")
        self._category = category

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
      if not isinstance(new_name, str):
        raise ValueError("magazine name shld be a str")
      if (len(new_name) < 2 or len(new_name) > 16):
        raise ValueError("magazine name shld be a str")
      self._name = new_name
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, new_category):
        if (type(new_category) == str) and len(new_category) > 0:
            self._category = new_category
        else:
            raise ValueError("Catgory must be a str and > 0 char.")

    def articles(self):
        return list(set(article for article in Article.all if article.magazine == self))

    def contributors(self):
        return list(set(article.author for article in Article.all if article.magazine == self))

    def article_titles(self):
        art_titles = [article.title for article in Article.all if article.magazine == self]
        if len(art_titles) > 0:
            return art_titles
        else:
            return None

    def contributing_authors(self):
        # authorCountDict = {}
        articleAuthors = [article.author for article in Article.all if article.magazine == self]
        result = []
        # for author in articleAuthors:
            # if not authorCountDict.get(author):
            #     authorCountDict[author] = 0
            # authorCountDict[author] += 1
            # if authorCountDict[author] == 2:
            #     result.append(author)
        
        for author in articleAuthors:
            if result.count(author) == 0 and articleAuthors.count(author) >= 2:
                result.append(author)

        if len(result) > 0:
            return result
        else:
            return None
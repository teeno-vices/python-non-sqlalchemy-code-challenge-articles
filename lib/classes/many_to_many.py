# Definition of the class Article.
class Article:
    # Initialize all to empty array(list).
    # This is a Class Attribute to store instances for the Article class (To store the Articles).
    all = list()

    # Attribute initialization. (author, magazine, title).
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        # Appending each new Article to all list (The class Attribute).
        Article.all.append(self)

    # Definition of the title property.(Allow it to be accessed as attributes)
    @property
    def title(self):
        return self._title

    # The below allow assigning of new value to title attribute
    @title.setter
    def title(self, new_title):
        # Check whether "title" attribute already exists for the instance
        # If so, raise Attribute error.
        if hasattr(self, 'title'):
             AttributeError('Title cannot be changed')
        # The below checks if the new title is a string and is of lenth between 5 and 50 characters
        if isinstance(new_title, str) and 5 <= len(new_title) <= 50:
        # If so new_title is assigned a New Value.
            self._title = new_title
        # If not so the below code blockis the one that runs.(ValueError)
        else:
             ValueError('Title must be a string between 5 and 50 characters')

    # Definition of the author property.(Allow it to be accessed as an attribute)
    @property
    def author(self):
        return self._author

    # setter method allows assigning a new value to author attribute.
    @author.setter
    def author(self, new_author):
        # Pass a codition to check whether the new author is an instance of the Author class.
        if isinstance(new_author, Author):
        # If so, new_author is assigned a New Value.
            self._author = new_author
        # If not, the following block of code runs which is a TypeError.
        else:
            raise TypeError("Author must be an instance of Author")

    # Definition of the magazine property.(Allow it to be accessed as an attribute)
    @property
    def magazine(self):
        return self._magazine
    
    # setter method allows assigning a new value to magazine attribute.
    @magazine.setter
    def magazine(self, new_magazine):
        # Pass a codition to check whether the new magazine is an instance of the Magazine class.
        if isinstance(new_magazine, Magazine):
        # If so, new_magazine is assigned a New Value.
            self._magazine = new_magazine
        # If not, the following block of code runs which is a TypeError.
        else:
            raise TypeError("Magazine must be an instance of Magazine")


# Definition of the class Author
class Author:

    # Attribute initialization which is name (instance attribute)
    def __init__(self, name):
        self.name = name

    # Definition of the name property.(Returns the value of the name Attribute)
    @property
    def name(self):
        return self._name

    # setter method allows assigning a new value to name attribute.
    @name.setter
    def name (self, new_name):
        # Condition to check if the name attribute already exists for the instance, if so it passes an Attribute error
        if hasattr(self, "name"):
            AttributeError("Name cannot be changed")
        # if not so, The following block of code runs
        # The below checks if the name if not empty string. if so it sets name attribute to new name.
        else:
            # Checks if name is a string
            if isinstance(new_name, str):
                # Checks the length of the new_name
                if len(new_name):
                    self._name = new_name
                # If the above is not true, the below is the one that runs raising a ValueError 
                else:
                    ValueError("Name must be longer than 0 characters")
            # If the condition for checking if the name is a string is false this code block runs(TypeError)
            else:
                TypeError("Name must be a string")

    def articles(self): # Article method
        # Iteration.
        # returns a list of articles written by the author.
        return [article for article in Article.all if self == article.author]

    def magazines(self): # Magazine method
        # Returns the list of magazines the Author has made contributions
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title): # add_article method
        # Adds an article to the magazine.(list of contributions)
        return Article(self, magazine, title)

    def topic_areas(self): # topic_areas method
        # Returns a list of topic areas for all articles by author.(which he has contributed to)
        areas = list({magazine.category for magazine in self.magazines()})
        return areas if areas else None

# Definition of the Magazine classs
class Magazine:
    # Initialisation of the instance attributes.
    def __init__(self, name, category):
        self.name = name
        self.category = category

    # Defines a property named name which when accessed returns value of name attribute 
    @property
    def name(self):
        return self._name

    # setter method for assigning a new value to name attribute.
    @name.setter
    def name(self, new_name):
        # Control flow:
        # Check if new name is a string and falls in length 2 to 16
        # if so name attribute is set to new name
        if isinstance(new_name, str) and 2 <= len(new_name) <= 16:
            self._name = new_name
        # Otherwise ValueError.
        else:
             ValueError("Name must be a string between 2 and 16 characters")

    # Defines a property named category which when accessed returns value of category attribute
    @property
    def category(self):
        return self._category

    # setter method for assigning a new value to category attribute.
    @category.setter
    def category(self, new_category):
        # Control flow:
        # Checks if category is on instance string and of length greater than 0(Not empty)
        # If true, sets category attribute to new category
        if isinstance(new_category, str) and len(new_category) > 0:
            self._category = new_category
        # Otherwise ValueError.
        else:
             ValueError("Category must be a non-empty string")

    # Methods:
    # articles methodreturns a list of articles in the magazine.
    def articles(self):
        return [article for article in Article.all if self == article.magazine]

    # contributors method returns a list of authors who have contributed to the magazine.
    def contributors(self):
        return list({article.author for article in self.articles()})

    # article_titles method returns a list of titles of articles in the magazine.
    def article_titles(self):
        article_titles = [article.title for article in self.articles()]
        return article_titles if article_titles else None

    # contributing_authors returns a list of authors who have contributed multiple articles to the magazine.
    # First counting the number of articles contributted by each Author and filters out those contributing more than two articles.
    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            author_counts[article.author] = author_counts.get(article.author, 0) + 1

        return [author for author, count in author_counts.items() if count >= 2] or None
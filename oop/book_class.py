class Book:
    def __init__(self, title, author, year):
        """Constructor to initialize the book attributes"""
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """Return a readable string representation"""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Return an official representation that can recreate the object"""
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """Destructor called when the object is deleted"""
        print(f"Deleting {self.title}")

mylist = [1,2,3]

class Sample():
    pass

mysample = Sample()


class Book():

    def __init__(self,title,author,pages):

        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages


b = Book('Hello World','Hannah Fry',300)

print(str(b))

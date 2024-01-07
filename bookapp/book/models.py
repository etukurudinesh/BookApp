from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index


# Author page
class AuthorPage(Page):

    # Name of the Author
    authorName = models.CharField(
        max_length = 30,
        default='New Author',
        null=False,
        blank=False
    )

    # Description of the Author
    authorDescription = RichTextField(
        blank=True, # allow field to be blank
        default="Enter description here"
    )

    # Filter by authorName
    search_fields = Page.search_fields + [ 
        index.FilterField('authorName')
    ]

    # Display the fields for user to populate data
    content_panels = Page.content_panels + [
        FieldPanel('authorName'),
        FieldPanel('authorDescription')
    ]



# Book Page
class BookPage(Page):
    # Name of the book
    bookName = models.CharField(
        max_length = 30,
        default='New Book',
        null=False,
        blank=False
    )

    # Published Date of the book
    bookPublishedOn = models.DateField(
        null = True,
        blank = True
    )

    # Description of the book
    bookDescription = RichTextField(
        blank=True, # allow field to be blank
        null=True, # allow db to be blank
        default="enter description here"
    )

    # search by bookName
    search_fields = Page.search_fields + [ 
        index.SearchField('bookName'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('bookName'),
        FieldPanel('bookDescription'),
        FieldPanel('bookPublishedOn')
    ]

    

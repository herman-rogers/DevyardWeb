from django.db import models
from django.contrib import admin

class Post( models.Model ):
    title    = models.CharField( max_length = 60 )
    author   = models.CharField( max_length = 60 )
    body     = models.TextField( )
    created  = models.DateTimeField( auto_now_add=True )
    
    def __unicode__( self ):
        return self.title
        return self.author

###Installing Admin Here
class PostAdmin( admin.ModelAdmin ):
    search_fields = ["title", "author"]

# BUGGY on mobile browsers

TODO

1. django-allauth integration
2. upgrade user profile to include avatar for comments
3. Profile avatar maybe some more data?
4. File upload to data creation
5. Secure
6. ratelimit
7. User logs on content changes

# API endpoints


Info 

This gives the content needed for the home page, article page and articles to view annonomously

http://localhost:8000/api/info/

API route with links to rest of the end points

http://localhost:8000/api/

```

{
    "update/page": "http://localhost:8000/api/update/page/",
    "update/pagegallery": "http://localhost:8000/api/update/pagegallery/",
    "update/article": "http://localhost:8000/api/update/article/",
    "update/articlegallery": "http://localhost:8000/api/update/articlegallery/",
    "update/message": "http://localhost:8000/api/update/message/",
    "update/contact": "http://localhost:8000/api/update/contact/"
}

```

## Galleries 
Each page and article has a gallery and a hero image along with headers and paragraphs to display content

```
    {
        "id": 8,
        "article": 1,
        "name": "Kamala",
        "image": "http://localhost:8000/media/page/image/8/kamala.jpg",
        "description": "Kamala",
        "thumbnail": "http://localhost:8000/media/page/thumb/8/kamala_Y12PdFU.jpg"
    }
```

Can be infinite

```
    {
        "id": 3,
        "creator": "admin",
        "name": "Article",
        "page": "article",
        "title": "Free Article publishing",
        "title_description": "articlesharing.com.",
        "hero_image": "http://localhost:8000/media/page/image/3/article.jpg",
        "paragraph_1": "This is a site that tries to be inline editatble. When you own the article or are the logged in as the Site Admin, you can edit the content.",
        "paragraph_2": "Please change me use ... for an empty line",
        "paragraph_3": "This is your timeline, create a good one.",
        "paragraph_4": "Share the news you find interesting.",
        "paragraph_5": "Please change me use ... for an empty line",
        "file": null,
        "created_at": "2024-08-23T07:51:41.108709Z",
        "updated_at": "2024-08-23T07:53:18.094396Z",
        "active": false
    },
```

Only the admin should be able to change these, some fields not being used


### Messaging 

Is only one thread deep, you can reply to a message, but not it's children
```
    {
        "user": "jody",
        "article": 3,
        "message": "Well that was awkward",
        "message_id": null,
        "first_name": "Jody",
        "last_name": "Beggs",
        "created_at": "2024-08-23T09:12:35.736079Z"
    }
```

### Contact

Not implemented yet
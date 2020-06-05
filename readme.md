## oas movie app

- requirement: [pdf](Coding%20Task%20(2).pdf) | [movies.json](movies.json)
- key features and/or requirements
    - Import movie from json (Data is given in movies.json, design, model and implement a Django app for this data.)
        - I did this with django's built in command
    - Develop Movie Listing Page
        - I used django's generic list view
    - Develop Movie Detail Page
        - I used django's generic detail view
    - Develop Javascript search bar which filters movies listed on the Movie Listing Page based on their names
        - Currently just implemented a very simple search bar with debounced jquery and drf-based search API. Disclaimer: I get it from [here](https://openfolder.sh/django-tutorial-as-you-type-search-with-ajax)
        - I must admit that I can do this better. For production apps, I prefer to build with more sophisticated tech. I'd probably go with react, debounced the search input component for several ms, and trigger an API call with modules like axios. 
        Again, considered for simplicity, I choosed this instead of implementing whole new app just for the search bar. I hope this can be tolerated.
    -  (optional) I tried to implement S3Boto3Storage
        - all the movie's thumbnail and static files are saved at AWS S3 bucket, so django didn't need to serve all of this and goes directly into s3.
        - Django only needs to create a pre-signed URL, which I believe, is a lot less work
- techs used:
    - Django mvc
    - aws s3 for storing images thumbnail
    - for the IDE, I used PyCharm Professional, if that matters.

{% extends 'base.html' %}

{% block content %}

<div style="text-align: left">
<h1>About Us</h1>

{%filter markdown%}

# 数据库实践

## Application Server File Structure

<pre>
<code>.
├── api                             -- Application Interfaces
│   ├── __init__.py                 -- Home inteface
│   ├── login.py                    -- Login Interface
│   ├── posts.py                    -- Post Interface
│   ├── search.py                   -- Search Interface
│   ├── service                     -- Application Services
│   │   ├── CommentService.py       -- Comment Stuff
│   │   ├── PostService.py          -- Get Posts under varies conditions
│   │   ├── SearchService.py        -- Search Posts
│   │   ├── TagService.py           -- Get tags
│   │   └── UserService.py          -- Login or User Stuff
│   └── users.py                    -- User Interfaces
├── app.py                          -- APPLICATION ENTRY
├── config.py                       -- Application configuration
├── environment.yml                 -- Anaconda Environment
├── models                          -- SQL Table Structure
│   ├── comments.py                 -- table comments
│   ├── fields.py                   -- table fields
│   ├── functions.py                -- Postgresql DIY Functions
│   ├── __init__.py                 -- db initiation
│   ├── posts.py                    -- table posts
│   ├── post_tags.py                -- table post tags
│   ├── procedures.py               -- Postgresql DIY Procedures
│   ├── profanity.py                -- table profanity
│   ├── semantic_embeddings.py      -- table embedding
│   ├── tags.py                     -- table tag
│   ├── user_credentials.py         -- table user credential
│   └── users.py                    -- table users
├── notebook.ipynb                  -- scripts
├── README.md                       -- README
├── templates                       -- Static Files
│   ├── ...                        
│   └── user.html                 
└── utils                           -- utils, helpers
    ├── get_semantic.py             -- title embeddings with pytorch
    ├── helper.py                   -- helper functions
    ├── __init__.py
    └── ML                          -- Machine Learning Functions
        └── __init__.py
12 directories, 88 files
</code>
</pre>



{%endfilter%}
</div>

{% endblock %}

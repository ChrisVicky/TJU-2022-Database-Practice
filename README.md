<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/lxgw-wenkai-webfont@1.1.0/style.css" />
  <!-- Lite version -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/lxgw-wenkai-lite-webfont@1.1.0/style.css" />
  <!-- TC version -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/lxgw-wenkai-tc-webfont@1.0.0/style.css" />
  <!-- Screen version -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/lxgw-wenkai-screen-webfont@1.1.0/style.css" />
  <style>
    body {
      font-family: "LXGW WenKai", sans-serif;
      /* Lite version */
      font-family: "LXGW WenKai Lite", sans-serif;
      /* TC version */
      font-family: "LXGW WenKai TC", sans-serif;
      /* Screen version */
      font-family: "LXGW WenKai Screen", sans-serif;
    }
  </style>
</head>
<body>
<div>
# Forum in Flask -- 數據庫實踐大作業

## Project Structure

<pre>
<code>.
├── build.sh                            -- Docker File Script
├── Dockerfile                          -- Docker File
├── forum-in-flask
│   ├── api                             -- Application Interfaces            
│   │   ├── __init__.py                 -- Home inteface                     
│   │   ├── login.py                    -- Login Interface                   
│   │   ├── posts.py                    -- Post Interface                    
│   │   ├── search.py                   -- Search Interface                  
│   │   ├── service                     -- Application Services              
│   │   │   ├── CommentService.py       -- Comment Stuff                     
│   │   │   ├── PostService.py          -- Get Posts under varies conditions 
│   │   │   ├── SearchService.py        -- Search Posts                      
│   │   │   ├── TagService.py           -- Get tags                          
│   │   │   └── UserService.py          -- Login or User Stuff               
│   │   └── users.py                    -- User Interfaces                   
│   ├── app.py                          -- APPLICATION ENTRY                 
│   ├── config.py                       -- Application configuration         
│   ├── environment.yml                 -- Anaconda Environment              
│   ├── models                          -- SQL Table Structure               
│   │   ├── comments.py                 -- table comments                    
│   │   ├── fields.py                   -- table fields                      
│   │   ├── functions.py                -- Postgresql DIY Functions          
│   │   ├── __init__.py                 -- db initiation                     
│   │   ├── posts.py                    -- table posts                       
│   │   ├── post_tags.py                -- table post tags                   
│   │   ├── procedures.py               -- Postgresql DIY Procedures         
│   │   ├── profanity.py                -- table profanity                   
│   │   ├── semantic_embeddings.py      -- table embedding                   
│   │   ├── tags.py                     -- table tag                         
│   │   ├── user_credentials.py         -- table user credential             
│   │   └── users.py                    -- table users                       
│   ├── notebook.ipynb                  -- scripts                           
│   ├── README.md                       -- README                            
│   ├── templates                       -- Static Files                      
│   │   ├── ...                                                              
│   │   └── user.html                                                        
│   └── utils                           -- utils, helpers                    
│       ├── get_semantic.py             -- title embeddings with pytorch     
│       ├── helper.py                   -- helper functions                  
│       ├── __init__.py                                                      
│       └── ML                          -- Machine Learning Functions        
│           └── __init__.py                                                  
├── Makefile                            -- Command Alias
├── README.md                           -- README.md
└── requirements.txt                    -- Python Environment (Without Torch)

14 directories, 91 files
</code>
</pre>

## Deploy via Docker
* default port: 8087
```shell
make docker
```
</div>
</body>
</html>



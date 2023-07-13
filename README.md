
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
* config.py

```shell
cd ./forum-in-flask
cp config_example.py config.py
```
* Modify `SECRET_KEY` and `SQLALCHEMY_DATABASE_URI` then run following command

```shell
make docker
```
* default port: 8087

## Database SQLs

Refer to https://github.com/fkcptlst/db_exercise

pack:
	zip -r archive ./*

deploy:
	sudo bash ./build.sh

run:
	ln -s /home/shujuku/forum-in-flask/cached_posts ./cached_posts
	ln -s /home/shujuku/forum-in-flask/cached_search ./cached_search
	python3 ./forum-in-flask/app.py

push:
	git add . && git commit -m "makefile Commit" && git push

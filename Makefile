pack:
	zip -r archive ./*

deploy:
	sudo bash ./build.sh

local:
	# mkdir ./cached_posts ./cached_search 
	python3 ./forum-in-flask/app.py

run:
	ln -s /home/shujuku/forum-in-flask/cached_posts ./cached_posts
	ln -s /home/shujuku/forum-in-flask/cached_search ./cached_search
	python3 ./forum-in-flask/app.py

push:
	git add . && git commit -m "makefile Commit" && git push

rerun:
	docker run -itd \
		--name $name_run \
		-v /home/shujuku/forum-in-flask/cached_posts:/cached_posts \
		-v /home/shujuku/forum-in-flask/cached_search:/cached_search \
		-v /root/Coding/forum-in-flask/forum-in-flask:/forum-in-flask \
		-p ${port}:${portin} \
		$name_img:latest

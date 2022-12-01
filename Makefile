pack:
	zip -r archive ./*

docker:
	sudo ./build.sh

run:
	python3 ./forum-in-flask/app.py

push:
	git add . && git commit -m "makefile Commit" && git push

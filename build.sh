
name_run=forum_run
name_img=forum_img

docker stop $name_run
docker rm $name_run
docker rmi $name_img

path=`pwd`
port=8087
portin=8085

docker build -t $name_img .

docker run -itd \
	--name $name_run \
	-v ${home}/forum-in-flask/cached_posts:/cached_posts \
	-v ${home}/forum-in-flask/cached_search:/cached_search \
	-v ${home}/forum-in-flask/forum-in-flask:/forum-in-flask \
	-p ${port}:${portin} \
	$name_img:latest




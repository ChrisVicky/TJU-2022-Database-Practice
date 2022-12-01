
name_run=forum_run
name_img=forum_img

docker stop $name_run
docker rm $name_run
docker rmi $name_img

path=`pwd`
port=8087
portin=8085

echo docker build -t $name_img .
docker build -t $name_img .

echo docker run -itd --name $name_run -p ${port}:${portin} $name_img:latest
docker run -itd --name $name_run -p ${port}:${portin} $name_img:latest

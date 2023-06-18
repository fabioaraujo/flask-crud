criando um container docker com mysql 
docker run --name mysql-server -e MYSQL_ROOT_PASSWORD=rute -e MYSQL_ROOT_HOST='%' -d -p 3306:3306 mysql:latest
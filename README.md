criando um container docker com mysql

```bash
docker run --name mysql-server -e MYSQL_ROOT_PASSWORD=rute -e MYSQL_ROOT_HOST='%' -d -p 3306:3306 mysql:latest
```

Para criar um container com a configuração do arquivo docker-compose.yml

```bash
docker compose up
```

git pull
docker-compose down
sudo docker system prune -a -f
docker-compose up --build -d
docker logs -f hello-txt
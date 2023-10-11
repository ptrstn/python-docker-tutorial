# Python Docker Tutorial

https://www.youtube.com/watch?v=0H2miBK_gAk

https://github.com/patrickloeber/python-docker-tutorial/


## Commands

Stop all containers 

```bash
docker stop $(docker ps -a -q) .
docker remove $(docker ps -a -q) .
```

```bash
docker build -t fastapi-image .
docker images  # List available images
docker run --name fastapi-container -p 8080:8000 fastapi-image
docker run -d --name fastapi-container -p 8080:8000 fastapi-image
```

### Volumes

Persistent data

- Map ```$(pwd)``` to ```/code``` inside the container
- whenever there are changes in the code, the container updates immediately

```bash
docker run -d --name fastapi-container -p 8080:8000 -v $(pwd):/code fastapi-image
```

### SSH into Container

```bash
docker exec -it fastapi-container /bin/bash
```

## Docker-Compose

- defining and running multi container docker apps

```yaml
services:
  app:  # name of service
    build: .  # build from local Dockerfile
    # Alternative to build: image:<name>
    container_name: python-server
    command: uvicorn src.main:app --host 0.0.0.0 --port 80 --reload
    ports:
      - 80:80
    volumes:
      - .:/code
```
- specify services

start services in docker-compose.yml:

```bash
docker-compose up
docker-compose down
docker-compose up --build -d # rebuild image, detached
```
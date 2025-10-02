## Build to docker image with version.
# --platform linux/amd64, linux/arm64, darwin/amd64
docker build -t "artour-filter-spam:latest" .

## Run docker service.
docker compose up -d

## Remove unused images.
docker image prune -f

## Show process.
docker ps
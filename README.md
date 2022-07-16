# Учебный проект для Otus - Microservice Architecture
### Запуск проекта в docker:
```shell
docker-compose up
```

### Dependencies
Python 3.10
```shell
poetry install --no-root
```
### Запуск проекта Pycharm:
- Module name: `uvicorn`
- Parameters: `src.main:app`
- Working directory: `{{ path project folder }}/project`


### DockerHUB
```shell
docker tag otus-ms-architecture zlustniy/otus-ms-architecture
docker push zlustniy/otus-ms-architecture
```
To push a new tag to this repository,
```shell
docker push zlustniy/otus-ms-architecture-zakirov:tagname
```
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
docker-compose build
docker tag otus-ms-architecture zlustniy/otus-ms-architecture:latest
docker push zlustniy/otus-ms-architecture:latest
```
To push a new tag to this repository,
```shell
docker push zlustniy/otus-ms-architecture:tagname
```

### K8S
```shell
minikube start –vm-driver=virtualbox
minikube dashboard
```

```shell
kubectl apply -f 1-deployment.yaml
```
```shell
kubectl --namespace otus port-forward pod/otus-first-homework-69fd7c856d-2nzjr 8000:8000
```
```shell
minikube ip
```

```shell
kubectl get -n otus deployments
```


### Запуск приложения:
```shell
kubectl create ns otus
kubectl apply -f .
```
```shell
kubectl create ns postgres
kubectl -n postgres apply -f postgres.yaml
kubectl -n postgres port-forward postgres-statefulset-0 5435:5432
```

```shell
kubectl port-forward service/otus-app-postgresql 5435:5432
```

### Удаление приложения:
```shell
kubectl delete ingress -n otus otus-first-homework
kubectl delete service -n otus otus-first-homework
kubectl delete deployment -n otus otus-first-homework
kubectl delete ns otus
```

```shell
helm install otus-app ./app-chart
```
```shell
helm delete otus-app
```

```shell
kubectl get all
```

### Работа с БД. Миграции.

Для создания миграции:

```shell
alembic revision --message=message --autogenerate
```

Для применения миграции:

```shell
alembic upgrade head
```

Откатить последнюю миграцию:

```shell
alembic downgrade -1
```

Если добавляется новая модель, необходимо обязательно ее импортировать в ../models/__init__.py, чтобы alembic стал
отслеживать ее.

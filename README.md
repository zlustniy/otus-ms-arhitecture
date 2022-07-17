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
docker push zlustniy/otus-ms-architecture:tagname
```

### K8S
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
### Удаление приложения:
```shell
kubectl delete ingress -n otus otus-first-homework
kubectl delete service -n otus otus-first-homework
kubectl delete deployment -n otus otus-first-homework
kubectl delete ns otus
```
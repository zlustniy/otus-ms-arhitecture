1. Ссылка на github c манифестами: https://github.com/zlustniy/otus-ms-arhitecture/tree/master/k8s/manifest
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

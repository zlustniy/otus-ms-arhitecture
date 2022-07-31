1.
```
ссылка на директорию в github, где находится директория с манифестами кубернетеса
```

2. 
```
инструкция по запуску приложения
```
- команда установки БД из helm, вместе с файлом values.yaml: 

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
4. Коллекция Postman https://github.com/zlustniy/otus-ms-arhitecture/blob/master/homework-1/OTUS.postman_collection.json
   ```shell
   /otus-ms-arhitecture/homework-1$ newman run OTUS.postman_collection.json
   newman
   
   OTUS
   
   → health
     GET http://arch.homework/health/ [200 OK, 147B, 52ms]
     ✓  Status code is 200
     ✓  Status OK
   
   → health rewrite пути
     GET http://arch.homework/otusapp/zakirov-max/health/ [200 OK, 147B, 12ms]
     ✓  Status code is 200
     ✓  Status OK
   
   ┌─────────────────────────┬───────────────────┬──────────────────┐
   │                         │          executed │           failed │
   ├─────────────────────────┼───────────────────┼──────────────────┤
   │              iterations │                 1 │                0 │
   ├─────────────────────────┼───────────────────┼──────────────────┤
   │                requests │                 2 │                0 │
   ├─────────────────────────┼───────────────────┼──────────────────┤
   │            test-scripts │                 4 │                0 │
   ├─────────────────────────┼───────────────────┼──────────────────┤
   │      prerequest-scripts │                 2 │                0 │
   ├─────────────────────────┼───────────────────┼──────────────────┤
   │              assertions │                 4 │                0 │
   ├─────────────────────────┴───────────────────┴──────────────────┤
   │ total run duration: 150ms                                      │
   ├────────────────────────────────────────────────────────────────┤
   │ total data received: 30B (approx)                              │
   ├────────────────────────────────────────────────────────────────┤
   │ average response time: 32ms [min: 12ms, max: 52ms, s.d.: 20ms] │
   └────────────────────────────────────────────────────────────────┘
   ```
1. Сделал helm-chart
https://github.com/zlustniy/otus-ms-arhitecture/tree/master/k8s/manifest
https://github.com/zlustniy/otus-ms-arhitecture/tree/master/k8s/manifest/app-chart
2. Запуск приложения:
   1. Запуск приложения, вместе с базой данных:
       ```shell
       helm install otus-app ./app-chart
       ```
   2. JOB миграции
      ```
      kubectl apply -f initdb.yaml 
      ```

Команда удаления приложения:
```shell
helm delete otus-app
```
3. Коллекция Postman https://github.com/zlustniy/otus-ms-arhitecture/blob/master/homework-2/OTUS-2.postman_collection.json
```shell
   /otus-ms-arhitecture/homework-2$ newman run OTUS-2.postman_collection.json 
   newman
   
   OTUS-2
   
   → Создание пользователя
     POST http://arch.homework/user/ [200 OK, 272B, 101ms]
     ✓  Status code is 200
   
   → Получение пользователя
     GET http://arch.homework/user/15/ [200 OK, 272B, 19ms]
   
   → Обновление пользователя
     PUT http://arch.homework/user/15/ [200 OK, 288B, 16ms]
     ✓  Status code is 200
   
   → Удаление пользователя
     DELETE http://arch.homework/user/15/ [200 OK, 288B, 19ms]
     ✓  Status code is 200
   
   → Удалить всех пользователей
     DELETE http://arch.homework/user/ [200 OK, 133B, 20ms]
   
   ┌─────────────────────────┬───────────────────┬───────────────────┐
   │                         │          executed │            failed │
   ├─────────────────────────┼───────────────────┼───────────────────┤
   │              iterations │                 1 │                 0 │
   ├─────────────────────────┼───────────────────┼───────────────────┤
   │                requests │                 5 │                 0 │
   ├─────────────────────────┼───────────────────┼───────────────────┤
   │            test-scripts │                 9 │                 0 │
   ├─────────────────────────┼───────────────────┼───────────────────┤
   │      prerequest-scripts │                 5 │                 0 │
   ├─────────────────────────┼───────────────────┼───────────────────┤
   │              assertions │                 3 │                 0 │
   ├─────────────────────────┴───────────────────┴───────────────────┤
   │ total run duration: 340ms                                       │
   ├─────────────────────────────────────────────────────────────────┤
   │ total data received: 590B (approx)                              │
   ├─────────────────────────────────────────────────────────────────┤
   │ average response time: 35ms [min: 16ms, max: 101ms, s.d.: 33ms] │
   └─────────────────────────────────────────────────────────────────┘
```
# coffee_delivery

## Notice
work only on `dev` branch

after review and test, should merge into `main` branch

## Project Features

1. User
2. Coffee List
3. Purchase
4. Purchased List

## Requests and Responses

* GET User
`/users/{username}`

Request

```dart
       var response = await dio.get('http://localhost:8080/users/amir',
        options: Options(headers: {
          "token":
              "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhbWlyIiwiZXhwIjoxNjI3ODI2Njg3fQ.jyMWAN3o0qF07xmID0T15wowdWT1Ku0BUcCPWlVLafU"
        })); 
```

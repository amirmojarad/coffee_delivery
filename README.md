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
var response = await dio.get(URL_ADDRESS,
       options: Options(headers: {
          "token": token
        })); 
```

Response
```json
 {
    "id": int,
    "full_name": string,
    "is_active": boolean,
    "access_token": string,
    "email": string,
    "hashed_password": string,
    "username": string
  },
```

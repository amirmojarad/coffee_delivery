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
var response = await Dio().get(URL_ADDRESS,
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
* Post User

Request

```dart
var response = await dio.post(
      'http://localhost:8080/users/sign_up',
      options: Options(contentType: Headers.formUrlEncodedContentType),
      data: {
        "username": "test_username",
        "password": "test_password",
      },
    );
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

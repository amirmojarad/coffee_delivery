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

### GET User
`/users/{username}`

Request

```dart
var response = await Dio().get(URL_ADDRESS/users/{username},
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
### POST User

Request

```dart
var response = await dio.post(
      'URL_ADDRESS/users/sign_up',
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
### PUT User

Request
```dart
var response = await Dio().put('URL_ADDRESS/users/{username}',
        options: Options(headers: {
          "token": token
        }),
        queryParameters: {
          "full_name": Optional[str],
          "email": Optional[str]
        });
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
### GET User's Coffee

Request
```dart
var response = await dio.get(
      'http://localhost:8080/users/{username}/coffee/',
      options: Options(
        headers: {
          "token": token
        },
      ),
    );
```

Response
```json
[
  {
    "id": int,
    "caffeine": float,
    "cholesterol": float,
    "protein": float,
    "sugars": float,
    "total_fat": float,
    "img": string,
    "calories": float,
    "name": string,
    "sodium": float,
    "dietary_fiber": float,
    "saturated_fat": float,
    "total_carbohydrates": float
  },
]
```


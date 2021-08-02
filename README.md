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

### POST Coffee to User

Request
```dart
var response = await Dio().post(
      'URL_ADDRESS/users/{username}/coffee/',
      queryParameters: {"coffee_name": coffee_name},
      options: Options(
        headers: {
          "token": token
          },
      ),
    );
```

Response
```json
{
       "status_code": 200,
       "detail": "Added Successfully",
       "headers": null
}

```

### GET Coffee

Request 
```dart
    var response = await Dio().get(
      'URL_ADDRESS/coffee/',
    );
```

Response
```json
[
  {
    "id": 1,
    "caffeine": 225,
    "cholesterol": 0,
    "protein": 1,
    "sugars": 0,
    "total_fat": 0,
    "img": "files/americano.jpg",
    "calories": 15,
    "name": "Americano",
    "sodium": 10,
    "dietary_fiber": 0,
    "saturated_fat": 0,
    "total_carbohydrates": 2
  },
  {
    "id": 2,
    "caffeine": 150,
    "cholesterol": 15,
    "protein": 7,
    "sugars": 10,
    "total_fat": 4,
    "img": "files/misto.jpg",
    "calories": 110,
    "name": "Misto",
    "sodium": 100,
    "dietary_fiber": 0,
    "saturated_fat": 2,
    "total_carbohydrates": 10
  },
  {
    "id": 3,
    "caffeine": 150,
    "cholesterol": 20,
    "protein": 9,
    "sugars": 12,
    "total_fat": 4,
    "img": "files/cappuccino.jpg",
    "calories": 140,
    "name": "Cappuccino",
    "sodium": 120,
    "dietary_fiber": 0,
    "saturated_fat": 2,
    "total_carbohydrates": 14
  },
  {
    "id": 4,
    "caffeine": 150,
    "cholesterol": 20,
    "protein": 1,
    "sugars": 12,
    "total_fat": 4,
    "img": "files/caramel_macchiato.jpg",
    "calories": 15,
    "name": "Caramel Macchiato",
    "sodium": 120,
    "dietary_fiber": 0,
    "saturated_fat": 2,
    "total_carbohydrates": 2
  },
  {
    "id": 5,
    "caffeine": 150,
    "cholesterol": 20,
    "protein": 1,
    "sugars": 12,
    "total_fat": 4,
    "img": "files/espresso.jpg",
    "calories": 15,
    "name": "Espresso",
    "sodium": 120,
    "dietary_fiber": 0,
    "saturated_fat": 2,
    "total_carbohydrates": 2
  },
  {
    "id": 6,
    "caffeine": 150,
    "cholesterol": 20,
    "protein": 1,
    "sugars": 12,
    "total_fat": 4,
    "img": "files/flat_white.jpg",
    "calories": 15,
    "name": "Flat White",
    "sodium": 120,
    "dietary_fiber": 0,
    "saturated_fat": 2,
    "total_carbohydrates": 2
  },
  {
    "id": 7,
    "caffeine": 150,
    "cholesterol": 20,
    "protein": 1,
    "sugars": 12,
    "total_fat": 4,
    "img": "files/mocha.jpg",
    "calories": 15,
    "name": "Mocha",
    "sodium": 120,
    "dietary_fiber": 0,
    "saturated_fat": 2,
    "total_carbohydrates": 2
  }
]
```

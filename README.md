# flask api simple

In this project we use flask for create a restful server.

for generate database and fill data run `model.py`

Use can change secret key in `env.py`

Run `boot.py` for start server.

for test you can use this statement:

This command can login;
```
    curl -X POST 127.0.0.1:5000/login -i -u ali:123
    curl -X POST 127.0.0.1:5000/login -i -H "Authorization: Basic YWxpOjEyMw=="
```

Two above Lines is equal, You must send **Base64** of username:password.
`YWxpOjEyMw==` is Base64 of `ali:123`

After login you got this response:

```
    {
        "duration": 600,
        "token": "eyJhbGciOiJIUzI1NiIsImV4cCI6MTUxMTQxNzIzMSwiaWF0IjoxNTExNDE2NjMxfQ.eyJpZCI6MX0.EaaqUk_wk9FdJJkNiTUwI78h4heVkfoNLX9u6VH2KUw"
    }
```

Now you can use **token** for next requests.

```
    curl -X POST 127.0.0.1:5000/ -i -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsImV4cCI6MTUxMTQxNjc4MSwiaWF0IjoxNTExNDE2MTgxfQ.eyJpZCI6MX0.0Of_YE-UyIeOXW0JcP1-gaamK3x9dZYrBt4c2Q2D6uE"
```


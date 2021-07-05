# API Reference

This is contains all the endpoints of the API

## Specific Endpoints for Movies

### Get all movies

```http
  GET /api/movies
```

### Get Specific Movie

```http
  GET /api/movie/${id}
```

| Parameter | Type     | Description               |
| :-------- | :------- | :------------------------ |
| `id`      | `string` | **Required**. Id of Movie |

### Update Specific Movie

```http
  POST /api/movie-update/${id}
```

| Parameter | Type     | Description               |
| :-------- | :------- | :------------------------ |
| `id`      | `string` | **Required**. Id of Movie |

### Create a New Movie

```http
  PUT /api/movie-create/
```

### Delete a Movie along with its Movie Reviews

```http
  DELETE /api/movie-delete/${id}
```

| Parameter | Type     | Description               |
| :-------- | :------- | :------------------------ |
| `id`      | `string` | **Required**. Id of Movie |

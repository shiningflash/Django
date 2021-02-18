# Django REST-Framework

## CRUD

* Create / Insert / Add - `POST`
* Retrive / Fetch - `GET`
* Update / Modify / Edit - `PUT`
* Delete / Remove - `Delete`

-----------

#### GET: http://127.0.0.1:8000/student/

GET /student/

```json
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "student_id": "20241035",
        "fullname": "HASAN JAYED",
        "cgpa": 3.89,
        "contact_no": "01543125678"
    },
    {
        "id": 2,
        "student_id": "17986745",
        "fullname": "HASIB IQBAL",
        "cgpa": 3.21,
        "contact_no": "01345678234"
    }
]
```

----------

#### POST: http://127.0.0.1:8000/student/

POST /student/

```json
{
    "id": 2,
    "student_id": "17986745",
    "fullname": "HASIB IQBAL",
    "cgpa": 3.21,
    "contact_no": "01345678234"
}
```

Then,

```json
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 2,
    "student_id": "17986745",
    "fullname": "HASIB IQBAL",
    "cgpa": 3.21,
    "contact_no": "01345678234"
}
```

-----------

#### GET: http://127.0.0.1:8000/student/2

GET /student/2

```json
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 2,
    "student_id": "17986745",
    "fullname": "HASIB IQBAL",
    "cgpa": 3.21,
    "contact_no": "01345678234"
}
```

--------------

#### PUT: http://127.0.0.1:8000/student/2/

PUT /student/2

```json
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 2,
    "student_id": "18975642",
    "fullname": "HABIB IQBAL",
    "cgpa": 3.21,
    "contact_no": "01345678234"
}
```
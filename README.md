# FastAPI CRUD Learning Project

A simple CRUD API built with **FastAPI** to practice backend fundamentals, REST principles, request validation, and state management.

This project simulates a lightweight service for managing items with status tracking, timestamps, and UUID-based identification.


## 🚀 Features
* Create items with auto-generated UUID
* Read all items
* Read item by ID
* Update item status
* Delete items
* Enum-based status validation
* Timezone-aware timestamps
* In-memory storage (for learning/demo purposes)


## 🧱 Tech Stack

* **FastAPI**
* **Pydantic**
* **Python 3.11**
* UUID for unique ID generation


## 📌 Data Model

Each item contains:

* `ug_id` (UUID)
* `response_text`
* `status` (Enum: Pending, Processing, Completed, Failed)
* `source`
* `tenant`
* `created_at`
* `updated_at`


## 📡 API Endpoints

### Create Item

```
POST /items
```

### Get All Items

```
GET /items
```

### Get Item by ID

```
GET /items/{ug_id}
```

### Update Item Status

```
PUT /items/{ug_id}/status
```

### Delete Item

```
DELETE /items/{ug_id}
```



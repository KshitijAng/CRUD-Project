# FastAPI CRUD Learning Project

A simple CRUD API built with **FastAPI** to practice backend fundamentals, REST principles, request validation, and layered architecture.

This project simulates a lightweight service for managing items with status tracking, timestamps, and UUID-based identification.


## 🚀 Features

* Create items with auto-generated UUID
* Read all items
* Read item by ID
* Update item status (partial update)
* Delete items
* Enum-based validation for status, source, and tenant
* Timezone-aware timestamps
* SQLite persistence (`crud.db`)
* Health check endpoint
* Request logging middleware


## 🧱 Tech Stack

* **FastAPI**
* **Pydantic** (DTOs in `dtos/`)
* **SQLAlchemy** (ORM, SQLite)
* **Python 3.11**
* UUID for unique ID generation


## 📁 Project Structure

* **Routers** — Route definitions and `get_db` dependency
* **Controllers** — HTTP handling (e.g. 404) and service calls
* **Services** — Business logic and DB access
* **Repositories** — DB engine, session, and models (`Orm.py`, `models/item_model.py`)
* **DTOs** — Pydantic request/response models (`dtos/item.py`)
* **Utils** — Enums for status, source, tenant


## 📌 Data Model

Each item contains:

| Field           | Type     | Description                                                                 |
|-----------------|----------|-----------------------------------------------------------------------------|
| `ug_id`         | UUID     | Primary key, auto-generated                                                |
| `response_text` | string   | Optional                                                                    |
| `status`        | string   | Enum: Pending, Processing, Completed, Failed                               |
| `source`        | string   | Enum: CHAT, EMAIL, API                                                      |
| `tenant`        | string   | Enum: GMAIL, HIVERWEB, OMNI                                                |
| `created_at`    | datetime | Set on create                                                              |
| `updated_at`    | datetime | Set on create and update                                                   |


## 📡 API Endpoints

| Method | Endpoint          | Description        |
|--------|-------------------|--------------------|
| GET    | `/`               | Health check       |
| POST   | `/items/`         | Create item        |
| GET    | `/items/`         | Get all items      |
| GET    | `/items/{ug_id}`  | Get item by ID     |
| PATCH  | `/items/{ug_id}`  | Update item status |
| DELETE | `/items/{ug_id}`  | Delete item        |

### Create Item

```
POST /items/
```

**Body (JSON):** `response_text` (optional), `status`, `source`, `tenant` (see enums above).

### Get All Items

```
GET /items/
```

### Get Item by ID

```
GET /items/{ug_id}
```

### Update Item Status

```
PATCH /items/{ug_id}
```

**Body (JSON):** `{"status": "Pending" | "Processing" | "Completed" | "Failed"}`

(Uses PATCH for partial update; only status is updated.)

### Delete Item

```
DELETE /items/{ug_id}
```

Returns `204 No Content` on success, `404` if not found.


## 🏃 Run the Project

```bash
uvicorn main:app --reload
```

API docs: **http://127.0.0.1:8000/docs**

# Flask Task Manager API

A simple RESTful API for managing to‑do tasks, built with Flask and SQLAlchemy, backed by a local SQLite database.

## Features

* Create, read, update, and delete tasks
* JSON-based API
* Automatic database initialization

## Tech Stack

* Python 3.x
* Flask (2.2.2)
* SQLAlchemy (2.0.x)
* SQLite (local file `tasks.db`)

## Project Structure

```
.
├── app.py             # Application factory & entry point
├── database.py        # DB engine, session setup & init_db()
├── models.py          # SQLAlchemy models (Task)
├── routes.py          # Flask Blueprint with CRUD endpoints
├── services.py        # Business‑logic layer & ORM calls
├── requirements.txt   # Python dependencies
└── test_routes.py     # Pytest suite for API endpoints
```

> **Note:** `tasks.db` is created automatically on first run via `init_db()` in `routes.py`.

## Prerequisites

* **Git**

  * Ubuntu/Debian: `sudo apt-get update && sudo apt-get install git`
  * macOS (Homebrew): `brew install git`
  * Windows: [Download Git](https://git-scm.com/download/win)

## Installation

1. **Clone the repo**

   ```bash
  git clone https://github.com/binarynectar/task-manager.git
  cd task-manager
   ```

2. **Create & activate a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

```bash
python app.py
```

* By default, the app runs in debug mode on `http://127.0.0.1:5000`
* The SQLite file `tasks.db` will be created in the project root

## API Endpoints

All endpoints accept and return JSON.

| Method | Endpoint          | Description                           | Request Body                                      | Response                       |
| ------ | ----------------- | ------------------------------------- | ------------------------------------------------- | ------------------------------ |
| GET    | `/tasks`          | List all tasks                        | *None*                                            | `[{id, title, completed}, …]`  |
| GET    | `/tasks/<int:id>` | Retrieve a single task                | *None*                                            | `{id, title, completed}`       |
| POST   | `/tasks`          | Create a new task                     | `{ \"title\": string, \"completed\"?: boolean }`  | `{id, title, completed}` (201) |
| PUT    | `/tasks/<int:id>` | Update title and/or completion status | `{ \"title\"?: string, \"completed\"?: boolean }` | `{id, title, completed}`       |
| DELETE | `/tasks/<int:id>` | Delete a task                         | *None*                                            | *Empty body* (204)             |

### Examples

* **Create**

  ```bash
  curl -X POST http://127.0.0.1:5000/tasks \
       -H \"Content-Type: application/json\" \
       -d '{\"title\":\"Buy milk\"}'
  ```

* **Update**

  ```bash
  curl -X PUT http://127.0.0.1:5000/tasks/1 \
       -H \"Content-Type: application/json\" \
       -d '{\"completed\":true}'
  ```

* **Delete**

  ```bash
  curl -X DELETE http://127.0.0.1:5000/tasks/1
  ```

## Testing

This project uses **pytest** to validate all CRUD operations:

```bash
pytest test_routes.py
```

Tests automatically recreate the database schema for isolation.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/foo`)
3. Commit your changes (`git commit -am 'Add foo'`)
4. Push to the branch (`git push origin feature/foo`)
5. Open a Pull Request

## License

This project is released under the MIT License.

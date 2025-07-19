# Flask Task Manager

A combined Flask API and built‑in web UI for creating, reading, updating, and deleting to‑do tasks.

## Features

- **REST API** for tasks (`/tasks`): create, list, view, update, delete.
- **Web UI** served at `/`: add, edit, complete, and remove tasks with a modern Bootstrap design.
- **Single origin**—no CORS required: back end and front end run together.
- **SQLite** persistence in `tasks.db`, auto‑initialized on first launch.

## Tech Stack

- Python 3.x  
- Flask (2.2.2)  
- SQLAlchemy (2.0.x)  
- SQLite  
- Bootstrap 5 + Bootstrap Icons (front‑end)

## Project Structure

```
.
├── app.py             # Entry point: configures Flask, serves static UI, registers routes
├── database.py        # DB engine, session setup & init_db()
├── models.py          # SQLAlchemy Task model
├── routes.py          # Blueprint: API endpoints (GET/POST/PUT/DELETE /tasks)
├── services.py        # TaskService: business logic & ORM calls
├── static/            # Front‑end assets
│   └── index.html     # Single‑page UI, interacts with API
├── requirements.txt   # Python dependencies
└── test_routes.py     # Pytest suite for API endpoints
```

> **Note:** `tasks.db` is created automatically via `init_db()` when you start the app.

## Prerequisites

- **Git** (for cloning & updates)
  - Ubuntu/Debian: `sudo apt-get update && sudo apt-get install git`
  - macOS (Homebrew): `brew install git`
  - Windows: [Download Git](https://git-scm.com/download/win)
- **Python 3.8+**

## Setup & Git Commands

```bash
# Clone the repo (first time)
git clone git@github.com:<your-username>/task-manager.git
cd task-manager

# Pull latest changes
git pull origin main

# (Optional) Virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt
```

## Running Locally

```bash
python app.py
```

- Opens server on **http://127.0.0.1:5000/**
- API at `/tasks`  
- UI at `/` (renders `static/index.html`)

## Web UI Usage

1. Navigate to **http://127.0.0.1:5000/** in your browser.  
2. Add a new task via the input field and **+** button.  
3. Toggle a task’s completion with the checkbox.  
4. Edit a task title with the **✏️ Edit** button.  
5. Remove a task with the **🗑️ Delete** button.

## API Endpoints

All endpoints accept and return JSON.

| Method | Endpoint          | Description                           | Request Body                                   | Response                         |
| ------ | ----------------- | ------------------------------------- | ---------------------------------------------- | -------------------------------- |
| GET    | `/tasks`          | List all tasks                        | _None_                                         | `[{id, title, completed}, …]`    |
| GET    | `/tasks/<id>`     | Retrieve a single task                | _None_                                         | `{id, title, completed}`         |
| POST   | `/tasks`          | Create a new task                     | `{"title": string}`                            | `{id, title, completed}` (201)   |
| PUT    | `/tasks/<id>`     | Update title and/or completion status | `{"title"?: string, "completed"?: boolean}`    | `{id, title, completed}`         |
| DELETE | `/tasks/<id>`     | Delete a task                         | _None_                                         | _Empty body_ (204)               |

### Example cURL

```bash
# Create
echo '{"title":"Buy milk"}' \
  | curl -X POST http://127.0.0.1:5000/tasks \
         -H "Content-Type: application/json" \
         -d @-

# Update
echo '{"completed":true}' \
  | curl -X PUT http://127.0.0.1:5000/tasks/1 \
         -H "Content-Type: application/json" \
         -d @-

# Delete
curl -X DELETE http://127.0.0.1:5000/tasks/1
```

## Testing

Run the Pytest suite to verify API functionality:

```bash
pytest test_routes.py
```

## Contributing

1. Fork the repo  
2. Create a feature branch: `git checkout -b feature/foo`  
3. Commit: `git commit -m 'Add foo'`  
4. Push: `git push origin feature/foo`  
5. Open a Pull Request

## License

Released under the MIT License.

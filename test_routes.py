import pytest
from app import create_app
from database import init_db, engine
from models import Base

@pytest.fixture(autouse=True)
def client():
    # Recreate schema for each test run
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_and_get_task(client):
    # Create
    res = client.post('/tasks', json={'title': 'Test Task'})
    assert res.status_code == 201
    data = res.get_json()
    assert data['title'] == 'Test Task'
    # Read back
    res2 = client.get(f"/tasks/{data['id']}")
    assert res2.status_code == 200
    assert res2.get_json() == data

def test_update_task(client):
    res = client.post('/tasks', json={'title': 'Old'})
    task = res.get_json()
    res2 = client.put(f"/tasks/{task['id']}", json={'title': 'New', 'completed': True})
    assert res2.status_code == 200
    updated = res2.get_json()
    assert updated['title'] == 'New'
    assert updated['completed'] == True

def test_delete_task(client):
    res = client.post('/tasks', json={'title': 'ToDelete'})
    task = res.get_json()
    res2 = client.delete(f"/tasks/{task['id']}")
    assert res2.status_code == 204
    # Ensure it’s gone
    res3 = client.get(f"/tasks/{task['id']}")
    assert res3.status_code == 404

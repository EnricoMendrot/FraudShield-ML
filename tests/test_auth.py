def test_register_new_user(client):
    """
    
    """
    payload = {
        "username": "tester",
        "email": "tester@example.com",
        "password": "pwd123password",
        "is_active": True,
        "is_admin": False
    }

    response = client.post("/auth/register", json=payload)
    
    assert response.status_code == 200
    assert response.json() == {"message": "Registration successful tester."}


def test_register_duplicate_email(client):
    """
    
    """
    payload = {
        "username": "tester2",
        "email": "tester@example.com",
        "password": "pwd123password",
        "is_active": True,
        "is_admin": False
    }

    response = client.post("/auth/register", json=payload)
    
    assert response.status_code == 400
    assert response.json()["detail"] == "User already exists."

def test_login_simple(client):
    """
    
    """
    response = client.post("/auth/login")
    assert response.status_code == 200
    assert response.json() == {"message": "Login successful."}
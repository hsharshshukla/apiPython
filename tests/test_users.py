import pytest
from app import schemas
from jose import jwt
from app.config import settings


def test_root(client):
    res = client.get("/")
    assert res.json().get('message') == 'Home Page'
    assert res.status_code == 200

def test_create_user(client):
    res = client.post("/users/", json={"email":"harsh@gmail.com", "password": "password"})    
    new_user = schemas.UserOut(**res.json())

    assert new_user.email == "harsh@gmail.com"
    assert res.status_code == 201

def test_login_user(client,test_user):
    res = client.post("/login",data={"username":test_user['email'],"password":test_user['password']})
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=settings.algorithm)
    id: str = payload.get("user_id")

    assert id == test_user['id']
    assert login_res.token_type == 'bearer'
    assert res.status_code ==200

@pytest.mark.parametrize("email,password,status_code",[
    ('h@gmail.com','password',403),
    ('harsh@gmail.com','password1',403),
    ('h@gmail.com',None,422)
])
def test_incorrect_login(client,test_user,email,password,status_code):
    res = client.post("/login",data={"username":email,"password":password})
    assert res.status_code == status_code
    # assert res.json().get('detail') == 'Invalid Credentials'  # this doesnt apply on 422

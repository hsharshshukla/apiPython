import pytest
from typing import List
from app import schemas


# def test_get_all_posts(authorized_client,test_posts):
#     res = authorized_client.get("/posts/")
#     # print(res.json())
    
#     def validate(post):
#         return schemas.PostOut(**post)

#     posts_map = map(validate,res.json())
#     # print(list(posts_map))
#     posts_list = list(posts_map)
#     assert len(res.json()) ==len(test_posts)
#     assert res.status_code ==200

# def test_unauthorized_get_all_posts(client,test_posts):
#     res = client.get("/posts/")

#     assert res.status_code == 401


# def test_unauthorized_get_one_post(client,test_posts):
#     res = client.get(f"/posts/{test_posts[0].id}")

#     assert res.status_code == 401

# def test_get_one_post_does_not_exist(authorized_client,test_posts):
#     res = authorized_client.get(f"/posts/99999999999999999999")

#     assert res.status_code == 404

# def test_get_one_post(authorized_client,test_posts):
#     res = authorized_client.get(f"/posts/{test_posts[0].id}")
#     post = schemas.PostOut(**res.json())

#     assert post.Post.id == test_posts[0].id
#     assert post.Post.content == test_posts[0].content

# @pytest.mark.parametrize("title,content,published",[
#     ("awesome new title","new content",True),
#     ("aachar","poodi",True),
#     ("karlo","party",False),
# ])
# def test_create_post(authorized_client,test_user,title,content,published):
#     res = authorized_client.post("/posts/",json={"title":title,"content":content,"published":published})
#     created_post = schemas.Post(**res.json())

#     assert res.status_code ==201
#     assert created_post.title == title
#     assert created_post.content == content
#     assert created_post.published == published
#     assert created_post.owner_id == test_user['id']

# def test_create_post_default_published_true(authorized_client,test_user,test_posts):
#     res = authorized_client.post("/posts/",json={"title":"First title","content":"content lajdlj"})
#     created_post = schemas.Post(**res.json())

#     assert res.status_code ==201
#     assert created_post.title == "First title"
#     assert created_post.content == "content lajdlj"
#     assert created_post.published == True
#     assert created_post.owner_id == test_user['id']

# def test_unauthorized_user_create_post(client,test_user,test_posts):
#     res = client.post("/posts/",json={"title":"First title","content":"content lajdlj"})

#     assert res.status_code == 401

# def test_unauthorized_user_delete_post(client,test_user,test_posts):
#     res = client.delete(f"/posts/{test_posts[0].id}")
#     assert res.status_code == 401


# def test_delete_post_success(authorized_client,test_user,test_posts):
#     res = authorized_client.delete(f"/posts/{test_posts[0].id}")
#     assert res.status_code == 204

# def test_delete_post_non_exist(authorized_client,test_user,test_posts):
#     res = authorized_client.delete("/posts/909090990")
#     assert res.status_code == 404

# def test_delete_other_user_post(authorized_client,test_user,test_posts):
#     res = authorized_client.delete(f"/posts/{test_posts[2].id}")

#     assert res.status_code ==403

def test_update_post(authorized_client,test_user,test_posts):
    data = {
        "title":"updated title",
        "content":"updated content",
        "id":test_posts[0].id
    }

    res = authorized_client.put(f"/posts/{test_posts[0].id}",json=data)
    updated_post = schemas.Post(**res.json())
    
    assert res.status_code ==200
    assert updated_post.title ==data['title']
    assert updated_post.content ==data['content']

def test_update_other_user_post(authorized_client,test_user,test_user2,test_posts):
    data = {
        "title":"updated ",
        "content":"updated ",
        "id":test_posts[2].id
    }
    
    res = authorized_client.put(f"/posts/{test_posts[2].id}",json=data)
    assert res.status_code == 403
    
def test_unauthorized_user_update_post(client,test_user,test_posts):
    res = client.put(f"/posts/{test_posts[0].id}")

    assert res.status_code ==401

def test_unauthorized_user_update_post_not_exist(authorized_client,test_user,test_posts):
    data = {
        "title":"updated ",
        "content":"updated ",
        "id":test_posts[2].id
    }    
    res = authorized_client.put(f"/posts/8000000",json=data)

    assert res.status_code ==404
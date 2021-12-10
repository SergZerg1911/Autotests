import requests


def test_get():
    response = requests.get('https://reqres.in/api/users?page=2')
    assert response.status_code == 200


def test_get_users():
    response = requests.get('https://reqres.in/api/users?page=2')
    assert response.text == '{"page":2,"per_page":6,"total":12,"total_pages":2,"data":[{"id":7,' \
                            '"email":"michael.lawson@reqres.in","first_name":"Michael","last_name":"Lawson",' \
                            '"avatar":"https://reqres.in/img/faces/7-image.jpg"},{"id":8,' \
                            '"email":"lindsay.ferguson@reqres.in","first_name":"Lindsay","last_name":"Ferguson",' \
                            '"avatar":"https://reqres.in/img/faces/8-image.jpg"},{"id":9,' \
                            '"email":"tobias.funke@reqres.in","first_name":"Tobias","last_name":"Funke",' \
                            '"avatar":"https://reqres.in/img/faces/9-image.jpg"},{"id":10,' \
                            '"email":"byron.fields@reqres.in","first_name":"Byron","last_name":"Fields",' \
                            '"avatar":"https://reqres.in/img/faces/10-image.jpg"},{"id":11,' \
                            '"email":"george.edwards@reqres.in","first_name":"George","last_name":"Edwards",' \
                            '"avatar":"https://reqres.in/img/faces/11-image.jpg"},{"id":12,' \
                            '"email":"rachel.howell@reqres.in","first_name":"Rachel","last_name":"Howell",' \
                            '"avatar":"https://reqres.in/img/faces/12-image.jpg"}],"support":{' \
                            '"url":"https://reqres.in/#support-heading","text":"To keep ReqRes free, contributions ' \
                            'towards server costs are appreciated!"}}'


def test_post_new_user():
    info = {"name": "morpheus", "job": "leader"}
    response = requests.post('https://reqres.in/api/users', params=info)
    assert response.text == '{"name": "morpheus","job": "leader","id": "294","createdAt": "2021-12-09T04:47:47.558Z"}'

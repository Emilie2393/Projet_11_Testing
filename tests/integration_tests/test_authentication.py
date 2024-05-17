from tests.conftest import client, users

def test_login_route(client, users):

    # login page access and club points list displayed tested
    response = client.get('/')
    assert response.status_code == 200
    assert 'Club name' in response.data.decode()

    # home page access through email checking
    response = client.post('/showSummary', data={'email': users[0]['email'][0]})
    assert response.status_code == 200
    assert "Welcome" in response.data.decode()
    

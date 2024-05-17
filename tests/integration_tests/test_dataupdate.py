from tests.conftest import client, competitions

def test_data_updated_after_purchase(client, competitions):

    # booking 10 places when the club have 13 points : points are updated
    response = client.post('/purchasePlaces', data={"club": competitions[0]["club"], "competition": competitions[0]["competition"], "places": competitions[0]["places"]})
    assert response.status_code == 200
    assert 'Points available: 3' in response.data.decode()

    # back on login page : points are also updated
    response = client.get('/')
    assert response.status_code == 200
    assert 'Points : 3' in response.data.decode() 
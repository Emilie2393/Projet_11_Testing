from tests.conftest import client, competitions

def test_purchaseplaces_url(client, competitions):

    # booking 15 places when the club don't have enough points
    response = client.post('/purchasePlaces', data={"club":competitions[0]['club'], "competition": competitions[0]['competition'], "places": competitions[0]['places'][1]})
    assert "You don't have enough points" in response.data.decode()
    assert response.status_code == 400

    # booking 13 places when the club have enough points
    response = client.post('/purchasePlaces', data={"club":competitions[0]['club'], "competition": competitions[0]['competition'], "places": competitions[0]['places'][2]})
    assert "You can't book more than 12 places per competition" in response.data.decode()
    assert response.status_code == 400

    # booking 10 places when the club have enough points
    response = client.post('/purchasePlaces', data={"club":competitions[0]['club'], "competition": competitions[0]['competition'], "places": competitions[0]['places'][0]})
    assert "Great-booking complete" in response.data.decode()
    assert response.status_code == 200

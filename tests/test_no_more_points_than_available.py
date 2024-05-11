from tests.conftest import client

class TestPointsNumberAvailable:

    def test_booking_10_places(self, client, competitions):
      response = client.post('/purchasePlaces', data={"club":competitions[0]['club'], "competition": competitions[0]['competition'], "places": competitions[0]['places'][0]})
      assert "Great-booking complete" in response.data.decode()
      assert response.status_code == 200

    def test_booking_15_places(self, client, competitions):
      response = client.post('/purchasePlaces', data={"club":competitions[0]['club'], "competition": competitions[0]['competition'], "places": competitions[0]['places'][1]})
      assert "You don't have enough points" in response.data.decode()
      assert response.status_code == 400

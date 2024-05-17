from tests.conftest import client, competitions

class TestPlacesNumber:

	def test_booking_10_places(self, client, competitions):
		response = client.post('/purchasePlaces', data={"club":competitions[0]['club'], "competition": competitions[0]['competition'], "places": competitions[0]['places'][0]})
		assert response.status_code == 200
	
	def test_booking_13_places(self, client, competitions):
		response = client.post('/purchasePlaces', data={"club":competitions[0]['club'], "competition": competitions[0]['competition'], "places": competitions[0]['places'][1]})
		assert response.status_code == 400


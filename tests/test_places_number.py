from tests.conftest import client, competitions

class TestPlacesNumber:
	""" Test for booking less than 12 places """

	def test_booking_10_places(self, client, competitions):
		""" Test for booking 10 places for a club with 13 points
		Args:
		 	client (func): client returned in contest file to simulate the app
			competitions (list): data simulation
		"""
		response = client.post('/purchasePlaces', data={"club":competitions[0]['club'], "competition": competitions[0]['competition'], "places": competitions[0]['places'][0]})
		assert response.status_code == 200
	
	def test_booking_13_places(self, client, competitions):
		""" Test for booking 13 places for a club with 13 places
		Args:
		 	client (func): client returned in contest file to simulate the app
			competitions (list): data simulation
		"""
		response = client.post('/purchasePlaces', data={"club":competitions[0]['club'], "competition": competitions[0]['competition'], "places": competitions[0]['places'][2]})
		assert "You can't book more than 12 places per competition" in response.data.decode()
		assert response.status_code == 400


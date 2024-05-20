from tests.conftest import client, competitions

class TestClubPointsUpdate:
	""" Test if club points are correctly deducted """

	def test_points_correctly_deducted(self, client, competitions):
		""" Test to deducte 10 points for a club with 13 points and to find 3 points available in the http response
		Args:
			client (func): client returned in contest file to simulate the app
			competitions (list): data simulation
		"""
		response = client.post('/purchasePlaces', data={"club": competitions[0]["club"], "competition": competitions[0]["competition"], "places": competitions[0]["places"]})
		assert response.status_code == 200
		assert 'Points available: 3' in response.data.decode()


	def test_points_not_deducted(self, client, competitions):
		""" Test to deducte 10 points for a club with 13 points and not find 13 points available in the http response
		Args:
			client (func): client returned in contest file to simulate the app
			competitions (list): data simulation
		"""
		response = client.post('/purchasePlaces', data={"club":competitions[0]["club"], "competition": competitions[0]["competition"], "places": competitions[0]["places"]})
		assert 'Points available: 13' not in response.data.decode()

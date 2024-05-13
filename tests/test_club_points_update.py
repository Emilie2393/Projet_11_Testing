from tests.conftest import client, competitions

class TestClubPointsUpdate:

	def test_points_correctly_deducted(self, client, competitions):
		response = client.post('/purchasePlaces', data={"club": competitions[0]["club"], "competition": competitions[0]["competition"], "places": competitions[0]["places"]})
		assert response.status_code == 200
		assert 'Points available: 3' in response.data.decode()


	def test_points_not_deducted(self, client, competitions):
		response = client.post('/purchasePlaces', data={"club":competitions[0]["club"], "competition": competitions[0]["competition"], "places": competitions[0]["places"]})
		assert 'Points available: 13' not in response.data.decode()

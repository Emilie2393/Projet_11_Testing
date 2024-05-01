from tests.conftest import client

class TestClubPointsUpdate:
	club = "Simply Lift"
	competition = "Spring Festival"
	places = "10"

	def test_should_status_code_ok(self, client):
		response = client.post('/purchasePlaces', data={"club":self.club, "competition": self.competition, "places": self.places})
		assert response.status_code == 200
		assert 'Points available: 3' in response.data.decode()


	def test_previous_result(self, client):
		response = client.post('/purchasePlaces', data={"club":self.club, "competition": self.competition, "places": self.places})
		assert 'Points available: 13' not in response.data.decode()

from tests.conftest import client

class TestBookingPlaces:
	club = "Simply Lift"
	competition = "Spring Festival"
	places = "10"

	def test_should_status_code_ok(self, client):
		response = client.post('/purchasePlaces', data={"club":self.club, "competition": self.competition, "places": self.places})
		assert response.status_code == 200
		assert 'Points available: 3' in response.data.decode()

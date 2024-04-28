from tests.conftest import client

class TestPlacesNumber:

	def test_should_status_code_ok(self, client):
		club = "Simply Lift"
		competition = "Spring Festival"
		places = "10"
		response = client.post('/purchasePlaces', data={"club":club, "competition": competition, "places": places})
		assert response.status_code == 200


from tests.conftest import client

class TestClubPointsDiplayed:

	def test_club_points_displayed(self, client):
		response = client.get('/')
		assert response.status_code == 200
		assert 'Club name' in response.data.decode() 

from tests.conftest import client

class TestClubPointsDiplayed:
	""" Test for club points diplayed checking in home page """

	def test_club_points_displayed(self, client):
		""" Check for getting home page and if 'Club name' is displayed in home page
		Args:
		 	client (func): client returned in contest file to simulate the app
		"""
		response = client.get('/')
		assert response.status_code == 200
		assert 'Club name' in response.data.decode() 

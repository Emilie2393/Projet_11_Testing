from tests.conftest import client

class TestPointsDiplayBoard:

	def test_should_status_code_ok(self, client):
		response = client.get('/')
		assert response.status_code == 200
		assert 'Club name' in response.data.decode() 

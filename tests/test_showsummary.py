from tests.conftest import client, users

class TestUnknownEmail:

	def test_correct_email(self, client, users):
		response = client.post('/showSummary', data={'email': users[0]['email'][0]})
		assert "Welcome" in response.data.decode()
		assert response.status_code == 200

	def test_wrong_email(self, client, users):
		response = client.post('/showSummary', data={'email': users[0]['email'][1]})
		assert "Sorry, that email wasn't found" in response.data.decode()
		assert response.status_code == 404
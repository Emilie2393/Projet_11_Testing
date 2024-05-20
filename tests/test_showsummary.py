from tests.conftest import client, users

class TestUnknownEmail:
	""" Test if the email adress is correct to access home page """

	def test_correct_email(self, client, users):
		""" Test for a database correct email
		Args:
			client (func): client returned in contest file to simulate the app
			users (list): data simulation for users email
		"""
		response = client.post('/showSummary', data={'email': users[0]['email'][0]})
		assert "Welcome" in response.data.decode()
		assert response.status_code == 200

	def test_wrong_email(self, client, users):
		""" Test for a database wrong email
		Args:
			client (func): client returned in contest file to simulate the app
			users (list): data simulation for users email
		"""
		response = client.post('/showSummary', data={'email': users[0]['email'][1]})
		assert "Sorry, that email wasn't found" in response.data.decode()
		assert response.status_code == 404
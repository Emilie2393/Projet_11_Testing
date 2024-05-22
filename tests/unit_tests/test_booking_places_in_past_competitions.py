from tests.conftest import client

class TestBookingDates:
	""" Test if postdated competitions are not bookable """

	def test_past_date_not_available(self, client):
		""" Test for a database past date and if 'no longer available' is in the http response
		Args:
			client (func): client returned in contest file to simulate the app
		"""
		response = client.get('/book/Fall%20Classic/Simply%20Lift')
		assert "no longer available" in response.data.decode()
		assert response.status_code == 400
	
	def test_future_date_available(self, client):
		""" Test for a database future date and if 'Places available' is in the http response
		Args:
			client (func): client returned in contest file to simulate the app
		"""
		response = client.get('/book/Spring%20Festival/Simply%20Lift')
		assert "Places available" in response.data.decode()
		assert response.status_code == 200

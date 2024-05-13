from tests.conftest import client

class TestBookingDates:

	def test_past_date_not_available(self, client):
		response = client.get('/book/Fall%20Classic/Simply%20Lift')
		assert "no longer available" in response.data.decode()
		assert response.status_code == 400
	
	def test_future_date_available(self, client):
		response = client.get('/book/Spring%20Festival/Simply%20Lift')
		assert "Places available" in response.data.decode()
		assert response.status_code == 200

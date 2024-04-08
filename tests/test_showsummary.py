from tests.conftest import client


def test_should_status_code_ok(client):
	data = {'email': 'john@simplylift.co'}
	response = client.post('/showSummary', data=data)
	assert response.status_code == 200
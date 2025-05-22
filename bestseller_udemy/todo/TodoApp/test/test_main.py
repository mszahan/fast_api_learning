from fastapi.testclient import TestClient
from fastapi import status
# The sys.path modification is now handled by conftest.py
import main

client = TestClient(main.app)

def test_health_check():
    response = client.get('/healthy') # Corrected typo
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'status':'Healthy'}
import requests
from app import app

def test_case():
  req = app.test_client()
  response=req.get('/')
  assert response.status_code == 200

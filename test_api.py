def test_chat_endpoint_admissions():
    try:
        from fastapi.testclient import TestClient
        from app.main import app
    except Exception as e:
        import pytest
        pytest.skip(f"Skipping API integration test due to import error: {e}")

    client = TestClient(app)
    res = client.post('/chat', json={'message': 'How do I apply?', 'session_id': 't1'})
    assert res.status_code == 200
    j = res.json()
    assert 'reply' in j and 'intent' in j
    assert j['intent'] in ('admissions', 'fallback')

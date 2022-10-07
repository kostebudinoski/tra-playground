from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)
   

def test_post_rating_valid_data():
    
    response = client.post(
        '/rating/', 
        json={
            "scale": "EXCELLENT",
            "original_text": "Hello, how are you?",
            "translated_text": "Ciao, come stai?",
            "source_language": "en",
            "target_language": "it"
        }
    )

    assert response.status_code == 204

def test_post_rating_invalid_rating_scale():
    
    response = client.post(
        '/rating/', 
        json={
            "scale": "UNKNOWN",
            "original_text": "Hello, how are you?",
            "translated_text": "Ciao, come stai?",
            "source_language": "en",
            "target_language": "it"
        }
    )

    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": [
                    "body",
                    "scale"
                ],
                "msg": "value is not a valid enumeration member; permitted: 'UNACCEPTABLE', 'WEAK', 'GOOD', 'VERYGOOD', 'EXCELLENT'",
                "type": "type_error.enum",
                "ctx": {
                    "enum_values": [
                        "UNACCEPTABLE",
                        "WEAK",
                        "GOOD",
                        "VERYGOOD",
                        "EXCELLENT"
                    ]
                }
            }
        ]
    }
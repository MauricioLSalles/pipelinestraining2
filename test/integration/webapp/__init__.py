import os
import pytest

@pytest.fixture(scope="session")
def base_url():
    #return os.getenv("API_BASE_URL", "http://localhost:5000")    
    return os.getenv("API_BASE_URL", "http://172.18.0.1:5000")
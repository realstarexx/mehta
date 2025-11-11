import pytest
import sys
import os

# Add source to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

@pytest.fixture
def bot_instance():
    from mehta import telegram
    return telegram()

@pytest.fixture
def mock_message():
    class MockMessage:
        def __init__(self, text="", chat_id=123, message_id=1):
            self.text = text
            self.chat = type('Chat', (), {'id': chat_id})()
            self.message_id = message_id
            self.from_user = type('User', (), {'id': 456})()
    return MockMessage

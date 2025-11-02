
### Install
```bash
pip install mehta
```

```python
from mehta import telegram

bot = telegram()

@bot.commands(['start'])
def start(message):
    return "Hello! Bot started."

@bot.commands(['photo'])
def photo(message):
    return {'type': 'photo', 'url': 'image.jpg'}

@bot.message()
def echo(message):
    return f"You said: {message.text}"

bot.run("TOKEN")
```

### CLI
```bash
mehta run:<filename> # mehta run:app (.py)
```
### Response Types
```python
# Text - Simple text message
return "Hello World"
return f"Welcome {message.from_user.first_name}"
```

```python
# Photo - Send image from URL or local file
return {
    'type': 'photo',
    'url': 'https://picsum.photos/400/300',  # URL
    'url': 'local_image.jpg',                # Local file
    'caption': 'Optional caption text'       # Optional
}
```

```python
# Video - Send video file
return {
    'type': 'video',
    'url': 'video.mp4',                      # Local file or URL
    'caption': 'Video description'           # Optional
}
```

```python
# Audio - Send audio file
return {
    'type': 'audio',
    'url': 'audio.mp3',                      # Local file or URL  
    'caption': 'Audio title'                 # Optional
}
```

```python
# Document - Send any file
return {
    'type': 'document',
    'url': 'document.pdf',                   # Local file or URL
    'caption': 'File description'            # Optional
}
```

```python
# Location - Send location coordinates
return {
    'type': 'location',
    'lat': 28.6139,                          # Latitude
    'lon': 77.2090                           # Longitude
}
```

```python
# Contact - Share contact information
return {
    'type': 'contact',
    'phone': '+1234567890',                  # Phone number
    'first_name': 'John',                    # First name
    'last_name': 'Doe'                       # Optional last name
}
```

```python
# Poll - Create a poll
return {
    'type': 'poll',
    'question': 'What is your favorite color?',  # Poll question
    'options': ['Red', 'Blue', 'Green']          # Answer options
}
```

```python
# Dice - Send dice animation
return {
    'type': 'dice'                           # Default dice emoji
}
```

```python
# Dice with Emoji - Different dice types
return {
    'type': 'dice',
    'emoji': '🎯'                            # 🎲, 🎯, 🏀, ⚽, 🎰, 🎳
}
```

```python
# Keyboard - Reply keyboard buttons
return {
    'type': 'keyboard',
    'text': 'Choose option:',                # Message text
    'buttons': [                             # Button layout
        ['Button 1', 'Button 2'],            # First row
        ['Button 3']                         # Second row
    ],
    'one_time': True                         # Optional: hide after use
}
```

```python
# Inline Keyboard - Inline buttons
return {
    'type': 'inline',
    'text': 'Select:',                       # Message text
    'buttons': [                             # Button layout
        [                                    # First row
            {'text': 'Website', 'url': 'https://google.com'},      # URL button
            {'text': 'Click', 'data': 'button_click'}              # Callback button
        ]
    ]
}
```

```python
# Remove Keyboard - Hide current keyboard
return {
    'type': 'remove_keyboard',
    'text': 'Keyboard removed'               # Message text
}
```

```python
# Force Reply - Force user to reply
return {
    'type': 'force_reply', 
    'text': 'Please reply'                   # Message text
}
```

```python
# Delete - Delete user's message
return {
    'type': 'delete'                         # No parameters needed
}
```

```python
# Edit - Edit bot's previous message  
return {
    'type': 'edit',
    'text': 'Message updated'                # New message text
}
```

```python
# Pin - Pin message in chat
return {
    'type': 'pin'                            # No parameters needed
}
```

```python
# Unpin - Unpin message from chat
return {
    'type': 'unpin'                          # No parameters needed
}
```

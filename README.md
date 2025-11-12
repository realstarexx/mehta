<h1 align="center">Mehta</h1>

<p align="center">
  <b>A beginner-friendly telegram sdk providing intuitive command decorators.</b><br>
  This package is a <b>wrapper</b> that uses 
  <a href="https://github.com/eternnoir/pyTelegramBotAPI">pyTeleBot</a> and 
  <a href="https://github.com/LonamiWebs/Telethon">Telethon</a> for Telegram-related features.<br>
  When you install it, all required dependencies including 
  <a href="https://github.com/eternnoir/pyTelegramBotAPI">pyTeleBot</a>, 
  <a href="https://github.com/LonamiWebs/Telethon">Telethon</a>, 
  and others are automatically installed to ensure full functionality and seamless integration.
</p>

<br>

<p align="center">
  <img src="https://img.shields.io/badge/version-1.1.5-blue?style=for-the-badge" alt="Version">
  <img src="https://img.shields.io/badge/python-3.6%2B-green?style=for-the-badge" alt="Python">
  <img src="https://img.shields.io/badge/license-MIT-yellow?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/created%20by-Starexx-purple?style=for-the-badge" alt="Created by Starexx">
</p>


## Installation
```bash
pip install mehta
```

## Basic Setup
```python
from mehta import telegram

bot = telegram()

@bot.commands(['start'])
def start(message):
    return "Hello! Bot started."

@bot.message()
def echo(message):
    return f"You said: {message.text}"

bot.run("YOUR_BOT_TOKEN")
```

## Decorators Reference

| Decorator       | Parameters                                | Use Case                             |
|-----------------|-------------------------------------------|--------------------------------------|
| `@bot.commands` | `commandlist`, `rate_limit=None`, `timeout=None` | Bind handler to Telegram commands    |
| `@bot.message`  | **None**                                  | Handles all non-command messages     |
| `@bot.callback` | **None**                                  | Handles callback queries (inlines)   |
| `@bot.error`    | **None**                                  | Handles errors for all handlers      |

**Example:**
```python
@bot.commands(['hi'], rate_limit=1, timeout=3)
def hi(message):
   return "Hi, rate limit 1/min, timeout 3s!"
```
- `command([""])`: list of `commands`
- `rate_limit`: int, calls/user/min
- `timeout`: int, seconds for auto-timeout

### Text and Media Messages

| Function | Parameters | Use Case |
|-----------|-------------|-----------|
| text | content, parse, receiver, reply_to, preview, notify | Send plain text |
| photo | file, caption, parse, receiver, reply_to, notify | Send image/photo |
| video | file, caption, parse, receiver, reply_to, notify | Send video |
| audio | file, caption, parse, receiver, reply_to, notify | Send audio |
| document | file, caption, parse, receiver, reply_to, notify | Send document |
| sticker | file, receiver, reply_to, notify | Send sticker |
| voice | file, caption, parse, receiver, reply_to, notify | Send voice message |
| animation | file, caption, parse, receiver, reply_to, notify | Send GIF/animation |
| mediagroup | media_list, receiver, reply_to, notify | Send multiple media items |


### Location and Interaction

| Function | Parameters | Use Case |
|-----------|-------------|-----------|
| location | lat, lon, receiver, reply_to, notify | Send location |
| venue | lat, lon, title, address, receiver, reply_to, notify | Send venue |
| contact | phone, first_name, last_name, receiver, reply_to, notify | Send contact |
| poll | question, options, receiver, reply_to, notify | Send Telegram poll |
| dice | emoji, receiver, reply_to, notify | Send dice animation |


### Message Management

| Function | Parameters | Use Case |
|-----------|-------------|-----------|
| delete | message_id, receiver | Delete a specific message |
| edit | message_id, text, parse, receiver, preview | Edit an existing text or caption |
| forward | to_chat, message_id, receiver, notify | Forward message to another chat |
| copy | to_chat, message_id, caption, parse, receiver, notify | Copy a message |
| pin | message_id, receiver, notify | Pin message in chat |
| unpin | message_id, receiver | Unpin one message |
| unpin_all | receiver | Unpin all messages |


### Chat Control and Moderation

| Function | Parameters | Use Case |
|-----------|-------------|-----------|
| ban | user_id, until_date, receiver | Ban a user |
| unban | user_id, receiver | Unban a user |
| restrict | user_id, permissions, until_date, receiver | Restrict user permissions |
| promote | user_id, privileges, receiver | Promote member with privileges |
| chat_info | receiver | Get chat information |
| member_count | receiver | Get total members |
| member_info | user_id, receiver | Get info about specific user |
| invite_link | receiver | Generate chat invite link |


### Chat Configuration

| Function | Parameters | Use Case |
|-----------|-------------|-----------|
| set_title | title, receiver | Set chat title |
| set_description | description, receiver | Set chat description |
| set_photo | file, receiver | Set chat photo |
| delete_photo | receiver | Delete chat photo |


### Inline and Keyboard Components

| Function | Parameters | Use Case |
|-----------|-------------|-----------|
| keyboard | text, buttons, parse, receiver, reply_to, preview, notify | Send reply keyboard |
| inline | text, buttons, parse, receiver, reply_to, preview, notify | Inline buttons with callback data |
| remove_keyboard | text, parse, receiver, reply_to, preview, notify | Hide keyboard |
| force_reply | text, parse, receiver, reply_to, preview, notify | Force user reply |
| edit_message | message_id, text, parse, receiver, preview, buttons, caption, reply_markup | Edit message with buttons |
| answer_callback | query_id, text, show_alert, url | Answer callback query (inline button) |

## Response Types
### Text Message
```python

return "Hello World"
return f"Welcome {message.from_user.first_name}"

return {
    'type': 'text',
    'text': 'Your message here',             # Required
    'parse': 'HTML',                         # Optional: 'HTML', 'Markdown', 'MarkdownV2'
    'receiver': message.chat.id,             # Optional: Chat ID (auto-filled)
    'reply_to': message.message_id,          # Optional: Reply to message ID (auto-filled)
    'preview': False,                        # Optional: Disable link preview (default: True)
    'notify': False                          # Optional: Send silently (default: True)
}
```

### Photo Message

```python
return {
    'type': 'photo',
    'file': 'https://picsum.photos/400/300', # Required: URL or local file path
    'file': 'local_image.jpg',               # Required: Local file path
    'caption': 'Photo caption',              # Optional: Caption text
    'parse': 'HTML',                         # Optional: Parse mode for caption
    'receiver': message.chat.id,             # Optional: Chat ID (auto-filled)
    'reply_to': message.message_id,          # Optional: Reply to message ID (auto-filled)
    'notify': False                          # Optional: Send silently (default: True)
}
```

### Video Message

```python
return {
    'type': 'video',
    'file': 'video.mp4',                     # Required: URL or local file path
    'caption': 'Video description',          # Optional: Caption text
    'parse': 'HTML',                         # Optional: Parse mode for caption
    'receiver': message.chat.id,             # Optional: Chat ID (auto-filled)
    'reply_to': message.message_id,          # Optional: Reply to message ID (auto-filled)
    'notify': False                          # Optional: Send silently (default: True)
}
```

### Audio Message

```python
return {
    'type': 'audio',
    'file': 'audio.mp3',                     # Required: URL or local file path
    'caption': 'Audio title',                # Optional: Caption text
    'parse': 'HTML',                         # Optional: Parse mode for caption
    'receiver': message.chat.id,             # Optional: Chat ID (auto-filled)
    'reply_to': message.message_id,          # Optional: Reply to message ID (auto-filled)
    'notify': False                          # Optional: Send silently (default: True)
}
```

### Document Message

```python
return {
    'type': 'document',
    'file': 'document.pdf',                  # Required: URL or local file path
    'caption': 'File description',           # Optional: Caption text
    'parse': 'HTML',                         # Optional: Parse mode for caption
    'receiver': message.chat.id,             # Optional: Chat ID (auto-filled)
    'reply_to': message.message_id,          # Optional: Reply to message ID (auto-filled)
    'notify': False                          # Optional: Send silently (default: True)
}
```

### Voice Message

```python
return {
    'type': 'voice',
    'file': 'voice.ogg',                     # Required: URL or local file path
    'caption': 'Voice note',                 # Optional: Caption text
    'parse': 'HTML',                         # Optional: Parse mode for caption
    'receiver': message.chat.id,             # Optional: Chat ID (auto-filled)
    'reply_to': message.message_id,          # Optional: Reply to message ID (auto-filled)
    'notify': False                          # Optional: Send silently (default: True)
}
```

### Sticker Message

```python
return {
    'type': 'sticker',
    'file': 'sticker.webp',                  # Required: URL or local file path
    'receiver': message.chat.id,             # Optional: Chat ID (auto-filled)
    'reply_to': message.message_id,          # Optional: Reply to message ID (auto-filled)
    'notify': False                          # Optional: Send silently (default: True)
}
```

### Animation (GIF) Message

```python
return {
    'type': 'animation',
    'file': 'animation.gif',                 # Required: URL or local file path
    'caption': 'GIF description',            # Optional: Caption text
    'parse': 'HTML',                         # Optional: Parse mode for caption
    'receiver': message.chat.id,             # Optional: Chat ID (auto-filled)
    'reply_to': message.message_id,          # Optional: Reply to message ID (auto-filled)
    'notify': False                          # Optional: Send silently (default: True)
}
```

### Location Message

```python
return {
    'type': 'location',
    'lat': 28.6139,                          # Required: Latitude
    'lon': 77.2090,                          # Required: Longitude
    'receiver': message.chat.id,             # Optional: Chat ID (auto-filled)
    'reply_to': message.message_id,          # Optional: Reply to message ID (auto-filled)
    'notify': False                          # Optional: Send silently (default: True)
}
```

### Venue Message

```python
return {
    'type': 'venue',
    'lat': 28.6139,                          # Required: Latitude
    'lon': 77.2090,                          # Required: Longitude
    'title': 'Venue Name',                   # Required: Venue title
    'address': 'Venue Address',              # Required: Venue address
    'receiver': message.chat.id,             # Optional: Chat ID (auto-filled)
    'reply_to': message.message_id,          # Optional: Reply to message ID (auto-filled)
    'notify': False                          # Optional: Send silently (default: True)
}
```

### Contact Message

```python
return {
    'type': 'contact',
    'phone': '+1234567890',                  # Required: Phone number
    'first_name': 'John',                    # Required: First name
    'last_name': 'Doe',                      # Optional: Last name
    'receiver': message.chat.id,             # Optional: Chat ID (auto-filled)
    'reply_to': message.message_id,          # Optional: Reply to message ID (auto-filled)
    'notify': False                          # Optional: Send silently (default: True)
}
```

### Poll Message

```python
return {
    'type': 'poll',
    'question': 'Favorite color?',           # Required: Poll question
    'options': ['Red', 'Blue', 'Green'],     # Required: Answer options (2-10)
    'receiver': message.chat.id,             # Optional: Chat ID (auto-filled)
    'reply_to': message.message_id,          # Optional: Reply to message ID (auto-filled)
    'notify': False                          # Optional: Send silently (default: True)
}
```

### Media Group (Multiple Photos/Videos)

```python
return {
    'type': 'mediagroup',
    'media': [                               # Required: List of media items
        {
            'type': 'photo',                 # Required: 'photo' or 'video'
            'file': 'photo1.jpg',            # Required: File path or URL
            'caption': 'First photo'         # Optional: Caption (only for last media)
        },
        {
            'type': 'video',
            'file': 'video1.mp4',
            'caption': 'First video'
        }
    ],
    'receiver': message.chat.id,             # Optional: Chat ID (auto-filled)
    'reply_to': message.message_id,          # Optional: Reply to message ID (auto-filled)
    'notify': False                          # Optional: Send silently (default: True)
}
```

### Reply Keyboard

```python
return {
    'type': 'keyboard',
    'text': 'Choose option:',                # Required: Message text
    'buttons': [                             # Required: Button layout
        ['Button 1', 'Button 2'],            # First row
        ['Button 3', 'Button 4']             # Second row
    ],
    'parse': 'HTML',                         # Optional: Parse mode
    'receiver': message.chat.id,             # Optional: Chat ID (auto-filled)
    'reply_to': message.message_id,          # Optional: Reply to message ID (auto-filled)
    'preview': False,                        # Optional: Disable link preview (default: True)
    'notify': False,                         # Optional: Send silently (default: True)
    'resize': True,                          # Optional: Resize keyboard (default: True)
    'one_time': True                         # Optional: Hide after use (default: False)
}
```

### Inline Keyboard

```python
return {
    'type': 'inline',
    'text': 'Select option:',                # Required: Message text
    'buttons': [                             # Required: Button layout
        [                                    # First row
            {
                'text': 'Website',           # Required: Button text
                'url': 'https://google.com'  # Required for URL button: URL
            },
            {
                'text': 'Callback',          # Required: Button text
                'data': 'button_click'       # Required for callback: Callback data
            }
        ]
    ],
    'parse': 'HTML',                         # Optional: Parse mode
    'receiver': message.chat.id,             # Optional: Chat ID (auto-filled)
    'reply_to': message.message_id,          # Optional: Reply to message ID (auto-filled)
    'preview': False,                        # Optional: Disable link preview (default: True)
    'notify': False                          # Optional: Send silently (default: True)
}
```

### Remove Reply Keyboard

```python
return {
    'type': 'remove_keyboard',
    'text': 'Keyboard removed',              # Required: Message text
    'parse': 'HTML',                         # Optional: Parse mode
    'receiver': message.chat.id,             # Optional: Chat ID (auto-filled)
    'reply_to': message.message_id,          # Optional: Reply to message ID (auto-filled)
    'preview': False,                        # Optional: Disable link preview (default: True)
    'notify': False                          # Optional: Send silently (default: True)
}
```

### Force Reply

```python
return {
    'type': 'force_reply',
    'text': 'Please reply:',                 # Required: Message text
    'parse': 'HTML',                         # Optional: Parse mode
    'receiver': message.chat.id,             # Optional: Chat ID (auto-filled)
    'reply_to': message.message_id,          # Optional: Reply to message ID (auto-filled)
    'preview': False,                        # Optional: Disable link preview (default: True)
    'notify': False                          # Optional: Send silently (default: True)
}
```

### Delete Message

```python
return {
    'type': 'delete',
    'message_id': message.message_id,        # Optional: Message ID to delete (default: current message)
    'receiver': message.chat.id              # Optional: Chat ID (auto-filled)
}
```

### Edit Message Text

```python
return {
    'type': 'edittext',
    'message_id': 123,                       # Required: Message ID to edit
    'text': 'Updated text',                  # Required: New message text
    'parse': 'HTML',                         # Optional: Parse mode
    'receiver': message.chat.id,             # Optional: Chat ID (auto-filled)
    'preview': False                         # Optional: Disable link preview (default: True)
}
```

### Forward Message
```python
return {
    'type': 'forward',
    'to': -100123456789,                     # Required: Destination chat ID
    'message_id': message.message_id,        # Required: Message ID to forward
    'receiver': message.chat.id,             # Optional: Source chat ID (auto-filled)
    'notify': False                          # Optional: Send silently (default: True)
}
```

### Copy Message
```python
return {
    'type': 'copy',
    'to': -100123456789,                     # Required: Destination chat ID
    'message_id': message.message_id,        # Required: Message ID to copy
    'caption': 'New caption',                # Optional: New caption for media
    'parse': 'HTML',                         # Optional: Parse mode for caption
    'receiver': message.chat.id,             # Optional: Source chat ID (auto-filled)
    'notify': False                          # Optional: Send silently (default: True)
}
```

### Pin Message
```python
return {
    'type': 'pin',
    'message_id': message.message_id,        # Optional: Message ID to pin (default: current message)
    'receiver': message.chat.id,             # Optional: Chat ID (auto-filled)
    'notify': False                          # Optional: Send silently (default: True)
}
```

### Unpin Message
```python
return {
    'type': 'unpin',
    'message_id': 123,                       # Optional: Message ID to unpin (default: all messages)
    'receiver': message.chat.id              # Optional: Chat ID (auto-filled)
}
```

### Unpin All Messages
```python
return {
    'type': 'unpinall',
    'receiver': message.chat.id              # Optional: Chat ID (auto-filled)
}
```

## Chat Management
### Ban User
```python
return {
    'type': 'ban',
    'user': message.from_user.id,            # Required: User ID to ban
    'until': 1609459200,                     # Optional: Ban until timestamp
    'receiver': message.chat.id              # Optional: Chat ID (auto-filled)
}
```

### Unban User
```python
return {
    'type': 'unban',
    'user': 123456789,                       # Required: User ID to unban
    'receiver': message.chat.id              # Optional: Chat ID (auto-filled)
}
```

### Restrict User
```python
return {
    'type': 'restrict',
    'user': message.from_user.id,            # Required: User ID to restrict
    'send': False,                           # Optional: Can send messages (default: False)
    'media': False,                          # Optional: Can send media (default: False)
    'polls': False,                          # Optional: Can send polls (default: False)
    'other': False,                          # Optional: Can send other messages (default: False)
    'previews': False,                       # Optional: Can add web previews (default: False)
    'until': 1609459200,                     # Optional: Restrict until timestamp
    'receiver': message.chat.id              # Optional: Chat ID (auto-filled)
}
```

### Promote User
```python
return {
    'type': 'promote',
    'user': message.from_user.id,            # Required: User ID to promote
    'change_info': True,                     # Optional: Can change chat info (default: False)
    'post': True,                            # Optional: Can post messages (default: False)
    'edit': True,                            # Optional: Can edit messages (default: False)
    'delete': True,                          # Optional: Can delete messages (default: False)
    'invite': True,                          # Optional: Can invite users (default: False)
    'restrict': True,                        # Optional: Can restrict members (default: False)
    'pin': True,                             # Optional: Can pin messages (default: False)
    'promote': True,                         # Optional: Can promote members (default: False)
    'receiver': message.chat.id              # Optional: Chat ID (auto-filled)
}
```

### Get Chat Info
```python
return {
    'type': 'chatinfo',
    'receiver': message.chat.id              # Optional: Chat ID (auto-filled)
}
```

### Get Member Count
```python
return {
    'type': 'membercount',
    'receiver': message.chat.id              # Optional: Chat ID (auto-filled)
}
```

### Get Member Info
```python
return {
    'type': 'memberinfo',
    'user': message.from_user.id,            # Required: User ID to get info
    'receiver': message.chat.id              # Optional: Chat ID (auto-filled)
}
```

### Get Invite Link
```python
return {
    'type': 'invitelink',
    'receiver': message.chat.id              # Optional: Chat ID (auto-filled)
}
```

### Set Chat Title
```python
return {
    'type': 'settitle',
    'title': 'New Chat Title',               # Required: New chat title
    'receiver': message.chat.id              # Optional: Chat ID (auto-filled)
}
```

### Set Chat Description
```python
return {
    'type': 'setdescription',
    'description': 'New description',        # Required: New chat description
    'receiver': message.chat.id              # Optional: Chat ID (auto-filled)
}
```

### Set Chat Photo
```python
return {
    'type': 'setphoto',
    'file': 'photo.jpg',                     # Required: Photo file path or URL
    'receiver': message.chat.id              # Optional: Chat ID (auto-filled)
}
```

### Delete Chat Photo
```python
return {
    'type': 'deletephoto',
    'receiver': message.chat.id              # Optional: Chat ID (auto-filled)
}
```

## Callback Query Responses
### Answer Callback Query
```python
return {
    'type': 'answercallback',
    'query_id': call.id,                     # Required: Callback query ID
    'text': 'Button clicked!',               # Optional: Notification text
    'show_alert': True,                      # Optional: Show as alert (default: False)
    'url': 'https://example.com'             # Optional: URL to open
}
```

### Edit Message (Callback)

```python
return {
    'type': 'editmessage',
    'message_id': call.message.message_id,   # Required: Message ID to edit
    'text': 'Message updated!',              # Optional: New message text
    'caption': 'New caption',                # Optional: New caption for media
    'parse': 'HTML',                         # Optional: Parse mode
    'receiver': call.message.chat.id,        # Optional: Chat ID (auto-filled)
    'preview': False,                        # Optional: Disable link preview (default: True)
    'buttons': [                             # Optional: New inline buttons
        [{'text': 'New Button', 'data': 'new_data'}]
    ]
}
```

## Helper Functions Usage Guide
### Text Message

```python
# Simple text
return text("Hello World")

# With all parameters
return text(
    content="Welcome to the bot!",
    parse="HTML",                    # Optional: 'HTML', 'Markdown', 'MarkdownV2'
    receiver=message.chat.id,        # Optional: Auto-filled
    reply_to=message.message_id,     # Optional: Auto-filled  
    preview=False,                   # Optional: Disable link preview
    notify=False                     # Optional: Send silently
)
```

### Photo Message

```python
# Simple photo
return photo("image.jpg")

# Photo with caption and parameters
return photo(
    file="https://picsum.photos/400/300",
    caption="Beautiful landscape",   # Optional
    parse="HTML",                    # Optional
    receiver=message.chat.id,        # Optional: Auto-filled
    reply_to=message.message_id,     # Optional: Auto-filled
    notify=True                      # Optional
)
```

### Video Message

```python
return video(
    file="video.mp4",
    caption="My video",              # Optional
    parse="Markdown",                # Optional
    receiver=message.chat.id,        # Optional: Auto-filled
    reply_to=message.message_id,     # Optional: Auto-filled
    notify=False                     # Optional
)
```

### Audio Message

```python
return audio(
    file="audio.mp3", 
    caption="Song title",            # Optional
    parse="HTML",                    # Optional
    receiver=message.chat.id,        # Optional: Auto-filled
    reply_to=message.message_id,     # Optional: Auto-filled
    notify=True                      # Optional
)
```

### Document Message

```python
return document(
    file="document.pdf",
    caption="Important file",        # Optional
    parse="HTML",                    # Optional
    receiver=message.chat.id,        # Optional: Auto-filled
    reply_to=message.message_id,     # Optional: Auto-filled
    notify=False                     # Optional
)
```

### Voice Message

```python
return voice(
    file="voice.ogg",
    caption="Voice note",            # Optional
    parse="HTML",                    # Optional
    receiver=message.chat.id,        # Optional: Auto-filled
    reply_to=message.message_id,     # Optional: Auto-filled
    notify=True                      # Optional
)
```

### Sticker Message
```python
return sticker(
    file="sticker.webp",
    receiver=message.chat.id,        # Optional: Auto-filled
    reply_to=message.message_id,     # Optional: Auto-filled
    notify=False                     # Optional
)
```

### Animation (GIF) Message
```python
return animation(
    file="animation.gif",
    caption="Funny GIF",             # Optional
    parse="HTML",                    # Optional
    receiver=message.chat.id,        # Optional: Auto-filled
    reply_to=message.message_id,     # Optional: Auto-filled
    notify=True                      # Optional
)
```

### Location
```python
return location(
    lat=28.6139,                     # Required: Latitude
    lon=77.2090,                     # Required: Longitude
    receiver=message.chat.id,        # Optional: Auto-filled
    reply_to=message.message_id,     # Optional: Auto-filled
    notify=False                     # Optional
)
```

### Venue
```python
return venue(
    lat=28.6139,                     # Required: Latitude
    lon=77.2090,                     # Required: Longitude
    title="Taj Mahal",               # Required: Venue title
    address="Agra, India",           # Required: Venue address
    receiver=message.chat.id,        # Optional: Auto-filled
    reply_to=message.message_id,     # Optional: Auto-filled
    notify=True                      # Optional
)
```

### Contact
```python
return contact(
    phone="+1234567890",             # Required: Phone number
    first_name="John",               # Required: First name
    last_name="Doe",                 # Optional: Last name
    receiver=message.chat.id,        # Optional: Auto-filled
    reply_to=message.message_id,     # Optional: Auto-filled
    notify=False                     # Optional
)
```

## Interactive Helpers
### Poll
```python
return poll(
    question="Favorite programming language?",  # Required
    options=["Python", "JavaScript", "Java", "C++"],  # Required
    receiver=message.chat.id,        # Optional: Auto-filled
    reply_to=message.message_id,     # Optional: Auto-filled
    notify=True                      # Optional
)
```

## Keyboard Helpers
### Button Creator
```python
# URL button
btn1 = button("Visit Google", url="https://google.com")

# Callback button  
btn2 = button("Click me", data="button_click")

# Simple button (for reply keyboard)
btn3 = button("Simple Button")
```

### Reply Keyboard

```python
buttons = [
    ["Button 1", "Button 2"],        # First row
    ["Button 3", "Button 4"],        # Second row
    ["Button 5"]                     # Third row
]

return keyboard(
    text="Choose an option:",        # Required: Message text
    buttons=buttons,                 # Required: Button layout
    parse="HTML",                    # Optional
    receiver=message.chat.id,        # Optional: Auto-filled
    reply_to=message.message_id,     # Optional: Auto-filled
    preview=False,                   # Optional: Disable link preview
    notify=True                      # Optional
)
```

### Inline Keyboard
```python
website_btn = button("Website", url="https://example.com")
callback_btn = button("Click", data="action_click")
simple_btn = button("Simple")

buttons = [
    [website_btn, callback_btn],     # First row
    [simple_btn]                     # Second row
]

return inline(
    text="Select an action:",        # Required: Message text
    buttons=buttons,                 # Required: Button layout
    parse="HTML",                    # Optional
    receiver=message.chat.id,        # Optional: Auto-filled
    reply_to=message.message_id,     # Optional: Auto-filled
    preview=True,                    # Optional: Enable link preview
    notify=False                     # Optional
)
```

### Remove Keyboard

```python
return remove_keyboard(
    text="Keyboard removed",         # Required: Message text
    parse="HTML",                    # Optional
    receiver=message.chat.id,        # Optional: Auto-filled
    reply_to=message.message_id,     # Optional: Auto-filled
    preview=False,                   # Optional: Disable link preview
    notify=True                      # Optional
)
```

### Force Reply
```python
return force_reply(
    text="Please reply to this message",  # Required: Message text
    parse="Markdown",                # Optional
    receiver=message.chat.id,        # Optional: Auto-filled
    reply_to=message.message_id,     # Optional: Auto-filled
    preview=True,                    # Optional: Enable link preview
    notify=False                     # Optional
)
```

### Media Group
```python
media_list = [
    {
        'type': 'photo',
        'file': 'photo1.jpg',
        'caption': 'First photo'
    },
    {
        'type': 'photo', 
        'file': 'photo2.jpg',
        'caption': 'Second photo'
    },
    {
        'type': 'video',
        'file': 'video1.mp4',
        'caption': 'A video'
    }
]

return mediagroup(
    media_list=media_list,           # Required: List of media items
    receiver=message.chat.id,        # Optional: Auto-filled
    reply_to=message.message_id,     # Optional: Auto-filled
    notify=True                      # Optional
)
```

## Message Management
### Delete Message

```python
# Delete current message
return delete()

# Delete specific message
return delete(
    message_id=123,                  # Optional: Message ID to delete
    receiver=message.chat.id         # Optional: Auto-filled
)
```

### Edit Message Text

```python
return edit(
    message_id=message.message_id,   # Required: Message ID to edit
    text="Updated message text",     # Required: New text
    parse="HTML",                    # Optional
    receiver=message.chat.id,        # Optional: Auto-filled
    preview=False                    # Optional: Disable link preview
)
```

### Forward Message

```python
return forward(
    to_chat=-100123456789,           # Required: Destination chat ID
    message_id=message.message_id,   # Required: Message ID to forward
    receiver=message.chat.id,        # Optional: Source chat ID (auto-filled)
    notify=True                      # Optional
)
```

### Copy Message

```python
return copy(
    to_chat=-100123456789,           # Required: Destination chat ID
    message_id=message.message_id,   # Required: Message ID to copy
    caption="New caption",           # Optional: New caption
    parse="HTML",                    # Optional: Parse mode for caption
    receiver=message.chat.id,        # Optional: Source chat ID (auto-filled)
    notify=False                     # Optional
)
```

## Chat Management Helpers
### Pin Message

```python
# Pin current message
return pin()

# Pin specific message
return pin(
    message_id=123,                  # Optional: Message ID to pin
    receiver=message.chat.id,        # Optional: Auto-filled
    notify=True                      # Optional: Send notification
)
```

### Unpin Message

```python
# Unpin all messages
return unpin()

# Unpin specific message  
return unpin(
    message_id=123,                  # Optional: Message ID to unpin
    receiver=message.chat.id         # Optional: Auto-filled
)
```

### Unpin All Messages

```python
return unpin_all(
    receiver=message.chat.id         # Optional: Auto-filled
)
```

### Ban User

```python
return ban(
    user_id=message.from_user.id,    # Required: User ID to ban
    until_date=1609459200,           # Optional: Ban until timestamp
    receiver=message.chat.id         # Optional: Auto-filled
)
```

### Unban User

```python
return unban(
    user_id=123456789,               # Required: User ID to unban
    receiver=message.chat.id         # Optional: Auto-filled
)
```

### Restrict User

```python
permissions = {
    'send': False,                   # Can send messages
    'media': False,                  # Can send media
    'polls': False,                  # Can send polls  
    'other': False,                  # Can send other messages
    'previews': False                # Can add web previews
}

return restrict(
    user_id=message.from_user.id,    # Required: User ID to restrict
    permissions=permissions,         # Optional: Permission settings
    until_date=1609459200,           # Optional: Restrict until timestamp
    receiver=message.chat.id         # Optional: Auto-filled
)
```

### Promote User

```python
privileges = {
    'change_info': True,             # Can change chat info
    'post': True,                    # Can post messages
    'edit': True,                    # Can edit messages
    'delete': True,                  # Can delete messages
    'invite': True,                  # Can invite users
    'restrict': True,                # Can restrict members
    'pin': True,                     # Can pin messages
    'promote': True                  # Can promote members
}

return promote(
    user_id=message.from_user.id,    # Required: User ID to promote
    privileges=privileges,           # Optional: Privilege settings
    receiver=message.chat.id         # Optional: Auto-filled
)
```

## Chat Info Helpers
### Get Chat Info

```python
return chat_info(
    receiver=message.chat.id         # Optional: Auto-filled
)
```

### Get Member Count

```python
return member_count(
    receiver=message.chat.id         # Optional: Auto-filled
)
```

### Get Member Info

```python
return member_info(
    user_id=message.from_user.id,    # Required: User ID to get info
    receiver=message.chat.id         # Optional: Auto-filled
)
```

### Get Invite Link

```python
return invite_link(
    receiver=message.chat.id         # Optional: Auto-filled
)
```

### Set Chat Title

```python
return set_title(
    title="New Chat Title",          # Required: New title
    receiver=message.chat.id         # Optional: Auto-filled
)
```

### Set Chat Description

```python
return set_description(
    description="New chat description",  # Required: New description
    receiver=message.chat.id         # Optional: Auto-filled
)
```

### Set Chat Photo

```python
return set_photo(
    file="chat_photo.jpg",           # Required: Photo file
    receiver=message.chat.id         # Optional: Auto-filled
)
```

### Delete Chat Photo

```python
return delete_photo(
    receiver=message.chat.id         # Optional: Auto-filled
)
```

## Callback Query Helpers
### Answer Callback Query

```python
return answer_callback(
    query_id=call.id,                # Required: Callback query ID
    text="Action completed!",        # Optional: Notification text
    show_alert=True,                 # Optional: Show as alert
    url="https://example.com"        # Optional: URL to open
)
```

### Edit Message (Callback)
```python
new_buttons = [
    [button("New Button 1", data="new1"), button("New Button 2", data="new2")]
]

return edit_message(
    message_id=call.message.message_id,  # Required: Message ID to edit
    text="Message updated!",         # Optional: New text
    parse="HTML",                    # Optional: Parse mode
    receiver=call.message.chat.id,   # Optional: Auto-filled
    preview=False,                   # Optional: Disable link preview
    buttons=new_buttons,             # Optional: New inline buttons
    caption="New caption"            # Optional: New caption for media
)
```

## Using Webhook & Polling
**Polling (default):**
```python
bot.run("YOUR_BOT_TOKEN")
```

**Webhook:**
```python
bot.webhook("YOUR_BOT_TOKEN", "https://yourdomain.com/" [,port]) # Registers webhook and listens for messages via HTTP.
```
- Second arg: webhook URL.
- Optional: set a custom port (default 8000)

**Which to use?**
- **Polling**: Easiest for dev/small apps.
- **Webhook**: Production or cloud deployments.

## Client Integration
```python
from mehta import client

bot = client()

@bot.commands(['start'])
def start(message):
    return text("Hello from Telethon client")

@bot.message()
def echo(message):
    return text(f"Echo: {message.text}")

bot.run(api_id=YOUR_API_ID', api_hash='YOUR_API_HASH')
```
- Works all **possible** functions (`text`, `photo`, `video`, ...).

## FAQ & Notes
- **Auto-injection:** Helper functions (`text`, `photo`, etc.) are imported as globals for you automatically when you create a bot/client instance.
- **Return style:** All handlers can return either a dictionary or use the provided helper function style.
- **Error handling:** For both pyTelebot and Telethon, errors are printed nicely by default.
- **CLI:** `mehta run:yourfile.py`—auto detects main bot and starts automatically.
- **Rate limits:** Use `rate_limit` in command decorators for anti-spam.
- **Timeout:** Force handlers to exit after N seconds if unresponsive.
- **Extending:** For new types/variants, copy the dict pattern.

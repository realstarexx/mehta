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
  <img src="https://img.shields.io/badge/version-1.1.6-green?style=for-the-badge" alt="Version">
  <img src="https://img.shields.io/badge/python-3.6%2B-blue?style=for-the-badge" alt="Python">
  <img src="https://img.shields.io/badge/license-MIT-red?style=for-the-badge" alt="License">

## Installation
```bash
pip install mehta
```

### Basic Setup
```python
from mehta import telegram

bot = telegram()

@bot.commands(['start'])
def start(message):
    return "Hello! Bot started."

@bot.message()
def echo(message):
    return f"Echo: {message.text}"

bot.run("YOUR_BOT_TOKEN")
```
- **Auto-injection:** Helper functions (`text`, `photo`, etc.) are imported as globals for you automatically when you create a bot/client instance and works without prefixes.
- **Error handling:** For both pyTelebot and Telethon, errors are printed nicely by default.
- **CLI:** `mehta run:yourfile.py`, auto detects main bot and starts automatically.
- **Rate limits:** Use `rate_limit` in command decorators for anti-spam.
- **Timeout:** Force handlers to exit after N seconds if unresponsive.


## Decorators Reference

| Decorator       | Parameters                                | Use Case                             |
|-----------------|-------------------------------------------|--------------------------------------|
| `@bot.commands` | `commandlist`, `rate_limit=None`, `timeout=None` | Bind handler to Telegram commands    |
| `@bot.message`  | **None**                                  | Handles all non-command messages     |
| `@bot.callback` | **None**                                  | Handles callback queries (inlines)   |
| `@bot.error`    | **None**                                  | Handles errors for all handlers      |

**Example:**
```python
@bot.commands(['hi', 'hello'], rate_limit=1, timeout=3)
def hi(message):
    return text("Hi, rate limit 1/min, timeout 3s!")
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
return text(
    content="Hello World",
    parse="HTML",
    receiver=message.chat.id,
    reply_to=message.message_id,
    preview=False,
    notify=False
)
```
**Optional**: `parse`, `receiver`, `reply_to`, `preview`, `notify`

### Photo Message
```python
return photo(
    file="https://picsum.photos/400/300",
    caption="Beautiful landscape", 
    parse="HTML",             
    receiver=message.chat.id,       
    reply_to=message.message_id,     
    notify=True                     
)
```

**Optional**: `caption`, `parse`, `receiver`, `reply_to`, `notify`


### Video Message
```python
return video(
    file="video.mp4",
    caption="My video",
    parse="Markdown",
    receiver=message.chat.id,
    reply_to=message.message_id,
    notify=False
)
```

**Optional**: `caption`, `parse`, `receiver`, `reply_to`, `notify`


### Audio Message
```python
return audio(
    file="audio.mp3", 
    caption="Song title",
    parse="HTML",
    receiver=message.chat.id,
    reply_to=message.message_id,
    notify=True
)
```

**Optional**: `caption`, `parse`, `receiver`, `reply_to`, `notify`


### Document Message
```python
return document(
    file="document.pdf",
    caption="Important file",
    parse="HTML",
    receiver=message.chat.id,
    reply_to=message.message_id,
    notify=False
)
```

**Optional**: `caption`, `parse`, `receiver`, `reply_to`, `notify`


### Voice Message
```python
return voice(
    file="voice.ogg",
    caption="Voice note",
    parse="HTML",
    receiver=message.chat.id,
    reply_to=message.message_id,
    notify=True
)
```

**Optional**: `caption`, `parse`, `receiver`, `reply_to`, `notify`


### Sticker Message

```python
return sticker(
    file="sticker.webp",
    receiver=message.chat.id,
    reply_to=message.message_id,
    notify=False
)
```

**Optional**: `receiver`, `reply_to`, `notify`


### Animation Message
```python
return animation(
    file="animation.gif",
    caption="Funny GIF",
    parse="HTML",
    receiver=message.chat.id,
    reply_to=message.message_id,
    notify=True
)
```

**Optional**: `caption`, `parse`, `receiver`, `reply_to`, `notify`


### Location Message
```python
return location(
    lat=28.6139,
    lon=77.2090,
    receiver=message.chat.id,
    reply_to=message.message_id,
    notify=False
)
```

**Optional**: `receiver`, `reply_to`, `notify`


### Venue Message
```python
return venue(
    lat=28.6139,
    lon=77.2090,
    title="Taj Mahal",
    address="Agra, India",
    receiver=message.chat.id,
    reply_to=message.message_id,
    notify=True
)
```

**Optional**: `receiver`, `reply_to`, `notify`


### Contact Message
```python
return contact(
    phone="+1234567890",
    first_name="John",
    last_name="Doe",
    receiver=message.chat.id,
    reply_to=message.message_id,
    notify=False
)
```

**Optional**: `last_name`, `receiver`, `reply_to`, `notify`


### Poll Message
```python
return poll(
    question="Favorite programming language?",
    options=["Python", "JavaScript", "Java", "C++"],
    receiver=message.chat.id,
    reply_to=message.message_id,
    notify=True
)
```

**Optional**: `receiver`, `reply_to`, `notify`


### Dice Message
```python
return dice(
    emoji="🎯",
    receiver=message.chat.id,
    reply_to=message.message_id,
    notify=False
)
```

**Optional**: `emoji`, `receiver`, `reply_to`, `notify`


### Media Group Message

```python
media_list = [
    {'type': 'photo', 'file': 'photo1.jpg', 'caption': 'First photo'},
    {'type': 'video', 'file': 'video1.mp4', 'caption': 'A video'}
]

return mediagroup(
    media_list=media_list,
    receiver=message.chat.id,
    reply_to=message.message_id,
    notify=True
)
```

**Optional**: `receiver`, `reply_to`, `notify`

### Reply Keyboard
```python
buttons = [['Button 1', 'Button 2'], ['Button 3']]

return keyboard(
    text="Choose an option:",
    buttons=buttons,
    parse="HTML",
    receiver=message.chat.id,
    reply_to=message.message_id,
    preview=False,
    notify=True
)
```

**Optional**: `parse`, `receiver`, `reply_to`, `preview`, `notify`


### Inline Keyboard
```python
website_btn = button("Website", url="https://google.com")
callback_btn = button("Click", data="button_click")
buttons = [[website_btn, callback_btn]]

return inline(
    text="Select an action:",
    buttons=buttons,
    parse="HTML",
    receiver=message.chat.id,
    reply_to=message.message_id,
    preview=True,
    notify=False
)
```

**Optional**: `parse`, `receiver`, `reply_to`, `preview`, `notify`


### Remove Keyboard
```python
return remove_keyboard(
    text="Keyboard removed",
    parse="HTML",
    receiver=message.chat.id,
    reply_to=message.message_id,
    preview=False,
    notify=True
)
```

**Optional**: `parse`, `receiver`, `reply_to`, `preview`, `notify`


### Force Reply
```python
return force_reply(
    text="Please reply to this message",
    parse="Markdown",
    receiver=message.chat.id,
    reply_to=message.message_id,
    preview=True,
    notify=False
)
```

**Optional**: `parse`, `receiver`, `reply_to`, `preview`, `notify`


### Delete Message
```python
return delete(
    message_id=123,
    receiver=message.chat.id
)
```

**Optional**: `message_id`, `receiver`


### Edit Message Text
```python
return edit(
    message_id=message.message_id,
    text="Updated message text",
    parse="HTML",
    receiver=message.chat.id,
    preview=False
)
```

**Optional**: `parse`, `receiver`, `preview`


### Forward Message
```python
return forward(
    to_chat=-100123456789,
    message_id=message.message_id,
    receiver=message.chat.id,
    notify=True
)
```

**Optional**: `receiver`, `notify`


### Copy Message
```python
return copy(
    to_chat=-100123456789,
    message_id=message.message_id,
    caption="New caption",
    parse="HTML",
    receiver=message.chat.id,
    notify=False
)
```

**Optional**: `caption`, `parse`, `receiver`, `notify`


### Pin Message
```python
return pin(
    message_id=123,
    receiver=message.chat.id,
    notify=True
)
```

**Optional**: `message_id`, `receiver`, `notify`


### Unpin Message
```python
return unpin(
    message_id=123,
    receiver=message.chat.id
)
```

**Optional**: `message_id`, `receiver`


### Unpin All Messages
```python
return unpin_all(
    receiver=message.chat.id
)
```

**Optional**: `receiver`

### Ban User
```python
return ban(
    user_id=message.from_user.id,
    until_date=1609459200,
    receiver=message.chat.id
)
```

**Optional**: `until`, `receiver`


### Unban User
```python
return unban(
    user_id=123456789,
    receiver=message.chat.id
)
```

**Optional**: `receiver`


### Restrict User
```python
permissions = {'send': False, 'media': False, 'polls': False, 'other': False, 'previews': False}

return restrict(
    user_id=message.from_user.id,
    permissions=permissions,
    until_date=1609459200,
    receiver=message.chat.id
)
```

**Optional**: `send`, `media`, `polls`, `other`, `previews`, `until`, `receiver`


### Promote User
```python
privileges = {'change_info': True, 'post': True, 'edit': True, 'delete': True, 'invite': True, 'restrict': True, 'pin': True, 'promote': True}

return promote(
    user_id=message.from_user.id,
    privileges=privileges,
    receiver=message.chat.id
)
```

**Optional**: `change_info`, `post`, `edit`, `delete`, `invite`, `restrict`, `pin`, `promote`, `receiver`


### Get Chat Info
```python
return chat_info(
    receiver=message.chat.id
)
```

**Optional**: `receiver`


### Get Member Count
```python
return member_count(
    receiver=message.chat.id
)
```

**Optional**: `receiver`

### Get Member Info
```python
return member_info(
    user_id=message.from_user.id,
    receiver=message.chat.id
)
```

**Optional**: `receiver`


### Get Invite Link
```python
return invite_link(
    receiver=message.chat.id
)
```

**Optional**: `receiver`


### Set Chat Title
```python
return set_title(
    title="New Chat Title",
    receiver=message.chat.id
)
```

**Optional**: `receiver`


### Set Chat Description
```python
return set_description(
    description="New chat description",
    receiver=message.chat.id
)
```

**Optional**: `receiver`

### Set Chat Photo
```python
return set_photo(
    file="chat_photo.jpg",
    receiver=message.chat.id
)
```
**Optional**: `receiver`

### Delete Chat Photo
```python
return delete_photo(
    receiver=message.chat.id
)
```

**Optional**: `receiver`


### Answer Callback Query
```python
return answer_callback(
    query_id=call.id,
    text="Action completed!",
    show_alert=True,
    url="https://example.com"
)
```

**Optional**: `text`, `show_alert`, `url`

### Edit Message (Callback)
```python
new_buttons = [[button("New Button 1", data="new1")]]

return edit_message(
    message_id=call.message.message_id,
    text="Message updated!",
    parse="HTML",
    receiver=call.message.chat.id,
    preview=False,
    buttons=new_buttons,
    caption="New caption"
)
```

**Optional**: `text`, `caption`, `parse`, `receiver`, `preview`, `buttons`


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
    return text("Hello from Telethon Client!")

@bot.message()
def echo(message):
    return text(f"Echo: {message.text}")

bot.run(api_id=YOUR_API_ID', api_hash='YOUR_API_HASH')
```
- Works with all **possible** functions (`text`, `photo`, `video`, etc).

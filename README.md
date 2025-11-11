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
def hi(message): return "Hi, rate limit 1/min, timeout 3s!"
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

### Send Message
| Function Call                                      | Equivalent Dictionary                                              |
|-----------------------------------------------------------|---------------------------------------------------------------------------|
| `text('{content}', parse='{parse}', receiver='{receiver}', reply_to='{reply_to}', preview='{preview}', notify='{notify}')` | `{'type': 'text', 'text': '{content}', 'parse': '{parse}', 'receiver': '{receiver}', 'reply_to': '{reply_to}', 'preview': '{preview}', 'notify': '{notify}'}` |
| `photo('{file}', caption='{caption}', parse='{parse}', receiver='{receiver}', reply_to='{reply_to}', notify='{notify}')` | `{'type': 'photo', 'file': '{file}', 'caption': '{caption}', 'parse': '{parse}', 'receiver': '{receiver}', 'reply_to': '{reply_to}', 'notify': '{notify}'}` |
| `video('{file}', caption='{caption}', parse='{parse}', receiver='{receiver}', reply_to='{reply_to}', notify='{notify}')` | `{'type': 'video', 'file': '{file}', 'caption': '{caption}', 'parse': '{parse}', 'receiver': '{receiver}', 'reply_to': '{reply_to}', 'notify': '{notify}'}` |
| `audio('{file}', caption='{caption}', parse='{parse}', receiver='{receiver}', reply_to='{reply_to}', notify='{notify}')` | `{'type': 'audio', 'file': '{file}', 'caption': '{caption}', 'parse': '{parse}', 'receiver': '{receiver}', 'reply_to': '{reply_to}', 'notify': '{notify}'}` |
| `document('{file}', caption='{caption}', parse='{parse}', receiver='{receiver}', reply_to='{reply_to}', notify='{notify}')` | `{'type': 'document', 'file': '{file}', 'caption': '{caption}', 'parse': '{parse}', 'receiver': '{receiver}', 'reply_to': '{reply_to}', 'notify': '{notify}'}` |
| `sticker('{file}', receiver='{receiver}', reply_to='{reply_to}', notify='{notify}')` | `{'type': 'sticker', 'file': '{file}', 'receiver': '{receiver}', 'reply_to': '{reply_to}', 'notify': '{notify}'}` |
| `voice('{file}', caption='{caption}', parse='{parse}', receiver='{receiver}', reply_to='{reply_to}', notify='{notify}')` | `{'type': 'voice', 'file': '{file}', 'caption': '{caption}', 'parse': '{parse}', 'receiver': '{receiver}', 'reply_to': '{reply_to}', 'notify': '{notify}'}` |
| `animation('{file}', caption='{caption}', parse='{parse}', receiver='{receiver}', reply_to='{reply_to}', notify='{notify}')` | `{'type': 'animation', 'file': '{file}', 'caption': '{caption}', 'parse': '{parse}', 'receiver': '{receiver}', 'reply_to': '{reply_to}', 'notify': '{notify}'}` |
| `mediagroup([{ 'type': '{media_type}', 'file': '{file}' }], receiver='{receiver}', reply_to='{reply_to}', notify='{notify}')` | `{'type': 'mediagroup', 'media': [{'type': '{media_type}', 'file': '{file}'}], 'receiver': '{receiver}', 'reply_to': '{reply_to}', 'notify': '{notify}'}` |
| `location({lat}, {lon}, receiver='{receiver}', reply_to='{reply_to}', notify='{notify}')` | `{'type': 'location', 'lat': {lat}, 'lon': {lon}, 'receiver': '{receiver}', 'reply_to': '{reply_to}', 'notify': '{notify}'}` |
| `venue({lat}, {lon}, '{title}', '{address}', receiver='{receiver}', reply_to='{reply_to}', notify='{notify}')` | `{'type': 'venue', 'lat': {lat}, 'lon': {lon}, 'title': '{title}', 'address': '{address}', 'receiver': '{receiver}', 'reply_to': '{reply_to}', 'notify': '{notify}'}` |
| `contact('{phone}', '{first_name}', '{last_name}', receiver='{receiver}', reply_to='{reply_to}', notify='{notify}')` | `{'type': 'contact', 'phone': '{phone}', 'first_name': '{first_name}', 'last_name': '{last_name}', 'receiver': '{receiver}', 'reply_to': '{reply_to}', 'notify': '{notify}'}` |
| `poll('{question}', ['{option1}', '{option2}'], receiver='{receiver}', reply_to='{reply_to}', notify='{notify}')` | `{'type': 'poll', 'question': '{question}', 'options': ['{option1}', '{option2}'], 'receiver': '{receiver}', 'reply_to': '{reply_to}', 'notify': '{notify}'}` |
| `dice('{emoji}', receiver='{receiver}', reply_to='{reply_to}', notify='{notify}')` | `{'type': 'dice', 'emoji': '{emoji}', 'receiver': '{receiver}', 'reply_to': '{reply_to}', 'notify': '{notify}'}` |
| `delete({message_id}, receiver='{receiver}')` | `{'type': 'delete', 'message_id': {message_id}, 'receiver': '{receiver}'}` |
| `edit({message_id}, '{text}', parse='{parse}', receiver='{receiver}', preview='{preview}', buttons={buttons}, caption='{caption}', reply_markup='{reply_markup}')` | `{'type': 'edit', 'message_id': {message_id}, 'text': '{text}', 'parse': '{parse}', 'receiver': '{receiver}', 'preview': '{preview}', 'buttons': {buttons}, 'caption': '{caption}', 'reply_markup': '{reply_markup}'}` |
| `forward({to_chat}, {message_id}, receiver='{receiver}', notify='{notify}')` | `{'type': 'forward', 'to': {to_chat}, 'message_id': {message_id}, 'receiver': '{receiver}', 'notify': '{notify}'}` |
| `copy({to_chat}, {message_id}, caption='{caption}', parse='{parse}', receiver='{receiver}', notify='{notify}')` | `{'type': 'copy', 'to': {to_chat}, 'message_id': {message_id}, 'caption': '{caption}', 'parse': '{parse}', 'receiver': '{receiver}', 'notify': '{notify}'}` |
| `pin({message_id}, receiver='{receiver}', notify='{notify}')` | `{'type': 'pin', 'message_id': {message_id}, 'receiver': '{receiver}', 'notify': '{notify}'}` |
| `unpin({message_id}, receiver='{receiver}')` | `{'type': 'unpin', 'message_id': {message_id}, 'receiver': '{receiver}'}` |
| `unpin_all(receiver='{receiver}')` | `{'type': 'unpinall', 'receiver': '{receiver}'}` |
| `ban({user_id}, until_date='{until_date}', receiver='{receiver}')` | `{'type': 'ban', 'user': {user_id}, 'until_date': '{until_date}', 'receiver': '{receiver}'}` |
| `unban({user_id}, receiver='{receiver}')` | `{'type': 'unban', 'user': {user_id}, 'receiver': '{receiver}'}` |
| `restrict({user_id}, permissions={permissions}, until_date='{until_date}', receiver='{receiver}')` | `{'type': 'restrict', 'user': {user_id}, 'permissions': {permissions}, 'until_date': '{until_date}', 'receiver': '{receiver}'}` |
| `promote({user_id}, privileges={privileges}, receiver='{receiver}')` | `{'type': 'promote', 'user': {user_id}, 'privileges': {privileges}, 'receiver': '{receiver}'}` |
| `chat_info(receiver='{receiver}')` | `{'type': 'chatinfo', 'receiver': '{receiver}'}` |
| `member_count(receiver='{receiver}')` | `{'type': 'membercount', 'receiver': '{receiver}'}` |
| `member_info({user_id}, receiver='{receiver}')` | `{'type': 'memberinfo', 'user': {user_id}, 'receiver': '{receiver}'}` |
| `invite_link(receiver='{receiver}')` | `{'type': 'invitelink', 'receiver': '{receiver}'}` |
| `set_title('{title}', receiver='{receiver}')` | `{'type': 'settitle', 'title': '{title}', 'receiver': '{receiver}'}` |
| `set_description('{description}', receiver='{receiver}')` | `{'type': 'setdescription', 'description': '{description}', 'receiver': '{receiver}'}` |
| `set_photo('{file}', receiver='{receiver}')` | `{'type': 'setphoto', 'file': '{file}', 'receiver': '{receiver}'}` |
| `delete_photo(receiver='{receiver}')` | `{'type': 'deletephoto', 'receiver': '{receiver}'}` |
| `keyboard('{text}', {buttons}, parse='{parse}', receiver='{receiver}', reply_to='{reply_to}', preview='{preview}', notify='{notify}')` | `{'type': 'keyboard', 'text': '{text}', 'buttons': {buttons}, 'parse': '{parse}', 'receiver': '{receiver}', 'reply_to': '{reply_to}', 'preview': '{preview}', 'notify': '{notify}'}` |
| `inline('{text}', {buttons}, parse='{parse}', receiver='{receiver}', reply_to='{reply_to}', preview='{preview}', notify='{notify}')` | `{'type': 'inline', 'text': '{text}', 'buttons': {buttons}, 'parse': '{parse}', 'receiver': '{receiver}', 'reply_to': '{reply_to}', 'preview': '{preview}', 'notify': '{notify}'}` |
| `remove_keyboard('{text}', parse='{parse}', receiver='{receiver}', reply_to='{reply_to}', preview='{preview}', notify='{notify}')` | `{'type': 'remove_keyboard', 'text': '{text}', 'parse': '{parse}', 'receiver': '{receiver}', 'reply_to': '{reply_to}', 'preview': '{preview}', 'notify': '{notify}'}` |
| `force_reply('{text}', parse='{parse}', receiver='{receiver}', reply_to='{reply_to}', preview='{preview}', notify='{notify}')` | `{'type': 'force_reply', 'text': '{text}', 'parse': '{parse}', 'receiver': '{receiver}', 'reply_to': '{reply_to}', 'preview': '{preview}', 'notify': '{notify}'}` |
| `answer_callback('{query_id}', text='{text}', show_alert='{show_alert}', url='{url}')` | `{'type': 'answercallback', 'query_id': '{query_id}', 'text': '{text}', 'show_alert': '{show_alert}', 'url': '{url}'}` |
| `edit_message({message_id}, '{text}', parse='{parse}', receiver='{receiver}', preview='{preview}', buttons={buttons}, caption='{caption}', reply_markup='{reply_markup}')` | `{'type': 'editmessage', 'message_id': {message_id}, 'text': '{text}', 'parse': '{parse}', 'receiver': '{receiver}', 'preview': '{preview}', 'buttons': {buttons}, 'caption': '{caption}', 'reply_markup': '{reply_markup}'}` |

**Tip:** Most parameters auto-fill to message context if omitted (e.g., `receiver`, `reply_to`).

## Response Type Usage

```python
@bot.commands(['types'])
def demo(message):
    # Text
    return text("A simple message.", parse='MarkdownV2')
    
    # Photo
    # return photo('img.jpg', caption='A cool pic!', notify=True)
    
    # Keyboard
    # return keyboard('Choose:', [['A','B']])
```

## Using Webhook & Polling
**Polling**:
```python
bot.run("YOUR_BOT_TOKEN")
```

**Webhook**:
```python
bot.webhook("YOUR_BOT_TOKEN", "https://yourdomain.com/" [,port]) # Webhook and listens for messages via HTTP.
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
    return { 'type': 'text', 'text': "Hello from mehta client" }

@bot.message()
def echo(message):
    return text(f"You said: {message.text}")

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

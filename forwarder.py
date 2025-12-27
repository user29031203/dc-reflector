# main.py
import discord
import json
import os
import signal
from config import (
    USER_TOKEN,
    SOURCE_CHANNEL_ID,
    DESTINATION_CHANNEL_ID,
    MAPPING_FILE,
    LOG_REACTIONS
)

client = discord.Client(self_bot=True)

# Load persistent mapping
if os.path.exists(MAPPING_FILE):
    forwarded_messages = json.load(open(MAPPING_FILE))
    forwarded_messages = {int(k): int(v) for k, v in forwarded_messages.items()}
    print(f"Loaded {len(forwarded_messages):,} forwarded messages")
else:
    forwarded_messages = {}

def save_mapping():
    json.dump(forwarded_messages, open(MAPPING_FILE, "w"), indent=2)

@client.event
async def on_ready():
    print(f"Self-bot ready → {client.user} ({client.user.id})")
    print(f"Source → {SOURCE_CHANNEL_ID}")
    print(f"Destination → {DESTINATION_CHANNEL_ID}")
    print(f"Tracking {len(forwarded_messages)} messages\n")

@client.event
async def on_message(message):
    if message.channel.id != SOURCE_CHANNEL_ID:
        return
    if message.id in forwarded_messages:
        return

    dest = client.get_channel(DESTINATION_CHANNEL_ID)
    if not dest:
        print("Cannot access destination channel!")
        return

    author = f"{message.author.name}#{message.author.discriminator}"
    text = message.content.strip()
    content = f"**{author}**" + (f": {text}" if text else " (media/embed)")

    for att in message.attachments:
        content += f"\n{att.url}"
    for embed in message.embeds:
        if embed.title:
            content += f"\n**{embed.title}**"
        if embed.description:
            content += f"\n{embed.description[:300]}"

    try:
        sent = await dest.send(content.strip())
        forwarded_messages[message.id] = sent.id
        save_mapping()

        # Copy existing reactions
        for r in message.reactions:
            emoji = r.emoji
            emoji_str = f"<{'' if not getattr(emoji, 'animated', False) else 'a'}:{emoji.name}:{emoji.id}>" \
                        if getattr(emoji, 'id', None) else str(emoji)
            await sent.add_reaction(emoji_str)

        print(f"Forwarded {message.id} → {sent.id}")

    except Exception as e:
        print(f"Error sending message: {e}")

# =============== REACTION HANDLING (RAW) ===============
async def handle_reaction(payload, add=True):
    if payload.channel_id != SOURCE_CHANNEL_ID:
        return
    if payload.message_id not in forwarded_messages:
        return

    fwd_id = forwarded_messages[payload.message_id]
    dest = client.get_channel(DESTINATION_CHANNEL_ID)
    if not dest:
        return

    try:
        msg = await dest.fetch_message(fwd_id)

        emoji = payload.emoji
        emoji_str = f"<{'' if not emoji.animated else 'a'}:{emoji.name}:{emoji.id}>" \
                    if emoji.is_custom_emoji() else emoji.name

        if add:
            await msg.add_reaction(emoji_str)
        else:
            await msg.remove_reaction(emoji_str, client.user)

        if LOG_REACTIONS:
            action = "Added" if add else "Removed"
            print(f"{action} reaction {emoji_str} → {fwd_id}")

    except discord.NotFound:
        print(f"Forwarded message missing: {fwd_id}")
    except Exception as e:
        print(f"Reaction error: {e}")

@client.event
async def on_raw_reaction_add(payload):
    await handle_reaction(payload, add=True)

@client.event
async def on_raw_reaction_remove(payload):
    await handle_reaction(payload, add=False)

# =============== CLEAN SHUTDOWN ===============
def shutdown(sig=None, frame=None):
    print("\nSaving mapping & exiting...")
    save_mapping()
    os._exit(0)

signal.signal(signal.SIGINT, shutdown)
signal.signal(signal.SIGTERM, shutdown)

# =============== START ===============
if __name__ == "__main__":
    if USER_TOKEN == "YOUR_USER_TOKEN_HERE":
        print("ERROR: Set your token in config.py first!")
    else:
        client.run(USER_TOKEN)
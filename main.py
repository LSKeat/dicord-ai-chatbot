import os

from discord import Intents, Client, Message
# If using llama2 model change response_gemini -> response_llama2
from response_llama2 import get_response

# Replace your discord api token
TOKEN = 'DISCORD_TOKEN'

intents: Intents = Intents.default()
intents.message_content = True 
client: Client = Client(intents=intents)

async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return
    
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

# Run the bot
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')


# Receive message
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)

# Start client
def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()

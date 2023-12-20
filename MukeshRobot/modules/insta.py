import instaloader
import os
from MukeshRobot import telethn as tbot

# Define the function to handle the /insta command
@tbot.on(tbot.pyro_cmd("insta ?(.*)"))
async def insta(event):
    link = event.pattern_match.group(1)

    if link:
        # Download the Instagram reel
        try:
            # Initialize an Instaloader instance
            L = instaloader.Instaloader()

            # Extract information from the link
            post = instaloader.Post.from_shortcode(L.context, link)

            # Download the reel
            filename = f'{post.owner_username}_{post.shortcode}.mp4'
            L.download_post(post, target=f'downloads/{filename}')

            # Send the downloaded reel to the user
            await event.reply(file=f'downloads/{filename}')

        except Exception as e:
            await event.reply(f'Error: {e}')

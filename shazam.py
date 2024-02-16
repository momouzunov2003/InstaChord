import asyncio
from shazamio import Shazam

def get_song_name(path):
  async def main():
    shazam = Shazam()
    out = await shazam.recognize_song(path)
    return out['track']['title']

  loop = asyncio.get_event_loop()
  return(loop.run_until_complete(main()))
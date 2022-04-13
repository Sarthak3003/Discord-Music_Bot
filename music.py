import discord
from discord.ext import commands
import youtube_dl

class music(commands.Cog):
    def __init__(self, client):
      self.client = client
    
    #this is join command
    @commands.command()
    async def join(self,ctx):
      if ctx.author.voice is None:
        await ctx.send("VC toh Join kr gandu")
      voice_channel = ctx.author.voice.channel
      if ctx.voice_client is None:
        await voice_channel.connect()
      else:
        await ctx.voice_client.move_to(voice_channel)
    
    #this is disconnect command
    @commands.command()
    async def disconnect(self,ctx):
      await ctx.voice_client.disconnect()
    
    #this is play command
    @commands.command()
    async def play(self,ctx,url):
      ctx.voice_client.stop()
      FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
      YDL_OPTIONS = {'format':"bestaudio"}
      vc = ctx.voice_client

      with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']
        source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
        vc.play(source)
    
    #this is pause command
    @commands.command()
    async def pause(self,ctx):
      text1 = "Paused ⏸️"
      await ctx.voice_client.pause()
      await ctx.send(text1)
    
    #this is resume command
    @commands.command()
    async def resume(self,ctx):
      text2 = "Resumed ▶️"
      await ctx.voice_client.resume()
      await ctx.send(text2)


def setup(client):
  client.add_cog(music(client))

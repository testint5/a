import os
import threading
import requests
import random
import time
from dhooks import Webhook, Embed
import colorama
from colorama import Fore

# Initialize colorama
colorama.init()
time.sleep(1)

def groupfinder():
    id = random.randint(30000000, 36000000)  # this is changeable, this allows you to filter what group ID'S are searched
    r = requests.get(f"https://www.roblox.com/groups/group.aspx?gid={id}") 
    if 'owned' not in r.text:
        re = requests.get(f"https://groups.roblox.com/v1/groups/{id}")
        if 'isLocked' not in re.text and 'owner' in re.text:
            if re.json()['publicEntryAllowed'] == True and re.json()['owner'] == None:
                # Create an embed
                embed = Embed(
                    title=f"Group Found: {id}",
                    url=f"https://www.roblox.com/groups/group.aspx?gid={id}",
                    color=0x00ff00,
                )
                embed.set_footer(text="Moo Group Finder | discord.gg/frv")
                embed.add_field(name="Group Name:", value=re.json()['name'], inline=False)
                embed.add_field(name="Group ID:", value=id, inline=True)
                embed.add_field(name="Member Count:", value=re.json()['memberCount'], inline=True)

                # Send the message to the webhook
                hook.send("MooTube Tutorial Finder", embed=embed)
                print(f"[+ +] : Roblox Group Finder 2023 {id}")  # add name so ping yay!!
            else:
                print(f"[-] No Entry Allowed: {id}")
        else:
            print(f"[-] Group Locked: {id}")
    else:
        print(f"[-] Group Already Owned: {id}")

# Get user input


# Set your webhook URL manually for testing purposes
hook_url = "https://discord.com/api/webhooks/1296129794551058485/VQFoXK7r00Rj5mIr3mFqS2LH5QFqHuZ6xv1fwdSEh-jHTcgPcBnOvPHLlSa5oUa8ANlk"  # Replace with your actual webhook URL
threads = 500

hook = Webhook(hook_url)

while True:
    if threading.active_count() <= threads:
        threading.Thread(target=groupfinder).start()
    time.sleep(0.3)

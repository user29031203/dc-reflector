# Dc-Reflector 

<!-- shields -->
![Static Badge](https://img.shields.io/badge/-0.1.0-blue?style=for-the-badge&label=dc-reflector)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/discord.py-self?pypiBaseUrl=https%3A%2F%2Fpypi.org&style=for-the-badge&color=brightgreen)
![GitHub License](https://img.shields.io/github/license/user29031203/dc-reflector?style=for-the-badge)
<!-- end shields -->

Dc-Reflector is a Python program to forward/copy messages of a channel to another channel. It doesn't handle deleted messages. That means Dc-Reflector will create replicate/archived version of the desired channel dynamically. It can handle/forward embeds, emoji reactions and more!

<!-- legal warning/info -->
> ⚠️ **Any tool that automates actions on user accounts, including this one, could result in account termination.** (see [self-bots][self-bots]).  
> Use at your own risk! ([discussion](https://github.com/victornpb/undiscord/discussions/273)).
<!-- end legal warning/info -->

## How does it work?

Simply using your Discord account to log-in and listen for new messages on the tracked channel. It uses [discord.py-self] library.

## Installation

1. Install Python 
2. Install required modules.
3. Congrats!

```
pip install -r requirements.txt
```

## Configuration

Enter your credentials to [config](config.py), e.g. below. 

```
# ================== DISCORD SETTINGS ==================
USER_TOKEN = "mytoken"                  

SOURCE_CHANNEL_ID = 11209392130               
DESTINATION_CHANNEL_ID = 21323981930     

# ================== FILE SETTINGS ==================
MAPPING_FILE = "forwarded_mapping.json"            
LOG_REACTIONS = True                             
# ======================================================
```

## Note/Extra

If you won't plan to reuse it again for the same channel, **cleaning [forwarded messages database](forwarded_mapping.json) is recommended after end of usage** since it will never be cleaned automatically. You should keep the json brackets.

----
## ⛔️ DO NOT SHARE YOUR AUTH TOKEN! ⛔️ ##

Sharing your authToken on the internet will give full access to your account! [There are bots gathering credentials all over the internet](https://github.com/rndinfosecguy/Scavenger).
If you post your token by accident, LOGOUT from discord on that **same browser** you got that token imediately.
Changing your password will make sure that you get logged out of every device. I advice that you turn on [2FA](https://support.discord.com/hc/en-us/articles/219576828-Setting-up-Two-Factor-Authentication) afterwards.

If you are unsure do not post screenshots, or logs on the internet.

----
## Security Concerns

Using third-party scripts means you trust that the script’s developer hasn’t inserted malicious functionality into the code and has secured it against attackers trying to do the same. You should never run code you don't trust.

----
#### DISCLAIMER

> THE SOFTWARE AND ALL INFORMATION HERE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
>
> By using any code or information provided here you are agreeing to all parts of the above Disclaimer.


<!-- links/refs -->
[discord.py-self]: https://pypi.org/project/discord.py-self/

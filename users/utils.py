import random
import urllib.parse

def _generate_avatar_url(username: str) -> str:
    color = random.choice(_AVATAR_COLORS)
    name = urllib.parse.quote(username)
    return (
        f"https://ui-avatars.com/api/"
        f"?name={name}&background={color}&color=fff&size=200&bold=true"
    )
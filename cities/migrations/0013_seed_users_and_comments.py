import random
import urllib.parse

from django.contrib.auth.hashers import make_password
from django.db import migrations


_AVATAR_COLORS = [
    'e63946', 'f72585', 'fb5607', 'ffbe0b', '06d6a0',
    '118ab2', '4361ee', '7209b7', 'ef476f', 'bc6c25',
]


def _avatar_url(username):
    color = random.choice(_AVATAR_COLORS)
    name = urllib.parse.quote(username)
    return (
        f"https://ui-avatars.com/api/"
        f"?name={name}&background={color}&color=fff&size=200&bold=true"
    )


# Personas reflecting the app's core audience: Black travelers, African diaspora,
# and mixed-race couples. Used to seed believable comments so city pages aren't empty.
USERS = [
    {
        "username": "aaliyahjay",
        "email": "aaliyah.johnson@example.com",
        "first_name": "Aaliyah",
        "last_name": "Johnson",
    },
    {
        "username": "kwame.mensah",
        "email": "kwame.mensah@example.com",
        "first_name": "Kwame",
        "last_name": "Mensah",
    },
    {
        "username": "amara_d",
        "email": "amara.diallo@example.com",
        "first_name": "Amara",
        "last_name": "Diallo",
    },
    {
        "username": "jcarter88",
        "email": "jamal.carter@example.com",
        "first_name": "Jamal",
        "last_name": "Carter",
    },
    {
        "username": "niathompson",
        "email": "nia.thompson@example.com",
        "first_name": "Nia",
        "last_name": "Thompson",
    },
    {
        "username": "tmoyo",
        "email": "tendai.moyo@example.com",
        "first_name": "Tendai",
        "last_name": "Moyo",
    },
    {
        "username": "yewande.a",
        "email": "yewande.adeyemi@example.com",
        "first_name": "Yewande",
        "last_name": "Adeyemi",
    },
    {
        "username": "andresilvamusic",
        "email": "andre.silva@example.com",
        "first_name": "Andre",
        "last_name": "Silva",
    },
    {
        "username": "emmaandbrad",
        "email": "emma.brad.travels@example.com",
        "first_name": "Emma & Brad",
        "last_name": "Whitfield",
    },
]

# (username, city_slug, score, body)
# Counts are intentionally uneven (1-3 per persona) — real review distributions
# are lumpy, not round-robin.
COMMENTS = [
    (
        "aaliyahjay", "lisbon-portugal", 7,
        "Lisbon surprised me — the African and Cape Verdean communities in Mouraria gave "
        "the city real warmth, and aside from a few stares on the tram, it was nothing "
        "close to what I braced for. Solo Black women, this one's worth it!"
    ),
    (
        "aaliyahjay", "marrakech-morocco", 8,
        "Felt safer here than in plenty of European capitals! The medina vendors don't "
        "let up (true for every visitor, not a race thing). Loved being somewhere "
        "Black-majority for once."
    ),
    (
        "kwame.mensah", "accra-ghana", 10,
        "Akwaaba really means it — my wife and I felt embraced everywhere: markets, "
        "churches, taxis, you name it. If you're diaspora and on the fence, just go."
    ),
    (
        "yewande.a", "accra-ghana", 9,
        "Accra felt like meeting an old relative for the first time — instantly familiar, "
        "instantly warm. The jollof debates alone are worth the trip!"
    ),
    (
        "emmaandbrad", "accra-ghana", 9,
        "Brad's wanted to visit Ghana for years and Accra delivered: Jamestown, Osu, the "
        "food stalls at night. Emma got just as warm a welcome as he did. Already planning "
        "the next trip back!"
    ),
    (
        "kwame.mensah", "dubai-united-arab-emirates", 7,
        "Impressive skyline, impersonal vibe. Incredible experience to leave  at least once."
    ),
    (
        "amara_d", "dakar-senegal", 9,
        "Dakar is where my Senegalese roots and French upbringing finally made sense "
        "together. So many good conversations about identity over ataya tea, and Gorée "
        "Island hit me harder than I expected."
    ),
    (
        "amara_d", "paris-france", 6,
        "Mixed feelings, as always. Château Rouge and Belleville feel like home (full of "
        "African and Caribbean energy), but step into the wrong boutique near the centre "
        "and watch the temperature drop."
    ),
    (
        "jcarter88", "new-orleans-united-states", 9,
        "My partner is white, I'm Black, and New Orleans is the rare US city where we "
        "never felt like the exception. Heavy history in places, but the Tremé and the "
        "music scene made this our favorite trip yet."
    ),
    (
        "tmoyo", "new-orleans-united-states", 8,
        "Didn't expect to feel so at home in the American South — the Tremé's history is "
        "heavy, but the music and the people carry it with such pride. Left with a long "
        "list of places to revisit."
    ),
    (
        "niathompson", "kingston-jamaica", 10,
        "Kingston is home, so of course it scores high from me — but even as a returning "
        "visitor: the welcome from strangers, the music, the food stalls on every corner... "
        "every Black traveler should experience this once."
    ),
    (
        "jcarter88", "kingston-jamaica", 9,
        "Spent a week here with my partner and the warmth caught us both off guard — "
        "strangers waving us into yard parties, vendors cracking jokes nonstop. Loud, "
        "vibrant, unforgettable."
    ),
    (
        "niathompson", "montreal-canada", 8,
        "Little Burgundy reminded me so much of home. Haitian bakeries, Caribbean "
        "grocers, real community. As a Jamaican-Canadian, I could finally exhale here."
    ),
    (
        "niathompson", "bahia-brazil", 9,
        "Found a piece of Jamaica's spirit in Bahia, of all places! Capoeira circles, "
        "drumming, food stalls everywhere. Strangers treated me like family the moment "
        "I said I was from the Caribbean."
    ),
    (
        "tmoyo", "london-united-kingdom", 7,
        "Hard to generalize a city this size. Brixton and Peckham felt like extensions "
        "of the diaspora I grew up around in Harare; other parts, colder. Find your "
        "community and you'll be fine."
    ),
    (
        "yewande.a", "cape-town-south-africa", 8,
        "Traveled with the kids, and my Nigerian-American family had a wonderful time — "
        "Bo-Kaap, the township tours with local guides, District Six Museum. Cape Town "
        "doesn't shy away from its history, and that honesty made us feel respected."
    ),
    (
        "yewande.a", "barcelona-spain", 6,
        "Beautiful city, mostly easy with kids. A couple of run-ins with shopkeepers "
        "left a sour taste, but overall? Glad we went."
    ),
    (
        "andresilvamusic", "salvador-brazil", 10,
        "The most African city I've ever set foot in outside the continent! Performing "
        "in Pelourinho during a Candomblé celebration was a full-circle moment for me as "
        "an Afro-Brazilian musician. This city wears its Black heritage with pride."
    ),
    (
        "andresilvamusic", "lisbon-portugal", 7,
        "Brazilian and Cape Verdean communities here feel like home. Short stop, would "
        "absolutely return."
    ),
    (
        "emmaandbrad", "san-francisco-united-states", 8,
        "We're a mixed couple — Emma's white British, Brad's Black American — and SF is "
        "one of the few US cities where genuinely nobody looked twice at us. The Fillmore "
        "has real Black history, and the food reflects it. Pricey, but worth it!"
    ),
    (
        "emmaandbrad", "cartagena-colombia", 7,
        "Afro-Colombian heritage everywhere you look: the music, the food, the Getsemaní "
        "murals. Locals were happy to talk to Brad about Palenque and the maroon history. "
        "Street vendors are relentless, but hey — that's every tourist destination, isn't it?"
    ),
]


def seed_users_and_comments(apps, schema_editor):
    User = apps.get_model("users", "User")
    City = apps.get_model("cities", "City")
    Comment = apps.get_model("cities", "Comment")

    user_by_username = {}
    for data in USERS:
        user, _ = User.objects.get_or_create(
            username=data["username"],
            defaults={
                "email": data["email"],
                "first_name": data["first_name"],
                "last_name": data["last_name"],
                "avatar_url": _avatar_url(data["username"]),
                "password": make_password(None),
                "is_active": True,
                "email_verified": True,
            },
        )
        user_by_username[data["username"]] = user

    for username, slug, score, body in COMMENTS:
        try:
            city = City.objects.get(slug=slug)
        except City.DoesNotExist:
            continue
        Comment.objects.get_or_create(
            city=city,
            author=user_by_username[username],
            body=body,
            defaults={"score": score, "is_approved": True},
        )


def unseed_users_and_comments(apps, schema_editor):
    User = apps.get_model("users", "User")
    Comment = apps.get_model("cities", "Comment")

    usernames = [data["username"] for data in USERS]
    Comment.objects.filter(author__username__in=usernames).delete()
    User.objects.filter(username__in=usernames).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("cities", "0012_city_base_score"),
        ("users", "0003_user_email_verified"),
    ]

    operations = [
        migrations.RunPython(seed_users_and_comments, reverse_code=unseed_users_and_comments),
    ]

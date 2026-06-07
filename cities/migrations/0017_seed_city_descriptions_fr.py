# Hand-authored French translations of City.description / meta_description.
#
# Written directly as static seed content (same approach as the original
# English seed migration) rather than via any translation service — avoids
# both the cost of a paid API and the unreliability of free ones.

from django.db import migrations

DESCRIPTIONS_FR = {
    "paris-france": (
        "Paris est la capitale de la France et l'une des villes les plus visitées au monde, "
        "connue pour son art, sa gastronomie et ses monuments emblématiques. La ville abrite "
        "une communauté diasporique africaine et caribéenne de longue date, en particulier "
        "dans des quartiers comme Château-Rouge et Belleville. Les voyageurs noirs rapportent "
        "une atmosphère globalement accueillante dans les zones touristiques, bien que le "
        "profilage racial par la police reste un problème documenté."
    ),
    "nice-france": (
        "Nice est une ville baignée de soleil sur la Côte d'Azur, appréciée pour ses plages, "
        "sa vieille ville et sa cuisine méditerranéenne. Elle est moins cosmopolite que Paris, "
        "et la région des Alpes-Maritimes environnante a une histoire politique plutôt à "
        "droite. Les touristes noirs sont généralement bien accueillis dans les zones "
        "touristiques, mais la ville manque de la communauté diasporique africaine visible "
        "que l'on trouve dans la capitale."
    ),
    "lyon-france": (
        "Lyon est la capitale gastronomique de la France et une ville classée au patrimoine "
        "mondial de l'UNESCO, célèbre pour son centre historique Renaissance et sa scène "
        "culinaire animée. La ville accueille une importante communauté ouest-africaine et "
        "nord-africaine, ce qui ajoute à sa diversité culturelle. Les voyageurs noirs trouvent "
        "généralement Lyon accueillante, bien que les expériences puissent varier en dehors "
        "du centre-ville."
    ),
    "bordeaux-france": (
        "Bordeaux est une élégante ville portuaire du sud-ouest de la France, mondialement "
        "connue pour son vin et son architecture du XVIIIe siècle remarquablement préservée. "
        "C'est une ville universitaire à la population internationale croissante, bien "
        "qu'elle reste majoritairement blanche comparée à Paris ou Lyon. Les voyageurs noirs "
        "venant pour l'œnotourisme ou la culture rapportent généralement des expériences "
        "neutres à positives."
    ),
    "barcelona-spain": (
        "Barcelone est la capitale cosmopolite de la Catalogne, réputée pour son architecture "
        "de Gaudí, ses plages et sa vie nocturne animée. La ville est généralement considérée "
        "comme l'une des plus diverses et des plus ouvertes d'Espagne, avec une importante "
        "communauté immigrée latino-américaine et africaine. Les voyageurs noirs classent "
        "régulièrement Barcelone parmi les destinations européennes les plus accueillantes."
    ),
    "madrid-spain": (
        "Madrid est la capitale cosmopolite et le centre culturel de l'Espagne, abritant des "
        "musées de renommée mondiale, une excellente gastronomie et une vie nocturne animée. "
        "La ville s'est considérablement diversifiée au cours des deux dernières décennies, "
        "avec des communautés africaines et latino-américaines bien établies. La plupart des "
        "voyageurs noirs rapportent des interactions agréables et chaleureuses dans toute "
        "la ville."
    ),
    "seville-spain": (
        "Séville est la capitale historique de l'Andalousie, célèbre pour le flamenco, les "
        "tapas et une remarquable architecture mauresque. Moins cosmopolite que Madrid ou "
        "Barcelone, Séville compte moins de résidents noirs mais reste très orientée vers le "
        "tourisme et globalement accueillante. Les voyageurs noirs apprécient la chaleur et "
        "la culture de la ville, bien que les regards insistants soient signalés plus "
        "fréquemment que dans les grandes villes espagnoles."
    ),
    "valencia-spain": (
        "Valence est la troisième ville d'Espagne, célèbre pour sa paella, sa futuriste Cité "
        "des Arts et des Sciences, et son mode de vie méditerranéen détendu. La ville a une "
        "population internationale croissante et est généralement considérée comme amicale "
        "et décontractée. Les voyageurs noirs trouvent généralement Valence accueillante, "
        "avec très peu d'incidents signalés."
    ),
    "new-york-united-states": (
        "New York est l'une des métropoles les plus diverses au monde, avec une importante "
        "population afro-américaine, caribéenne et immigrée africaine répartie dans les cinq "
        "arrondissements. Harlem, Bedford-Stuyvesant et Jamaica sont des centres historiques "
        "de la culture noire. La ville obtient un score élevé en matière d'accueil des "
        "voyageurs noirs, offrant une représentation culturelle profonde, des commerces "
        "appartenant à des Noirs et de solides réseaux communautaires."
    ),
    "los-angeles-united-states": (
        "Los Angeles est une ville tentaculaire et ensoleillée abritant l'une des plus "
        "grandes communautés noires des États-Unis, centrée sur des quartiers comme Leimert "
        "Park, Inglewood et Compton. L'industrie du divertissement y a historiquement mis en "
        "valeur la culture noire. Les voyageurs noirs y trouvent un environnement familier "
        "et culturellement riche, bien que les inégalités socio-économiques et les disparités "
        "policières restent de réelles préoccupations."
    ),
    "new-orleans-united-states": (
        "La Nouvelle-Orléans est l'une des villes les plus singulières des États-Unis sur le "
        "plan culturel, profondément façonnée par les héritages africain, caribéen et "
        "créole. Le jazz, les défilés « second line » et le Mardi Gras ont tous des racines "
        "noires profondes. Les voyageurs noirs classent systématiquement la Nouvelle-Orléans "
        "parmi les meilleures destinations, avec une cuisine et une musique exceptionnelles, "
        "et une communauté visiblement fière de son histoire afro-américaine."
    ),
    "beijing-china": (
        "Pékin est l'ancienne capitale et le centre politique de la Chine, abritant la Cité "
        "interdite, la Grande Muraille et certains des monuments historiques les plus "
        "importants au monde. Les voyageurs noirs rapportent des regards fréquents et des "
        "demandes de photos non sollicitées, et des cas documentés de discrimination dans le "
        "logement et les services existent. L'expérience est globalement sûre mais peut "
        "sembler socialement inconfortable pour les visiteurs visiblement différents."
    ),
    "shanghai-china": (
        "Shanghai est le principal centre financier de la Chine et sa ville la plus "
        "cosmopolite, avec une scène internationale sophistiquée dans des quartiers comme la "
        "Concession française. Elle est plus exposée à l'international que la plupart des "
        "villes chinoises, ce qui peut faciliter les interactions, mais les voyageurs noirs "
        "continuent de signaler des regards insistants, des gestes non sollicités pour "
        "toucher leurs cheveux et parfois une discrimination dans les services."
    ),
    "xian-china": (
        "Xi'an est l'une des plus anciennes villes de Chine et le terminus oriental de "
        "l'ancienne Route de la Soie, surtout connue pour son armée de terre cuite. Elle "
        "reçoit moins de visiteurs internationaux que Pékin ou Shanghai, ce qui rend les "
        "voyageurs noirs plus visibles et susceptibles d'attirer des regards prolongés et "
        "des demandes de photos. La ville est sûre, mais cette curiosité ouverte peut "
        "sembler intrusive."
    ),
    "guangzhou-china": (
        "Guangzhou abrite l'une des plus grandes communautés commerciales africaines d'Asie, "
        "centrée sur le quartier de Xiaobei. Malgré cette présence, des résidents et "
        "voyageurs noirs ont signalé des discriminations dans le logement, les hôtels et les "
        "espaces publics, ce qui a attiré l'attention internationale pendant la période de "
        "la COVID-19. Les expériences varient considérablement : certains trouvent une "
        "communauté familière, d'autres font face à des préjugés ouverts."
    ),
    "rome-italy": (
        "Rome est la capitale éternelle de l'Italie, débordante de ruines antiques, d'art de "
        "renommée mondiale et d'une cuisine exceptionnelle. Le tourisme est son principal "
        "moteur, et la plupart des interactions dans le centre historique sont "
        "professionnelles et accueillantes. Les voyageurs noirs rapportent des expériences "
        "globalement positives en tant que touristes, bien que des incidents racistes et des "
        "graffitis anti-Noirs aient été documentés, et que le harcèlement de rue visant les "
        "femmes noires soit signalé."
    ),
    "florence-italy": (
        "Florence est le berceau de la Renaissance, attirant des millions de visiteurs grâce "
        "à ses collections d'art, son architecture et sa cuisine inégalées. C'est une ville "
        "majoritairement blanche, moins diversifiée sur le plan ethnique que Rome ou Milan, "
        "et certains voyageurs noirs disent s'y sentir visibles ou être confrontés à des "
        "préjugés subtils. Les zones touristiques sont généralement accueillantes, mais "
        "l'expérience vécue en dehors peut varier."
    ),
    "venice-italy": (
        "Venise est une ville d'une beauté unique construite sur une lagune, célèbre pour "
        "ses canaux, son carnaval et son architecture byzantino-gothique. Très dépendante du "
        "tourisme, la ville est habituée aux visiteurs internationaux de tous horizons. Les "
        "voyageurs noirs y vivent généralement des séjours sans incident, bien que la "
        "diminution de sa population permanente signifie globalement moins de diversité "
        "culturelle."
    ),
    "milan-italy": (
        "Milan est la capitale italienne de la mode et de la finance, bien plus cosmopolite "
        "et tournée vers l'international que les autres villes italiennes. La ville compte "
        "une importante communauté immigrée africaine et une main-d'œuvre internationale "
        "diversifiée dans les secteurs du design et de la finance. Les voyageurs noirs "
        "trouvent Milan nettement plus accueillante que les villes italiennes plus petites, "
        "bien que la discrimination raciale soit encore présente dans certains contextes."
    ),
    "istanbul-turkey": (
        "Istanbul est à cheval sur l'Europe et l'Asie et constitue depuis des millénaires un "
        "carrefour de civilisations. La ville est une destination touristique majeure très "
        "habituée aux visiteurs internationaux, et la plupart des voyageurs noirs rapportent "
        "des interactions amicales, curieuses et respectueuses. Les voyageurs originaires "
        "d'Afrique subsaharienne signalent parfois une curiosité non sollicitée, mais les "
        "incidents graves restent rares."
    ),
    "antalya-turkey": (
        "Antalya est la principale destination balnéaire de Turquie sur la côte "
        "méditerranéenne turquoise, attirant des dizaines de millions de touristes chaque "
        "année. Son économie tournée vers le tourisme balnéaire signifie que le personnel "
        "est formé pour accueillir des visiteurs internationaux de tous horizons. Les "
        "voyageurs noirs trouvent généralement Antalya hospitalière, bien que la ville offre "
        "une profondeur culturelle limitée au-delà du tourisme balnéaire."
    ),
    "cappadocia-turkey": (
        "La Cappadoce est un paysage volcanique surréaliste du centre de la Turquie, célèbre "
        "pour ses cheminées de fées, ses hôtels troglodytes et ses vols en montgolfière au "
        "lever du soleil au-dessus de la vallée. L'économie de la région repose entièrement "
        "sur le tourisme international, et les voyageurs noirs rapportent un accueil "
        "chaleureux et peu d'incidents. C'est une destination incontournable qui attire une "
        "foule mondialement diverse."
    ),
    "izmir-turkey": (
        "Izmir est la troisième plus grande ville de Turquie et est réputée pour être la "
        "plus laïque et la plus libérale, avec un caractère égéen détendu très différent "
        "d'Istanbul. La ville compte une communauté étudiante et expatriée internationale "
        "en pleine croissance. Les voyageurs noirs y rapportent des expériences généralement "
        "positives et discrètes, avec moins de pression touristique qu'à Istanbul ou Antalya."
    ),
    "mexico-city-mexico": (
        "Mexico est l'une des capitales les plus grandes et les plus riches culturellement "
        "de l'hémisphère occidental, avec des musées de renommée mondiale, une excellente "
        "gastronomie et une scène artistique florissante. La ville est cosmopolite et "
        "globalement accueillante envers les visiteurs internationaux de tous horizons. Les "
        "voyageurs noirs — y compris ceux d'héritage afro-mexicain originaires de la région "
        "de Costa Chica — y trouvent une ville curieuse et ouverte, bien que le colorisme "
        "reste une réalité sociale documentée dans la culture mexicaine."
    ),
    "cancun-mexico": (
        "Cancún est la destination balnéaire la plus visitée du Mexique, une ville-station "
        "construite spécifiquement sur la côte des Caraïbes pour accueillir les touristes "
        "internationaux toute l'année. La zone hôtelière est conçue pour servir tous les "
        "visiteurs internationaux, et la plupart des voyageurs noirs rapportent des "
        "expériences agréables et sans heurts dans les complexes touristiques. En dehors de "
        "la zone touristique, les expériences peuvent être plus variables."
    ),
    "oaxaca-mexico": (
        "Oaxaca est une ville au riche patrimoine culturel dans le sud du Mexique, célébrée "
        "pour son héritage zapotèque indigène, sa cuisine remarquable et sa scène artistique "
        "vibrante. L'État d'Oaxaca abrite également la communauté afro-mexicaine de la Costa "
        "Chica, conférant à la région des racines diasporiques africaines authentiques. Les "
        "voyageurs noirs trouvent Oaxaca chaleureuse et sincèrement curieuse des liens "
        "culturels partagés."
    ),
    "tulum-mexico": (
        "Tulum est une ville côtière branchée de la péninsule du Yucatán, connue pour ses "
        "ruines mayas surplombant les Caraïbes, ses cénotes et son ambiance balnéaire "
        "bohème. Elle attire une clientèle mondiale et cosmopolite, et les voyageurs noirs "
        "rapportent généralement des expériences confortables et inclusives. La ville est "
        "devenue ces dernières années une destination notable au sein des communautés de "
        "voyageurs noirs."
    ),
    "berlin-germany": (
        "Berlin est la capitale allemande, audacieuse et multiculturelle, réputée pour sa "
        "politique progressiste, sa vie nocturne de renommée mondiale et sa scène artistique "
        "florissante. La ville compte d'importantes communautés africaines et "
        "afro-allemandes, en particulier dans des quartiers comme Neukölln et Wedding. Les "
        "voyageurs noirs classent systématiquement Berlin parmi les villes les plus "
        "accueillantes d'Europe continentale."
    ),
    "munich-germany": (
        "Munich est la prospère capitale de la Bavière, célèbre pour l'Oktoberfest, ses "
        "brasseries en plein air et sa proximité avec les Alpes. Elle est nettement moins "
        "diversifiée que Berlin, Hambourg ou Francfort, et certains voyageurs noirs disent "
        "s'y sentir plus visibles. Les expériences y sont généralement sûres, mais le "
        "caractère homogène de la ville peut donner aux visiteurs non blancs le sentiment "
        "d'être plus étrangers."
    ),
    "hamburg-germany": (
        "Hambourg est la principale ville portuaire d'Allemagne et sa deuxième plus grande "
        "ville, avec une longue histoire de commerce international et un caractère "
        "cosmopolite et diversifié. La ville compte une communauté africaine et "
        "afro-allemande visible, et les voyageurs noirs y rapportent généralement des "
        "expériences positives. Les quartiers de Schanzenviertel et HafenCity sont "
        "particulièrement diversifiés et accueillants."
    ),
    "frankfurt-germany": (
        "Francfort est le centre financier de l'Allemagne et l'une des villes les plus "
        "internationales d'Europe, abritant la Banque centrale européenne et un important "
        "aéroport mondial. Sa population multinationale d'entreprise la rend visiblement "
        "diverse, et les voyageurs noirs y trouvent une ville habituée aux visiteurs "
        "internationaux de tous horizons. Les quartiers de Sachsenhausen et Nordend offrent "
        "des atmosphères accueillantes et cosmopolites."
    ),
    "bangkok-thailand": (
        "Bangkok est la capitale animée et chaotique de la Thaïlande, célèbre pour ses "
        "temples ornés, sa street food et sa vie nocturne légendaire. La culture "
        "thaïlandaise valorise la peau claire et le colorisme est répandu dans les médias et "
        "la publicité, ce qui peut se traduire par un traitement subtilement différent dans "
        "certains contextes. La plupart des voyageurs noirs rapportent des interactions "
        "amicales et curieuses dans une ville tournée vers l'hospitalité."
    ),
    "chiang-mai-thailand": (
        "Chiang Mai est la capitale culturelle du nord de la Thaïlande, une ville au rythme "
        "plus lent entourée de montagnes, célèbre pour ses temples historiques, ses "
        "sanctuaires d'éléphants et sa communauté de nomades numériques. Très orientée vers "
        "le tourisme, elle offre généralement un accueil chaleureux aux voyageurs noirs, "
        "bien que le même colorisme culturel présent à Bangkok s'y retrouve également."
    ),
    "phuket-thailand": (
        "Phuket est la plus grande île de Thaïlande et sa destination balnéaire la plus "
        "populaire, attirant des millions de touristes internationaux sur ses plages de "
        "sable blanc et ses eaux turquoise. Son économie touristique fait que le secteur de "
        "l'hôtellerie est rodé à l'accueil d'une clientèle diverse, et les voyageurs noirs y "
        "passent généralement des séjours agréables et sans incident dans les zones "
        "touristiques."
    ),
    "krabi-thailand": (
        "Krabi est une province pittoresque de la côte thaïlandaise de la mer d'Andaman, "
        "connue pour ses spectaculaires pitons calcaires, ses plages immaculées et son "
        "excellente escalade. Moins développée que Phuket, elle a une ambiance plus "
        "détendue et accueillante pour les routards. Les voyageurs noirs y rapportent des "
        "expériences globalement similaires à celles des autres destinations balnéaires "
        "thaïlandaises — sûres et hospitalières au sein de la zone touristique."
    ),
    "london-united-kingdom": (
        "Londres est l'une des villes les plus diverses au monde, avec des communautés "
        "noires britanniques bien établies à Brixton, Hackney, Peckham et au-delà. La ville "
        "entretient des liens historiques et culturels profonds avec la diaspora africaine "
        "et caribéenne, et les voyageurs noirs y trouvent une ville où ils sont très "
        "visibles, culturellement représentés et largement bien accueillis. Elle reste une "
        "destination de premier plan dans les guides de voyage destinés aux voyageurs noirs "
        "du monde entier."
    ),
    "edinburgh-united-kingdom": (
        "Édimbourg est la saisissante capitale de l'Écosse, perchée entre une ancienne "
        "falaise volcanique et une nouvelle ville géorgienne, célèbre pour son château, son "
        "festival et son whisky. Elle est nettement moins diversifiée que Londres, et "
        "certains voyageurs noirs disent s'y sentir plus visibles, en particulier en dehors "
        "du centre touristique. La ville est globalement sûre et accueillante, mais manque "
        "des infrastructures communautaires noires que l'on trouve plus au sud."
    ),
    "manchester-united-kingdom": (
        "Manchester est la dynamique deuxième ville d'Angleterre, connue pour son "
        "patrimoine musical, le football et une population diversifiée façonnée par des "
        "vagues d'immigration en provenance des Caraïbes, d'Asie du Sud et d'Afrique de "
        "l'Ouest. Moss Side, Hulme et Longsight abritent des communautés noires britanniques "
        "bien établies. Les voyageurs noirs trouvent Manchester familière, vibrante et "
        "culturellement engagée."
    ),
    "liverpool-united-kingdom": (
        "Liverpool entretient des liens historiques avec l'Afrique à travers la traite "
        "transatlantique des esclaves, une histoire reconnue au Musée international de "
        "l'esclavage sur les quais. La ville abrite l'une des plus anciennes communautés "
        "noires de Grande-Bretagne, et les voyageurs noirs y trouvent une ville à la "
        "profondeur culturelle authentique et à l'accueil chaleureux et populaire. La "
        "culture musicale et footballistique vibrante de Liverpool ajoute à son attrait."
    ),
    "accra-ghana": (
        "Accra est la capitale du Ghana et l'une des destinations les plus importantes pour "
        "la diaspora africaine, portée par l'initiative gouvernementale « Year of Return » "
        "invitant les descendants d'Africains réduits en esclavage à rentrer au pays. La "
        "ville offre une expérience profondément valorisante pour les voyageurs noirs, avec "
        "une riche culture ghanéenne, une scène nocturne afrobeats florissante, des forts "
        "esclavagistes historiques le long de la côte et une chaleur communautaire sincère."
    ),
    "cape-town-south-africa": (
        "Le Cap est l'une des villes les plus spectaculaires au monde sur le plan paysager, "
        "nichée au pied de la montagne de la Table à la pointe sud de l'Afrique. L'héritage "
        "de l'apartheid reste visible dans les inégalités spatiales entre quartiers "
        "majoritairement blancs et quartiers métis/noirs. Pour les voyageurs noirs, la ville "
        "offre une beauté naturelle à couper le souffle et des expériences culturelles "
        "afrikaner, xhosa et cape malay, bien qu'il soit conseillé de rester conscient des "
        "dynamiques raciales persistantes."
    ),
    "salvador-brazil": (
        "Salvador de Bahia est souvent qualifiée de ville la plus africaine en dehors de "
        "l'Afrique — plus de 80 % de sa population est d'ascendance africaine, et la "
        "culture, la cuisine, la musique et la religion (Candomblé) de la ville sont "
        "profondément enracinées dans les traditions ouest-africaines. Pour les voyageurs "
        "noirs, Salvador offre une expérience rare d'appartenance culturelle profonde, "
        "célébrée à travers le Carnaval, la capoeira et l'acarajé à chaque coin de rue."
    ),
    "lisbon-portugal": (
        "Lisbonne est régulièrement citée dans les guides de voyage pour les voyageurs "
        "noirs comme l'une des capitales les plus accueillantes d'Europe. Les liens "
        "historiques profonds du Portugal avec l'Afrique et le Brésil ont donné naissance à "
        "une importante communauté afro-portugaise — notamment originaire du Cap-Vert, "
        "d'Angola et du Mozambique — qui fait que les voyageurs noirs s'y sentent vus et "
        "chez eux. Des quartiers comme Mouraria et Intendente vibrent au rythme de la "
        "culture afro-portugaise."
    ),
    "dakar-senegal": (
        "Dakar est la capitale la plus occidentale d'Afrique et une fière plaque tournante "
        "de la culture, de la musique et de l'art panafricains. La Teranga — le concept "
        "wolof de l'hospitalité — est une valeur culturelle fondamentale, et les voyageurs "
        "de la diaspora décrivent régulièrement Dakar comme une expérience transformatrice : "
        "une ville où ils se sentent racialement invisibles au meilleur sens du terme, "
        "entourés d'une identité africaine moderne et florissante."
    ),
    "marrakech-morocco": (
        "Marrakech est la ville la plus visitée du Maroc, une explosion sensorielle de "
        "marchés d'épices, de riads et de l'immense place Jemaa el-Fna. En tant que ville "
        "africaine à majorité noire et amazighe, les voyageurs noirs de la diaspora trouvent "
        "souvent Marrakech plus détendue que les destinations européennes. Les interactions "
        "y sont généralement chaleureuses, bien que l'attention insistante des vendeurs dans "
        "la médina touche tous les touristes de la même façon."
    ),
    "kingston-jamaica": (
        "Kingston est la capitale culturelle de la Jamaïque et le berceau du reggae, du "
        "dancehall et du ska. En tant que ville majoritairement noire, elle offre un "
        "environnement immédiatement valorisant pour les voyageurs de la diaspora africaine "
        "en quête de connexion culturelle. Le musée Bob Marley, la galerie nationale et une "
        "scène de street food vibrante en font une destination riche, bien que les "
        "visiteurs doivent rester attentifs à la sécurité des quartiers comme dans toute "
        "grande ville."
    ),
    "montreal-canada": (
        "Montréal est la ville la plus vibrante culturellement du Canada — bilingue, "
        "cosmopolite, et abritant une importante communauté diasporique haïtienne et "
        "afro-caribéenne, en particulier dans les quartiers de la Petite-Bourgogne et de "
        "Côte-des-Neiges. Les voyageurs noirs classent régulièrement Montréal parmi les "
        "villes les plus accueillantes d'Amérique du Nord, avec une scène artistique noire "
        "florissante, une excellente gastronomie et une culture urbaine véritablement "
        "diverse."
    ),
    "bahia-brazil": (
        "Bahia — centrée sur Salvador de Bahia — est souvent qualifiée de ville la plus "
        "africaine en dehors de l'Afrique, avec plus de 80 % de sa population d'ascendance "
        "africaine. La culture, la cuisine, la musique et la religion Candomblé de la ville "
        "sont profondément enracinées dans les traditions ouest-africaines. Pour les "
        "voyageurs noirs, Bahia offre une expérience rare d'appartenance culturelle "
        "profonde, exprimée à travers le Carnaval, la capoeira et l'acarajé à chaque coin "
        "de rue."
    ),
    "cartagena-colombia": (
        "Carthagène est une ville portuaire coloniale classée au patrimoine mondial de "
        "l'UNESCO sur la côte caribéenne de la Colombie, avec une population majoritairement "
        "afro-colombienne. Le quartier de Getsemaní de la ville vibre au rythme de la "
        "culture afro-caribéenne, de la cumbia et de l'art urbain. Les voyageurs noirs "
        "d'Amérique du Nord et des Caraïbes citent régulièrement Carthagène comme l'une des "
        "villes les plus accueillantes d'Amérique latine, avec un profond sentiment "
        "d'identité culturelle partagée."
    ),
    "dubai-united-arab-emirates": (
        "Dubaï est l'une des villes les plus connectées au monde sur le plan international, "
        "attirant des visiteurs venus d'Afrique, d'Asie du Sud et d'Occident. Elle est "
        "extrêmement sûre et accueillante pour les touristes, avec des infrastructures et "
        "des services de classe mondiale. Les voyageurs noirs rapportent des expériences "
        "globalement positives dans les zones touristiques, bien que le colorisme dans "
        "l'embauche et les services ait été documenté, et les voyageurs LGBTQ+ ou ceux qui "
        "ne se conforment pas aux coutumes locales devraient faire preuve de prudence."
    ),
    "singapore-singapore": (
        "Singapour est l'une des villes les plus sûres et les plus efficaces au monde, avec "
        "une société multiraciale construite autour des communautés chinoise, malaise et "
        "indienne. Elle est très internationale, avec une forte présence d'expatriés, et "
        "les voyageurs noirs y rapportent des séjours globalement confortables et sans "
        "incident. L'État de droit strict du pays signifie que la discrimination y est "
        "rarement ouverte, bien que les voyageurs noirs notent que Singapour manque de "
        "repères culturels significatifs liés à la diaspora africaine."
    ),
    "amsterdam-netherlands": (
        "Amsterdam est l'une des villes les plus libérales et ouvertes d'Europe, avec une "
        "communauté surinamienne et antillaise dynamique qui façonne la cuisine, la musique "
        "et la culture de la ville depuis des générations. Des quartiers comme Bijlmer sont "
        "des centres de la vie afro-néerlandaise. Les voyageurs noirs accordent à Amsterdam "
        "de très bonnes notes pour son ouverture et sa diversité, bien que la controverse "
        "annuelle autour de Sinterklaas révèle des tensions culturelles persistantes autour "
        "de la question raciale dont les voyageurs devraient avoir conscience."
    ),
    "san-francisco-united-states": (
        "San Francisco est l'une des villes les plus progressistes des États-Unis, "
        "longtemps façonnée par l'activisme pour les droits civiques et le leadership de la "
        "communauté noire dans le quartier de Fillmore, historiquement surnommé le « Harlem "
        "de l'Ouest ». La gentrification de l'ère technologique a considérablement déplacé "
        "la population noire de la ville — passant de plus de 13 % dans les années 1970 à "
        "environ 5 % aujourd'hui — vidant les quartiers mêmes qui ont forgé la réputation de "
        "la ville. Les voyageurs noirs y trouvent un environnement accueillant et "
        "politiquement conscient, bien que le coût de la vie élevé et la perte des espaces "
        "noirs historiques soient des réalités bien réelles et visibles."
    ),
}

META_TEMPLATE_FR = (
    "{name} est-elle accueillante pour les voyageurs noirs ? "
    "Lisez les avis, découvrez le score d'accueil, trouvez des lieux à visiter."
)


def seed_descriptions_fr(apps, schema_editor):
    City = apps.get_model('cities', 'City')
    for city in City.objects.all():
        description_fr = DESCRIPTIONS_FR.get(city.slug)
        if not description_fr:
            continue
        city.description_fr = description_fr
        city.meta_description_fr = META_TEMPLATE_FR.format(name=city.name)
        city.save(update_fields=['description_fr', 'meta_description_fr'])


def clear_descriptions_fr(apps, schema_editor):
    City = apps.get_model('cities', 'City')
    City.objects.filter(slug__in=DESCRIPTIONS_FR.keys()).update(
        description_fr='', meta_description_fr=''
    )


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0016_city_description_fr'),
    ]

    operations = [
        migrations.RunPython(seed_descriptions_fr, clear_descriptions_fr),
    ]

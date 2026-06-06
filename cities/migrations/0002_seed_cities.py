from django.db import migrations


CITIES = [
    # --- France ---
    {
        "name": "Paris",
        "country": "France",
        "slug": "paris-france",
        "description": (
            "Paris is France's capital and one of the world's most-visited cities, "
            "known for its art, cuisine, and iconic landmarks. The city has a long-standing "
            "African and Caribbean diaspora community, particularly in neighborhoods like "
            "Château-Rouge and Belleville. Black travelers report a generally welcoming "
            "atmosphere in tourist areas, though racial profiling by police remains a documented issue."
        ),
        "welcome_score": 6.5,
        "latitude": 48.856600,
        "longitude": 2.352200,
        "meta_description": "Is Paris welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "Nice",
        "country": "France",
        "slug": "nice-france",
        "description": (
            "Nice is a sun-drenched city on the French Riviera, popular for its beaches, "
            "Old Town, and Mediterranean cuisine. It is less cosmopolitan than Paris, "
            "and the surrounding Alpes-Maritimes region has a history of right-leaning politics. "
            "Black tourists are generally well-received in resort areas, but the city lacks "
            "the visible African diaspora community found in the capital."
        ),
        "welcome_score": 6.0,
        "latitude": 43.710200,
        "longitude": 7.262000,
        "meta_description": "Is Nice welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "Lyon",
        "country": "France",
        "slug": "lyon-france",
        "description": (
            "Lyon is France's gastronomic capital and a UNESCO World Heritage city, "
            "famed for its Renaissance old town and vibrant food scene. The city hosts "
            "a significant West African and North African community, adding to its cultural "
            "diversity. Black travelers generally find Lyon welcoming, though experiences "
            "can vary outside the city center."
        ),
        "welcome_score": 6.5,
        "latitude": 45.764000,
        "longitude": 4.835700,
        "meta_description": "Is Lyon welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "Bordeaux",
        "country": "France",
        "slug": "bordeaux-france",
        "description": (
            "Bordeaux is a handsome port city in southwest France, world-famous for its "
            "wine and well-preserved 18th-century architecture. It is a university city "
            "with a growing international population, though it remains predominantly white "
            "compared to Paris or Lyon. Black travelers visiting for wine tourism or culture "
            "typically report neutral to positive experiences."
        ),
        "welcome_score": 6.5,
        "latitude": 44.837800,
        "longitude": -0.579200,
        "meta_description": "Is Bordeaux welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    # --- Spain ---
    {
        "name": "Barcelona",
        "country": "Spain",
        "slug": "barcelona-spain",
        "description": (
            "Barcelona is Catalonia's cosmopolitan capital, renowned for its Gaudí architecture, "
            "beaches, and vibrant nightlife. The city is generally regarded as one of Spain's "
            "most diverse and open cities, with a significant Latin American and African immigrant "
            "community. Black travelers consistently rate Barcelona among the more welcoming "
            "European destinations."
        ),
        "welcome_score": 7.5,
        "latitude": 41.385100,
        "longitude": 2.173400,
        "meta_description": "Is Barcelona welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "Madrid",
        "country": "Spain",
        "slug": "madrid-spain",
        "description": (
            "Madrid is Spain's cosmopolitan capital and cultural hub, home to world-class "
            "museums, excellent food, and a lively nightlife scene. The city has grown "
            "considerably more diverse over the past two decades, with African and Latin American "
            "communities well established. Most Black travelers report comfortable, welcoming "
            "interactions throughout the city."
        ),
        "welcome_score": 7.0,
        "latitude": 40.416800,
        "longitude": -3.703800,
        "meta_description": "Is Madrid welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "Seville",
        "country": "Spain",
        "slug": "seville-spain",
        "description": (
            "Seville is Andalusia's historic capital, famed for flamenco, tapas, and stunning "
            "Moorish architecture. Less cosmopolitan than Madrid or Barcelona, Seville sees "
            "fewer Black residents but is heavily tourist-oriented and generally hospitable. "
            "Black travelers enjoy the city's warmth and culture, though stares are reported "
            "more frequently than in larger Spanish cities."
        ),
        "welcome_score": 6.5,
        "latitude": 37.389100,
        "longitude": -5.984500,
        "meta_description": "Is Seville welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "Valencia",
        "country": "Spain",
        "slug": "valencia-spain",
        "description": (
            "Valencia is Spain's third-largest city, celebrated for paella, its futuristic "
            "City of Arts and Sciences, and a relaxed Mediterranean lifestyle. The city has "
            "a growing international population and is widely considered friendly and easygoing. "
            "Black travelers generally find Valencia welcoming with minimal incidents reported."
        ),
        "welcome_score": 7.0,
        "latitude": 39.469900,
        "longitude": -0.376300,
        "meta_description": "Is Valencia welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    # --- United States ---
    {
        "name": "New York",
        "country": "United States",
        "slug": "new-york-united-states",
        "description": (
            "New York City is one of the most diverse metropolises on earth, with a massive "
            "African American, Caribbean, and African immigrant population spread across all five "
            "boroughs. Harlem, Bedford-Stuyvesant, and Jamaica are historic centers of Black "
            "culture. The city scores high for welcoming Black travelers, offering deep cultural "
            "representation, Black-owned businesses, and strong community networks."
        ),
        "welcome_score": 8.0,
        "latitude": 40.712800,
        "longitude": -74.006000,
        "meta_description": "Is New York welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "Los Angeles",
        "country": "United States",
        "slug": "los-angeles-united-states",
        "description": (
            "Los Angeles is a sprawling, sun-soaked city with one of the largest Black "
            "communities in the United States, centered in neighborhoods like Leimert Park, "
            "Inglewood, and Compton. The entertainment industry has historically elevated "
            "Black culture here. Black travelers find a familiar, culturally rich environment, "
            "though socioeconomic inequality and policing disparities remain real concerns."
        ),
        "welcome_score": 7.5,
        "latitude": 34.052200,
        "longitude": -118.243700,
        "meta_description": "Is Los Angeles welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "New Orleans",
        "country": "United States",
        "slug": "new-orleans-united-states",
        "description": (
            "New Orleans is one of the most culturally unique cities in America, shaped "
            "profoundly by African, Caribbean, and Creole heritage. Jazz, second-line parades, "
            "and Mardi Gras all have deep Black roots. Black travelers consistently rate "
            "New Orleans as a top destination, with exceptional food, music, and a community "
            "that takes visible pride in its African American history."
        ),
        "welcome_score": 8.5,
        "latitude": 29.951100,
        "longitude": -90.071500,
        "meta_description": "Is New Orleans welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "San Francisco",
        "country": "United States",
        "slug": "san-francisco-united-states",
        "description": (
            "San Francisco is one of the United States' most progressive cities, long shaped "
            "by civil rights activism and Black community leadership in the Fillmore District, "
            "historically known as the 'Harlem of the West.' Tech-era gentrification has "
            "dramatically displaced the city's Black population — from over 13% in the 1970s "
            "to around 5% today — hollowing out the very neighborhoods that gave the city its "
            "reputation. Black travelers find a welcoming, politically aware environment, "
            "though the steep cost of living and loss of historic Black spaces are real and visible."
        ),
        "welcome_score": 7.5,
        "latitude": 37.774900,
        "longitude": -122.419400,
        "meta_description": "Is San Francisco welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    # --- China ---
    {
        "name": "Beijing",
        "country": "China",
        "slug": "beijing-china",
        "description": (
            "Beijing is China's ancient capital and political center, home to the Forbidden City, "
            "the Great Wall, and some of the world's most significant historical monuments. "
            "Black travelers report frequent staring and unsolicited photo requests, and documented "
            "cases of discrimination in housing and services exist. The experience is generally "
            "safe but can feel socially uncomfortable for visitors who are visibly different."
        ),
        "welcome_score": 5.5,
        "latitude": 39.904200,
        "longitude": 116.407400,
        "meta_description": "Is Beijing welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "Shanghai",
        "country": "China",
        "slug": "shanghai-china",
        "description": (
            "Shanghai is China's global financial hub and most cosmopolitan city, with a "
            "sophisticated international scene in neighborhoods like the French Concession. "
            "It is more internationally exposed than most Chinese cities, which can ease "
            "interactions, but Black travelers still report staring, unsolicited touching of hair, "
            "and occasional service discrimination."
        ),
        "welcome_score": 5.5,
        "latitude": 31.230400,
        "longitude": 121.473700,
        "meta_description": "Is Shanghai welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "Xi'an",
        "country": "China",
        "slug": "xian-china",
        "description": (
            "Xi'an is one of China's oldest cities and the eastern terminus of the ancient "
            "Silk Road, most famous for the Terracotta Army. It sees fewer international "
            "visitors than Beijing or Shanghai, meaning Black travelers are more visibly "
            "conspicuous and may attract prolonged stares and photo requests. "
            "The city is safe, but overt curiosity can feel intrusive."
        ),
        "welcome_score": 5.0,
        "latitude": 34.341600,
        "longitude": 108.939800,
        "meta_description": "Is Xi'an welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "Guangzhou",
        "country": "China",
        "slug": "guangzhou-china",
        "description": (
            "Guangzhou hosts one of the largest African trading communities in Asia, "
            "centered on the Xiaobei district. Despite this presence, Black residents and "
            "travelers have reported discrimination in housing, hotels, and public spaces, "
            "which gained international attention during the COVID-19 period. "
            "Experiences are highly variable — some find a familiar community, others face open bias."
        ),
        "welcome_score": 5.5,
        "latitude": 23.129100,
        "longitude": 113.264400,
        "meta_description": "Is Guangzhou welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    # --- Italy ---
    {
        "name": "Rome",
        "country": "Italy",
        "slug": "rome-italy",
        "description": (
            "Rome is Italy's eternal capital, overflowing with ancient ruins, world-class art, "
            "and exceptional food. Tourism is its lifeblood, and most interactions in the "
            "historic center are professional and welcoming. Black travelers report mostly "
            "positive experiences as tourists, though racial incidents and anti-Black graffiti "
            "have been documented, and street harassment targeting Black women is reported."
        ),
        "welcome_score": 6.5,
        "latitude": 41.902800,
        "longitude": 12.496400,
        "meta_description": "Is Rome welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "Florence",
        "country": "Italy",
        "slug": "florence-italy",
        "description": (
            "Florence is the cradle of the Renaissance, drawing millions to its unmatched "
            "art collections, architecture, and cuisine. It is a predominantly white city "
            "with less ethnic diversity than Rome or Milan, and some Black travelers report "
            "feeling conspicuous or encountering subtle bias. Tourist areas are generally "
            "hospitable, but lived experience outside them can vary."
        ),
        "welcome_score": 6.0,
        "latitude": 43.769600,
        "longitude": 11.255800,
        "meta_description": "Is Florence welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "Venice",
        "country": "Italy",
        "slug": "venice-italy",
        "description": (
            "Venice is a uniquely beautiful city built on a lagoon, famous for its canals, "
            "Carnival, and Byzantine-Gothic architecture. Heavily tourist-dependent, the city "
            "is accustomed to international visitors of all backgrounds. Black travelers "
            "generally have uneventful experiences, though the city's shrinking permanent "
            "population means less cultural diversity overall."
        ),
        "welcome_score": 6.5,
        "latitude": 45.440800,
        "longitude": 12.315500,
        "meta_description": "Is Venice welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "Milan",
        "country": "Italy",
        "slug": "milan-italy",
        "description": (
            "Milan is Italy's fashion and financial capital, far more cosmopolitan and "
            "internationally-minded than other Italian cities. The city has a significant "
            "African immigrant community and a diverse international workforce in design "
            "and finance. Black travelers find Milan notably more welcoming than smaller "
            "Italian cities, though racial discrimination is still present in some contexts."
        ),
        "welcome_score": 7.0,
        "latitude": 45.464200,
        "longitude": 9.190000,
        "meta_description": "Is Milan welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    # --- Turkey ---
    {
        "name": "Istanbul",
        "country": "Turkey",
        "slug": "istanbul-turkey",
        "description": (
            "Istanbul straddles Europe and Asia and has been a crossroads of civilizations "
            "for millennia. The city is a major tourist destination highly accustomed to "
            "international visitors, and most Black travelers report friendly, curious, "
            "and respectful interactions. Sub-Saharan African travelers occasionally report "
            "unsolicited curiosity, but serious incidents are uncommon."
        ),
        "welcome_score": 7.0,
        "latitude": 41.008200,
        "longitude": 28.978400,
        "meta_description": "Is Istanbul welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "Antalya",
        "country": "Turkey",
        "slug": "antalya-turkey",
        "description": (
            "Antalya is Turkey's premier beach resort destination on the turquoise Mediterranean "
            "coast, attracting tens of millions of tourists each year. Its resort economy "
            "means service staff are trained to accommodate international guests of all "
            "backgrounds. Black travelers generally find Antalya hospitable, though the city "
            "offers limited cultural depth beyond beach tourism."
        ),
        "welcome_score": 6.5,
        "latitude": 36.896900,
        "longitude": 30.713300,
        "meta_description": "Is Antalya welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "Cappadocia",
        "country": "Turkey",
        "slug": "cappadocia-turkey",
        "description": (
            "Cappadocia is a surreal volcanic landscape in central Turkey, famous for its "
            "fairy chimneys, cave hotels, and hot-air balloon rides over the valley at sunrise. "
            "The area's economy revolves entirely around international tourism, and Black "
            "travelers report welcoming service and few incidents. It is a bucket-list "
            "destination that draws a globally diverse crowd."
        ),
        "welcome_score": 6.5,
        "latitude": 38.643100,
        "longitude": 34.829700,
        "meta_description": "Is Cappadocia welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "Izmir",
        "country": "Turkey",
        "slug": "izmir-turkey",
        "description": (
            "Izmir is Turkey's third-largest city and reputedly its most secular and liberal, "
            "with a relaxed Aegean character very different from Istanbul. The city has a "
            "growing international student and expat community. Black travelers report "
            "generally positive, low-key experiences here, with less tourist-industry "
            "pressure than in Istanbul or Antalya."
        ),
        "welcome_score": 6.5,
        "latitude": 38.419200,
        "longitude": 27.128700,
        "meta_description": "Is Izmir welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    # --- Mexico ---
    {
        "name": "Mexico City",
        "country": "Mexico",
        "slug": "mexico-city-mexico",
        "description": (
            "Mexico City is one of the Western Hemisphere's largest and most culturally rich "
            "capitals, with world-class museums, food, and a thriving arts scene. "
            "The city is cosmopolitan and generally welcoming to international visitors "
            "of all backgrounds. Black travelers — including those of African-Mexican heritage "
            "from the Costa Chica region — find a city curious and open, though colorism "
            "is a documented social reality in Mexican culture."
        ),
        "welcome_score": 7.5,
        "latitude": 19.432600,
        "longitude": -99.133200,
        "meta_description": "Is Mexico City welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "Cancún",
        "country": "Mexico",
        "slug": "cancun-mexico",
        "description": (
            "Cancún is Mexico's most-visited beach destination, a purpose-built resort city "
            "on the Caribbean coast catering to international tourists year-round. "
            "The Hotel Zone is designed to serve all international guests, and most Black "
            "travelers report smooth, pleasant experiences in resort settings. "
            "Outside the tourist zone, experiences may be more variable."
        ),
        "welcome_score": 7.0,
        "latitude": 21.161900,
        "longitude": -86.851500,
        "meta_description": "Is Cancún welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "Oaxaca",
        "country": "Mexico",
        "slug": "oaxaca-mexico",
        "description": (
            "Oaxaca is a richly cultured city in southern Mexico celebrated for its Indigenous "
            "Zapotec heritage, outstanding cuisine, and vibrant arts scene. The state of "
            "Oaxaca is also home to the Afro-Mexican community of the Costa Chica, giving "
            "the region authentic African diasporic roots. Black travelers find Oaxaca "
            "warm and genuinely curious about shared cultural connections."
        ),
        "welcome_score": 7.5,
        "latitude": 17.073200,
        "longitude": -96.726600,
        "meta_description": "Is Oaxaca welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "Tulum",
        "country": "Mexico",
        "slug": "tulum-mexico",
        "description": (
            "Tulum is a trendy coastal town on the Yucatán Peninsula, known for its Maya "
            "ruins perched above the Caribbean, cenotes, and bohemian resort scene. "
            "It attracts a global, cosmopolitan crowd and Black travelers generally report "
            "comfortable, inclusive experiences. The town has become a notable destination "
            "in Black travel communities in recent years."
        ),
        "welcome_score": 7.0,
        "latitude": 20.211400,
        "longitude": -87.465400,
        "meta_description": "Is Tulum welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    # --- Germany ---
    {
        "name": "Berlin",
        "country": "Germany",
        "slug": "berlin-germany",
        "description": (
            "Berlin is Germany's edgy, multicultural capital with a reputation for progressive "
            "politics, world-class nightlife, and a thriving arts scene. The city has "
            "significant African and Afro-German communities, particularly in neighborhoods "
            "like Neukölln and Wedding. Black travelers consistently rate Berlin as one of "
            "the most welcoming cities in continental Europe."
        ),
        "welcome_score": 7.5,
        "latitude": 52.520000,
        "longitude": 13.405000,
        "meta_description": "Is Berlin welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "Munich",
        "country": "Germany",
        "slug": "munich-germany",
        "description": (
            "Munich is Bavaria's prosperous capital, famous for Oktoberfest, beer gardens, "
            "and proximity to the Alps. It is notably less diverse than Berlin, Hamburg, "
            "or Frankfurt, and some Black travelers report feeling more conspicuous here. "
            "Experiences are generally safe, but the city's homogeneous character can "
            "make non-white visitors feel more like outsiders."
        ),
        "welcome_score": 6.5,
        "latitude": 48.135100,
        "longitude": 11.582000,
        "meta_description": "Is Munich welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "Hamburg",
        "country": "Germany",
        "slug": "hamburg-germany",
        "description": (
            "Hamburg is Germany's major port city and second-largest city, with a long "
            "history of international trade and a diverse, cosmopolitan character. "
            "The city has a visible African and Afro-German community, and Black travelers "
            "generally report positive experiences. The Schanzenviertel and HafenCity "
            "neighborhoods are particularly diverse and welcoming."
        ),
        "welcome_score": 7.0,
        "latitude": 53.551100,
        "longitude": 9.993700,
        "meta_description": "Is Hamburg welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "Frankfurt",
        "country": "Germany",
        "slug": "frankfurt-germany",
        "description": (
            "Frankfurt is Germany's financial hub and one of Europe's most international "
            "cities, home to the European Central Bank and a major global airport. "
            "Its multinational corporate population makes it visibly diverse, and Black "
            "travelers find a city accustomed to international visitors of all backgrounds. "
            "The Sachsenhausen and Nordend neighborhoods offer welcoming, cosmopolitan atmospheres."
        ),
        "welcome_score": 7.0,
        "latitude": 50.110900,
        "longitude": 8.682100,
        "meta_description": "Is Frankfurt welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    # --- Thailand ---
    {
        "name": "Bangkok",
        "country": "Thailand",
        "slug": "bangkok-thailand",
        "description": (
            "Bangkok is Thailand's vibrant, chaotic capital, famous for ornate temples, "
            "street food, and a legendary nightlife scene. Thai culture prizes light skin "
            "and colorism is prevalent in media and advertising, which can translate to "
            "subtly different treatment in some contexts. Most Black travelers report "
            "friendly, curious interactions and a city focused on hospitality."
        ),
        "welcome_score": 6.5,
        "latitude": 13.756300,
        "longitude": 100.501800,
        "meta_description": "Is Bangkok welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "Chiang Mai",
        "country": "Thailand",
        "slug": "chiang-mai-thailand",
        "description": (
            "Chiang Mai is northern Thailand's cultural capital, a slower-paced city "
            "surrounded by mountains and famed for its historic temples, elephant sanctuaries, "
            "and digital nomad community. It is highly tourist-oriented and Black travelers "
            "report a generally welcoming atmosphere, though the same cultural colorism "
            "present in Bangkok applies here as well."
        ),
        "welcome_score": 6.5,
        "latitude": 18.788300,
        "longitude": 98.985300,
        "meta_description": "Is Chiang Mai welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "Phuket",
        "country": "Thailand",
        "slug": "phuket-thailand",
        "description": (
            "Phuket is Thailand's largest island and most popular beach destination, "
            "drawing millions of international tourists to its white sand beaches and "
            "turquoise waters. The resort economy means the hospitality sector is "
            "well-practiced with diverse guests, and Black travelers typically have "
            "comfortable, incident-free stays in tourist areas."
        ),
        "welcome_score": 6.5,
        "latitude": 7.880400,
        "longitude": 98.392300,
        "meta_description": "Is Phuket welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "Krabi",
        "country": "Thailand",
        "slug": "krabi-thailand",
        "description": (
            "Krabi is a scenic province on Thailand's Andaman coast, known for dramatic "
            "limestone karsts, pristine beaches, and excellent rock climbing. Less "
            "developed than Phuket, it has a more relaxed, backpacker-friendly vibe. "
            "Black travelers report experiences broadly similar to other Thai resort "
            "destinations — safe and hospitable within the tourist zone."
        ),
        "welcome_score": 6.5,
        "latitude": 8.086300,
        "longitude": 98.906300,
        "meta_description": "Is Krabi welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    # --- United Kingdom ---
    {
        "name": "London",
        "country": "United Kingdom",
        "slug": "london-united-kingdom",
        "description": (
            "London is one of the world's most diverse cities, with long-established "
            "Black British communities in Brixton, Hackney, Peckham, and beyond. "
            "The city has deep historical and cultural ties to the African and Caribbean "
            "diaspora, and Black travelers find a city where they are highly visible, "
            "culturally represented, and largely welcomed. It remains a top destination "
            "in Black travel guides globally."
        ),
        "welcome_score": 8.0,
        "latitude": 51.507400,
        "longitude": -0.127800,
        "meta_description": "Is London welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "Edinburgh",
        "country": "United Kingdom",
        "slug": "edinburgh-united-kingdom",
        "description": (
            "Edinburgh is Scotland's striking capital, perched between an ancient volcanic "
            "crag and a Georgian new town, famous for its castle, festival, and whisky. "
            "It is significantly less diverse than London and some Black travelers report "
            "feeling conspicuous, particularly outside the tourist center. "
            "The city is generally safe and hospitable, but lacks the cultural Black "
            "community infrastructure found further south."
        ),
        "welcome_score": 7.0,
        "latitude": 55.953300,
        "longitude": -3.188300,
        "meta_description": "Is Edinburgh welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "Manchester",
        "country": "United Kingdom",
        "slug": "manchester-united-kingdom",
        "description": (
            "Manchester is England's dynamic second city, known for its music heritage, "
            "football, and a diverse population shaped by waves of immigration from "
            "the Caribbean, South Asia, and West Africa. Moss Side, Hulme, and Longsight "
            "have well-established Black British communities. Black travelers find "
            "Manchester familiar, vibrant, and culturally engaged."
        ),
        "welcome_score": 7.5,
        "latitude": 53.480800,
        "longitude": -2.242600,
        "meta_description": "Is Manchester welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "Liverpool",
        "country": "United Kingdom",
        "slug": "liverpool-united-kingdom",
        "description": (
            "Liverpool has historical ties to Africa through the transatlantic slave trade, "
            "and acknowledges this history at the International Slavery Museum on the waterfront. "
            "The city has one of the oldest Black communities in Britain, and Black travelers "
            "find a city with genuine cultural depth and a warm, working-class welcome. "
            "Liverpool's vibrant music and football culture adds to its appeal."
        ),
        "welcome_score": 7.5,
        "latitude": 53.408400,
        "longitude": -2.991600,
        "meta_description": "Is Liverpool welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    # --- Group B: Top 5 cities for Black travelers / African diaspora ---
    {
        "name": "Accra",
        "country": "Ghana",
        "slug": "accra-ghana",
        "description": (
            "Accra is the capital of Ghana and one of the most important destinations for "
            "the African diaspora, amplified by the government's 'Year of Return' initiative "
            "inviting descendants of enslaved Africans home. The city offers a deeply affirming "
            "experience for Black travelers, with rich Ghanaian culture, thriving Afrobeats "
            "nightlife, historic slave castles along the coast, and genuine community warmth."
        ),
        "welcome_score": 9.0,
        "latitude": 5.603700,
        "longitude": -0.187000,
        "meta_description": "Is Accra welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "Cape Town",
        "country": "South Africa",
        "slug": "cape-town-south-africa",
        "description": (
            "Cape Town is one of the world's most scenically stunning cities, set beneath "
            "Table Mountain on the southern tip of Africa. The legacy of apartheid is still "
            "visible in spatial inequality between predominantly white and Coloured/Black "
            "neighborhoods. For Black travelers, the city offers breathtaking natural beauty "
            "and Afrikaner, Xhosa, and Cape Malay cultural experiences, though awareness "
            "of lingering racial dynamics is advised."
        ),
        "welcome_score": 7.0,
        "latitude": -33.924900,
        "longitude": 18.424100,
        "meta_description": "Is Cape Town welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "Salvador",
        "country": "Brazil",
        "slug": "salvador-brazil",
        "description": (
            "Salvador da Bahia is often called the most African city outside of Africa — "
            "over 80% of its population is of African descent and the city's culture, "
            "cuisine, music, and religion (Candomblé) are deeply rooted in West African "
            "traditions. For Black travelers, Salvador offers a rare experience of "
            "profound cultural belonging, celebrated through Carnaval, capoeira, "
            "and acarajé on every street corner."
        ),
        "welcome_score": 8.5,
        "latitude": -12.971400,
        "longitude": -38.501400,
        "meta_description": "Is Salvador welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "Lisbon",
        "country": "Portugal",
        "slug": "lisbon-portugal",
        "description": (
            "Lisbon is consistently highlighted in Black travel guides as one of Europe's "
            "most welcoming capitals. Portugal's deep historical connections to Africa and "
            "Brazil have produced a large Afro-Portuguese community — particularly from "
            "Cape Verde, Angola, and Mozambique — making Black travelers feel seen and "
            "at home. Neighborhoods like Mouraria and Intendente are vibrant with "
            "Afro-Portuguese culture."
        ),
        "welcome_score": 8.5,
        "latitude": 38.722300,
        "longitude": -9.139300,
        "meta_description": "Is Lisbon welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
    {
        "name": "Dakar",
        "country": "Senegal",
        "slug": "dakar-senegal",
        "description": (
            "Dakar is the westernmost capital city in Africa and a proud hub of "
            "Pan-African culture, music, and art. Teranga — the Wolof concept of "
            "hospitality — is a guiding cultural value, and Black travelers from the "
            "diaspora routinely describe Dakar as transformative: a city where they "
            "feel racially invisible in the best possible sense and surrounded by "
            "a thriving, modern African identity."
        ),
        "welcome_score": 9.0,
        "latitude": 14.716700,
        "longitude": -17.467700,
        "meta_description": "Is Dakar welcoming for Black travelers? Read reviews, get the welcome score, find places to visit.",
    },
]


def seed_cities(apps, schema_editor):
    City = apps.get_model("cities", "City")
    for data in CITIES:
        City.objects.create(
            name=data["name"],
            country=data["country"],
            slug=data["slug"],
            description=data["description"],
            welcome_score=data["welcome_score"],
            score_count=0,
            latitude=data["latitude"],
            longitude=data["longitude"],
            hero_image_url="",
            meta_description=data["meta_description"],
        )


def unseed_cities(apps, schema_editor):
    City = apps.get_model("cities", "City")
    slugs = [city["slug"] for city in CITIES]
    City.objects.filter(slug__in=slugs).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("cities", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_cities, reverse_code=unseed_cities),
    ]

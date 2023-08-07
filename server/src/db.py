import sqlite3
from passlib.hash import bcrypt

def initialize_database():
    conn = sqlite3.connect('./database.db')
    cursor = conn.cursor()

    # Create a users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')

    # Create a revoked_tokens table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS revoked_tokens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            token TEXT UNIQUE
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS languages (
            num_id INTEGER PRIMARY KEY,
            lang_family	VARCHAR(512) NOT NULL,
            lang_name VARCHAR(512) NOT NULL,
            lang_id_udhr VARCHAR(512) NOT NULL,
            text_udhr VARCHAR(512) NOT NULL
        );
    ''')
    
    conn.commit()
    conn.close()
    
    add_languages()

def revoke_refresh_token(refresh_token):
    conn = sqlite3.connect('./database.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO revoked_tokens (token) VALUES (?)
    ''', (refresh_token,))

    conn.commit()
    conn.close()

def is_refresh_token_revoked(refresh_token):
    conn = sqlite3.connect('./database.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT EXISTS (SELECT 1 FROM revoked_tokens WHERE token=?)
    ''', (refresh_token,))

    result = cursor.fetchone()
    conn.close()

    return result[0] == 1

def register_user(username, email, password):
    conn = sqlite3.connect('./database.db')
    cursor = conn.cursor()

    try:
        # Hash the password
        hashed_password = bcrypt.hash(password)

        # Insert the user data into the database
        cursor.execute('''
            INSERT INTO users (username, email, password)
            VALUES (?, ?, ?)
        ''', (username, email, hashed_password))

        conn.commit()
        conn.close()
    except sqlite3.IntegrityError as e:
        conn.close()
        error_message = str(e)

        if "UNIQUE constraint failed: users.username" in error_message:
            return "Username already in use."
        elif "UNIQUE constraint failed: users.email" in error_message:
            return "Email already in use."
    
    return "User registered successfully."

def verify_user(username, password):
    conn = sqlite3.connect('./database.db')
    cursor = conn.cursor()

    # Retrieve the user data from the database
    cursor.execute('''
        SELECT id, username, password FROM users WHERE username=?
    ''', (username,))
    user_data = cursor.fetchone()

    if user_data:
        user_id, _, hashed_password = user_data
        if bcrypt.verify(password, hashed_password):
            conn.close()
            return user_id

    conn.close()
    return None

def is_email_registered(email):
    conn = sqlite3.connect('./database.db')
    cursor = conn.cursor()

    cursor.execute('SELECT id FROM users WHERE email=?', (email,))
    user_id = cursor.fetchone()

    conn.close()

    return user_id is not None

def get_user_id_by_email(email):
    conn = sqlite3.connect('./database.db')
    cursor = conn.cursor()

    cursor.execute('SELECT id FROM users WHERE email=?', (email,))
    user_id = cursor.fetchone()

    conn.close()

    return user_id[0] if user_id else None

def update_user_password(user_id, new_password):
    conn = sqlite3.connect('./database.db')
    cursor = conn.cursor()

    hashed_password = bcrypt.hash(new_password)

    cursor.execute('UPDATE users SET password=? WHERE id=?', (hashed_password, user_id))

    conn.commit()
    conn.close()
    
def add_languages():
    conn = sqlite3.connect('./database.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO languages (num_id,lang_family,lang_name,lang_id_udhr,text_udhr) VALUES
	        ('001', 'Afroasiatic', 'Amharic', 'udhr_amharic', 'የሰው፡ልጅ፡ሁሉ፡ሲወለድ፡ነጻና፡በክብርና፡በመብትም፡እኩልነት፡ያለው፡ነው።፡የተፈጥሮ፡ማስተዋልና፡ሕሊና፡ስላለው፡አንዱ፡ሌላውን፡በወንድማማችነት፡መንፈስ፡መመልከት፡ይገባዋል።'),
	        ('002', 'Afroasiatic', 'Arabic – Bahrani', 'udhr_bahraini', 'jinweldun kil''in''nas xürrien u mitsöwjin f''il kärame w''il xgyugy, mügdejien b''il ghägyülh w''id''dyemier u lözim gheleigüm jighamlun bäghädygüm bäghädy keqengüm ixhwan.'),
	        ('003', 'Afroasiatic', 'Arabic – Egyptian', 'udhr_ar-egypt', 'الإعلان العالمي لحقوق الإنسان، المادة الأولانية البني أدمين كلهم مولودين حرين ومتساويين في الكرامة والحقوق. إتوهبلهم العقل والضمير، والمفروض يعاملوا بعض بروح الأخوية.'),
	        ('004', 'Afroasiatic', 'Arabic – Gulf Pidgin Arabic', 'udhr_ar-gpa', 'كلوا نفر في ولادة حر وسمسم في كرامة وسمسم في حقوق. الله في إعطى هو عقل وضمير، ولازم هو سوي مع تاني نفر سمسم أخ'),
	        ('005', 'Afroasiatic', 'Arabic – Lebanese', 'udhr_lebanese', 'Kill el ba¡ar byechlaqò aħrár w mütasévyín bil carámet w''el ħoqúq. W hinné nwahabò xaqel w đamír, w xleyun y''xémlò baxdon el baxed b''rúħ el ochuẅet.'),
	        ('006', 'Afroasiatic', 'Arabic – Modern Standard', 'udhr_ar', 'يولد جميع الناس أحراراً متساوين في الكرامة والحقوق. وقد وهبوا عقلاً وضميراً وعليهم ان يعامل بعضهم بعضاً بروح اﻹخاء.'),
	        ('007', 'Afroasiatic', 'Arabic – Tunisian', 'udhr_ar-tunisia', 'In-nès il-kull muludìn ħurrìn w mitsèwìn fi’l-karàme w’il-ħuqùq. Tagħŧàw għqal w żamìr w lèzim ygħàmlu bgħażhum kìf l-axwa.'),
	        ('008', 'Afroasiatic', 'Aramaic – Isaric dialect', 'udhr_aramaic', 'Yàlidïn ìnon čol-ènašëya čwaþ χeḁrrëya we šàwyëya va ǧurča we va zìdqëya. Bìyìzvədun yal χuešaba we yal þeḁrþa, we koyìsˀərun χàd ləwaþ χàd va ruχa di àχuþa.'),
	        ('009', 'Afroasiatic', 'Hebrew', 'udhr_hb', 'כֹּל בְּנֵי הָאָדָם נוֹלְדוּ בְּנֵי חוֹרִין וְשָׁוִים בְּעֶרְכָּם וּבִזְכֻיּוֹתֵיהֶם. כֻּלָּם חוֹנְנוּ בַּתְּבוּנָה וּבְמַצְפּוּן, לְפִיכָךְ חוֹבָה עֲלֵיהֶם לִנְהֹוג אִישׁ בְּרֵעֵהוּ בְּרוּחַ שֶׁל אַחֲוָה.'),
	        ('010', 'Afroasiatic', 'Maltese', 'udhr_maltese', 'Il-bnedmin kollha jitwieldu ħielsa u ugwali fid-dinjità u d-drittijiet. Huma mogħnija bir-raġuni u bil-kuxjenza u għandhom inġibu ruħhom ma'' xulxin bi spirtu ta'' aħwa.'),
	        ('011', 'Afroasiatic', 'Somali', 'udhr_so', 'Aadanaha dhammaantiis wuxuu dhashaa isagoo xor ah kana siman xagga sharafta iyo xuquuqada. Waxaa Alle siiyay aqoon iyo wacyi, waana in qof la arkaa qofka kale ula dhaqmaa si walaaltinimo ah. | 𐒛𐒆𐒖𐒒𐒖𐒔𐒖 𐒊𐒖𐒑𐒑𐒛𐒒𐒂𐒕𐒈 𐒓𐒚𐒄𐒓 𐒊𐒖𐒉𐒛 𐒘𐒈𐒖𐒌𐒝 𐒄𐒙𐒇 𐒖𐒔 𐒏𐒖𐒒𐒖 𐒈𐒘𐒑𐒖𐒒 𐒄𐒖𐒌𐒌𐒖 𐒉𐒖𐒇𐒖𐒍𐒂𐒖 𐒘𐒕𐒙 𐒄𐒚𐒎𐒓𐒎𐒖𐒆𐒖 𐒓𐒖𐒄𐒛 𐒖𐒐𐒐𐒗 𐒈𐒕𐒕𐒖𐒕 𐒖𐒎𐒝𐒒 𐒘𐒕𐒙 𐒓𐒖𐒋𐒕𐒘, 𐒓𐒛𐒒𐒖 𐒘𐒒 𐒎𐒙𐒍 𐒐𐒖 𐒖𐒇𐒏𐒛 𐒎𐒙𐒍𐒏𐒖 𐒏𐒖𐒐𐒗 𐒚𐒐𐒖 𐒊𐒖𐒎𐒑𐒛 𐒈𐒘 𐒓𐒖𐒐𐒛𐒐𐒂𐒘𐒒𐒘𐒑𐒙 𐒖𐒔'),
	        ('012', 'Afroasiatic', 'Tigrinya', 'udhr_tigrinya', 'ብመንፅር ክብርን መሰልን ኩሎም ሰባት እንትውለጹ ነፃን ማዕረን እዮም። ምስትውዓልን ሕልናን ዝተዓደሎም ብምዃኖም ብሕውነታዊ መንፈስ ክተሓላዩ ኣለዎም።'),
	        ('013', 'Austro-Asiatic', 'Vietnamese', 'udhr_vi', '畢哿每𠊛生𠚢調得自由吧平等𧗱人品吧 權。每𡥵𠊛調得造化頒朱理智吧良心吧勤沛對處𢭲膮𥪝情朋友。'),
	        ('014', 'Austronesian', 'Acehnese', 'udhr_acehnese', 'Bandum ureuëng lahé deungon meurdéhka, dan deungon martabat dan hak njang saban. Ngon akai geuseumiké, ngon haté geumeurasa, bandum geutanjoë lagèë sjèëdara. Hak dan keumuliaan.'),
	        ('015', 'Austronesian', 'Balinese', 'udhr2_balinese', 'ᬫᬓᬲᬫᬶᬫᬦᬸᬲᬦᬾᬓᬳᭂᬫ᭄ᬩᬲᬶᬦ᭄ᬫᬳᬃᬤᬶᬓᬮᬦ᭄ᬧᬢᬾ᭪᭟ ​ᬲᬚᬦᬶᬂᬓᬳᬦᬦ᭄ᬮᬦ᭄ᬓᬸᬲ᭟ ᬳᬶᬧᬸᬦ᭄ᬓᬦᬸᬕ᭄ᬭᬳᬶᬦᬶᬯᬾᬓᬮᬦ᭄ᬩᬸᬤ᭄ᬥᬶ᭟ ​ᬧᬦ᭄ᬢᬭᬦᬶᬂᬫᬦᬸᬲᬫᬂᬤᬦᬾ​ ​ᬧᬭᬲ᭄ᬧᬭᭀᬲ᭄ᬫᬲᬫᬾᬢᭀᬦᬦ᭄'),
	        ('016', 'Austronesian', 'Bikol', 'udhr_bikol', 'An gabos na tawo ipinangaking may katalinkasan asin parantay sa dignidad asin derechos. Sinda gabos tinawan nin pag-isip asin conciencia kaya dapat na makipag-iriba sa lambang saro bilang mga magturugang.'),
	        ('017', 'Austronesian', 'Bugisnese', 'udhr_bugisnese', 'ᨔᨗᨊᨗᨊ ᨑᨘᨄ ᨈᨕᨘ ᨑᨗ ᨍᨍᨗᨕᨊᨁᨗ ᨑᨗᨒᨗᨊᨚᨕᨙ ᨊᨄᨘᨊᨕᨗ ᨆᨊᨙᨊᨁᨗ ᨑᨗᨕᨔᨙᨊᨁᨙ ᨕᨒᨙᨅᨗᨑᨙ᨞ ᨊᨄᨘᨊᨕᨗ ᨑᨗᨕᨔᨙᨊᨁᨙ ᨕᨀᨒᨙ᨞ ᨊᨄᨘᨊᨕᨗ ᨑᨗᨕᨔᨙᨊᨁᨙ ᨕᨈᨗ ᨆᨑᨙᨊᨗ ᨊ ᨔᨗᨅᨚᨒᨙ ᨅᨚᨒᨙᨊ ᨄᨉ ᨔᨗᨄᨀᨈᨕᨘ ᨄᨉ ᨆᨔᨒᨔᨘᨑᨙ᨞'),
	        ('018', 'Austronesian', 'Cebuano', 'udhr_cebuano', 'Ang tanang katawhan gipakatawo nga may kagawasan ug managsama sa kabililhon. Sila gigasahan sa salabutan ug tanlag og mag-ilhanay isip managsoon sa usa''g-usa diha sa diwa sa ospiritu.'),
	        ('019', 'Austronesian', 'Fijian', 'udhr_fijian', 'Era sucu ena galala na tamata yadua, era tautauvata ena nodra dokai kei na nodra dodonu. E tiko na nodra vakasama kei na nodra lewaeloma, sa dodonu mera veidokadokai ena yalo ni veitacini.'),
	        ('020', 'Austronesian', 'Hawaiian', 'udhr_hawaiian', 'Hānau kū''oko''a ''ia nā kānaka apau loa, a ua kau like ka hanohano a me nā pono kīvila ma luna o kākou pākahi. Ua ku''u mai ka no''ono''o pono a me ka ''ike pono ma luna o kākou, no laila, e aloha kākou kekahi i kekahi.'),
	        ('021', 'Austronesian', 'Indonesian', 'udhr_in', 'Semua orang dilahirkan merdeka dan mempunyai martabat dan hak-hak yang sama. Mereka dikaruniai akal dan hati nurani dan hendaknya bergaul satu sama lain dalam semangat persaudaraan.'),
	        ('022', 'Austronesian', 'Javanese', 'udhr_javanese1', 'ꦱꦧꦼꦤ꧀ꦲꦸꦮꦺꦴꦁꦏꦭꦲꦶꦂꦫꦏ꧀ꦏꦺꦏꦤ꧀ꦛꦶꦩꦂꦢꦶꦏꦭꦤ꧀ꦢꦂꦧꦺꦩꦂꦠꦧꦠ꧀ꦭꦤꦲꦏ꧀ꦲꦏ꧀ꦏꦁꦥꦝ꧉ ꦏꦧꦺꦃꦥꦶꦤꦫꦶꦁꦔꦤ꧀ꦲꦏꦭ꧀ꦭꦤ꧀ꦏꦭ꧀ꦧꦸꦱꦂꦠꦏꦲꦗꦧ꧀ꦥ ꦱꦿꦮꦸꦁꦔꦤ꧀ꦲꦁꦒꦺꦴꦤ꧀ꦤꦺꦩꦼꦩꦶ ꦠꦿꦤ꧀ꦱꦶꦗꦶꦭꦤ꧀ꦱꦶꦗꦶꦤꦺꦏꦤ꧀ꦛꦶꦗꦶꦮꦱꦸꦩꦢꦸꦭꦸꦂ꧉'),
	        ('023', 'Austronesian', 'Māori', 'udhr_maori', 'Ko te katoa o nga tangata i te whanaungatanga mai e watea ana i nga here katoa; e tauriterite ana hoki nga mana me nga tika. E whakawhiwhia ana hoki ki a ratou te ngakau whai whakaaro me te hinengaro mohio ki te tika me te he, a e tika ana kia meinga te mahi a tetahi ki tetahi me ma roto atu i te wairua o te noho tahi, ano he teina he tuakana i ringa i te whakaaro kotahi.'),
	        ('024', 'Austronesian', 'Madurese', 'udhr_madurese', 'Sadajana oreng lahir mardika e sarenge drajat klaban hak-hak se dha-padha. Sadajana eparenge akal sareng nurani ban kodu areng-sareng akanca kadi taretan.'),
	        ('025', 'Austronesian', 'Malagasy', 'udhr_malagasy', 'Teraka afaka sy mitovy zo sy fahamendrehana ny olombelona rehetra. Samy manan-tsaina sy fieritreretana ka tokony hifampitondra ampirahalahiana.'),
	        ('026', 'Austronesian', 'Malay', 'udhr_ms', 'Semua manusia dilahirkan bebas dan samarata dari segi kemuliaan dan hak-hak. Mereka mempunyai pemikiran dan perasaan hati dan hendaklah bertindak di antara satu sama lain dengan semangat persaudaraan.'),
	        ('027', 'Austronesian', 'Minangkabau', 'udhr_minangkabau', 'سادوڽو مأنسي دلهياكن مرديكا دان ڤوڽو مرتبت ساراتو حق-حق نن سامو. مريك دكارونياي اكا جو هاتي نوراني، سوڤيو ساتو سامو لاين باڬاول ساروڤو اورڠ بادونسانق.'),
	        ('028', 'Austronesian', 'Rarotongan', 'udhr_rarotongan', 'Kua anau rangatira ia te tangata katoatoa ma te aiteite i te au tikaanga e te tu ngateitei tiratiratu. Kua ki ia ratou e te mero kimi ravenga e te akavangakau e kia akono tetai i tetai, i roto i te vaerua piri anga taeake.'),
	        ('029', 'Austronesian', 'Rejang', 'udhr_rejang', 'Kutê tun laher mêrdiko, tmu''an hok-hok gi srai. Kutênê nagiakba akêa peker ngen atêi, kêrno o kêloknê bêkuatba do ngen luyên nêak lêm asai sêpasuak.'),
	        ('030', 'Austronesian', 'Sundanese', 'udhr_sundanese', 'ᮞᮊᮥᮙ᮪ᮔ ᮏᮜ᮪ᮙ ᮌᮥᮘᮢᮌ᮪ ᮊ ᮃᮜᮙ᮪ ᮓᮥᮑ ᮒᮨᮂᮞᮤᮖᮒ᮪ᮔ ᮙᮨᮛ᮪ᮓᮤᮊ ᮏᮦᮀ ᮘᮧᮌ ᮙᮛ᮪ᮒᮘᮒ᮪ ᮊᮒᮥᮒ᮪ ᮠᮊ᮪-ᮠᮊ᮪ ᮃᮔᮥ ᮞᮛᮥᮃ. ᮙᮛᮔᮦᮨᮂᮔ ᮓᮤᮘᮨᮛᮨ ᮃᮊᮜ᮪ ᮏᮩᮠᮀᮒᮨ ᮔᮥᮛᮔᮤ, ᮎᮙ᮪ᮕᮥᮁᮛ᮪-ᮌᮅᮜ᮪ ᮏᮩᮀ ᮞᮞᮙᮔ ᮃᮚ ᮓᮤᮔ ᮞᮥᮙᮔᮨᮒ᮪ ᮓᮥᮓᮥᮜᮥᮛᮔ᮪.'),
	        ('031', 'Austronesian', 'Tagalog', 'udhr_tl', 'Ang lahat ng tao''y isinilang na malaya at pantay-pantay sa karangalan at mga karapatan. Sila''y pinagkalooban ng katwiran at budhi at dapat magpalagayan ang isa''t isa sa diwa ng pagkakapatiran. | ᜀᜅ᜔ ᜎᜑᜆ᜔ ᜅ᜔ ᜆᜂᜌ᜔ ᜁᜐᜒᜈᜒᜎᜅ᜔ ᜈ ᜋᜎᜌ ᜀᜆ᜔ ᜉᜈ᜔ᜆᜌ᜔-ᜉᜈ᜔ᜆᜌ᜔ ᜐ ᜃᜇᜅᜎᜈ᜔ ᜀᜆ᜔ ᜋ᜔ᜄ ᜃᜇᜉᜆᜈ᜔᜶ ᜐᜒᜎᜌ᜔ ᜉᜒᜈᜄ᜔ᜃᜎᜓᜂᜊᜈ᜔ ᜅ᜔ ᜃᜆ᜔ᜏᜒᜇᜈ᜔ ᜀᜆ᜔ ᜊᜓᜇ᜔ᜑᜒ ᜀᜆ᜔ ᜇᜉᜆ᜔ ᜋᜄ᜔ᜉᜎᜄᜌᜈ᜔ ᜀᜅ᜔ ᜁᜐᜆ᜔ ᜁᜐ ᜐ ᜇᜒᜏ ᜅ᜔ ᜉᜄ᜔ᜃᜃᜉᜆᜒᜇᜈ᜔᜶'),
	        ('032', 'Austronesian', 'Terengganu Malay', 'udhr_terenganumalay', 'Segheme manusie lahér-lahér je bébah, sameghate daghi segi kemulieang nge hok-hok ye. Maséng-maséng ade ppikéghang nge peghasaang, kene tulong antaghe satu same laéng nge semangak pesedagheang.'),
	        ('033', 'Austronesian', 'Tetum', 'udhr_tetum', 'Ema hotu hotu moris hanesan ho dignidade ho direitu. Sira hotu iha hanoin, konsiensia n''e duni tenki hare malu hanesan espiritu maun-alin.'),
	        ('034', 'Austronesian', 'Tuvaluan', 'udhr_tuvaluan', 'E fā''nau mai a tino katoa i te saolotoga kae e ''pau telotou tūlaga fakaaloalogina mo telotou aiā. Ne tuku atu ki a lātou a te mafaufau mo te loto lagona, tēlā lā, e ''tau o gā''lue fakatasi lātou e pēlā me ne taina.'),
	        ('035', 'Bantu', 'Swahili', 'udhr_swahili', 'Watu wote wamezaliwa huru, hadhi na haki zao ni sawa. Wote wamejaliwa akili na dhamiri, hivyo yapasa watendeane kindugu.'),
	        ('036', 'Bantu', 'Zulu', 'udhr_zulu', 'Bonke abantu bazalwa bekhululekile belingana ngesithunzi nangamalungelo. Bahlanganiswe wumcabango nangunembeza futhi kufanele baphathane ngomoya wobunye.'),
	        ('037', 'Celtic', 'Irish Gaelic', 'udhr_irish', 'Saolaítear na daoine uile saor agus comhionann ina ndínit agus ina gcearta. Tá bua an réasúin agus an choinsiasa acu agus dlíd iad féin d''iompar de mheon bráithreachais i leith a chéile.'),
	        ('038', 'Celtic', 'Manx Gaelic', 'udhr_gv', 'Ta dagh chooilley ghooinney ruggit seyr as corrym rish dy chooilley ghooinney elley ayns ooashley as ayns cairys. Ta resoon as cooinsheanse stowit orroo as lhisagh ad dellal rish y cheilley lesh spyrryd braaraghyn.'),
	        ('039', 'Celtic', 'Scottish Gaelic', 'udhr_ga', 'Rugadh na h-uile duine saor agus co-ionnan nan urram ''s nan còirichean. Tha iad reusanta is cogaiseach, agus bu chòir dhaibh a ghiùlain ris a chèile ann an spiorad bràthaireil.'),
	        ('040', 'Celtic', 'Welsh', 'udhr_cy', 'Genir pawb yn rhydd ac yn gydradd â''i gilydd mewn urddas a hawliau. Fe''u cynysgaeddir â rheswm a chydwybod, a dylai pawb ymddwyn y naill at y llall mewn ysbryd cymodlon.'),
	        ('041', 'Constructed', 'Esperanto', 'udhr_esperanto', 'Ĉiuj homoj estas denaske liberaj kaj egalaj laŭ digno kaj rajtoj. Ili posedas racion kaj konsciencon, kaj devus konduti unu al alia en spirito de frateco.'),
	        ('042', 'Constructed', 'Folkspraak', 'udhr_folkspraak', 'All mensklik wesings âre boren frî on'' gelîk in werđigheid on'' rejte. Đê âre begifted mid ferstand on'' gewitt on'' skulde behandele êlkên in en gêst av brôđerhêd.'),
	        ('043', 'Constructed', 'Ido', 'udhr_ido', 'Omna homi naskas libera ed egala relate digneso e yuri. Li es dotita perraciono e koncienco e devas agar vers l''una l''altra en spirito di frateso.'),
	        ('044', 'Constructed', 'Lingua Franca Nova', 'udhr_lfn', 'Тота уманес насе либре е егал ен диниа е диретос. Лос ес донада разона е консиенса е дебе ата ла ун а ла отра ен ун спирито де фратиа.'),
	        ('045', 'Constructed', 'Lojban', 'udhr_lojban', 'ro remna cu se jinzi co zifre je simdu''i be le ry. nilselsi''a .e lei ry. selcru .i ry. se menli gi''e se sezmarde .i .ei jeseki''ubo ry. simyzu''e ta''i le tunba'),
	        ('046', 'Constructed', 'Toki Pona', 'udhr_tokipona', 'jan ale/ali li kama lon nasin ni: ona li ken pali e wile ona. ona li jo e suli jan sama e ken sama. ona li jo e sona pona e lawa insa pi pali pona. ni la, ona li wile pali tawa jan ante ale/ali kepeken nasin olin.'),
	        ('047', 'Constructed', 'Volapük', 'udhr_volapuk', 'Mens valik pemotons libiko e leigiko tefü digäd e gitäts. Labons tikäli e konsieni, e sötons kosädön ko ods siämü svistäl.'),
	        ('048', 'Dravidian', 'Kannada', 'udhr_kn', 'ಎಲ್ಲಾ ಮಾನವರೂ ಸ್ವತಂತ್ರರಾಗಿಯೇ ಜನಿಸಿದ್ದಾರೆ. ಹಾಗೂ ಘನತೆ ಮತ್ತು ಹಕ್ಕು ಗಳಲ್ಲಿ ಸಮಾನರಾಗಿದ್ದರೆ. ವಿವೇಕ ಮತ್ತು ಅಂತಃಕರಣ ಗಳನ್ನು ಪಡೆದವರಾದ್ದರಿಂದ ಅವರು ಪರಸ್ಪರ ಸಹೋದರ ಭಾವದಿಂದ ವರ್ತಿಸಬೇಕು.'),
	        ('049', 'Dravidian', 'Malayalam', 'udhr_malayalam', 'മനുഷ്യരെല്ലാവരും തുല്യാവകാശങ്ങളോടും അന്തസ്സോടും സ്വാതന്ത്ര്യത്തോടുംകൂടി ജനിച്ചവരാണ്. അന്യോന്യം ഭ്രാതൃഭാവത്തോടെ പെരുമാറുവാനാണ് മനുഷ്യന്നു വിവേകബുദ്ധിയും മനസ്സാക്ഷിയും സിദ്ധമായിരിക്കുന്നത്.'),
	        ('050', 'Dravidian', 'Tamil', 'udhr_tamil', 'மனிதப் பிறவியினர் சகலரும் சுதந்திரமாகவே பிறக்கின்றனர்; அவர்கள் மதிப்பிலும் உரிமைகளிலும் சமமானவர்கள். அவர்கள் நியாயத்தையும் மனசாட்சியையும் இயற்பண்பாகப் பெற்றவர்கள். அவர்கள் ஒருவருடனொருவர் சகோதர உணர்வுப் பாங்கில் நடந்துகொள்ளல் வேண்டும்.'),
	        ('051', 'Eskimo-Aleut', 'Greenlandic', 'udhr_kl', 'Inuit tamarmik inunngorput nammineersinnaassuseqarlutik assigiimmillu ataqqinassuseqarlutillu pisinnaatitaaffeqarlutik. Silaqassusermik tarnillu nalunngissusianik pilersugaapput, imminnullu iliorfigeqatigiittariaqaraluarput qatanngutigiittut peqatigiinnerup anersaavani.'),
	        ('052', 'Indo-European – Albanian', 'Albanian – Gheg', 'udhr_albanian-gheg', 'Zhdo njeri kan le t''lir mê njãjit dinjitêt edhê dreta. Ata jan të pajisun mê mênjê edhê vet-dijê edhê duhën të veprôjn ka njãni-tjetrin mê nji shpirt vllâznimit.'),
	        ('053', 'Indo-European – Albanian', 'Albanian – Tosk', 'udhr_sq', 'Të gjithë njerëzit lindin të lirë dhe të barabartë në dinjitet dhe në të drejta. Ata kanë arsye dhe ndërgjegje dhe duhet të sillen ndaj njëri tjetrit me frymë vëllazërimi.'),
	        ('054', 'Indo-European – Armenian', 'Eastern Armenian', 'udhr_hy', 'Բոլոր մարդիկ ծնվում են ազատ ու հավասար` իրենց արժանապատվությամբ և իրավունքներով: Նրանք օժտված են բանականությամբ ու խղճով, և պարտավոր են միմյանց նկատմամբ վարվել եղբայրության ոգով.'),
	        ('055', 'Indo-European – Armenian', 'Western Armenian', 'udhr_hy-western', 'Բոլոր մարդիկ կը ծնուին ազատ եւ հաւասար իրենց արժանապատուութեամբ եւ իրաւունքներով: Իրենք օժտուած են բանականութեամբ ու խիղճով, եւ պարտաւորուած են միմեանց հանդէպ եղբայրութեան ոգիով վարուիլ:'),
	        ('056', 'Indo-European – Baltic', 'Latvian', 'udhr_latvian', 'Visi cilvēki piedzimst brīvi un vienlīdzīgi savā pašcieņā un tiesībās. Viņi ir apveltīti ar saprātu un sirdsapziņu, un viņiem jāizturas citam pret citu brālības garā.'),
	        ('057', 'Indo-European – Baltic', 'Lithuanian', 'udhr_lt', 'Visi žmonės gimsta laisvi ir lygūs savo orumu ir teisėmis. Jiems suteiktas protas ir sąžinė ir jie turi elgtis vienas kito atžvilgiu kaip broliai.'),
	        ('058', 'Indo-European – Germanic', 'Afrikaans', 'udhr_af', 'Alle menslike wesens word vry, met gelyke waardigheid en regte, gebore. Hulle het rede en gewete en behoort in die gees van broederskap teenoor mekaar op te tree.'),
	        ('059', 'Indo-European – Germanic', 'Danish', 'udhr_dk', 'Alle mennesker er født frie og lige i værdighed og rettigheder. De er udstyret med fornuft og samvittighed, og de bør handle mod hverandre i en broderskabets ånd.'),
	        ('060', 'Indo-European – Germanic', 'Dutch', 'udhr_nl', 'Alle mensen worden vrij en gelijk in waardigheid en rechten geboren. Zij zijn begiftigd met verstand en geweten, en behoren zich jegens elkander in een geest van broederschap te gedragen.'),
	        ('061', 'Indo-European – Germanic', 'East Frisian', 'udhr_eastfrisian', 'Âl minsken wordent fräj un glīk in wērderğkaid un rechten bōren. Säi hebbent küen un gewäiten mitkrēgen un söölent mitnanner in brörskup lēven.'),
	        ('062', 'Indo-European – Germanic', 'English', 'udhr_en', 'All human beings are born free and equal in dignity and rights. They are endowed with reason and conscience and should act towards one another in a spirit of brotherhood.'),
	        ('063', 'Indo-European – Germanic', 'Faroese', 'udhr_faroese', 'Øll menniskju eru fødd fræls og jøvn til virðingar og mannarættindi. Tey hava skil og samvitsku og eiga at fara hvørt um annað í bróðuranda.'),
	        ('064', 'Indo-European – Germanic', 'Swiss German – Lucerne dialect', 'udhr_swissgerman', 'Alli Mönshe send frey ond geboore met gliicher Wörd ond gliiche Rächt. Si send xägnet met Vernonft ond Gwösse ond sölled enand e brüederlechem Gäisht begägne.'),
	        ('065', 'Indo-European – Germanic', 'German', 'udhr_de', 'Alle Menschen sind frei und gleich an Würde und Rechten geboren. Sie sind mit Vernunft und Gewissen begabt und sollen einander im Geist der Brüderlichkeit begegnen.'),
	        ('066', 'Indo-European – Germanic', 'Icelandic', 'udhr_is', 'Hver maður er borinn frjáls og jafn öðrum að virðingu og réttindum. Menn eru gæddir vitsmunum og samvisku, og ber þeim að breyta bróðurlega hverjum við annan.'),
	        ('067', 'Indo-European – Germanic', 'Luxembourgish', 'udhr_lb', 'All Mënsch kënnt fräi a mat deer selwechter Dignitéit an dene selwechte Rechter op d''Welt. Jiddereen huet säi Verstand a säi Gewësse krut an soll an engem Geescht vu Bridderlechkeet denen anere géintiwwer handelen.'),
	        ('068', 'Indo-European – Germanic', 'North Low Saxon', 'udhr_lowsaxon', 'Wat Wöörd'' un Rechten sünd, daar sünd all de Minschen free un liek mit boorn. Se hebbt dat Tüüg för Vernimm un Gewäten mitkrägen, un dat böört jüm, dat se eenanner in''n Geest vun Bröderschup in de Mööt kaamt.'),
	        ('069', 'Indo-European – Germanic', 'Norwegian Bokmål', 'udhr_no', 'Alle mennesker er født frie og med samme menneskeverd og menneskerettigheter. De er utstyrt med fornuft og samvittighet og bør handle mot hverandre i brorskapets ånd.'),
	        ('070', 'Indo-European – Germanic', 'Norwegian Nynorsk', 'udhr_ny', 'Alle menneske er fødde til fridom og med same menneskeverd og menneskerettar. Dei har fått fornuft og samvit og skal leve med kvarandre som brør.'),
	        ('071', 'Indo-European – Germanic', 'Old English', 'udhr_oldenglish', 'Ealle menn sindon āre and rihtes efen ġeboren, and frēo. Him sindon ġiefeþe ġerād and inġehyġd, and hī sċulon dōn tō ōþrum on brōþorsċipes fēore.'),
	        ('072', 'Indo-European – Germanic', 'Old Norse', 'udhr_oldnorse', 'Allir menn eru bornir frjálsir ok jafnir at virðingu ok réttum. Þeir eru allir viti gœddir ok samvizku, ok skulu gøra hvárr til annars bróðurliga.'),
	        ('073', 'Indo-European – Germanic', 'Swedish', 'udhr2_sv', 'Alla människor är födda fria och lika i värdighet och rättigheter. De är utrustade med förnuft och samvete och bör handla gentemot varandra i en anda av broderskap.'),
	        ('074', 'Indo-European – Germanic', 'Sylt – Insular North Frisian language', 'udhr_northfrisian-sylt', 'Ali Mensken sen frii, likwērtig en me disalev Rochten bēren. Ja haa Forstant en Giweeten mefingen en skul arküđer üs Bröđern öntöögentreer.'),
	        ('075', 'Indo-European – Germanic', 'Värmlandic', 'udhr_varmlandic', 'All mensher ä född fri å ä lik i vaaL å rätt. De ''a gûes ômdömm å samvett å boL hannel a varanner i broderskapsånn.'),
	        ('076', 'Indo-European – Germanic', 'West Frisian', 'udhr_westfrisian', 'Alle minsken wurde frij en gelyk yn weardigens en rjochten berne. Hja hawwe ferstân en gewisse meikrigen en hearre har foar inoar oer yn in geast fan bruorskip te hâlden en te dragen.'),
	        ('077', 'Indo-European – Germanic', 'Yiddish – Taytsch', 'udhr_yiddish', 'Yeder mentsh vert geboyrn fray un glaykh in koved un rekht. Yeder vert bashonkn mit farshtand un gevisn; yeder zol zikh firn mit a tsveytn in a gemit fun brudershaft.'),
	        ('078', 'Indo-European – Hellenic', 'Greek', 'udhr_greek2', 'Ολοι οι άνθρωποι γεννιούνται ελεύθεροι και ίσοι στην αξιοπρέπεια και τα δικαιώματα. Είναι προικισμένοι με λογική και συνείδηση, και οφείλουν να συμπεριφέρονται μεταξύ τους με πνεύμα αδελφοσύνης.'),
	        ('079', 'Indo-European – Indo-Iranian', 'Assamese', 'udhr_assamese', 'জন্মগতভাৱে সকলো মানুহ মৰ্য্যদা আৰু অধিকাৰত সমান আৰু স্বতন্ত্ৰ। তেওঁলোকৰ বিবেক আছে, বুদ্ধি আছে। তেওঁলোকে প্ৰত্যেকে প্ৰেত্যেকক ভ্ৰাতৃভাৱে ব্যৱহাৰ কৰা উচিত।'),
	        ('080', 'Indo-European – Indo-Iranian', 'Bengali', 'udhr_bn', 'সমস্ত মানুষ স্বাধীনভাবে সমান মর্যাদা এবং অধিকার নিয়ে জন্মগ্রহণ করে | তাঁদের বিবেক এবং বুদ্ধি আছে সুতরাং সকলেরই একে অপরের প্রতি ভ্রাতৃত্বসুলভ মনোভাব নিয়ে আচরণ করা উচিত্ |'),
	        ('081', 'Indo-European – Indo-Iranian', 'Chittagonian', 'udhr_chittagonian', 'বিয়াক মানুশ ইজ্‌জত এদ‌্দে অ়কর ই়শাবে আজাদ আর উ়য়াইন্‌না অ়ইয়েরে ফ়য়দা অ়য়। ই়তারাত্‌তু আহল এদ্‌দে বিবেক আছে ; এতল্‌লায় এজ্‌জন আরেজ্‌জনর উ়য়ারে ভাইয়ুর নান বেভার গরন দরহার।'),
	        ('082', 'Indo-European – Indo-Iranian', 'Hindi', 'udhr_hindi', 'सभी मनुष्यों को गौरव और अधिकारों के मामले में जन्मजात स्वतन्त्रता और समानता प्राप्त है। उन्हें बुद्धि और अन्तरात्मा की देन प्राप्त है और परस्पर उन्हें भाईचारे के भाव से बर्ताव करना चाहिए।'),
	        ('083', 'Indo-European – Indo-Iranian', 'Kashmiri', 'udhr_kashmiri', 'سٔری لُکھ چهہٕ حقوٗق تِہ عزت لِحاظٕ ہِہیٖ ژامِت. تِمن چه‍ہِ ضمير تِہ عَقل دِنِ آمٕژ. تٔوے پَزٕ تُمن بھٲئی برادری سانٛ روزُن.'),
	        ('084', 'Indo-European – Indo-Iranian', 'Khowar', 'udhr_khowar', 'Saf insān āzād wa ḥuqūq-ochay izzato ėʿtibāro sora barābaar paidā biti asuni. hetantey żamīr ôchay ʿaql ataa koronu biti sher. Hey bachen hetan taan muzhi brar gariyo sulūk korelik.'),
	        ('085', 'Indo-European – Indo-Iranian', 'Kurdish', 'udhr_kurdish', 'Hemû mirov azad û di weqar û mafan de wekhev tên dinyayê. Ew xwedî hiş û şuûr in û divê li hember hev bi zihniyeteke bratiyê bilivin.'),
	        ('086', 'Indo-European – Indo-Iranian', 'Maldivian', 'udhr_maldivian', 'ހުރިހާ އިންސާނުން ވެސް އުފަންވަނީ، ދަރަޖައާއި ޙައްޤުތަކުގައި މިނިވަންކަމާއި ހަމަހަމަކަން ލިބިގެންވާ ބައެއްގެ ގޮތުގައެވެ. އެމީހުންނަށް ހެޔޮ ވިސްނުމާއި، ހެޔޮ ބުއްދީގެ ބާރު ލިބިގެންވެއެވެ. އަދި އެމީހުން އެކަކު އަނެކަކާ މެދު މުޢާމަލާތް ކުރަންވާނީ، އުޚުއްވަތްތެރި ކަމުގެ ރޫޙެއްގައެވެ.'),
	        ('087', 'Indo-European – Indo-Iranian', 'Marathi', 'udhr_marathi', 'सर्व मनुष्यजात जन्मतःच स्वतंत्र आहे व सर्वजणांना समान प्रतिष्ठा व समान अधिकार आहेत. त्यांना विचारशक्ती व सदसद्विवेकबुद्धी लाभलेली आहे व त्यांनी एकमेकांशी बंधुत्वाच्या भावनेने आचरण करावे.'),
	        ('088', 'Indo-European – Indo-Iranian', 'Marwari', 'udhr_marwari', 'سگݪا مݨکه نے گورو ان ادهکاروں رے راسے مای جݪم سوں سوتنترا انے سمانتا پراپت چهے. وݨی رے گوڑے بده ان انتراتما ری پراپتی چهے ان وݨی نے بهیئیپاݪا بهاونا سو اےکبیجے رے سارو ورتن کرݨو جوییجے چهے.'),
	        ('089', 'Indo-European – Indo-Iranian', 'Nepali', 'udhr_ne', 'सबै व्यक्तिहरू जन्मजात स्वतन्त्र हुन् ती सबैको समान अधिकार र महत्व छ। निजहरूमा विचार शक्ति र सद्विचार भएकोले निजहरूले आपस्तमा भ्रातृत्वको भावनाबाट व्यवहार गर्नु पर्छ।'),
	        ('090', 'Indo-European – Indo-Iranian', 'Odia', 'udhr_oriya', 'ସବୁ ମନୁଷ୍ୟ ଜନ୍ମକାଳରୁ ସ୍ୱାଧୀନ. ସେମାନଙ୍କର ମର୍ଯ୍ୟାଦା ଓ ଅଧିକାର ସମାନ. ସେମାନଙ୍କଠାରେ ପ୍ରଜ୍ଞା ଓ ବିବେକ ନିହିତ ଅଛି. ସେମାନେ ପରସ୍ପର ପ୍ରତି ଭାତୃଭାବ ପୋଷଣ କରି କାର୍ଯ୍ୟ କରିବା ଦରକାର.'),
	        ('091', 'Indo-European – Indo-Iranian', 'Ossetian', 'udhr_ossetian', 'Адӕймӕгтӕ се ''ппӕт дӕр райгуырынц сӕрибарӕй ӕмӕ ӕмхуызонӕй сӕ барты. Уыдон ӕххӕст сты зонд ӕмӕ намысӕй, ӕмӕ кӕрӕдзийӕн хъуамӕ уой ӕфсымӕрты хуызӕн.'),
	        ('092', 'Indo-European – Indo-Iranian', 'Persian', 'udhr_fa1', 'تمام افراد بشر آزاد به دنیا می آیند و از لحاظ حیثیت و حقوق با هم برابرند, همه دارای عقل و وجدان می باشند و باید نسبت به یک دیگر با روح برادری رفتار کنند.'),
	        ('093', 'Indo-European – Indo-Iranian', 'Punjabi – Eastern', 'udhr_pa', 'ਸਾਰਾ ਮਨੁੱਖੀ ਪਰਿਵਾਰ ਆਪਣੀ ਮਹਿਮਾ, ਸ਼ਾਨ ਅਤੇ ਹੱਕਾਂ ਦੇ ਪੱਖੋਂ ਜਨਮ ਤੋਂ ਹੀ ਆਜ਼ਾਦ ਹੈ ਅਤੇ ਸੁਤੇ ਸਿੱਧ ਸਾਰੇ ਲੋਕ ਬਰਾਬਰ ਹਨ । ਉਨ੍ਹਾਂ ਸਭਨਾ ਨੂੰ ਤਰਕ ਅਤੇ ਜ਼ਮੀਰ ਦੀ ਸੌਗਾਤ ਮਿਲੀ ਹੋਈ ਹੈ ਅਤੇ ਉਨ੍ਹਾਂ ਨੂੰ ਭਰਾਤਰੀਭਾਵ ਦੀ ਭਾਵਨਾ ਰਖਦਿਆਂ ਆਪਸ ਵਿਚ ਵਿਚਰਣਾ ਚਾਹੀਦਾ ਹੈ ।'),
	        ('094', 'Indo-European – Indo-Iranian', 'Sanskrit', 'udhr_sanskrit', 'सर्वे मानवाः स्वतन्त्राः समुत्पन्नाः वर्तन्ते अपि च, गौरवदृशा अधिकारदृशा च समानाः एव वर्तन्ते। एते सर्वे चेतना-तर्क-शक्तिभ्यां सुसम्पन्नाः सन्ति। अपि च, सर्वेऽपि बन्धुत्व-भावनया परस्परं व्यवहरन्तु।'),
	        ('095', 'Indo-European – Indo-Iranian', 'Sinhala', 'udhr_sinhala', 'සියලූ මනුෂ්‍යයෝ නිදහස්ව උපත ලබා ඇත. ගරුත්වයෙන් හා අයිතිවාසිකම් සමාන වෙති. යුක්ති අයුක්ති පිළිබඳ හැඟීමෙන් හා හෘදය සාක්ෂියෙන් යුත් ඔවුනොවුන්වුන්ට සැළකිය යුත්තේ සහෝදරත්වය පිළිබඳ හැඟීමෙනි.'),
	        ('096', 'Indo-European – Indo-Iranian', 'Urdu', 'udhr_urdu2', 'تمام انسان آزاد اور حقوق و عزت کے اعتبار سے برابر پیدا ہوۓ ہیں۔ انہیں ضمیر اور عقل ودیعت ہوئی ہے۔ اسلیۓ انہیں ایک دوسرے کے ساتھ بھائی چارے کا سلوک کرنا چاہیۓ۔'),
	        ('097', 'Indo-European – Italic', 'Classical Latin', 'udhr_latin_classical2', 'Omnes homines dignitate et iure liberi et pares nascuntur, rationis et conscientiae participes sunt, quibus inter se concordiae studio est agendum.'),
	        ('098', 'Indo-European – Romance', 'Aragonese', 'udhr_aragonese', 'Toz os ombres naxen libres y iguals en dinidat y en dreitos. Adotatos de razón y de conzenzia, deben apachar-sen unos con atros d''una manera freternal.'),
	        ('099', 'Indo-European – Romance', 'Aromanian', 'udhr_aromanian', 'Tuti iatsâli umineshtsâ s-fac liberi shi egali la nâmuzea shi-ndrepturli. Eali suntu hârziti cu fichiri shi sinidisi shi lipseashti un cu alantu sh-si poartâ tu duhlu-a frâtsâljiljei.'),
	        ('100', 'Indo-European – Romance', 'Asturian', 'udhr_asturian', 'Tolos seres humanos nacen llibres y iguales en dignidá y drechos y, pola mor de la razón y la conciencia de so, han comportase hermaniblemente los unos colos otros.'),
	        ('101', 'Indo-European – Romance', 'Brazilian Portuguese', 'udhr_pt-br', 'Todos os seres humanos nascem livres e iguais em dignidade e direitos. São dotados de razão e consciência e devem agir em relação uns aos outros com espírito de fraternidade.'),
	        ('102', 'Indo-European – Romance', 'Catalan', 'udhr_catalan', 'Tots els éssers humans neixen lliures i iguals en dignitat i en drets. Són dotats de raó i de consciència, i han de comportar-se fraternalment els uns amb els altres.'),
	        ('103', 'Indo-European – Romance', 'French – Canada', 'udhr_fr-ca', 'Tous les êtres humains naissent libres et égaux en dignité et en droits. Ils sont doués de raison et de conscience et doivent agir les uns envers les autres dans un esprit de fraternité.'),
	        ('104', 'Indo-European – Romance', 'French – France', 'udhr_fr', 'Tous les êtres humains naissent libres et égaux en dignité et en droits. Ils sont doués de raison et de conscience et doivent agir les uns envers les autres dans un esprit de fraternité.'),
	        ('105', 'Indo-European – Romance', 'Galician', 'udhr_gl', 'Tódolos seres humanos nacen libres e iguais en dignidade e dereitos e, dotados como están de razón e conciencia, díbense comportar fraternalmente uns cos outros.'),
	        ('106', 'Indo-European – Romance', 'Italian', 'udhr_it', 'Tutti gli esseri umani nascono liberi ed eguali in dignità e diritti. Essi sono dotati di ragione e di coscienza e devono agire gli uni verso gli altri in spirito di fratellanza.'),
	        ('107', 'Indo-European – Romance', 'Lombard', 'udhr_lombard', 'Töcc i véser umà i nas líber e precís en dignità e diricc. I è dotacc de rizú e de coscenssa e i ga de comportà-s, de giü con l''óter, en spírit de fradelanssa.'),
	        ('108', 'Indo-European – Romance', 'Lorrain', 'udhr_lorrain', 'Totes li hàmmes v''nàt au monde libes et égaux de la dignitè et da lo drâ. Ils so dotès de rahho et d''conscience et so t''nus d''se compoutè li ines enwoués lis autes da in esprit d''fraternitè.'),
	        ('109', 'Indo-European – Romance', 'Occitan', 'udhr_occitan', 'Totas las personas nàisson liuras e parièras en dignitat e en dreches. Son cargadas de rason e de consciéncia e mai lor se cal comportar entre elas amb un eime de frairetat.'),
	        ('110', 'Indo-European – Romance', 'Piedmontese', 'udhr_piedmontese', 'Tùit j''esse uman a nasso lìber e uguaj an dignità e an drit. A son dotà ‘d sust e ‘d consiensa e a dëvo agì j’un con j’àutri ant n’ëspìrit ëd fradlansa.'),
	        ('111', 'Indo-European – Romance', 'Portuguese', 'udhr_pt', 'Todos os seres humanos nascem livres e iguais em dignidade e em direitos. Dotados de razão e de consciência, devem agir uns para com os outros em espírito de fraternidade.'),
	        ('112', 'Indo-European – Romance', 'Romanian', 'udhr_ro', 'Toate ființele umane se nasc libere și egale în demnitate și în drepturi. Ele sunt înzestrate cu rațiune și conștiință și trebuie să se comporte unele față de altele în spiritul fraternității.'),
	        ('113', 'Indo-European – Romance', 'Sicilian', 'udhr_sicilian', 'Tutti l''omini nascinu libbiri cu a stissa dignità i diritti. Iddi hannu a raggiuni i cuscienza i hannu a travagghiari ''nzemmula cu spiritu di fratirnità.'),
	        ('114', 'Indo-European – Romance', 'Spanish – Andalucía', 'udhr_es2', 'Todos los seres humanos nacen libres e iguales en dignidad y derechos y, dotados como están de razón y conciencia, deben comportarse fraternalmente los unos con los otros.'),
	        ('115', 'Indo-European – Romance', 'Spanish – Mexico', 'udhr_es-mx', 'Todos los seres humanos nacen libres e iguales en dignidad y derechos y, dotados como están de razón y conciencia, deben comportarse fraternalmente los unos con los otros.'),
	        ('116', 'Indo-European – Romance', 'Spanish – Peru', 'udhr_es-peru', 'Todos los seres humanos nacen libres e iguales en dignidad y derechos y, dotados como están de razón y conciencia, deben comportarse fraternalmente los unos con los otros.'),
	        ('117', 'Indo-European – Romance', 'Spanish – Valencia', 'udhr_es', 'Todos los seres humanos nacen libres e iguales en dignidad y derechos y, dotados como están de razón y conciencia, deben comportarse fraternalmente los unos con los otros.'),
	        ('118', 'Indo-European – Romance', 'Valencian', 'udhr_valencian', 'Tots els éssers humans naixen lliures i iguals en dignitat i en drets i, dotats com estan de raó i de consciència, s’han de comportar fraternalment els uns amb els altres.'),
	        ('119', 'Indo-European – Romance', 'Walloon', 'udhr_walloon', 'Tos lès-omes vinèt-st-å monde lîbes, èt so-l''minme pîd po çou qu''ènn''èst d''leu dignité èt d''leus dreûts. I n''sont nin foû rêzon èt-z-ont-i leû consyince po zèls, çou qu''èlzès deût miner a s''kidûre onk'' po l''ôte tot come dès frés.'),
	        ('120', 'Indo-European – Slavic', 'Belarusian', 'udhr_be', 'Usie ludzi naradžajucca svabodnymi i roŭnymi ŭ svajoj hodnaści i pravach. Jany nadzieleny rozumam i sumleńniem i pavinny stavicca adzin da adnaho ŭ duchu bractva.'),
	        ('121', 'Indo-European – Slavic', 'Bulgarian', 'udhr_bg', 'Всички хора се раждат свободни и равни по достойнство и права. Tе са надарени с разум и съвест и следва да се отнасят помежду си в дух на братство.'),
	        ('122', 'Indo-European – Slavic', 'Croatian', 'udhr_hr', 'Sva ljudska bića rađaju se slobodna i jednaka u dostojanstvu i pravima. Ona su obdarena razumom i sviješću i trebaju jedna prema drugima postupati u duhu bratstva.'),
	        ('123', 'Indo-European – Slavic', 'Czech', 'udhr_cz', 'Všichni lidé se rodí svobodní a sobě rovní co do důstojnosti a práv. Jsou nadáni rozumem a svědomím a mají spolu jednat v duchu bratrství.'),
	        ('124', 'Indo-European – Slavic', 'Macedonian', 'udhr_macedonian', 'Ситe чoвeчки суштeствa сe рaѓaaт слoбoдни и eднaкви пo дoстoинствo и прaвa. Tиe сe oбдaрeни сo рaзум и сoвeст и трeбa дa сe oднeсувaaт eдeн кoн друг вo дуxoт нa oпштo чoвeчкaтa припaднoст.'),
	        ('125', 'Indo-European – Slavic', 'Polish', 'udhr_pl', 'Wszyscy ludzie rodzą się wolni i równi w swojej godności i prawach. Są obdarzeni rozumem i sumieniem i powinni postępować wobec siebie w duchu braterstwa.'),
	        ('126', 'Indo-European – Slavic', 'Russian', 'udhr2_ru', 'Все люди рождаются свободными и равными в своем достоинстве и правах. Они наделены разумом и совестью и должны поступать в отношении друг друга в духе братства.'),
	        ('127', 'Indo-European – Slavic', 'Serbian', 'udhr_sr', 'Сва људска бића рађају се слободна и једнака у достојанству и правима. Она су обдарена разумом и свешћу и треба једни према другима да поступају у духу братства. | Sva ljudska bića rađaju se slobodna i jednaka u dostojanstvu i pravima. Ona su obdarena razumom i svešću i treba jedni prema drugima da postupaju u duhu bratstva.'),
	        ('128', 'Indo-European – Slavic', 'Slovak', 'udhr_sk', 'Všetci ľudia sa rodia slobodní a sebe rovní, čo sa týka ich dostôjnosti a práv. Sú obdarení rozumom a majú navzájom jednať v bratskom duchu.'),
	        ('129', 'Indo-European – Slavic', 'Slovenian', 'udhr_slovenian', 'Vsi ljudje se rodijo svobodni in imajo enako dostojanstvo in enake pravice. Obdarjeni so z razumom in vestjo in bi morali ravnati drug z drugim kakor bratje.'),
	        ('130', 'Indo-European – Slavic', 'Ukrainian', 'udhr_uk', 'Всі люди народжуються вільними і рівними у своїй гідності та правах. Вони наділені розумом і совістю і повинні діяти у відношенні один до одного в дусі братерства.'),
	        ('131', 'Isolates', 'Basque', 'udhr_eu', 'Gizon-emakume guztiak aske jaiotzen dira, duintasun eta eskubide berberak dituztela; eta ezaguera eta kontzientzia dutenez gero, elkarren artean senide legez jokatu beharra dute.'),
	        ('132', 'Japonic', 'Japanese', 'udhr_jp', 'すべての人間は、生まれながらにして自由であり、かつ、尊厳と権利とについて平等である。人間は、理性と良心を授けられてあり、互いに同胞の精神をもって行動しなければならない。'),
	        ('133', 'Koreanic', 'Korean', 'udhr_kr', '모든 인간은 태어날 때부터 자유로우며 그 존엄과 권리에 있어 동등하다. 인간은 천부적으로 이성과 양심을 부여받았으며 서로 형제애의 정신으로 행동하여야 한다.'),
	        ('134', 'Mongolic', 'Mongolian', 'udhr1_mo', 'ᠬᠦᠮᠦᠨ ᠪᠦᠷ ᠲᠥᠷᠥᠵᠦ ᠮᠡᠨᠳᠡᠯᠡᠬᠦ ᠡᠷᠬᠡ ᠴᠢᠯᠥᠭᠡ ᠲᠡᠢ᠂ ᠠᠳᠠᠯᠢᠬᠠᠨ ᠨᠡᠷ᠎ᠡ ᠲᠥᠷᠥ ᠲᠡᠢ᠂ ᠢᠵᠢᠯ ᠡᠷᠬᠡ ᠲᠡᠢ ᠪᠠᠢᠠᠭ᠃ ᠣᠶᠤᠨ ᠤᠬᠠᠭᠠᠨ᠂ ᠨᠠᠨᠳᠢᠨ ᠴᠢᠨᠠᠷ ᠵᠠᠶᠠᠭᠠᠰᠠᠨ ᠬᠦᠮᠦᠨ ᠬᠡᠭᠴᠢ ᠥᠭᠡᠷ᠎ᠡ ᠬᠣᠭᠣᠷᠣᠨᠳᠣ᠎ᠨ ᠠᠬᠠᠨ ᠳᠡᠭᠦᠦ ᠢᠨ ᠦᠵᠢᠯ ᠰᠠᠨᠠᠭᠠ ᠥᠠᠷ ᠬᠠᠷᠢᠴᠠᠬᠥ ᠤᠴᠢᠷ ᠲᠠᠢ᠃.'),
	        ('135', 'Niger-Congo', 'Akuapim Twi', 'udhr_twi', 'Wɔɑwo ɑdesɑmmɑ nyinɑɑ sɛ nnipɑ ɑ wɔwɔ ɑhofɑdi. Wɔn nyinɑɑ wɔ nidi ne kyɛfɑ koro. Wɔwɔ ɑdwene ne ɑhonim, nɑ ɛsɛ sɛ wobu wɔn ho wɔn ho sɛ ɑnuɑnom.'),
	        ('136', 'Niger-Congo', 'Wolof', 'udhr_wo', 'Doomi aadama yépp dañuy juddu, yam ci tawfeex ci sag ak sañ-sañ. Nekk na it ku xam dëgg te ànd na ak xelam, te war naa jëflante ak nawleem, te teg ko ci wàllu mbokk.'),
	        ('137', 'Pidgins and creoles', 'Betawi', 'udhr_betawi', 'Semue orang ntu dilahirin bebas ame punye martabat dan hak-hak yang same. Mereka ntu dikasih akal ame ati nurani dan kudu bergaul satu ame lainnye dalem semangat persaudaraan.'),
	        ('138', 'Pidgins and creoles', 'Chavacano', 'udhr_chabacano', 'Todo''l maga ser humano nace libre e igual en dignidad y maga derecho. Dotado con ellos el razon y conciencia y debe ellos comporta fraternalmente con el maga uno con el maga otro.'),
	        ('139', 'Pidgins and creoles', 'Pijin – Solomons Pidgin', 'udhr_pijin', 'Evri man en mere olketa born frii en ikwol lo digniti en raits blo olketa. Olketa evriwan olketa garem maeni fo tingting en olketa sapos fo treatim isada wittim spirit blo bradahood.'),
	        ('140', 'Sino-Tibetan', 'Burmese', 'udhr_burmese', 'လူတိုင်းသည် တူညီ လွတ်လပ်သော ဂုဏ်သိက္ခာဖြင့် လည်းကောင်း၊ တူညီလွတ်လပ်သော အခွင့်အရေးများဖြင့် လည်းကောင်း၊ မွေးဖွားလာသူများ ဖြစ်သည်။ ထိုသူတို့၌ ပိုင်းခြား ဝေဖန်တတ်သော ဉာဏ်နှင့် ကျင့်ဝတ် သိတတ်သော စိတ်တို့ရှိကြ၍ ထိုသူတို့သည် အချင်းချင်း မေတ္တာထား၍ ဆက်ဆံကျင့်သုံးသင့်၏။'),
	        ('141', 'Sino-Tibetan', 'Cantonese', 'udhr_cantonese', '人人生出嚟就係自由嘅，喺尊嚴同權利上一律平等。佢哋具有理性同良心，而且應該用兄弟間嘅關係嚟互相對待。'),
	        ('142', 'Sino-Tibetan', 'Karbi', 'udhr_karbi', 'Monit hijan angbong kibi kethe kangtui kangdai pu ave. Arnam monit aphan kamathathek ajakong kipi. Lasi ning isivet pen dorapsi kachinghon chijinso pen donang ji.'),
	        ('143', 'Sino-Tibetan', 'Mandarin Chinese', 'udhr_mandarin', '人人生而自由﹐在尊嚴和權利上一律平等。他們賦有理性和良心﹐並應以兄弟關係的精神互相對待。'),
	        ('144', 'Siouan', 'Lakota', 'udhr_lakota', 'Wičháša na wíŋyaŋ otóiyohi iglúhapi na iyéhaŋyaŋ wówažapi. Tȟaŋmáhel slol''íč''iyapi na kičhíwičhowepi s''e kičhíčhuwapi kta héčha.'),
	        ('145', 'Tai-Kadai', 'Thai', 'udhr_th', 'เราทุกคนเกิดมาอย่างอิสระ เราทุกคนมีความคิดและความเข้าใจเป็นของเราเอง เราทุกคนควรได้รับการปฏิบัติในทางเดียวกัน.'),
	        ('146', 'Turkic', 'Azerbaijani', 'udhr_azturk', 'بوتون اينسانلار حيثييت و حاقلار باخيميندان دنك و اركين دوغولارلار.اوس و اويات ييهﺳﻴﺪيرلر و بير بيرلرينه قارشى قارداشليق روحو ايله داوراماليدرلار.'),
	        ('147', 'Turkic', 'Kyrgyz', 'udhr_kyrgyz', 'Бардык адамдар өз беделинде жана укуктарында эркин жана тең укуктуу болуп жаралат. Алардын аң -сезими менен абийири бар жана бири-бирине бир туугандык мамиле кылууга тийиш.'),
	        ('148', 'Turkic', 'Turkish', 'udhr_tr', 'Bütün insanlar hür, haysiyet ve haklar bakımından eşit doğarlar. Akıl ve vicdana sahiptirler ve birbirlerine karşı kardeşlik zihniyeti ile hareket etmelidirler. | بتون انسانلر حر، حيشيت و حقلر باقمڭدن اشت طوغرلر. عقل و وجدانه صحبترلر و بربرلرينه قارشو قرداشلق ذهنيت ايله حركت اتمهلودرلر.'),
	        ('149', 'Turkic', 'Turkmen', 'udhr_turkmen', 'Хемме адамлар өз мертебеси ве хукуклары бюнча дең ягдайда дүнйә инйәрлер.Олара аң хем выждан берлендир ве олар бир-бирлери билен доганлык рухундакы гарайышда болмалыдырлар.'),
	        ('150', 'Turkic', 'Uyghur', 'udhr_uyghur', 'ﮬﻪﻣﻤﻪ ئادەم زاﻧﯩﺪﯨﻨﻼ ﺋﻪﺭﻛﯩﻦ، ﺋﯩﺰﺯﻩﺕ-ھۆرﻣﻪت ۋە ھوقۇقتا باپباراۋەر بولۇپ تۇغۇلغان. ئۇلار ﺋﻪﻗﯩﻠﮕﻪ ۋە ۋﯨﺠﺪﺍﻧﻐﺎ ﺋﯩﮕﻪ ﮬﻪﻣﺪﻩ ﺑﯩﺮ-ﺑﯩﺮﯨﮕﻪ ﻗﯧﺮﯨﻨﺪﺍﺷﻠﯩﻖ ﻣﯘﻧﺎﺳﯩﯟﯨﺘﯩﮕﻪ ﺧﺎﺱ ﺭﻭﮪ ﺑﯩﻠﻪﻥ ﻣﯘﺋﺎﻣﯩﻠﻪ ﻗﯩﻠﯩﺸﻰ ﻛﯧﺮەك.'),
	        ('151', 'Turkic', 'Uzbek', 'udhr_uz', 'H̡əmmə adəm zatidinla ərkin, izzət-h̡ɵrmət wə hok̡uk̡ta babbarawər bolup tuƣulƣan. Ular ək̡ilƣə wə wijdanƣa igə h̡əmdə bir-birigə k̡erindaxlik̡ munasiwitigə hax roh bilən mu’amilə k̡ilixi kerək.'),
	        ('152', 'Uralic', 'Estonian', 'udhr_et', 'Kõik inimesed sünnivad vabadena ja võrdsetena oma väärikuselt ja õigustelt. Neile on antud mõistus ja südametunnistus ja nende suhtumist üksteisesse peab kandma vendluse vaim.'),
	        ('153', 'Uralic', 'Finnish', 'udhr2_fi', 'Kaikki ihmiset syntyvät vapaina ja tasavertaisina arvoltaan ja oikeuksiltaan. Heille on annettu järki ja omatunto, ja heidän on toimittava toisiaan kohtaan veljeyden hengessä.'),
	        ('154', 'Uralic', 'Hungarian', 'udhr_hu', 'Minden emberi lény szabadon születik és egyenlő méltósága és joga van. Az emberek, ésszel és lelkiismerettel bírván, egymással szemben testvéri szellemben kell hogy viseltessenek.'),
	        ('155', 'Uralic', 'Livonian', 'udhr_livonian', 'Amād rovzt attõ sindõnd brīd ja īdlizt eņtš vǟrtitõks ja õigiztõks. Näntõn um andtõd mūoštõks ja sidāmtundimi, ja näntõn um īdtuoisõ tuoimõmõst veļkub vaimsõ.'),
	        ('156', 'Uralic', 'North Sámi', 'udhr_northernsami', 'Buot olbmot leat riegádan friddjan ja olmmošárvvu ja olmmošvuoigatvuođaid dáfus . Sii leat jierbmalaš olbmot geain lea oamedovdu ja sii gálggaše leat dego vieljačagat.'); 
    ''')

    conn.commit()
    conn.close()
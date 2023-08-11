Registration: user inputs credentials into registration form, browser sends credentials to /register.
Login: user inputs credentials into login form, browser sends credentials to /login, gets access token + refresh token
Token Refresh: once access token has expired (15 min), browser sends refresh token to /refresh to get new access token
Logout: browser sends POST to /logout, server revokes refresh tokens
Gameplay: browser sends GET requests to /language, $n_{fakes} + 1$ times, shows true audio, shows true and fake scripts, once user has chosen, it displays what was right and wrong, the language families of all texts, and the correct name of the fakes, browser sends points to /points (to be implemented) and server adds the points to DB
Hints: TBD

# CS50 Final Project `lang50`

## Context

The `lang50` project is a joint venture of Ulysse Berra and Aurélien Berra. It serves as our Harvard CS50x final project, as well as changing the world, one nerdy game at a time.

## Definition and Aim

Develop a simple web-based language quiz app. It requires the user to listen to audio snippets of natural or constructed languages and to identify matching transcriptions in the original scripts.

## Inspiration

Our main inspiration is the online geeky game Language Squad. It was itself derived from the extinct project [The Great Language Game](https://greatlanguagegame.com/), for which legacy documentation and [data](https://lars.yencken.org/datasets/great-language-game/) are available. The open (CC BY) data consist in "a confusion dataset based on usage" and is "meant to help researchers and hobbyists examine what languages people commonly confuse for one another": "Usage data from the Great Language Game, containing the guesses users made in identifying unknown foreign language audio samples. The 2014-03-02 version of this dataset contains some 16 million records of guesses, one JSON record per line." These data could provide a criterion for setting difficulty levels.

Other similar projects are mentioned by the creator of the original game:

* [Ling Your Language](https://lingyourlanguage.com/) uses only audio snippets, but implements most of the features we initially had in mind and many more:
    * samples: "Over 2,500 samples in nearly 100 languages and 200 dialects from around the world"
    * learning resources about language families: "Information on every language available both in-game and on a dedicated Learn page", with classifications and link to scholarly articles
    * user profiles and leaderboard: "User profiles: track your high scores and compare them with other players, and level up your account from mere “Language enthusiast” to “Omniglot” – master of all languages!"
    * competition: "Two different multiplayer modes, each for up to four players - compete with friends and family to see who’s got the best ear for languages!"
* [Language Squad](https://www.languagesquad.com/)'s originality is that it features two modes : audio to guess from spoken samples or alphabet to guess from written languages in the original scripts. After selecting a difficulty level, the user has to choose between an increasing number of language names, either scoring points for good answers or bumping the bombs count for errors – 3 bombs, and it is game over. There are no user accounts.
    * audio difficulty levels
        * beginner: 11 languages
        * easy: 24 languages
        * medium: 58 languages
        * hard: 92 languages
    * alphabet difficulty levels
        * easy: 20 alphabets
        * hard: 46 alphabets
    * interesting UI features
        * zoom on written samples (either Unicode text or images)
        * autoplay option for spoken samples
* [Name That Language](https://namethatlanguage.org/) was a simpler version, with different aesthetic choices. It does not work anymore. Apparently it had no difficulty levels, only rounds to go through with 3 lives.

## Technologies

We use the following technologies:

* Wireframing
    * [Figma](https://www.figma.com/)
* Back-end
    * [Java](https://www.java.com/) + [Spring Boot](https://spring.io/)
    * [H2 database](http://h2database.com/)
* Front-end
    * [Svelte](https://svelte.dev/) front end compiler
        * [Svelte Tutorial](https://svelte.dev/tutorial/)
        * [Svelte Documentation](https://svelte.dev/docs)
    * [SvelteKit](https://kit.svelte.dev/) Web framework
        * [SvelteKit Introduction](https://learn.svelte.dev/tutorial/introducing-sveltekit)
        * [SvelteKit Documentation](https://kit.svelte.dev/docs/introduction)
    * [TypeScript](https://www.typescriptlang.org/) language extending JavaScript
    * [Tailwind](https://tailwindcss.com/) CSS framework
    * [daisyUI](https://daisyui.com/) Tailwind CSS Components
* Language Resources
    * [Ethnologue](https://www.ethnologue.com/)
    * [Glottolog](https://glottolog.org/)
    * spoken snippets: [Wikitongues](https://wikitongues.org/)
    * scripts: ?

## Specifications

* Defining features
    * foreground association of oral and written forms of the languages: instead of recognizing the language being spoken, the user must choose the correct transcription in the original script out of a number of options
    * include constructed languages, on top of natural languages
    * include language variants: dialects, accents, historical forms [to be further defined]
    * make the game a learning experience: after the user answers the question, they are shown the correct script, along with the language's name; if the user chooses wrong, they are also shown the name of the written language they selected
    * provide hints to the user: specific language features to look for
    * add life refill mechanism: after 5 consecutive correct answers, 1 life gets refilled out of initial 3
    * provide the option to exclude specific languages, e.g. the user's native language

* Languages: first list (50 in total, as in `lang50`?)
    * natural languages (44, including 3 ancient)
        * Indo-European
            * Germanic
                * Afrikaans · afr | [Ethnologue](http://www.ethnologue.com/language/afr/) · [ISO](http://https//iso639-3.sil.org/code/afr) · [UDHR txt](https://unicode.org/udhr/d/udhr_afr.txt)
                * Danish · dan | [Ethnologue](http://www.ethnologue.com/language/dan/) · [ISO](http://https//iso639-3.sil.org/code/dan) · [UDHR txt](https://unicode.org/udhr/d/udhr_dan.txt)
                * Dutch · nld | [Ethnologue](http://www.ethnologue.com/language/nld/) · [ISO](http://https//iso639-3.sil.org/code/nld) · [UDHR txt](https://unicode.org/udhr/d/udhr_nld.txt)
                * English · eng | [Ethnologue](http://www.ethnologue.com/language/eng/) · [ISO](http://https//iso639-3.sil.org/code/eng) · [UDHR txt](https://unicode.org/udhr/d/udhr_eng.txt)
                * German · deu | [Ethnologue](http://www.ethnologue.com/language/deu/) · [ISO](http://https//iso639-3.sil.org/code/deu) · [UDHR txt](https://unicode.org/udhr/d/udhr_deu_1996.txt) [fix inconsistent use of ß/ss?]
                * Norwegian · nob | [Ethnologue](http://www.ethnologue.com/language/nob/) · [ISO](http://https//iso639-3.sil.org/code/nob) · [UDHR txt](https://unicode.org/udhr/d/udhr_nob.txt)
                * Swedish · swe | [Ethnologue](http://www.ethnologue.com/language/swe/) · [ISO](http://https//iso639-3.sil.org/code/swe) · [UDHR txt](https://unicode.org/udhr/d/udhr_swe.txt)
            * Latin
                * Classical Latin · lat | [Ethnologue](http://www.ethnologue.com/language/lat/) · [ISO](http://https//iso639-3.sil.org/code/lat) · [UDHR txt](https://unicode.org/udhr/d/udhr_lat.txt)
                * French · fra | [Ethnologue](http://www.ethnologue.com/language/fra/) · [ISO](http://https//iso639-3.sil.org/code/fra) · [UDHR txt](https://unicode.org/udhr/d/udhr_fra.txt)
                * Italian · ita | [Ethnologue](http://www.ethnologue.com/language/ita/) · [ISO](http://https//iso639-3.sil.org/code/ita) · [UDHR txt](https://unicode.org/udhr/d/udhr_ita.txt)
                * Portuguese (Portugal) · por_PT | [Ethnologue](http://www.ethnologue.com/language/por/) · [ISO](http://https//iso639-3.sil.org/code/por) · [UDHR txt](https://unicode.org/udhr/d/udhr_por_PT.txt)
                * Portuguese (Brazil) · por_BR | [Ethnologue](http://www.ethnologue.com/language/por/) · [ISO](http://https//iso639-3.sil.org/code/por) · [UDHR txt](https://unicode.org/udhr/d/udhr_por_BR.txt)
                * Romanian · ron | [Ethnologue](http://www.ethnologue.com/language/ron/) · [ISO](http://https//iso639-3.sil.org/code/ron) · [UDHR txt](https://unicode.org/udhr/d/udhr_ron_2006.txt)
                * Spanish · spa | [Ethnologue](http://www.ethnologue.com/language/spa/) · [ISO](http://https//iso639-3.sil.org/code/spa) · [UDHR txt](https://unicode.org/udhr/d/udhr_spa.txt)
            * Indo-Iranian
                * Bengali · ben | [Ethnologue](http://www.ethnologue.com/language/ben/) · [ISO](http://https//iso639-3.sil.org/code/ben) · [UDHR txt](https://unicode.org/udhr/d/udhr_ben.txt)
                * Farsi · pes | [Ethnologue](http://www.ethnologue.com/language/pes/) · [ISO](http://https//iso639-3.sil.org/code/pes) · [UDHR txt](https://unicode.org/udhr/d/udhr_pes_1.txt)
                * Hindi · hin | [Ethnologue](http://www.ethnologue.com/language/hin/) · [ISO](http://https//iso639-3.sil.org/code/hin) · [UDHR txt](https://unicode.org/udhr/d/udhr_hin.txt)
                * Marathi · mar | [Ethnologue](http://www.ethnologue.com/language/mar/) · [ISO](http://https//iso639-3.sil.org/code/mar) · [UDHR txt](https://unicode.org/udhr/d/udhr_mar.txt)
                * Punjabi · pnb | [Ethnologue](http://www.ethnologue.com/language/pnb/) · [ISO](http://https//iso639-3.sil.org/code/pnb) · [UDHR txt](https://unicode.org/udhr/d/udhr_pnb.txt)
                * Sanskrit · san | [Ethnologue](http://www.ethnologue.com/language/san/) · [ISO](http://https//iso639-3.sil.org/code/san) · [UDHR txt](https://unicode.org/udhr/d/udhr_san.txt)
                * Urdu · urd | [Ethnologue](http://www.ethnologue.com/language/urd/) · [ISO](http://https//iso639-3.sil.org/code/urd) · [UDHR txt](https://unicode.org/udhr/d/udhr_urd.txt)
            * Hellenic
                * Ancient Greek · grc @find-source | [Ethnologue](http://www.ethnologue.com/language/grc/) · [ISO](http://https//iso639-3.sil.org/code/grc) · [UDHR txt](https://unicode.org/udhr/d/udhr_grc.txt)
                * Modern Greek · ell | [Ethnologue](http://www.ethnologue.com/language/ell/) · [ISO](http://https//iso639-3.sil.org/code/ell) · [UDHR txt](https://unicode.org/udhr/d/udhr_ell_monotonic.txt)
            * Slavic
                * Czech · ces | [Ethnologue](http://www.ethnologue.com/language/ces/) · [ISO](http://https//iso639-3.sil.org/code/ces) · [UDHR txt](https://unicode.org/udhr/d/udhr_ces.txt)
                * Polish · pol | [Ethnologue](http://www.ethnologue.com/language/pol/) · [ISO](http://https//iso639-3.sil.org/code/pol) · [UDHR txt](https://unicode.org/udhr/d/udhr_pol.txt)
                * Russian · rus | [Ethnologue](http://www.ethnologue.com/language/rus/) · [ISO](http://https//iso639-3.sil.org/code/rus) · [UDHR txt](https://unicode.org/udhr/d/udhr_rus.txt)
                * Slovak · slk | [Ethnologue](http://www.ethnologue.com/language/slk/) · [ISO](http://https//iso639-3.sil.org/code/slk) · [UDHR txt](https://unicode.org/udhr/d/udhr_slk.txt)
                * Ukranian · ukr | [Ethnologue](http://www.ethnologue.com/language/ukr/) · [ISO](http://https//iso639-3.sil.org/code/ukr) · [UDHR txt](https://unicode.org/udhr/d/udhr_ukr.txt)
        * Dravidian
            * Kannada · kan | [Ethnologue](http://www.ethnologue.com/language/kan/) · [ISO](http://https//iso639-3.sil.org/code/kan) · [UDHR txt](https://unicode.org/udhr/d/udhr_kan.txt)
            * Malayalam · mal | [Ethnologue](http://www.ethnologue.com/language/mal/) · [ISO](http://https//iso639-3.sil.org/code/mal) · [UDHR txt](https://unicode.org/udhr/d/udhr_mal.txt)
            * Tamil · tam | [Ethnologue](http://www.ethnologue.com/language/tam/) · [ISO](http://https//iso639-3.sil.org/code/tam) · [UDHR txt](https://unicode.org/udhr/d/udhr_tam.txt)
            * Telugu · tel | [Ethnologue](http://www.ethnologue.com/language/tel/) · [ISO](http://https//iso639-3.sil.org/code/tel) · [UDHR txt](https://unicode.org/udhr/d/udhr_tel.txt)
        * Sino-Tibetan
            * Cantonese Chinese · yue | [Ethnologue](http://www.ethnologue.com/language/yue/) · [ISO](http://https//iso639-3.sil.org/code/yue) · [UDHR txt](https://unicode.org/udhr/d/udhr_yue.txt)
            * Mandarin Chinese · cmn | [Ethnologue](http://www.ethnologue.com/language/cmn/) · [ISO](http://https//iso639-3.sil.org/code/cmn) · [UDHR txt](https://unicode.org/udhr/d/udhr_cmn_hant.txt)
        * Austronesian
            * Indonesian · ind | [Ethnologue](http://www.ethnologue.com/language/ind/) · [ISO](http://https//iso639-3.sil.org/code/ind) · [UDHR txt](https://unicode.org/udhr/d/udhr_ind.txt)
        * Afro-Asiatic
            * Arabic · arb | [Ethnologue](http://www.ethnologue.com/language/arb/) · [ISO](http://https//iso639-3.sil.org/code/arb) · [UDHR txt](https://unicode.org/udhr/d/udhr_arb.txt)
            * Hebrew · heb | [Ethnologue](http://www.ethnologue.com/language/heb/) · [ISO](http://https//iso639-3.sil.org/code/heb) · [UDHR txt](https://unicode.org/udhr/d/udhr_heb.txt)
        * @TODO classify languages below
            * Basque · eus | [Ethnologue](http://www.ethnologue.com/language/eus/) · [ISO](http://https//iso639-3.sil.org/code/eus) · [UDHR txt](https://unicode.org/udhr/d/udhr_eus.txt)
            * Georgian · kat | [Ethnologue](http://www.ethnologue.com/language/kat/) · [ISO](http://https//iso639-3.sil.org/code/kat) · [UDHR txt](https://unicode.org/udhr/d/udhr_kat.txt)
            * Japanese · jpn | [Ethnologue](http://www.ethnologue.com/language/jpn/) · [ISO](http://https//iso639-3.sil.org/code/jpn) · [UDHR txt](https://unicode.org/udhr/d/udhr_jpn.txt)
            * Khmer · khm | [Ethnologue](http://www.ethnologue.com/language/khm/) · [ISO](http://https//iso639-3.sil.org/code/khm) · [UDHR txt](https://unicode.org/udhr/d/udhr_khm.txt)
            * Nigerian Pidgin · pcm | [Ethnologue](http://www.ethnologue.com/language/pcm/) · [ISO](http://https//iso639-3.sil.org/code/pcm) · [UDHR txt](https://unicode.org/udhr/d/udhr_pcm.txt)
            * Thai · tha | [Ethnologue](http://www.ethnologue.com/language/tha/) · [ISO](http://https//iso639-3.sil.org/code/tha) · [UDHR txt](https://unicode.org/udhr/d/udhr_tha.txt)
            * Turkish · tur | [Ethnologue](http://www.ethnologue.com/language/tur/) · [ISO](http://https//iso639-3.sil.org/code/tur) · [UDHR txt](https://unicode.org/udhr/d/udhr_tur.txt)
            * Vietnamese · vie | [Ethnologue](http://www.ethnologue.com/language/vie/) · [ISO](http://https//iso639-3.sil.org/code/vie) · [UDHR txt](https://unicode.org/udhr/d/udhr_vie.txt)
        * archive: language groups not represented
            * Niger-Congo
            * Uralic
            * Trans-New Guinea
    * constructed languages (6)
        * Esperanto · epo | [Ethnologue](http://www.ethnologue.com/language/epo/) · [ISO](http://https//iso639-3.sil.org/code/epo) · [UDHR txt](https://unicode.org/udhr/d/udhr_epo.txt)
        * High Valyrian (_Game of Thrones_)
        * Klingon (_Star Trek_)
        * Na'vi (_Avatar_)
        * Quenya (Tolkien)
        * Toki Pona
        * archive: constructed languages for which data are insufficient
            * Oqolaawak ([Biblaridion](https://www.youtube.com/channel/UCMjTcpv56G_W0FRIdPHBn4A))
            * Nekāchti ([Biblaridion](https://www.youtube.com/channel/UCMjTcpv56G_W0FRIdPHBn4A))
            * Edun ([Biblaridion](https://www.youtube.com/channel/UCMjTcpv56G_W0FRIdPHBn4A))
            * Ilothwii ([Biblaridion](https://www.youtube.com/channel/UCMjTcpv56G_W0FRIdPHBn4A))

* Languages: selected audio samples from Omniglot, Article 1 of the Universal Declaration of Human Rights (UDHR)
    * see list in files

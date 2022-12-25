# CS50 Final Project `lang50`

## Context

The `lang50` project is a joint venture of Ulysse Berra and Aurélien Berra. It serves as our Harvard CS50x final project, as well as changing the world, one nerdy game at a time.

## Definition and Aim

Develop a simple web-based language quiz app. It requires the user to listen to audio snippets of natural or constructed languages and to identify matching transcriptions in the original scripts.

## Inspiration

Our main inspiration is the online geeky game Language Squad. It was itself derived from the extinct project [The Great Language Game](https://greatlanguagegame.com/), for which legacy documentation and [data](https://lars.yencken.org/datasets/great-language-game/) are available. The open (CC BY) data consist in "a confusion dataset based on usage" and is "meant to help researchers and hobbyists examine what languages people commonly confuse for one another": "Usage data from the Great Language Game, containing the guesses users made in identifying unknown foreign language audio samples. The 2014-03-02 version of this dataset contains some 16 million records of guesses, one JSON record per line." These data could provide a criterion for setting difficulty levels.

Other similar projects are mentioned by the creator of the original game:

-   [Ling Your Language](https://lingyourlanguage.com/) uses only audio snippets, but implements most of the features we initially had in mind and many more:
    -   samples: "Over 2,500 samples in nearly 100 languages and 200 dialects from around the world"
    -   learning resources about language families: "Information on every language available both in-game and on a dedicated Learn page", with classifications and link to scholarly articles
    -   user profiles and leaderboard: "User profiles: track your high scores and compare them with other players, and level up your account from mere “Language enthusiast” to “Omniglot” – master of all languages!"
    -   competition: "Two different multiplayer modes, each for up to four players - compete with friends and family to see who’s got the best ear for languages!"
-   [Language Squad](https://www.languagesquad.com/)'s originality is that it features two modes : audio to guess from spoken samples or alphabet to guess from written languages in the original scripts. After selecting a difficulty level, the user has to choose between an increasing number of language names, either scoring points for good answers or bumping the bombs count for errors – 3 bombs, and it is game over. There are no user accounts.
    -   audio difficulty levels
        -   beginner: 11 languages
        -   easy: 24 languages
        -   medium: 58 languages
        -   hard: 92 languages
    -   alphabet difficulty levels
        -   easy: 20 alphabets
        -   hard: 46 alphabets
    -   interesting UI features
        -   zoom on written samples (either Unicode text or images)
        -   autoplay option for spoken samples
-   [Name That Language](https://namethatlanguage.org/) was a simpler version, with different aesthetic choices. It does not work anymore. Apparently it had no difficulty levels, only rounds to go through with 3 lives.

## Technologies

We use the following technologies:

-   Back-end
    -   [Java](https://www.java.com/) + [Spring Boot](https://spring.io/)
    -   ? database
-   Front-end
    -   [Svelte](https://svelte.dev/) front end compiler
        -   [Svelte Tutorial](https://svelte.dev/tutorial/)
        -   [Svelte Documentation](https://svelte.dev/docs)
    -   [SvelteKit](https://kit.svelte.dev/) Web framework
        -   [SvelteKit Introduction](https://learn.svelte.dev/tutorial/introducing-sveltekit)
        -   [SvelteKit Documentation](https://kit.svelte.dev/docs/introduction)
    -   [Tailwind](https://tailwindcss.com/) CSS framework
    -   perhaps
        -   [TypeScript](https://www.typescriptlang.org/) language extending JavaScript
        -   [Bootstrap](https://getbootstrap.com/) front end framework
        -   ? unit test library
-   Wireframe
    -   [Figma](https://www.figma.com/)
-   Language Resources
    -   [Ethnologue](https://www.ethnologue.com/)
    -   [Glottolog](https://glottolog.org/)
    -   spoken snippets: [Wikitongues](https://wikitongues.org/)
    -   scripts: ?

## Specifications

-   Defining features

    -   include constructed languages, on top of natural languages
    -   provide hints to the user: specific language features to look for
    -   add life refill mechanism: after 5 consecutive correct answers, 1 life gets refilled out of initial 3
    -   foreground association of oral and written forms of the languages: instead of recognizing the language being spoken, the user must choose the correct transcription in the original script out of a number of options [to be further defined: also the reverse, i.e. see script and select audio?]
    -   provide the option to exclude specific languages, e.g. the user's native language
    -   include language variants: dialects, accents, historical forms [to be further defined]
    -   make the game a learning experience: after the user answers the question, they are shown the correct script, along with the language's name; if the user chooses wrong, they are also shown the name of the written language they selected

-   Languages (50 in total, as in `lang50`?)
    -   natural languages
        -   Indo-European
            -   Germanic
                -   Norwegian
                -   Swedish
                -   Danish
                -   German
                -   Dutch
                -   Afrikaans
            -   Latin
                -   French
                -   Classical Latin
                -   Spanish
                -   Italian
                -   Romanian
            -   Indo-Iranian
                -   Sanskrit
                -   Farsi
                -   Hindi
            -   Hellenic
                -   Ancient Greek
                -   Modern Greek
            -   Slavic
        -   Dravidian
        -   Sino-Tibetan
        -   Niger-Congo
        -   Austronesian
        -   Uralic
        -   Afro-Asiatic
            -   Arabic
            -   Hebrew
        -   Trans-New Guinea
    -   @REFERENCE Top 20 most spoken languages (Ethnologue, 2022)
        -   English (1.5 B)
        -   Mandarin Chinese (1.1 B)
        -   Hindi (602.2 M)
        -   Spanish (548.3 M)
        -   French (274.1 M)
        -   Standard Arabic (274.0 M)
        -   Bengali (272.7 M)
        -   Russian (258.2 M)
        -   Portuguese (257.7 M)
        -   Urdu (231.3 M)
        -   Indonesian (199.0 M)
        -   Standard German (134.6 M)
        -   Japanese (125.4 M)
        -   Nigerian Pidgin (120.7 M)
        -   Marathi (99.1 M)
        -   Telugu (95.7 M)
        -   Turkish (88.1 M)
        -   Tamil (86.4 M)
        -   Yue Chinese (85.6 M)
        -   Vietnamese (85.3 M)
    -   constructed languages (10)
        -   Esperanto
        -   Toki Pona
        -   Klingon (_Star Trek_)
        -   Quenya (Tolkien)
        -   High Valyrian (_Game of Thrones_)
        -   Na'vi (_Avatar_)
        -   Oqolaawak ([Biblaridion](https://www.youtube.com/channel/UCMjTcpv56G_W0FRIdPHBn4A))
        -   Nekāchti ([Biblaridion](https://www.youtube.com/channel/UCMjTcpv56G_W0FRIdPHBn4A))
        -   Edun ([Biblaridion](https://www.youtube.com/channel/UCMjTcpv56G_W0FRIdPHBn4A))
        -   Ilothwii ([Biblaridion](https://www.youtube.com/channel/UCMjTcpv56G_W0FRIdPHBn4A))

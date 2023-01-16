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

-   Wireframing
    -   [Figma](https://www.figma.com/)
-   Back-end
    -   [Java](https://www.java.com/) + [Spring Boot](https://spring.io/)
    -   [H2 database](http://h2database.com/)
-   Front-end
    -   [Svelte](https://svelte.dev/) front end compiler
        -   [Svelte Tutorial](https://svelte.dev/tutorial/)
        -   [Svelte Documentation](https://svelte.dev/docs)
    -   [SvelteKit](https://kit.svelte.dev/) Web framework
        -   [SvelteKit Introduction](https://learn.svelte.dev/tutorial/introducing-sveltekit)
        -   [SvelteKit Documentation](https://kit.svelte.dev/docs/introduction)
    -   [TypeScript](https://www.typescriptlang.org/) language extending JavaScript
    -   [Tailwind](https://tailwindcss.com/) CSS framework
    -   [daisyUI](https://daisyui.com/) Tailwind CSS Components
-   Language Resources
    -   [Ethnologue](https://www.ethnologue.com/)
    -   [Glottolog](https://glottolog.org/)
    -   spoken snippets: [Wikitongues](https://wikitongues.org/)
    -   scripts: ?

## Specifications

-   Defining features

    -   foreground association of oral and written forms of the languages: instead of recognizing the language being spoken, the user must choose the correct transcription in the original script out of a number of options
    -   include constructed languages, on top of natural languages
    -   include language variants: dialects, accents, historical forms [to be further defined]
    -   make the game a learning experience: after the user answers the question, they are shown the correct script, along with the language's name; if the user chooses wrong, they are also shown the name of the written language they selected
    -   provide hints to the user: specific language features to look for
    -   add life refill mechanism: after 5 consecutive correct answers, 1 life gets refilled out of initial 3
    -   provide the option to exclude specific languages, e.g. the user's native language

-   Languages (50 in total, as in `lang50`?)
    -   natural languages (44, including 3 ancient)
        -   Indo-European
            -   Germanic
                -   Afrikaans
                -   Danish
                -   Dutch
                -   English
                -   German
                -   Norwegian
                -   Swedish
            -   Latin
                -   Classical Latin
                -   French
                -   Italian
                -   Portuguese
                -   Romanian
                -   Spanish
            -   Indo-Iranian
                -   Bengali
                -   Farsi
                -   Hindi
                -   Marathi
                -   Punjabi
                -   Sanskrit
                -   Urdu
            -   Hellenic
                -   Ancient Greek
                -   Modern Greek
            -   Slavic
                -   Czech
                -   Polish
                -   Russian
                -   Slovak
                -   Ukranian
        -   Dravidian
            -   Kannada
            -   Malayalam
            -   Tamil
            -   Telugu
        -   Sino-Tibetan
            -   Cantonese Chinese
            -   Mandarin Chinese
        -   Austronesian
            -   Indonesian
        -   Afro-Asiatic
            -   Arabic
            -   Hebrew
        -   @TODO classify languages below
            -   Basque
            -   Georgian
            -   Japanese
            -   Khmer
            -   Nigerian Pidgin
            -   Thai
            -   Turkish
            -   Vietnamese
        -   archive: language groups not represented
            -   Niger-Congo
            -   Uralic
            -   Trans-New Guinea
    -   constructed languages (6)
        -   Esperanto
        -   High Valyrian (_Game of Thrones_)
        -   Klingon (_Star Trek_)
        -   Na'vi (_Avatar_)
        -   Quenya (Tolkien)
        -   Toki Pona
        -   archive: constructed languages for which data are insufficient
            -   Oqolaawak ([Biblaridion](https://www.youtube.com/channel/UCMjTcpv56G_W0FRIdPHBn4A))
            -   Nekāchti ([Biblaridion](https://www.youtube.com/channel/UCMjTcpv56G_W0FRIdPHBn4A))
            -   Edun ([Biblaridion](https://www.youtube.com/channel/UCMjTcpv56G_W0FRIdPHBn4A))
            -   Ilothwii ([Biblaridion](https://www.youtube.com/channel/UCMjTcpv56G_W0FRIdPHBn4A))

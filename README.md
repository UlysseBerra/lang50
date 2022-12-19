# CS50 Final Project `lang50`

## Context

The `lang50` project is a joint venture of Ulysse Berra and Aurélien Berra. It serves as our Harvard CS50x final project, as well as changing the world, one erudite joke at a time.

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
    -   [Name That Language](https://namethatlanguage.org/) was a simpler version, with different aesthetic choices. It does not work any more. Apparently it had no difficulty levels, only rounds to go through with 3 lives.

## Specifications

We use the following technologies:

-   Back-end
    -   Java + Spring Boot
    -   ? database
-   Front-end
    -   TypeScript + [Svelte](https://svelte.dev/) and [SvelteKit](https://kit.svelte.dev/)
        -   [Svelte Tutorial](https://svelte.dev/tutorial/)
        -   [Svelte Documentation](https://svelte.dev/docs)
        -   [SvelteKit Introduction](https://learn.svelte.dev/tutorial/introducing-sveltekit)
        -   [SvelteKit Documentation](https://kit.svelte.dev/docs/introduction)
    -   ? Tailwind or Bootstrap
    -   ? unit test library
-   Wireframing
    -   [Figma](https://www.figma.com/)
-   Language Resources
    -   spoken snippets: [Wikitongues](https://wikitongues.org/)
    -   scripts: ?

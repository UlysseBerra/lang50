<script>
  import WelcomeBox from '$lib/components/WelcomeBox.svelte';
  import lang50_logo from "$lib/images/lang50_logo_dark.png";
</script>

<svelte:head>
  <title>Home</title>
  <meta name="description" content="lang50 app" />
</svelte:head>

<section>

<div class="flex flex-col items-center mt-6 font-serif text-7xl italic">
  <WelcomeBox />
</div>

<div class="flex flex-col items-center mt-48">
  <span class="text-8xl rounded-lg hover:bg-opacity-100">
    &#9758; <a class="font-serif font-extrabold italic" href="/game">Play!</a> &#9756;
  </span>
  <p class="text-xl text-center mt-6">
    Identify languages — ancient, modern, and constructed.
  </p>
</div>

<h1 class="mt-72">
  <div class="text-center text-base">
    <p>
      <span class="lang50_logo">
      <picture>
        <source srcset={lang50_logo} type="image/png" />
        <img src={lang50_logo} width="55px" alt="lang50" />
      </picture>
      </span>
        is a project by <strong>Ulysse Berra</strong> and <strong>Aurélien Berra</strong>.
    </p>
    <p class="mt-5">
        This nerdy game serves as our
        <a href="https://cs50.harvard.edu/x/">Harvard CS50x</a>
        final project.

        It relies on the following technologies:
        design and wireframing with <a href="https://www.figma.com/">Figma</a>;
        back-end in <a href="https://www.python.org/">Python</a> with
        <a href="https://fastapi.tiangolo.com/">FastAPI</a>
        and a <a href="https://sqlite.org/">SQLite</a> database;
        front-end with <a href="https://svelte.dev/">Svelte</a> and
        <a href="https://kit.svelte.dev/">SvelteKit</a>,
        <a href="https://www.typescriptlang.org/">TypeScript</a>,
        <a href="https://tailwindcss.com/">Tailwind</a> and
        <a href="https://daisyui.com/">daisyUI</a>;
        project logo created in <a href="https://cran.r-project.org/">R</a>.
        The files were edited mostly in <a href="https://vscodium.com/">VSCodium</a>,
        <a href="https://code.visualstudio.com/">Visual Studio Code</a>,
        and <a href="https://neovim.io/">Neovim</a>.

        To research the languages, <a href="https://www.ethnologue.com/">Ethnologue</a>
        and <a href="https://www.wikipedia.org/">Wikipedia</a> have been invaluable resources.

        If you are curious about our source for the recordings and the texts,
        please visit the legacy <a href="https://unicode.org/udhr/">UDHR in Unicode</a> website,
        as well as the current form of this initiative, now hosted by the
        <a href="https://www.ohchr.org/en/human-rights/universal-declaration/universal-declaration-human-rights/about-universal-declaration-human-rights-translation-project">United Nations</a>.

        Details, data and code are available on the
        <a href="https://github.com/UlysseBerra/lang50">
          <code>lang50</code>
        </a>
        GitHub repository.

        Oh, and while the welcome messages on the homepage
        are actually in 50 different languages, the game uses 156 languages.
        How many will you recognize?
    </p>
  </div>
</h1>

</section>

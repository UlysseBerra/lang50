<script lang="ts">
  import { onMount } from "svelte";

  // Import data
  interface Language {
    lang_id: number;
    lang_name: string;
    lang_text: string;
    lang_iso: string;
    audio_file: string;
  }

  // Define needed variables
  let allLanguages: Language[] = [];
  let currentOptions: Language[] = [];
  let correctLang: Language | null = null;

  let previousCorrectId: number | null = null;
  let previousSet: number[] = [];

  let feedback = "";
  let lives = 3;
  let round = 0;
  let score = 0;
  let gameOver = false;
  let answered = false;
  let countdown: number = 0;

  let audioEl: HTMLAudioElement | null = null;

  // Create a round with 3 languages, including 1 correct answer
  async function fetchLanguages() {
    const res = await fetch("http://localhost:8000/language/all");
    allLanguages = await res.json();
    newRound();
  }

  function arraysEqual(a: number[], b: number[]) {
    return a.length === b.length && a.every((val, i) => val === b[i]);
  }

  function newRound() {
    if (lives <= 0) {
      gameOver = true;
      return;
    }

    round++;
    answered = false;
    feedback = "";
    countdown = 5;

    let options: Language[] = [];
    let newCorrect: Language | null = null;

    // Avoid having the same answers twice in a row:
    // shuffle until we get a different set of languages
    // and a different correct answer
    do {
      options = [...allLanguages]
        .sort(() => Math.random() - 0.5)
        .slice(0, 3);

      newCorrect = options[Math.floor(Math.random() * options.length)];
    } while (
      !newCorrect ||
      newCorrect.lang_id === previousCorrectId ||
      arraysEqual(options.map((o) => o.lang_id), previousSet)
    );

    currentOptions = options;
    correctLang = newCorrect;

    previousCorrectId = correctLang.lang_id;
    previousSet = options.map((o) => o.lang_id);

    // Load the audio element
    queueMicrotask(() => {
      if (audioEl) {
        audioEl.load();
      }
    });
  }

  // Set up answer and feedback mechanism
  function checkAnswer(lang: Language) {
    if (!correctLang || answered) return;
    answered = true;

    if (lang.lang_id === correctLang.lang_id) {
      // Correct answer
      score++;
      feedback = `
      <div class="game text-center text-xl"><br><br>
      <span class="text-green-500 font-bold">Correct!</span> This is
        <a href="https://www.ethnologue.com/language/${correctLang.lang_iso}" target="_blank">
          <strong>${correctLang.lang_name}</strong>.
        </a><br><br>
      <span class="italic font-serif">${correctLang.lang_text}</span><br><br>
      <a href="https://www.ethnologue.com/language/${correctLang.lang_iso}"
        target="_blank" style="display: flex; justify-content: right;" class="text-lg -mt-2">
        Learn about this language
      </a>
      </div>`;
    } else {
      // Wrong answer
      lives--;
      feedback = `
      <div class="game text-center text-xl"><br><br>
      <span class="text-red-500 font-bold">Wrong!</span> The correct answer was
        <a href="https://www.ethnologue.com/language/${correctLang.lang_iso}" target="_blank">
          <strong>${correctLang.lang_name}</strong>.
        </a><br><br>
      <span class="italic font-serif">${correctLang.lang_text}</span><br><br>
      <a href="https://www.ethnologue.com/language/${correctLang.lang_iso}"
        target="_blank" style="display: flex; justify-content: right;" class="text-lg -mt-2">
        Learn about this language
      </a>
      </div>`;

      if (lives <= 0) {
          countdown = 5;
          let interval = setInterval(() => {
          countdown--;
            if (countdown <= 0) {
            clearInterval(interval);
                gameOver = true;
            }
          }, 1000);
      }
    }
  }

  function restartGame() {
    lives = 3;
    round = 0;
    score = 0;
    gameOver = false;
    countdown = 5;
    previousCorrectId = null;
    previousSet = [];
    newRound();
  }

  onMount(fetchLanguages);

  // Construct a cache-busting URL so the audio refreshes
  // at the beginning of every round
  $: audioSrc =
    correctLang
      ? `http://localhost:8000/audio/${correctLang.audio_file}`
      : "";
</script>

<!-- Implement game logic: rounds, lives, score, until the game is over -->
{#if gameOver}
  <div class="text-center">
    <h2 class="text-3xl font-bold mt-20 mb-5 text-[#A855F7]">Game Over</h2>
    <p class="text-xl mt-2">You reached round {round}!</p>
    <p class="text-xl mt-2 font-semibold">Final Score: {score}</p>
    <button class="bg-transparent text-[#89B4FA] uppercase font-bold py-2 px-4 mt-20 rounded outline hover:text-[#A855F7]"
      on:click={restartGame}>
        Start again
    </button>
  </div>

{:else}
  <div class="game text-center">
    <h2 class="text-3xl mt-20 mb-5 text-purple-500">Round {round}</h2>
    <p class={lives <= 0 ? "text-xl mb-2 text-red-500 font-bold" : "text-xl mb-2"}>Lives: {lives}</p>
    <p class="text-xl mb-20">Score: {score}</p>

    {#if correctLang}
      {#key round}
        <audio bind:this={audioEl} controls preload="auto">
          <source src={audioSrc} type="audio/mpeg" />
            Your browser does not support the audio element.
        </audio>
      {/key}
    {/if}

    <div class="options mt-20 flex justify-center gap-4">
      {#each currentOptions as lang}
        <button
          class="bg-transparent uppercase font-bold py-2 px-4 rounded outline hover:text-[#A855F7] disabled:opacity-50 disabled:cursor-not-allowed"
          on:click={() => checkAnswer(lang)}
          disabled={answered}
        >
          {lang.lang_name}
        </button>
      {/each}
    </div>

    {#if feedback}
      <div class="mt-4">
        {@html feedback}
      </div>
    {/if}

    {#if lives > 0 && feedback}
      <div>
        <br><br>
        <button class="bg-transparent text-[#89B4FA] uppercase font-bold py-2 px-4 rounded outline hover:text-[#A855F7] disabled:opacity-50 disabled:cursor-not-allowed"
          on:click={() => newRound()}
          disabled={lives <= 0}>
            Start next round now
        </button>
      </div>
    {:else if lives <= 0}
    <button class="bg-transparent text-red-500 font-bold py-2 px-4 rounded outline mt-5">
      GAME OVER!<br>
      Recap in {countdown}…
    </button>
    {/if}

  </div>
{/if}

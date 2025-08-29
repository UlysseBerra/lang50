<script lang="ts">
  import { onMount } from "svelte";

  interface Language {
    lang_id: number;
    lang_name: string;
    lang_text: string;
    lang_iso: string;
    audio_file: string;
  }

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

  let audioEl: HTMLAudioElement | null = null;

  async function fetchLanguages() {
    const res = await fetch("http://localhost:8000/language/all");
    allLanguages = await res.json();
    newRound(); // start first round
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

    let options: Language[] = [];
    let newCorrect: Language | null = null;

    // Shuffle until we get a different set and a different correct answer
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

    // If the audio element exists, reload it
    queueMicrotask(() => {
      if (audioEl) {
        audioEl.load();
      }
    });
  }

  function checkAnswer(lang: Language) {
    if (!correctLang || answered) return;
    answered = true;

    if (lang.lang_id === correctLang.lang_id) {
      score++;
      feedback = `
        ✅ Correct! This is <strong>${correctLang.lang_name}</strong>.<br>
        <em>${correctLang.lang_text}</em><br>
        <a href="https://www.ethnologue.com/language/${correctLang.lang_iso}"
           target="_blank" class="text-blue-500 underline">
           Learn about this language
        </a>`;
      setTimeout(() => newRound(), 10000);
    } else {
      lives--;
      feedback = `
        ❌ Wrong! The correct answer was <strong>${correctLang.lang_name}</strong>.<br>
        <em>${correctLang.lang_text}</em><br>
        <a href="https://www.ethnologue.com/language/${correctLang.lang_iso}"
           target="_blank" class="text-blue-500 underline">
           Learn about this language
        </a>`;
        setTimeout(() => newRound(), 10000);

      if (lives <= 0) {
        gameOver = true;
      } else {
        // setTimeout(() => newRound(), 3000);
      }
    }
  }

  function restartGame() {
    lives = 3;
    round = 0;
    score = 0;
    gameOver = false;
    previousCorrectId = null;
    previousSet = [];
    newRound();
  }

  onMount(fetchLanguages);

  // Construct a cache-busting URL so the audio refreshes every round
  $: audioSrc =
    correctLang
      ? `http://localhost:8000/audio/${correctLang.audio_file}`
      : "";
</script>

{#if gameOver}
  <div class="text-center mt-10">
    <h2 class="text-2xl font-bold">Game Over</h2>
    <p class="mt-2">You reached round {round}.</p>
    <p class="mt-1 font-semibold">Final Score: {score}</p>
    <button class="btn btn-primary mt-4" on:click={restartGame}>
      Start Again
    </button>
  </div>
{:else}
  <div class="game text-center">
    <h2 class="text-xl mb-4">Round {round}</h2>
    <p class="mb-2">Lives: {lives} · Score: {score}</p>

    {#if correctLang}
      <!-- Force reload the audio when round changes -->
      {#key round}
        <audio bind:this={audioEl} controls preload="auto">
          <source src={audioSrc} type="audio/mpeg" />
          Your browser does not support the audio element.
        </audio>
      {/key}
    {/if}

    <div class="options mt-4 flex justify-center gap-4">
      {#each currentOptions as lang}
        <button
          class="btn btn-outline"
          disabled={answered}
          on:click={() => checkAnswer(lang)}
        >
          {lang.lang_name}
        </button>
      {/each}
    </div>

    {#if feedback}
      <div class="mt-4">
        {@html feedback}
      </div>
      <div>
        <button
          class="btn btn-outline"
          on:click={() => newRound()}
        >
          Start next round now!
        </button>
      </div>
    {/if}
  </div>
{/if}

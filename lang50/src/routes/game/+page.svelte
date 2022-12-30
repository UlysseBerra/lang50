<script>
    let scripts = 1;

    // import { AudioPlayer } from "svelte-mp3";
    import AudioPlayer, { stopAll } from "./AudioPlayer.svelte";
    import idontunderstand_el from "$lib/audio/idontunderstand_el.mp3";
    let audioTrack = idontunderstand_el;
    // let audioTrack = "https://sveltejs.github.io/assets/music/satie.mp3";

    import runes from "$lib/images/runes.png";
    import greek_modern from "$lib/images/greek_modern.png";
    import georgian from "$lib/images/georgian.png";
</script>

<svelte:head>
    <title>Game</title>
    <meta name="description" content="This is the game" />
</svelte:head>

<div class="text-column">
    <h1>Game</h1>

    <div class="stats shadow">
        <div class="stat place-items-center">
            <div class="stat-title">Round</div>
            <div class="stat-value">1</div>
        </div>

        <div class="stat place-items-center">
            <div class="stat-title">Score</div>
            <div class="stat-value">0</div>
        </div>

        <div class="stat place-items-center">
            <div class="stat-title">Lives</div>
            <div class="stat-value">3</div>
        </div>
    </div>

    <h2>Audio: listen!</h2>

    <!-- @TODO make this work as per https://www.npmjs.com/package/svelte-mp3
        <AudioPlayer urls=["https://sveltejs.github.io/assets/music/satie.mp3","https://sveltejs.github.io/assets/music/satie.mp3"] /> -->

    <AudioPlayer src={audioTrack} />
    <!-- <button class="btn btn-ghost" on:click={stopAll} style="width:300px"
        >Stop!
    </button> -->

    <!-- <h2>Scripts as text</h2>

    <label>
        <input type="radio" bind:group={scripts} value={1} />
        ᚠᛇᚻ᛫ᛒᛦᚦ᛫ᚠᚱᚩᚠᚢᚱ᛫ᚠᛁᚱᚪ᛫ᚷᛖᚻᚹᛦᛚᚳᚢᛗ
    </label>

    <label>
        <input type="radio" bind:group={scripts} value={2} />
        Τη γλώσσα μου έδωσαν ελληνική
    </label>

    <label>
        <input type="radio" bind:group={scripts} value={3} />
        ვეპხის ტყაოსანი შოთა რუსთაველი
    </label> -->

    <h2>Scripts: pick the right script!</h2>

    <label>
        <input type="radio" bind:group={scripts} value={1} />
        <picture>
            <source srcset={runes} type="image/png" />
            <img src={runes} alt="runes" width="500px" />
        </picture>
        <button class="btn btn-ghost">Hint</button>
    </label>

    <label>
        <input type="radio" bind:group={scripts} value={2} />
        <picture>
            <source srcset={greek_modern} type="image/png" />
            <img src={greek_modern} alt="greek_modern" width="500px" />
        </picture>
        <button class="btn btn-ghost">Hint</button>
    </label>

    <label>
        <input type="radio" bind:group={scripts} value={3} />
        <picture>
            <source srcset={georgian} type="image/png" />
            <img src={georgian} alt="georgian" width="500px" />
        </picture>
        <button class="btn btn-ghost">Hint</button>
    </label>
</div>

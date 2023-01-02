<script>
    let scripts = 1;

    import AudioPlayer from "$lib/components/AudioPlayer.svelte";
    import idontunderstand_el from "$lib/audio/idontunderstand_el.mp3";
    let audioTrack = idontunderstand_el;

    import encoded from "$lib/audio/tmp.json";
    const audio = encoded.audio;
    const test = `data:audio/mp3;base64,${audio}`;

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

    <div class="stats shadow mt-12 mb-12">
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

    <h2 class="mt-12">Audio: listen!</h2>

    <h3 class="mt-6 text-center">From MP3 file</h3>
    <AudioPlayer src={audioTrack} />

    <h3 class="mt-6 text-center">From base64 encoding in JSON file</h3>
    <audio controls preload="none">
        <source src="{test}" type="audio/mp3">
    </audio>

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

    <h2 class="mt-12">Scripts: pick the right script!</h2>

    <label>
        <input type="radio" bind:group={scripts} value={1} />
        <picture>
            <source srcset={runes} type="image/png" />
            <img src={runes} alt="runes" width="500px" />
        </picture>
    </label>

    <label>
        <input type="radio" bind:group={scripts} value={2} />
        <picture>
            <source srcset={greek_modern} type="image/png" />
            <img src={greek_modern} alt="greek_modern" width="500px" />
        </picture>
    </label>

    <label>
        <input type="radio" bind:group={scripts} value={3} />
        <picture>
            <source srcset={georgian} type="image/png" />
            <img src={georgian} alt="georgian" width="500px" />
        </picture>
    </label>

    <div class="collapse">
        <input type="checkbox" class="peer" />
        <div
            class="collapse-title bg-base-100 text-primary-content peer-checked:bg-primary-focus peer-checked:text-primary-content rounded-t-lg mt-6 text-center"
        >
            <div class="badge badge-lg badge-secondary badge-outline">Hint</div>
        </div>
        <div
            class="collapse-content bg-primary-focus text-primary-content peer-checked:bg-primary-focus peer-checked:text-primary-content rounded-b-lg text-center"
        >
            This is what you should know about the correct script. Enlightening?
        </div>
    </div>
</div>

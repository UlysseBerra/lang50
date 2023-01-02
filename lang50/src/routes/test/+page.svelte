<script lang="ts">
    import AudioControls from "$lib/components/AudioControls.svelte";
    // import AudioPlayer, { stopAll } from "$lib/components/AudioPlayer.svelte";
    import idontunderstand_el from "$lib/audio/idontunderstand_el.mp3";
    let audioTrack = idontunderstand_el;

    // Encode/decode text string with btoa/atob
    // const encode = window.btoa("Hello world");
    // console.log("ENCODED: ", encode);
    // const decode = window.atob(encode);
    // console.log("DECODED: ", decode);

    // Import base64 ASCII from JSON
    import encoded from "$lib/audio/test_audio.json";
    const audio = encoded.audio;
    const test = `data:audio/mp3;base64,${audio}`;
    // console.log(test)
</script>

<svelte:head>
    <title>Test page</title>
    <meta name="description" content="This is a test page" />
</svelte:head>

<div class="text-column">
    <h1>Test</h1>
</div>

<div class="mb-20">
    <audio controls preload="metadata">
        <source src={test} type="audio/mp3" />
    </audio>
</div>

<div class="w-fit place-self-center mb-20">
    <AudioControls src={test} display={true} />
</div>

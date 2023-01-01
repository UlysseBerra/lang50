<script lang="ts">
    import AudioControls from "$lib/components/AudioControls.svelte";
    // import AudioPlayer, { stopAll } from "$lib/components/AudioPlayer.svelte";
    import { AudioPlayer } from "svelte-mp3";
    import idontunderstand_el from "$lib/audio/idontunderstand_el.mp3";
    let audioTrack = idontunderstand_el;

    // Encode/decode string with atob/btoa
    // let encodedStr = "SGVsbG9AV29ybGQ=";
    // let decodedStr = window.atob(encodedStr);
    // console.log(decodedStr);

    // const encode = window.btoa("CodezUp");
    // console.log("ENCODED: ", encode);
    // const decode = window.btoa(encode);
    // console.log("DECODED: ", decode);

    // Import ASCII from JSON
    // @TODO how to play it after proper decoding?
    import encoded from "$lib/audio/test_audio2.json";
    // let decoded = window.atob(audio);
    let audio = encoded.audio.content;
    // test = window.atob(audio);
    // let test = new Audio("data:audio/ogg;base64,".concat(audio));
    // console.log(audio);
    let decoded = window.btoa(audio);
    // console.log("DECODED: ", decoded);
</script>

<svelte:head>
    <title>Test page</title>
    <meta name="description" content="This is a test page" />
</svelte:head>

<div class="text-column">
    <h1>Test</h1>

    <!-- <AudioPlayer src={audioTrack} /> -->

    <!-- @TODO play audio from base64 decoded data -->
</div>

<!-- @NOTE can't get the default audio tag to work -->

<!-- AudioControls component from https://github.com/Linkcube/svelte-audio-controls -->
<div>
    <AudioControls
        src="https://sveltejs.github.io/assets/music/satie.mp3"
        display={true}
        iconColor="#D926AA"
        barPrimaryColor="#661AE6"
        barSecondaryColor="#661AE6"
    />
</div>

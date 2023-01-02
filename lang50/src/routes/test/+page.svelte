<script lang="ts">
    import AudioControls from "$lib/components/AudioControls.svelte";
    import AudioPlayer, { stopAll } from "$lib/components/AudioPlayer.svelte";
    import idontunderstand_el from "$lib/audio/idontunderstand_el.mp3";
    let audioTrack = idontunderstand_el;
    // let audioTrack = "https://sveltejs.github.io/assets/music/satie.mp3";

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
    // import encoded from "$lib/audio/test_audio2.json";
    import encoded from "$lib/audio/tmp.json";
    const audio = encoded.audio;
    // const test = new Audio(`data:audio/mp3;base64,${audio}`);
    const test = `data:audio/mp3;base64,${audio}`;
    console.log(test)
</script>

<svelte:head>
    <title>Test page</title>
    <meta name="description" content="This is a test page" />
</svelte:head>

<div class="text-column">
    <h1>Test</h1>

    <!-- <AudioPlayer src={audioTrack} /> -->

</div>

<!-- AudioControls component from https://github.com/Linkcube/svelte-audio-controls -->
<!-- <div>
    <AudioControls
        src="https://sveltejs.github.io/assets/music/satie.mp3"
        display={true}
        iconColor="#D926AA"
        barPrimaryColor="#661AE6"
        barSecondaryColor="#661AE6"
    />
</div> -->


<div><audio controls> <!-- autoplay -->
    <source src="{test}" type="audio/mp3">
    </audio></div>
<div class="divider divider-vertical m-10">OR</div>
<div><AudioControls
    src={test}
    display={true}
    iconColor="#D926AA"
    barPrimaryColor="#661AE6"
    barSecondaryColor="#661AE6"
/></div>

<div class="m-10"></div>

<div class="flex w-full">
  <div class="grid h-20 flex-grow place-items-center"><audio controls preload="none">
    <!--
        autoplay 	Makes the audio start playing automatically
        loop 	    Makes the audio start playing again when it finishes
        muted 	    Makes the player muted by default
        preload 	Instructs the browser what to preload – the whole file (auto), its metadata (metadata) or nothing at all (none)
    -->
    <source src="{test}" type="audio/mp3">
    </audio></div>
  <div class="divider divider-horizontal">OR</div>
  <div class="grid h-20 flex-grow place-items-center"><AudioControls
    src={test}
    display={true}
/></div>
</div>

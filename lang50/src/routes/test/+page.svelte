<script lang="ts">
    // --- Encoding/decoding text string with btoa/atob
    // const encode = window.btoa("Hello world");
    // console.log("ENCODED: ", encode);
    // const decode = window.atob(encode);
    // console.log("DECODED: ", decode);

    // --- Importing audio from MP3 file
    // import AudioControls from "$lib/components/AudioControls.svelte";
    // import AudioPlayer from "$lib/components/AudioPlayer.svelte";
    import idontunderstand_el from "$lib/audio/idontunderstand_el.mp3";

    // --- Importing audio from base64 encoding in JSON file
    import test_json from "$lib/audio/test_audio.json";
    const audio_test_json = test_json.audio;
    const audio_json = `data:audio/mp3;base64,${audio_test_json}`;

    // --- Importing audio from base64 encoding in API
    import { onMount } from "svelte";
    // using the endpoint for an object, not for the whole array
    const api_endpoint = "http://localhost:8080/languages/1";
    export let data_api: any = [];
    onMount(async function () {
        const response = await fetch(api_endpoint);
        data_api = await response.json();
    });
</script>

<svelte:head>
    <title>Test page</title>
    <meta name="description" content="This is a test page" />
</svelte:head>

<div class="text-column">
    <h1>Test page</h1>
</div>

<h2 class="w-fit place-self-center mt-20">Importing audio from MP3 file</h2>
<audio controls preload="metadata">
    <source src={idontunderstand_el} type="audio/mp3" />
</audio>

<h2 class="w-fit place-self-center mt-20">
    Importing audio from base64 encoding in JSON file
</h2>

<audio controls preload="metadata">
    <source src={audio_json} type="audio/mp3" />
</audio>

<h2 class="w-fit place-self-center mt-20">
    Importing audio from base64 encoding in API
</h2>

<!-- Note: no need for an #each loop when calling API ending in `/1` -->
<!-- <p>id: {data_api.id} | name: {data_api.name} | script: {data_api.script}</p> -->
<div>
    {#await data_api then d}
        <audio
            controls
            preload="metadata"
            src={`data:audio/mp3;base64,${d.audio}`}
        />
    {/await}
</div>

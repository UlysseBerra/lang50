<script context="module">
    const players = new Set();

    export function stopAll() {
        players.forEach((p) => p.pause());
    }
</script>

<script>
    import { onMount } from "svelte";

    /**
     * @type {any}
     */
    export let src;

    /**
     * @type {HTMLAudioElement}
     */
    let player;

    onMount(() => {
        // Like players.push(player)
        players.add(player);
    });
</script>

<div>
    <audio bind:this={player} {src} controls>
        <track kind="captions" />
    </audio>
</div>

<script>
    import "../app.postcss";
    import Header from "./Header.svelte";
    import "./styles.css";
    import "./styles_output.css";
    import github from "$lib/images/github.svg";
    import Navbar from "$lib/components/Navbar.svelte";

    import { onMount } from "svelte";
    import { themeChange } from "theme-change";
    onMount(() => {
        themeChange(false);
    });
</script>

<div class="app">
    <!-- <header /> -->
    <Navbar />

    <main>
        <slot />
    </main>

    <footer>
        <p>
            This is <a href="https://github.com/UlysseBerra/lang50"
                ><code>lang50</code>
            </a>
            <a href="https://github.com/UlysseBerra/lang50">
                <img
                    class="logo"
                    src={github}
                    alt="lang50 GitHub"
                    width="25px"
                /></a
            >
        </p>
    </footer>
</div>

<style>
    .app {
        display: flex;
        flex-direction: column;
        min-height: 100vh;
    }

    main {
        flex: 1;
        display: flex;
        flex-direction: column;
        padding: 1rem;
        width: 100%;
        max-width: 64rem;
        margin: 0 auto;
        box-sizing: border-box;
    }

    footer {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 12px;
    }

    footer a {
        font-weight: bold;
    }

    @media (min-width: 480px) {
        footer {
            padding: 12px 0;
        }
    }
</style>

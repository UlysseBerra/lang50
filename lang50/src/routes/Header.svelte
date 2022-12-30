<script>
    import { page } from "$app/stores";
    import tmp_logo from "$lib/images/tmp_logo.png";
</script>

<header>
    <!-- <div class="corner">
        <a href=".">
            <img src={tmp_logo} alt="lang50" />
        </a>
    </div>

    <nav>
        <ul>
            <li aria-current={$page.url.pathname === "/" ? "page" : undefined}>
                <a href="/">Home</a>
            </li>
            <li
                aria-current={$page.url.pathname === "/game"
                    ? "page"
                    : undefined}
            >
                <a href="/game">Game</a>
            </li>
            <li
                aria-current={$page.url.pathname === "/leaderboard"
                    ? "page"
                    : undefined}
            >
                <a href="/leaderboard">Leaderboard</a>
            </li>
        </ul>
    </nav> -->

    <!--
    <div class="corner">
            <a href="https://github.com/UlysseBerra/lang50">
            <img src={github} alt="lang50 GitHub" />
        </a>
    </div>
-->
</header>

<style>
    header {
        display: flex;
        justify-content: space-between;
    }

    .corner {
        width: 3em;
        height: 3em;
    }

    .corner a {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 100%;
        height: 100%;
    }

    .corner img {
        width: 2em;
        height: 2em;
        object-fit: contain;
    }

    nav {
        display: flex;
        justify-content: center;
        --background: rgba(255, 255, 255, 0.7);
    }

    /* svg {
        width: 2em;
        height: 3em;
        display: block;
    } */

    /* path {
        fill: var(--background);
    } */

    ul {
        position: relative;
        padding: 0;
        margin: 0;
        height: 3em;
        display: flex;
        justify-content: center;
        align-items: center;
        list-style: none;
        background: var(--background);
        background-size: contain;
    }

    li {
        position: relative;
        height: 100%;
    }

    li[aria-current="page"]::before {
        --size: 6px;
        content: "";
        width: 0;
        height: 0;
        position: absolute;
        top: 0;
        left: calc(50% - var(--size));
        border: var(--size) solid transparent;
        border-top: var(--size) solid var(--color-theme-1);
    }

    nav a {
        display: flex;
        height: 100%;
        align-items: center;
        padding: 0 0.5rem;
        color: var(--color-text);
        font-weight: 700;
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        text-decoration: none;
        transition: color 0.2s linear;
    }

    a:hover {
        color: var(--color-theme-1);
    }
</style>

<script>
    import ThemeSelect from "./Theme-select.svelte";
</script>

<div class="navbar bg-primary text-primary-content">
    <div class="navbar-start">
        <a class="btn btn-ghost normal-case text-xl" href="."
            ><code>lang50</code></a
        >
    </div>
    <div class="navbar-center">
        <ul class="menu menu-horizontal px-1">
            <li><a href="/game">Game</a></li>
            <li><a href="/leaderboard">Leaderboard</a></li>
        </ul>
    </div>
    <div class="navbar-end">
        <ul class="menu menu-horizontal px-1">
            <li>
                <a class="menu menu-horizontal px-1" href="/authentication"
                    >Log in & Sign up</a
                >
            </li>
            <li><ThemeSelect /></li>
        </ul>
    </div>
</div>

<script>
    import ThemeSelect from "./Theme-select.svelte";
</script>

<div class="navbar bg-primary text-primary-content">
    <div class="navbar-start">
        <a class="btn btn-ghost normal-case text-xl" href=".">lang50</a>
    </div>
    <div class="navbar-center">
        <ul class="menu menu-horizontal px-1">
            <li><a href="/game">Game</a></li>
            <li><a href="/leaderboard">Leaderboard</a></li>
            <li>
                <a class="menu menu-horizontal px-1" href="/sign">Sign in</a>
            </li>
        </ul>
    </div>
    <div class="navbar-end">
        <ThemeSelect />
    </div>
</div>

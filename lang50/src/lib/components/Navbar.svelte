<script>
    // import ThemeSelect from "./Theme-select.svelte";
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
                    >Login</a
                >
            </li>
            <!-- <li><ThemeSelect /></li> -->
        </ul>

        <label class="swap">
            <input type="checkbox" />
            <div class="swap-on avatar online placeholder">
                <div
                    class="bg-neutral-focus text-neutral-content rounded-full w-11"
                >
                    Me
                </div>
            </div>
            <div class="swap-off avatar placeholder">
                <div
                    class="bg-neutral-focus text-neutral-content rounded-full w-11"
                >
                    Who?
                </div>
            </div>
        </label>
    </div>
</div>

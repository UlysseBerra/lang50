<script>
    const url = "https://jsonplaceholder.typicode.com/users";
    const fetchUsers = (async () => {
        const response = await fetch(url);
        let users = await response.json();
        return users;
    })();
</script>

<svelte:head>
    <title>Leaderboard</title>
    <meta name="description" content="Leaderboard" />
</svelte:head>

<div class="text-column">
    <h1>Leaderboard</h1>
</div>

{#await fetchUsers}
    <p>...waiting</p>
{:then users}
    <div class="overflow-x-auto">
        <table class="table table-compact w-full">
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Username</th>
                    <th>Email</th>
                </tr>
            </thead>
            <tbody>
                {#each users as user}
                    <tr>
                        <td>{user.name}</td>
                        <td>{user.username}</td>
                        <td>{user.email}</td>
                    </tr>
                {/each}
            </tbody>
        </table>
    </div>
{:catch error}
    <p>An error occurred!</p>
{/await}

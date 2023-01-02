<script>
    import lang50_logo from "$lib/images/lang50_logo.png";
</script>

<svelte:head>
    <title>Home</title>
    <meta name="description" content="lang50 app" />
</svelte:head>

<section>
    <h1>
        <span class="lang50_logo">
            <picture>
                <source srcset={lang50_logo} type="image/png" />
                <img src={lang50_logo} width="250px" alt="Welcome to lang50" />
            </picture>
        </span>
    </h1>

    <p class="text-center">
        The <code>lang50</code> project is a joint venture of Ulysse Berra and Aurélien
        Berra.
    </p>
    <p class="text-center">
        It serves as our Harvard CS50x final project, and modestly aims at
        changing the world – one nerdy game at a time.
    </p>
</section>

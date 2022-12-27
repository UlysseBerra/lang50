<script>
    // import Counter from "./Counter.svelte";
    import tmp_logo from "$lib/images/tmp_logo.png";
</script>

<svelte:head>
    <title>Home</title>
    <meta name="description" content="lang50 app" />
</svelte:head>

<section>
    <h1>
        <span class="tmp_logo">
            <picture>
                <source srcset={tmp_logo} type="image/png" />
                <img src={tmp_logo} width="300px" alt="Welcome to lang50" />
            </picture>
        </span>
    </h1>

    <!-- <Counter /> -->
</section>

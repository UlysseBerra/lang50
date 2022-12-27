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
                <img src={tmp_logo} width="250px" alt="Welcome to lang50" />
            </picture>
        </span>
    </h1>

    <p>
        You know what <code>lang50</code> is, right? Well, if you don't, here is
        a blurb: lorem ipsum tralala lorem ipsum tralala lorem ipsum tralala lorem
        ipsum tralala lorem ipsum tralala lorem ipsum tralala lorem ipsum tralala
        lorem ipsum tralala lorem ipsum tralala lorem ipsum tralala lorem ipsum tralala
        lorem ipsum tralala.
    </p>

    <!-- <Counter /> -->
</section>

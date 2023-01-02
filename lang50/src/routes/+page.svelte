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

    <div>
        <p class="mt-20 mb-10">
            The <strong><code>lang50</code></strong> project is a joint venture
            of
            <strong>Ulysse Berra</strong>
            and <strong>Aurélien Berra</strong>. It serves as our
            <a
                href="https://www.edx.org/course/introduction-computer-science-harvardx-cs50x"
                >Harvard CS50x</a
            >
            final project, and modestly aims at changing the world – one nerdy game
            at a time. We use the following technologies: design and wireframing
            with
            <a href="https://www.figma.com/">Figma </a>; back-end in
            <a href="https://www.java.com/">Java</a> with
            <a href="https://spring.io/">Spring Boot</a>
            and <a href="http://h2database.com/">H2 database</a>; front-end with
            <a href="https://svelte.dev/">Svelte</a> and
            <a href="https://kit.svelte.dev/">SvelteKit</a>,
            <a href="https://www.typescriptlang.org/">TypeScript</a>,
            <a href="https://tailwindcss.com/">Tailwind</a> and
            <a href="https://daisyui.com/">daisyUI</a>
            .
        </p>
    </div>
</section>

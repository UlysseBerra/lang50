<script lang="ts">
    let scripts = 1;

    // Get scripts from API
    import { onMount } from "svelte";
    const api_endpoint = "http://0.0.0.0:8000/language/";
    export let data_api_1: any = [];
    export let data_api_2: any = [];
    export let data_api_3: any = [];
    export let data_api_4: any = [];
    onMount(async function () {
        const response_1 = await fetch(api_endpoint);
        const response_2 = await fetch(api_endpoint);
        const response_3 = await fetch(api_endpoint);
        const response_4 = await fetch(api_endpoint);
        data_api_1 = await response_1.json();
        data_api_2 = await response_2.json();
        data_api_3 = await response_3.json();
        data_api_4 = await response_4.json();

        const radioLabels = document.querySelectorAll(".form-radio");
        const selectedScriptSpan = document.getElementById("selectedValue")!;
        // const validScriptId = ["1"];
        const resultStorage = document.getElementById("resultStorage")!;
        const counterDisplay = document.getElementById("counterDisplay")!;

        let selectedValue = "";
        let selectionCounter = 0;

        radioLabels.forEach((radio) => {
            radio.addEventListener("change", () => {
                if (radio.checked) {
                    const inputValue = radio.value;
                    console.log("Input Value:", inputValue);
                    console.log("rightNum:", rightNum);
                    if (parseInt(inputValue) === rightNum) {
                        selectedValue = inputValue;
                        selectedScriptSpan.textContent = "Right!";
                        selectedScriptSpan.style.color = "green";
                        resultStorage.textContent = `Stored Value: ${selectedValue}`;
                        selectionCounter++;
                        counterDisplay.textContent = `Selections: ${selectionCounter}`;
                    } else {
                        selectedValue = "";
                        selectedScriptSpan.textContent = "Wrong!";
                        selectedScriptSpan.style.color = "red";
                        resultStorage.textContent = "";
                        counterDisplay.textContent = `Selections: ${selectionCounter}`;
                    }
                }
            });
        });
    });

    // Define right script
    function randomNumber(min: number, max: number) {
        return Math.floor(Math.random() * (max - min) + min);
    }
    export let rightNum: number = randomNumber(1, 4);
    console.log(rightNum);
    console.log(typeof rightNum);

    // Get local audio
    import udhr_001 from "$lib/udhr_audio/001.mp3";

    import runes from "$lib/images/runes.png";
    import greek_modern from "$lib/images/greek_modern.png";
    import georgian from "$lib/images/georgian.png";
</script>

<svelte:head>
    <title>Game</title>
    <meta name="description" content="This is the game" />
</svelte:head>

<div class="text-column">
    <h1>Game</h1>

    <div class="stats shadow mt-12 mb-12">
        <div class="stat place-items-center">
            <div class="stat-title">Round</div>
            <div class="stat-value">1</div>
        </div>

        <div class="stat place-items-center">
            <div class="stat-title">Score</div>
            <div class="stat-value">0</div>
        </div>

        <div class="stat place-items-center">
            <div class="stat-title">Lives</div>
            <div class="stat-value">3</div>
        </div>
    </div>

    <h2 class="w-fit place-self-center mt-20">Audio: listen!</h2>

    <audio controls preload="metadata">
        <source src={udhr_001} type="audio/mp3" />
    </audio>

    <!-- <div>
        {#await data_api then d}
            <audio
                controls
                preload="metadata"
                src={`data:audio/mp3;base64,${d.audio}`}
            />
        {/await}
    </div>
 -->

    <h2 class="w-fit place-self-center mt-20">
        Scripts: pick the right script!
    </h2>

    <!--
        {d.lang_text}
        {d.lang_id}
        {d.lang_name}
        {d.lang_family} -->

    <label>
        <input type="radio" class="form-radio" bind:group={scripts} value="1" />
        {#await data_api_1 then d}
            {d.lang_text}
        {/await}
    </label>
    <label>
        <input type="radio" class="form-radio" bind:group={scripts} value="2" />
        {#await data_api_2 then d}
            {d.lang_text}
        {/await}
    </label>
    <label>
        <input type="radio" class="form-radio" bind:group={scripts} value="3" />
        {#await data_api_3 then d}
            {d.lang_text}
        {/await}
    </label>
    <label>
        <input type="radio" class="form-radio" bind:group={scripts} value="4" />
        {#await data_api_4 then d}
            {d.lang_text}
        {/await}
    </label>

    <p class="w-fit place-self-center mt-20">
        The selected answer is… <span id="selectedValue" />
    </p>
    <p class="w-fit place-self-center mt-20">
        Current storage: <span id="resultStorage" />
    </p>
    <p class="w-fit place-self-center mt-20">
        And the current score is: <span id="counterDisplay" />
    </p>

    <div class="collapse">
        <input type="checkbox" class="peer" />
        <div
            class="collapse-title bg-base-100 text-primary-content peer-checked:bg-primary-focus peer-checked:text-primary-content rounded-t-lg mt-6 text-center"
        >
            <div class="badge badge-lg badge-secondary badge-outline">Hint</div>
        </div>
        <div
            class="collapse-content bg-primary-focus text-primary-content peer-checked:bg-primary-focus peer-checked:text-primary-content rounded-b-lg text-center"
        >
            This is what you should know about the correct script. Enlightening?
        </div>
    </div>

    <script>
        // const radioLabels = document.querySelectorAll(".form-radio");
        // const selectedScriptSpan = document.getElementById("selectedValue");
        // // const validScriptId = ["1"];
        // const resultStorage = document.getElementById("resultStorage");
        // const counterDisplay = document.getElementById("counterDisplay");

        // let selectedValue = "";
        // let selectionCounter = 0;

        // radioLabels.forEach((radio) => {
        //     radio.addEventListener("change", () => {
        //         if (radio.checked) {
        //             const inputValue = radio.value;
        //             console.log("Input Value:", inputValue);
        //             console.log("rightNum:", rightNum);
        //             if (parseInt(inputValue) === rightNum) {
        //                 selectedValue = inputValue;
        //                 selectedScriptSpan.textContent = "Right!";
        //                 selectedScriptSpan.style.color = "green";
        //                 resultStorage.textContent = `Stored Value: ${selectedValue}`;
        //                 selectionCounter++;
        //                 counterDisplay.textContent = `Selections: ${selectionCounter}`;
        //             } else {
        //                 selectedValue = "";
        //                 selectedScriptSpan.textContent = "Wrong!";
        //                 selectedScriptSpan.style.color = "red";
        //                 resultStorage.textContent = "";
        //                 counterDisplay.textContent = `Selections: ${selectionCounter}`;
        //             }
        //         }
        //     });
        // });
    </script>
</div>

<script lang="ts">
    let scripts = 1;

    // Test from local JSON
    const fetchTestData_local = (async () => {
        const response = await fetch("src/lib/test_data_local.json");
        let test_data_local_raw = await response.json();
        let test_data_local_str: string =
            "[" + JSON.stringify(test_data_local_raw) + "]";
        let test_data_local = JSON.parse(test_data_local_str);
        console.log("test_data_local", test_data_local);
        return test_data_local;
    })();

    // Test from API
    import { onMount } from "svelte";
    const api_endpoint = "http://0.0.0.0:8000/language/";
    export let data_api_1: any = [];
    export let data_api_2: any = [];
    export let data_api_3: any = [];
    export let data_api_4: any = [];
    export let data_test: any = [];

    onMount(async function () {
        const response_1 = await fetch(api_endpoint);
        const response_2 = await fetch(api_endpoint);
        const response_3 = await fetch(api_endpoint);
        const response_4 = await fetch(api_endpoint);
        data_api_1 = await response_1.json();
        data_api_2 = await response_2.json();
        data_api_3 = await response_3.json();
        data_api_4 = await response_4.json();

        const response_test = await fetch(api_endpoint);
        data_test = await response_test.json();
        // Add square brackets to make JSON from API valid
        let data_test_str = "[" + JSON.stringify(data_test) + "]";
        data_test = JSON.parse(data_test_str);
    });

    // Preprocess audio imports and create the audioMap
    // let audioMap = {};

    // onMount(async function () {
    //     for (const data of [data_api_1, data_api_2, data_api_3, data_api_4]) {
    //         if (data && data.lang_id) {
    //             const langId = data.lang_id;
    //             const audioModule = await import(
    //                 `$lib/udhr_audio/${langId}.mp3`
    //             );
    //             if (
    //                 audioModule.default &&
    //                 Object.values(audioModule.default).length > 0
    //             ) {
    //                 audioMap[langId] = Object.values(audioModule.default);
    //             }
    //         }
    //     }
    // });
</script>

<svelte:head>
    <title>Test</title>
    <meta name="description" content="This is a test page" />
</svelte:head>

<div class="text-column">
    <h1>Test from local JSON</h1>

    {#await fetchTestData_local}
        <p>...waiting</p>
    {:then test_data_local}
        <div class="overflow-x-auto">
            <table class="table table-compact w-full">
                <thead>
                    <tr>
                        <th>lang_id</th>
                        <th>lang_name</th>
                        <th>lang_family</th>
                        <th>lang_text</th>
                    </tr>
                </thead>
                <tbody>
                    {#each test_data_local as d}
                        <tr>
                            <td>{d.lang_id}</td>
                            <td>{d.lang_name}</td>
                            <td>{d.lang_family}</td>
                            <td>{d.lang_text}</td>
                        </tr>
                    {/each}
                </tbody>
            </table>
        </div>
    {:catch error}
        <p>An error occurred!</p>
    {/await}
</div>

<div class="text-column">
    <h1>Test from API</h1>

    <div class="overflow-x-auto">
        <table class="table table-compact w-full">
            <thead>
                <tr>
                    <th>lang_id</th>
                    <th>lang_name</th>
                    <th>lang_family</th>
                    <th>lang_text</th>
                </tr>
            </thead>
            <tbody>
                {#each data_test as dt}
                    <tr>
                        <td>{dt.lang_id}</td>
                        <td>{dt.lang_name}</td>
                        <td>{dt.lang_family}</td>
                        <td>{dt.lang_text}</td>
                    </tr>
                {/each}
            </tbody>
        </table>
    </div>
</div>

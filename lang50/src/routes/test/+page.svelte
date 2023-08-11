<script lang="ts">
    let scripts = 1;
    // --- Encoding/decoding text string with btoa/atob
    // const encode = window.btoa("Hello world");
    // console.log("ENCODED: ", encode);
    // const decode = window.atob(encode);
    // console.log("DECODED: ", decode);

    // --- Importing audio from MP3 file
    // import AudioControls from "$lib/components/AudioControls.svelte";
    // import AudioPlayer from "$lib/components/AudioPlayer.svelte";
    import udhr_001 from "$lib/udhr_audio/001.mp3";
    import udhr_002 from "$lib/udhr_audio/002.mp3";
    import udhr_003 from "$lib/udhr_audio/003.mp3";
    import udhr_004 from "$lib/udhr_audio/004.mp3";
    import udhr_005 from "$lib/udhr_audio/005.mp3";
    import udhr_006 from "$lib/udhr_audio/006.mp3";
    import udhr_007 from "$lib/udhr_audio/007.mp3";
    import udhr_008 from "$lib/udhr_audio/008.mp3";
    import udhr_009 from "$lib/udhr_audio/009.mp3";
    import udhr_010 from "$lib/udhr_audio/010.mp3";
    import udhr_011 from "$lib/udhr_audio/011.mp3";
    import udhr_012 from "$lib/udhr_audio/012.mp3";
    import udhr_013 from "$lib/udhr_audio/013.mp3";
    import udhr_014 from "$lib/udhr_audio/014.mp3";
    import udhr_015 from "$lib/udhr_audio/015.mp3";
    import udhr_016 from "$lib/udhr_audio/016.mp3";
    import udhr_017 from "$lib/udhr_audio/017.mp3";
    import udhr_018 from "$lib/udhr_audio/018.mp3";
    import udhr_019 from "$lib/udhr_audio/019.mp3";
    import udhr_020 from "$lib/udhr_audio/020.mp3";
    import udhr_021 from "$lib/udhr_audio/021.mp3";
    import udhr_022 from "$lib/udhr_audio/022.mp3";
    import udhr_023 from "$lib/udhr_audio/023.mp3";
    import udhr_024 from "$lib/udhr_audio/024.mp3";
    import udhr_025 from "$lib/udhr_audio/025.mp3";
    import udhr_026 from "$lib/udhr_audio/026.mp3";
    import udhr_027 from "$lib/udhr_audio/027.mp3";
    import udhr_028 from "$lib/udhr_audio/028.mp3";
    import udhr_029 from "$lib/udhr_audio/029.mp3";
    import udhr_030 from "$lib/udhr_audio/030.mp3";
    import udhr_031 from "$lib/udhr_audio/031.mp3";
    import udhr_032 from "$lib/udhr_audio/032.mp3";
    import udhr_033 from "$lib/udhr_audio/033.mp3";
    import udhr_034 from "$lib/udhr_audio/034.mp3";
    import udhr_035 from "$lib/udhr_audio/035.mp3";
    import udhr_036 from "$lib/udhr_audio/036.mp3";
    import udhr_037 from "$lib/udhr_audio/037.mp3";
    import udhr_038 from "$lib/udhr_audio/038.mp3";
    import udhr_039 from "$lib/udhr_audio/039.mp3";
    import udhr_040 from "$lib/udhr_audio/040.mp3";
    import udhr_041 from "$lib/udhr_audio/041.mp3";
    import udhr_042 from "$lib/udhr_audio/042.mp3";
    import udhr_043 from "$lib/udhr_audio/043.mp3";
    import udhr_044 from "$lib/udhr_audio/044.mp3";
    import udhr_045 from "$lib/udhr_audio/045.mp3";
    import udhr_046 from "$lib/udhr_audio/046.mp3";
    import udhr_047 from "$lib/udhr_audio/047.mp3";
    import udhr_048 from "$lib/udhr_audio/048.mp3";
    import udhr_049 from "$lib/udhr_audio/049.mp3";
    import udhr_050 from "$lib/udhr_audio/050.mp3";
    import udhr_051 from "$lib/udhr_audio/051.mp3";
    import udhr_052 from "$lib/udhr_audio/052.mp3";
    import udhr_053 from "$lib/udhr_audio/053.mp3";
    import udhr_054 from "$lib/udhr_audio/054.mp3";
    import udhr_055 from "$lib/udhr_audio/055.mp3";
    import udhr_056 from "$lib/udhr_audio/056.mp3";
    import udhr_057 from "$lib/udhr_audio/057.mp3";
    import udhr_058 from "$lib/udhr_audio/058.mp3";
    import udhr_059 from "$lib/udhr_audio/059.mp3";
    import udhr_060 from "$lib/udhr_audio/060.mp3";
    import udhr_061 from "$lib/udhr_audio/061.mp3";
    import udhr_062 from "$lib/udhr_audio/062.mp3";
    import udhr_063 from "$lib/udhr_audio/063.mp3";
    import udhr_064 from "$lib/udhr_audio/064.mp3";
    import udhr_065 from "$lib/udhr_audio/065.mp3";
    import udhr_066 from "$lib/udhr_audio/066.mp3";
    import udhr_067 from "$lib/udhr_audio/067.mp3";
    import udhr_068 from "$lib/udhr_audio/068.mp3";
    import udhr_069 from "$lib/udhr_audio/069.mp3";
    import udhr_070 from "$lib/udhr_audio/070.mp3";
    import udhr_071 from "$lib/udhr_audio/071.mp3";
    import udhr_072 from "$lib/udhr_audio/072.mp3";
    import udhr_073 from "$lib/udhr_audio/073.mp3";
    import udhr_074 from "$lib/udhr_audio/074.mp3";
    import udhr_075 from "$lib/udhr_audio/075.mp3";
    import udhr_076 from "$lib/udhr_audio/076.mp3";
    import udhr_077 from "$lib/udhr_audio/077.mp3";
    import udhr_078 from "$lib/udhr_audio/078.mp3";
    import udhr_079 from "$lib/udhr_audio/079.mp3";
    import udhr_080 from "$lib/udhr_audio/080.mp3";
    import udhr_081 from "$lib/udhr_audio/081.mp3";
    import udhr_082 from "$lib/udhr_audio/082.mp3";
    import udhr_083 from "$lib/udhr_audio/083.mp3";
    import udhr_084 from "$lib/udhr_audio/084.mp3";
    import udhr_085 from "$lib/udhr_audio/085.mp3";
    import udhr_086 from "$lib/udhr_audio/086.mp3";
    import udhr_087 from "$lib/udhr_audio/087.mp3";
    import udhr_088 from "$lib/udhr_audio/088.mp3";
    import udhr_089 from "$lib/udhr_audio/089.mp3";
    import udhr_090 from "$lib/udhr_audio/090.mp3";
    import udhr_091 from "$lib/udhr_audio/091.mp3";
    import udhr_092 from "$lib/udhr_audio/092.mp3";
    import udhr_093 from "$lib/udhr_audio/093.mp3";
    import udhr_094 from "$lib/udhr_audio/094.mp3";
    import udhr_095 from "$lib/udhr_audio/095.mp3";
    import udhr_096 from "$lib/udhr_audio/096.mp3";
    import udhr_097 from "$lib/udhr_audio/097.mp3";
    import udhr_098 from "$lib/udhr_audio/098.mp3";
    import udhr_099 from "$lib/udhr_audio/099.mp3";
    import udhr_100 from "$lib/udhr_audio/100.mp3";
    import udhr_101 from "$lib/udhr_audio/101.mp3";
    import udhr_102 from "$lib/udhr_audio/102.mp3";
    import udhr_103 from "$lib/udhr_audio/103.mp3";
    import udhr_104 from "$lib/udhr_audio/104.mp3";
    import udhr_105 from "$lib/udhr_audio/105.mp3";
    import udhr_106 from "$lib/udhr_audio/106.mp3";
    import udhr_107 from "$lib/udhr_audio/107.mp3";
    import udhr_108 from "$lib/udhr_audio/108.mp3";
    import udhr_109 from "$lib/udhr_audio/109.mp3";
    import udhr_110 from "$lib/udhr_audio/110.mp3";
    import udhr_111 from "$lib/udhr_audio/111.mp3";
    import udhr_112 from "$lib/udhr_audio/112.mp3";
    import udhr_113 from "$lib/udhr_audio/113.mp3";
    import udhr_114 from "$lib/udhr_audio/114.mp3";
    import udhr_115 from "$lib/udhr_audio/115.mp3";
    import udhr_116 from "$lib/udhr_audio/116.mp3";
    import udhr_117 from "$lib/udhr_audio/117.mp3";
    import udhr_118 from "$lib/udhr_audio/118.mp3";
    import udhr_119 from "$lib/udhr_audio/119.mp3";
    import udhr_120 from "$lib/udhr_audio/120.mp3";
    import udhr_121 from "$lib/udhr_audio/121.mp3";
    import udhr_122 from "$lib/udhr_audio/122.mp3";
    import udhr_123 from "$lib/udhr_audio/123.mp3";
    import udhr_124 from "$lib/udhr_audio/124.mp3";
    import udhr_125 from "$lib/udhr_audio/125.mp3";
    import udhr_126 from "$lib/udhr_audio/126.mp3";
    import udhr_127 from "$lib/udhr_audio/127.mp3";
    import udhr_128 from "$lib/udhr_audio/128.mp3";
    import udhr_129 from "$lib/udhr_audio/129.mp3";
    import udhr_130 from "$lib/udhr_audio/130.mp3";
    import udhr_131 from "$lib/udhr_audio/131.mp3";
    import udhr_132 from "$lib/udhr_audio/132.mp3";
    import udhr_133 from "$lib/udhr_audio/133.mp3";
    import udhr_134 from "$lib/udhr_audio/134.mp3";
    import udhr_135 from "$lib/udhr_audio/135.mp3";
    import udhr_136 from "$lib/udhr_audio/136.mp3";
    import udhr_137 from "$lib/udhr_audio/137.mp3";
    import udhr_138 from "$lib/udhr_audio/138.mp3";
    import udhr_139 from "$lib/udhr_audio/139.mp3";
    import udhr_140 from "$lib/udhr_audio/140.mp3";
    import udhr_141 from "$lib/udhr_audio/141.mp3";
    import udhr_142 from "$lib/udhr_audio/142.mp3";
    import udhr_143 from "$lib/udhr_audio/143.mp3";
    import udhr_144 from "$lib/udhr_audio/144.mp3";
    import udhr_145 from "$lib/udhr_audio/145.mp3";
    import udhr_146 from "$lib/udhr_audio/146.mp3";
    import udhr_147 from "$lib/udhr_audio/147.mp3";
    import udhr_148 from "$lib/udhr_audio/148.mp3";
    import udhr_149 from "$lib/udhr_audio/149.mp3";
    import udhr_150 from "$lib/udhr_audio/150.mp3";
    import udhr_151 from "$lib/udhr_audio/151.mp3";
    import udhr_152 from "$lib/udhr_audio/152.mp3";
    import udhr_153 from "$lib/udhr_audio/153.mp3";
    import udhr_154 from "$lib/udhr_audio/154.mp3";
    import udhr_155 from "$lib/udhr_audio/155.mp3";
    import udhr_156 from "$lib/udhr_audio/156.mp3";

    // --- Importing audio from base64 encoding in JSON file
    // import test_json from "$lib/audio/test_audio.json";
    // const audio_test_json = test_json.audio;
    // const audio_json = `data:audio/mp3;base64,${audio_test_json}`;

    // --- Importing audio from base64 encoding in API
    // import { onMount } from "svelte";
    // // using the endpoint for an object, not for the whole array
    // const api_endpoint = "http://localhost:8080/languages/1";
    // export let data_api: any = [];
    // onMount(async function () {
    //     const response = await fetch(api_endpoint);
    //     data_api = await response.json();
    // });
</script>

<svelte:head>
    <title>Test page</title>
    <meta name="description" content="This is a test page" />
</svelte:head>

<div class="text-column">
    <h1>Test page</h1>
</div>

<h2 class="w-fit place-self-center mt-20">Audio: first, listen!</h2>
<audio controls preload="metadata">
    <source src={udhr_001} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_002} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_003} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_004} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_005} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_006} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_007} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_008} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_009} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_010} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_011} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_012} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_013} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_014} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_015} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_016} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_017} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_018} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_019} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_020} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_021} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_022} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_023} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_024} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_025} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_026} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_027} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_028} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_029} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_030} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_031} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_032} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_033} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_034} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_035} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_036} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_037} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_038} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_039} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_040} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_041} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_042} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_043} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_044} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_045} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_046} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_047} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_048} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_049} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_050} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_051} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_052} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_053} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_054} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_055} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_056} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_057} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_058} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_059} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_060} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_061} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_062} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_063} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_064} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_065} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_066} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_067} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_068} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_069} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_070} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_071} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_072} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_073} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_074} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_075} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_076} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_077} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_078} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_079} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_080} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_081} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_082} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_083} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_084} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_085} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_086} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_087} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_088} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_089} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_090} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_091} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_092} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_093} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_094} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_095} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_096} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_097} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_098} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_099} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_100} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_101} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_102} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_103} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_104} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_105} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_106} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_107} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_108} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_109} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_110} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_111} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_112} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_113} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_114} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_115} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_116} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_117} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_118} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_119} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_120} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_121} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_122} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_123} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_124} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_125} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_126} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_127} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_128} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_129} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_130} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_131} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_132} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_133} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_134} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_135} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_136} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_137} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_138} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_139} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_140} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_141} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_142} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_143} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_144} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_145} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_146} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_147} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_148} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_149} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_150} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_151} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_152} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_153} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_154} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_155} type="audio/mp3" />
</audio>
<audio controls preload="metadata">
    <source src={udhr_156} type="audio/mp3" />
</audio>

<h2 class="w-fit place-self-center mt-20">
    Scripts: next, pick the right script!
</h2>

<label>
    <input type="radio" bind:group={scripts} value={1} />
    የሰው፡ልጅ፡ሁሉ፡ሲወለድ፡ነጻና፡በክብርና፡በመብትም፡እኩልነት፡ያለው፡ነው።፡የተፈጥሮ፡ማስተዋልና፡ሕሊና፡ስላለው፡አንዱ፡ሌላውን፡በወንድማማችነት፡መንፈስ፡መመልከት፡ይገባዋል።
</label>

<label>
    <input type="radio" bind:group={scripts} value={2} />
    jinweldun kil'in'nas xürrien u mitsöwjin f'il kärame w'il xgyugy, mügdejien b'il
    ghägyülh w'id'dyemier u lözim gheleigüm jighamlun bäghädygüm bäghädy keqengüm
    ixhwan.
</label>

<label>
    <input type="radio" bind:group={scripts} value={3} />
    الإعلان العالمي لحقوق الإنسان، المادة الأولانية البني أدمين كلهم مولودين حرين
    ومتساويين في الكرامة والحقوق. إتوهبلهم العقل والضمير، والمفروض يعاملوا بعض بروح
    الأخوية.
</label>

<label>
    <input type="radio" bind:group={scripts} value={4} />
    كلوا نفر في ولادة حر وسمسم في كرامة وسمسم في حقوق. الله في إعطى هو عقل وضمير،
    ولازم هو سوي مع تاني نفر سمسم أخ
</label>

<label>
    <input type="radio" bind:group={scripts} value={5} />
    Kill el ba¡ar byechlaqò aħrár w mütasévyín bil carámet w'el ħoqúq. W hinné nwahabò
    xaqel w đamír, w xleyun y'xémlò baxdon el baxed b'rúħ el ochuẅet.
</label>

<label>
    <input type="radio" bind:group={scripts} value={6} />
    يولد جميع الناس أحراراً متساوين في الكرامة والحقوق. وقد وهبوا عقلاً وضميراً وعليهم
    ان يعامل بعضهم بعضاً بروح اﻹخاء.
</label>

<label>
    <input type="radio" bind:group={scripts} value={7} />
    In-nès il-kull muludìn ħurrìn w mitsèwìn fi’l-karàme w’il-ħuqùq. Tagħŧàw għqal
    w żamìr w lèzim ygħàmlu bgħażhum kìf l-axwa.
</label>

<label>
    <input type="radio" bind:group={scripts} value={8} />
    Yàlidïn ìnon čol-ènašëya čwaþ χeḁrrëya we šàwyëya va ǧurča we va zìdqëya. Bìyìzvədun
    yal χuešaba we yal þeḁrþa, we koyìsˀərun χàd ləwaþ χàd va ruχa di àχuþa.
</label>

<label>
    <input type="radio" bind:group={scripts} value={9} />
    כֹּל בְּנֵי הָאָדָם נוֹלְדוּ בְּנֵי חוֹרִין וְשָׁוִים בְּעֶרְכָּם וּבִזְכֻיּוֹתֵיהֶם.
    כֻּלָּם חוֹנְנוּ בַּתְּבוּנָה וּבְמַצְפּוּן, לְפִיכָךְ חוֹבָה עֲלֵיהֶם לִנְהֹוג
    אִישׁ בְּרֵעֵהוּ בְּרוּחַ שֶׁל אַחֲוָה.
</label>

<label>
    <input type="radio" bind:group={scripts} value={10} />
    Il-bnedmin kollha jitwieldu ħielsa u ugwali fid-dinjità u d-drittijiet. Huma
    mogħnija bir-raġuni u bil-kuxjenza u għandhom inġibu ruħhom ma' xulxin bi spirtu
    ta' aħwa.
</label>

<label>
    <input type="radio" bind:group={scripts} value={11} />
    Aadanaha dhammaantiis wuxuu dhashaa isagoo xor ah kana siman xagga sharafta iyo
    xuquuqada. Waxaa Alle siiyay aqoon iyo wacyi, waana in qof la arkaa qofka kale
    ula dhaqmaa si walaaltinimo ah. | 𐒛𐒆𐒖𐒒𐒖𐒔𐒖 𐒊𐒖𐒑𐒑𐒛𐒒𐒂𐒕𐒈 𐒓𐒚𐒄𐒓 𐒊𐒖𐒉𐒛 𐒘𐒈𐒖𐒌𐒝 𐒄𐒙𐒇 𐒖𐒔 𐒏𐒖𐒒𐒖
    𐒈𐒘𐒑𐒖𐒒 𐒄𐒖𐒌𐒌𐒖 𐒉𐒖𐒇𐒖𐒍𐒂𐒖 𐒘𐒕𐒙 𐒄𐒚𐒎𐒓𐒎𐒖𐒆𐒖 𐒓𐒖𐒄𐒛 𐒖𐒐𐒐𐒗 𐒈𐒕𐒕𐒖𐒕 𐒖𐒎𐒝𐒒 𐒘𐒕𐒙 𐒓𐒖𐒋𐒕𐒘, 𐒓𐒛𐒒𐒖 𐒘𐒒 𐒎𐒙𐒍
    𐒐𐒖 𐒖𐒇𐒏𐒛 𐒎𐒙𐒍𐒏𐒖 𐒏𐒖𐒐𐒗 𐒚𐒐𐒖 𐒊𐒖𐒎𐒑𐒛 𐒈𐒘 𐒓𐒖𐒐𐒛𐒐𐒂𐒘𐒒𐒘𐒑𐒙 𐒖𐒔
</label>

<label>
    <input type="radio" bind:group={scripts} value={12} />
    ብመንፅር ክብርን መሰልን ኩሎም ሰባት እንትውለጹ ነፃን ማዕረን እዮም። ምስትውዓልን ሕልናን ዝተዓደሎም ብምዃኖም ብሕውነታዊ
    መንፈስ ክተሓላዩ ኣለዎም።
</label>

<label>
    <input type="radio" bind:group={scripts} value={13} />
    畢哿每𠊛生𠚢調得自由吧平等𧗱人品吧 權。每𡥵𠊛調得造化頒朱理智吧良心吧勤沛對處𢭲膮𥪝情朋友。
</label>

<label>
    <input type="radio" bind:group={scripts} value={14} />
    Bandum ureuëng lahé deungon meurdéhka, dan deungon martabat dan hak njang saban.
    Ngon akai geuseumiké, ngon haté geumeurasa, bandum geutanjoë lagèë sjèëdara.
    Hak dan keumuliaan.
</label>

<label>
    <input type="radio" bind:group={scripts} value={15} />
    ᬫᬓᬲᬫᬶᬫᬦᬸᬲᬦᬾᬓᬳᭂᬫ᭄ᬩᬲᬶᬦ᭄ᬫᬳᬃᬤᬶᬓᬮᬦ᭄ᬧᬢᬾ᭪᭟ ​ᬲᬚᬦᬶᬂᬓᬳᬦᬦ᭄ᬮᬦ᭄ᬓᬸᬲ᭟ ᬳᬶᬧᬸᬦ᭄ᬓᬦᬸᬕ᭄ᬭᬳᬶᬦᬶᬯᬾᬓᬮᬦ᭄ᬩᬸᬤ᭄ᬥᬶ᭟
    ​ᬧᬦ᭄ᬢᬭᬦᬶᬂᬫᬦᬸᬲᬫᬂᬤᬦᬾ​ ​ᬧᬭᬲ᭄ᬧᬭᭀᬲ᭄ᬫᬲᬫᬾᬢᭀᬦᬦ᭄
</label>

<label>
    <input type="radio" bind:group={scripts} value={16} />
    An gabos na tawo ipinangaking may katalinkasan asin parantay sa dignidad asin
    derechos. Sinda gabos tinawan nin pag-isip asin conciencia kaya dapat na makipag-iriba
    sa lambang saro bilang mga magturugang.
</label>

<label>
    <input type="radio" bind:group={scripts} value={17} />
    ᨔᨗᨊᨗᨊ ᨑᨘᨄ ᨈᨕᨘ ᨑᨗ ᨍᨍᨗᨕᨊᨁᨗ ᨑᨗᨒᨗᨊᨚᨕᨙ ᨊᨄᨘᨊᨕᨗ ᨆᨊᨙᨊᨁᨗ ᨑᨗᨕᨔᨙᨊᨁᨙ ᨕᨒᨙᨅᨗᨑᨙ᨞ ᨊᨄᨘᨊᨕᨗ ᨑᨗᨕᨔᨙᨊᨁᨙ
    ᨕᨀᨒᨙ᨞ ᨊᨄᨘᨊᨕᨗ ᨑᨗᨕᨔᨙᨊᨁᨙ ᨕᨈᨗ ᨆᨑᨙᨊᨗ ᨊ ᨔᨗᨅᨚᨒᨙ ᨅᨚᨒᨙᨊ ᨄᨉ ᨔᨗᨄᨀᨈᨕᨘ ᨄᨉ ᨆᨔᨒᨔᨘᨑᨙ᨞
</label>

<label>
    <input type="radio" bind:group={scripts} value={18} />
    Ang tanang katawhan gipakatawo nga may kagawasan ug managsama sa kabililhon.
    Sila gigasahan sa salabutan ug tanlag og mag-ilhanay isip managsoon sa usa'g-usa
    diha sa diwa sa ospiritu.
</label>

<label>
    <input type="radio" bind:group={scripts} value={19} />
    Era sucu ena galala na tamata yadua, era tautauvata ena nodra dokai kei na nodra
    dodonu. E tiko na nodra vakasama kei na nodra lewaeloma, sa dodonu mera veidokadokai
    ena yalo ni veitacini.
</label>

<label>
    <input type="radio" bind:group={scripts} value={20} />
    Hānau kū'oko'a 'ia nā kānaka apau loa, a ua kau like ka hanohano a me nā pono
    kīvila ma luna o kākou pākahi. Ua ku'u mai ka no'ono'o pono a me ka 'ike pono
    ma luna o kākou, no laila, e aloha kākou kekahi i kekahi.
</label>

<label>
    <input type="radio" bind:group={scripts} value={21} />
    Semua orang dilahirkan merdeka dan mempunyai martabat dan hak-hak yang sama.
    Mereka dikaruniai akal dan hati nurani dan hendaknya bergaul satu sama lain dalam
    semangat persaudaraan.
</label>

<label>
    <input type="radio" bind:group={scripts} value={22} />
    ꦱꦧꦼꦤ꧀ꦲꦸꦮꦺꦴꦁꦏꦭꦲꦶꦂꦫꦏ꧀ꦏꦺꦏꦤ꧀ꦛꦶꦩꦂꦢꦶꦏꦭꦤ꧀ꦢꦂꦧꦺꦩꦂꦠꦧꦠ꧀ꦭꦤꦲꦏ꧀ꦲꦏ꧀ꦏꦁꦥꦝ꧉ ꦏꦧꦺꦃꦥꦶꦤꦫꦶꦁꦔꦤ꧀ꦲꦏꦭ꧀ꦭꦤ꧀ꦏꦭ꧀ꦧꦸꦱꦂꦠꦏꦲꦗꦧ꧀ꦥ
    ꦱꦿꦮꦸꦁꦔꦤ꧀ꦲꦁꦒꦺꦴꦤ꧀ꦤꦺꦩꦼꦩꦶ ꦠꦿꦤ꧀ꦱꦶꦗꦶꦭꦤ꧀ꦱꦶꦗꦶꦤꦺꦏꦤ꧀ꦛꦶꦗꦶꦮꦱꦸꦩꦢꦸꦭꦸꦂ꧉
</label>

<label>
    <input type="radio" bind:group={scripts} value={23} />
    Ko te katoa o nga tangata i te whanaungatanga mai e watea ana i nga here katoa;
    e tauriterite ana hoki nga mana me nga tika. E whakawhiwhia ana hoki ki a ratou
    te ngakau whai whakaaro me te hinengaro mohio ki te tika me te he, a e tika ana
    kia meinga te mahi a tetahi ki tetahi me ma roto atu i te wairua o te noho tahi,
    ano he teina he tuakana i ringa i te whakaaro kotahi.
</label>

<label>
    <input type="radio" bind:group={scripts} value={24} />
    Sadajana oreng lahir mardika e sarenge drajat klaban hak-hak se dha-padha. Sadajana
    eparenge akal sareng nurani ban kodu areng-sareng akanca kadi taretan.
</label>

<label>
    <input type="radio" bind:group={scripts} value={25} />
    Teraka afaka sy mitovy zo sy fahamendrehana ny olombelona rehetra. Samy manan-tsaina
    sy fieritreretana ka tokony hifampitondra ampirahalahiana.
</label>

<label>
    <input type="radio" bind:group={scripts} value={26} />
    Semua manusia dilahirkan bebas dan samarata dari segi kemuliaan dan hak-hak.
    Mereka mempunyai pemikiran dan perasaan hati dan hendaklah bertindak di antara
    satu sama lain dengan semangat persaudaraan.
</label>

<label>
    <input type="radio" bind:group={scripts} value={27} />
    سادوڽو مأنسي دلهياكن مرديكا دان ڤوڽو مرتبت ساراتو حق-حق نن سامو. مريك دكارونياي
    اكا جو هاتي نوراني، سوڤيو ساتو سامو لاين باڬاول ساروڤو اورڠ بادونسانق.
</label>

<label>
    <input type="radio" bind:group={scripts} value={28} />
    Kua anau rangatira ia te tangata katoatoa ma te aiteite i te au tikaanga e te
    tu ngateitei tiratiratu. Kua ki ia ratou e te mero kimi ravenga e te akavangakau
    e kia akono tetai i tetai, i roto i te vaerua piri anga taeake.
</label>

<label>
    <input type="radio" bind:group={scripts} value={29} />
    Kutê tun laher mêrdiko, tmu'an hok-hok gi srai. Kutênê nagiakba akêa peker ngen
    atêi, kêrno o kêloknê bêkuatba do ngen luyên nêak lêm asai sêpasuak.
</label>

<label>
    <input type="radio" bind:group={scripts} value={30} />
    ᮞᮊᮥᮙ᮪ᮔ ᮏᮜ᮪ᮙ ᮌᮥᮘᮢᮌ᮪ ᮊ ᮃᮜᮙ᮪ ᮓᮥᮑ ᮒᮨᮂᮞᮤᮖᮒ᮪ᮔ ᮙᮨᮛ᮪ᮓᮤᮊ ᮏᮦᮀ ᮘᮧᮌ ᮙᮛ᮪ᮒᮘᮒ᮪ ᮊᮒᮥᮒ᮪ ᮠᮊ᮪-ᮠᮊ᮪
    ᮃᮔᮥ ᮞᮛᮥᮃ. ᮙᮛᮔᮦᮨᮂᮔ ᮓᮤᮘᮨᮛᮨ ᮃᮊᮜ᮪ ᮏᮩᮠᮀᮒᮨ ᮔᮥᮛᮔᮤ, ᮎᮙ᮪ᮕᮥᮁᮛ᮪-ᮌᮅᮜ᮪ ᮏᮩᮀ ᮞᮞᮙᮔ ᮃᮚ ᮓᮤᮔ ᮞᮥᮙᮔᮨᮒ᮪
    ᮓᮥᮓᮥᮜᮥᮛᮔ᮪.
</label>

<label>
    <input type="radio" bind:group={scripts} value={31} />
    Ang lahat ng tao'y isinilang na malaya at pantay-pantay sa karangalan at mga
    karapatan. Sila'y pinagkalooban ng katwiran at budhi at dapat magpalagayan ang
    isa't isa sa diwa ng pagkakapatiran. | ᜀᜅ᜔ ᜎᜑᜆ᜔ ᜅ᜔ ᜆᜂᜌ᜔ ᜁᜐᜒᜈᜒᜎᜅ᜔ ᜈ ᜋᜎᜌ ᜀᜆ᜔ ᜉᜈ᜔ᜆᜌ᜔-ᜉᜈ᜔ᜆᜌ᜔
    ᜐ ᜃᜇᜅᜎᜈ᜔ ᜀᜆ᜔ ᜋ᜔ᜄ ᜃᜇᜉᜆᜈ᜔᜶ ᜐᜒᜎᜌ᜔ ᜉᜒᜈᜄ᜔ᜃᜎᜓᜂᜊᜈ᜔ ᜅ᜔ ᜃᜆ᜔ᜏᜒᜇᜈ᜔ ᜀᜆ᜔ ᜊᜓᜇ᜔ᜑᜒ ᜀᜆ᜔ ᜇᜉᜆ᜔ ᜋᜄ᜔ᜉᜎᜄᜌᜈ᜔
    ᜀᜅ᜔ ᜁᜐᜆ᜔ ᜁᜐ ᜐ ᜇᜒᜏ ᜅ᜔ ᜉᜄ᜔ᜃᜃᜉᜆᜒᜇᜈ᜔᜶
</label>

<label>
    <input type="radio" bind:group={scripts} value={32} />
    Segheme manusie lahér-lahér je bébah, sameghate daghi segi kemulieang nge hok-hok
    ye. Maséng-maséng ade ppikéghang nge peghasaang, kene tulong antaghe satu same
    laéng nge semangak pesedagheang.
</label>

<label>
    <input type="radio" bind:group={scripts} value={33} />
    Ema hotu hotu moris hanesan ho dignidade ho direitu. Sira hotu iha hanoin, konsiensia
    n'e duni tenki hare malu hanesan espiritu maun-alin.
</label>

<label>
    <input type="radio" bind:group={scripts} value={34} />
    E fā'nau mai a tino katoa i te saolotoga kae e 'pau telotou tūlaga fakaaloalogina
    mo telotou aiā. Ne tuku atu ki a lātou a te mafaufau mo te loto lagona, tēlā
    lā, e 'tau o gā'lue fakatasi lātou e pēlā me ne taina.
</label>

<label>
    <input type="radio" bind:group={scripts} value={35} />
    Watu wote wamezaliwa huru, hadhi na haki zao ni sawa. Wote wamejaliwa akili na
    dhamiri, hivyo yapasa watendeane kindugu.
</label>

<label>
    <input type="radio" bind:group={scripts} value={36} />
    Bonke abantu bazalwa bekhululekile belingana ngesithunzi nangamalungelo. Bahlanganiswe
    wumcabango nangunembeza futhi kufanele baphathane ngomoya wobunye.
</label>

<label>
    <input type="radio" bind:group={scripts} value={37} />
    Saolaítear na daoine uile saor agus comhionann ina ndínit agus ina gcearta. Tá
    bua an réasúin agus an choinsiasa acu agus dlíd iad féin d'iompar de mheon bráithreachais
    i leith a chéile.
</label>

<label>
    <input type="radio" bind:group={scripts} value={38} />
    Ta dagh chooilley ghooinney ruggit seyr as corrym rish dy chooilley ghooinney
    elley ayns ooashley as ayns cairys. Ta resoon as cooinsheanse stowit orroo as
    lhisagh ad dellal rish y cheilley lesh spyrryd braaraghyn.
</label>

<label>
    <input type="radio" bind:group={scripts} value={39} />
    Rugadh na h-uile duine saor agus co-ionnan nan urram 's nan còirichean. Tha iad
    reusanta is cogaiseach, agus bu chòir dhaibh a ghiùlain ris a chèile ann an spiorad
    bràthaireil.
</label>

<label>
    <input type="radio" bind:group={scripts} value={40} />
    Genir pawb yn rhydd ac yn gydradd â'i gilydd mewn urddas a hawliau. Fe'u cynysgaeddir
    â rheswm a chydwybod, a dylai pawb ymddwyn y naill at y llall mewn ysbryd cymodlon.
</label>

<label>
    <input type="radio" bind:group={scripts} value={41} />
    Ĉiuj homoj estas denaske liberaj kaj egalaj laŭ digno kaj rajtoj. Ili posedas
    racion kaj konsciencon, kaj devus konduti unu al alia en spirito de frateco.
</label>

<label>
    <input type="radio" bind:group={scripts} value={42} />
    All mensklik wesings âre boren frî on' gelîk in werđigheid on' rejte. Đê âre
    begifted mid ferstand on' gewitt on' skulde behandele êlkên in en gêst av brôđerhêd.
</label>

<label>
    <input type="radio" bind:group={scripts} value={43} />
    Omna homi naskas libera ed egala relate digneso e yuri. Li es dotita perraciono
    e koncienco e devas agar vers l'una l'altra en spirito di frateso.
</label>

<label>
    <input type="radio" bind:group={scripts} value={44} />
    Тота уманес насе либре е егал ен диниа е диретос. Лос ес донада разона е консиенса
    е дебе ата ла ун а ла отра ен ун спирито де фратиа.
</label>

<label>
    <input type="radio" bind:group={scripts} value={45} />
    ro remna cu se jinzi co zifre je simdu'i be le ry. nilselsi'a .e lei ry. selcru
    .i ry. se menli gi'e se sezmarde .i .ei jeseki'ubo ry. simyzu'e ta'i le tunba
</label>

<label>
    <input type="radio" bind:group={scripts} value={46} />
    jan ale/ali li kama lon nasin ni: ona li ken pali e wile ona. ona li jo e suli
    jan sama e ken sama. ona li jo e sona pona e lawa insa pi pali pona. ni la, ona
    li wile pali tawa jan ante ale/ali kepeken nasin olin.
</label>

<label>
    <input type="radio" bind:group={scripts} value={47} />
    Mens valik pemotons libiko e leigiko tefü digäd e gitäts. Labons tikäli e konsieni,
    e sötons kosädön ko ods siämü svistäl.
</label>

<label>
    <input type="radio" bind:group={scripts} value={48} />
    ಎಲ್ಲಾ ಮಾನವರೂ ಸ್ವತಂತ್ರರಾಗಿಯೇ ಜನಿಸಿದ್ದಾರೆ. ಹಾಗೂ ಘನತೆ ಮತ್ತು ಹಕ್ಕು ಗಳಲ್ಲಿ ಸಮಾನರಾಗಿದ್ದರೆ.
    ವಿವೇಕ ಮತ್ತು ಅಂತಃಕರಣ ಗಳನ್ನು ಪಡೆದವರಾದ್ದರಿಂದ ಅವರು ಪರಸ್ಪರ ಸಹೋದರ ಭಾವದಿಂದ ವರ್ತಿಸಬೇಕು.
</label>

<label>
    <input type="radio" bind:group={scripts} value={49} />
    മനുഷ്യരെല്ലാവരും തുല്യാവകാശങ്ങളോടും അന്തസ്സോടും സ്വാതന്ത്ര്യത്തോടുംകൂടി ജനിച്ചവരാണ്.
    അന്യോന്യം ഭ്രാതൃഭാവത്തോടെ പെരുമാറുവാനാണ് മനുഷ്യന്നു വിവേകബുദ്ധിയും മനസ്സാക്ഷിയും
    സിദ്ധമായിരിക്കുന്നത്.
</label>

<label>
    <input type="radio" bind:group={scripts} value={50} />
    மனிதப் பிறவியினர் சகலரும் சுதந்திரமாகவே பிறக்கின்றனர்; அவர்கள் மதிப்பிலும் உரிமைகளிலும்
    சமமானவர்கள். அவர்கள் நியாயத்தையும் மனசாட்சியையும் இயற்பண்பாகப் பெற்றவர்கள். அவர்கள்
    ஒருவருடனொருவர் சகோதர உணர்வுப் பாங்கில் நடந்துகொள்ளல் வேண்டும்.
</label>

<label>
    <input type="radio" bind:group={scripts} value={51} />
    Inuit tamarmik inunngorput nammineersinnaassuseqarlutik assigiimmillu ataqqinassuseqarlutillu
    pisinnaatitaaffeqarlutik. Silaqassusermik tarnillu nalunngissusianik pilersugaapput,
    imminnullu iliorfigeqatigiittariaqaraluarput qatanngutigiittut peqatigiinnerup
    anersaavani.
</label>

<label>
    <input type="radio" bind:group={scripts} value={52} />
    Zhdo njeri kan le t'lir mê njãjit dinjitêt edhê dreta. Ata jan të pajisun mê
    mênjê edhê vet-dijê edhê duhën të veprôjn ka njãni-tjetrin mê nji shpirt vllâznimit.
</label>

<label>
    <input type="radio" bind:group={scripts} value={53} />
    Të gjithë njerëzit lindin të lirë dhe të barabartë në dinjitet dhe në të drejta.
    Ata kanë arsye dhe ndërgjegje dhe duhet të sillen ndaj njëri tjetrit me frymë
    vëllazërimi.
</label>

<label>
    <input type="radio" bind:group={scripts} value={54} />
    Բոլոր մարդիկ ծնվում են ազատ ու հավասար` իրենց արժանապատվությամբ և իրավունքներով:
    Նրանք օժտված են բանականությամբ ու խղճով, և պարտավոր են միմյանց նկատմամբ վարվել
    եղբայրության ոգով.
</label>

<label>
    <input type="radio" bind:group={scripts} value={55} />
    Բոլոր մարդիկ կը ծնուին ազատ եւ հաւասար իրենց արժանապատուութեամբ եւ իրաւունքներով:
    Իրենք օժտուած են բանականութեամբ ու խիղճով, եւ պարտաւորուած են միմեանց հանդէպ
    եղբայրութեան ոգիով վարուիլ:
</label>

<label>
    <input type="radio" bind:group={scripts} value={56} />
    Visi cilvēki piedzimst brīvi un vienlīdzīgi savā pašcieņā un tiesībās. Viņi ir
    apveltīti ar saprātu un sirdsapziņu, un viņiem jāizturas citam pret citu brālības
    garā.
</label>

<label>
    <input type="radio" bind:group={scripts} value={57} />
    Visi žmonės gimsta laisvi ir lygūs savo orumu ir teisėmis. Jiems suteiktas protas
    ir sąžinė ir jie turi elgtis vienas kito atžvilgiu kaip broliai.
</label>

<label>
    <input type="radio" bind:group={scripts} value={58} />
    Alle menslike wesens word vry, met gelyke waardigheid en regte, gebore. Hulle
    het rede en gewete en behoort in die gees van broederskap teenoor mekaar op te
    tree.
</label>

<label>
    <input type="radio" bind:group={scripts} value={59} />
    Alle mennesker er født frie og lige i værdighed og rettigheder. De er udstyret
    med fornuft og samvittighed, og de bør handle mod hverandre i en broderskabets
    ånd.
</label>

<label>
    <input type="radio" bind:group={scripts} value={60} />
    Alle mensen worden vrij en gelijk in waardigheid en rechten geboren. Zij zijn
    begiftigd met verstand en geweten, en behoren zich jegens elkander in een geest
    van broederschap te gedragen.
</label>

<label>
    <input type="radio" bind:group={scripts} value={61} />
    Âl minsken wordent fräj un glīk in wērderğkaid un rechten bōren. Säi hebbent
    küen un gewäiten mitkrēgen un söölent mitnanner in brörskup lēven.
</label>

<label>
    <input type="radio" bind:group={scripts} value={62} />
    All human beings are born free and equal in dignity and rights. They are endowed
    with reason and conscience and should act towards one another in a spirit of
    brotherhood.
</label>

<label>
    <input type="radio" bind:group={scripts} value={63} />
    Øll menniskju eru fødd fræls og jøvn til virðingar og mannarættindi. Tey hava
    skil og samvitsku og eiga at fara hvørt um annað í bróðuranda.
</label>

<label>
    <input type="radio" bind:group={scripts} value={64} />
    Alli Mönshe send frey ond geboore met gliicher Wörd ond gliiche Rächt. Si send
    xägnet met Vernonft ond Gwösse ond sölled enand e brüederlechem Gäisht begägne.
</label>

<label>
    <input type="radio" bind:group={scripts} value={65} />
    Alle Menschen sind frei und gleich an Würde und Rechten geboren. Sie sind mit
    Vernunft und Gewissen begabt und sollen einander im Geist der Brüderlichkeit
    begegnen.
</label>

<label>
    <input type="radio" bind:group={scripts} value={66} />
    Hver maður er borinn frjáls og jafn öðrum að virðingu og réttindum. Menn eru
    gæddir vitsmunum og samvisku, og ber þeim að breyta bróðurlega hverjum við annan.
</label>

<label>
    <input type="radio" bind:group={scripts} value={67} />
    All Mënsch kënnt fräi a mat deer selwechter Dignitéit an dene selwechte Rechter
    op d'Welt. Jiddereen huet säi Verstand a säi Gewësse krut an soll an engem Geescht
    vu Bridderlechkeet denen anere géintiwwer handelen.
</label>

<label>
    <input type="radio" bind:group={scripts} value={68} />
    Wat Wöörd' un Rechten sünd, daar sünd all de Minschen free un liek mit boorn.
    Se hebbt dat Tüüg för Vernimm un Gewäten mitkrägen, un dat böört jüm, dat se
    eenanner in'n Geest vun Bröderschup in de Mööt kaamt.
</label>

<label>
    <input type="radio" bind:group={scripts} value={69} />
    Alle mennesker er født frie og med samme menneskeverd og menneskerettigheter.
    De er utstyrt med fornuft og samvittighet og bør handle mot hverandre i brorskapets
    ånd.
</label>

<label>
    <input type="radio" bind:group={scripts} value={70} />
    Alle menneske er fødde til fridom og med same menneskeverd og menneskerettar.
    Dei har fått fornuft og samvit og skal leve med kvarandre som brør.
</label>

<label>
    <input type="radio" bind:group={scripts} value={71} />
    Ealle menn sindon āre and rihtes efen ġeboren, and frēo. Him sindon ġiefeþe ġerād
    and inġehyġd, and hī sċulon dōn tō ōþrum on brōþorsċipes fēore.
</label>

<label>
    <input type="radio" bind:group={scripts} value={72} />
    Allir menn eru bornir frjálsir ok jafnir at virðingu ok réttum. Þeir eru allir
    viti gœddir ok samvizku, ok skulu gøra hvárr til annars bróðurliga.
</label>

<label>
    <input type="radio" bind:group={scripts} value={73} />
    Alla människor är födda fria och lika i värdighet och rättigheter. De är utrustade
    med förnuft och samvete och bör handla gentemot varandra i en anda av broderskap.
</label>

<label>
    <input type="radio" bind:group={scripts} value={74} />
    Ali Mensken sen frii, likwērtig en me disalev Rochten bēren. Ja haa Forstant
    en Giweeten mefingen en skul arküđer üs Bröđern öntöögentreer.
</label>

<label>
    <input type="radio" bind:group={scripts} value={75} />
    All mensher ä född fri å ä lik i vaaL å rätt. De 'a gûes ômdömm å samvett å boL
    hannel a varanner i broderskapsånn.
</label>

<label>
    <input type="radio" bind:group={scripts} value={76} />
    Alle minsken wurde frij en gelyk yn weardigens en rjochten berne. Hja hawwe ferstân
    en gewisse meikrigen en hearre har foar inoar oer yn in geast fan bruorskip te
    hâlden en te dragen.
</label>

<label>
    <input type="radio" bind:group={scripts} value={77} />
    Yeder mentsh vert geboyrn fray un glaykh in koved un rekht. Yeder vert bashonkn
    mit farshtand un gevisn; yeder zol zikh firn mit a tsveytn in a gemit fun brudershaft.
</label>

<label>
    <input type="radio" bind:group={scripts} value={78} />
    Ολοι οι άνθρωποι γεννιούνται ελεύθεροι και ίσοι στην αξιοπρέπεια και τα δικαιώματα.
    Είναι προικισμένοι με λογική και συνείδηση, και οφείλουν να συμπεριφέρονται μεταξύ
    τους με πνεύμα αδελφοσύνης.
</label>

<label>
    <input type="radio" bind:group={scripts} value={79} />
    জন্মগতভাৱে সকলো মানুহ মৰ্য্যদা আৰু অধিকাৰত সমান আৰু স্বতন্ত্ৰ। তেওঁলোকৰ বিবেক
    আছে, বুদ্ধি আছে। তেওঁলোকে প্ৰত্যেকে প্ৰেত্যেকক ভ্ৰাতৃভাৱে ব্যৱহাৰ কৰা উচিত।
</label>

<label>
    <input type="radio" bind:group={scripts} value={80} />
    সমস্ত মানুষ স্বাধীনভাবে সমান মর্যাদা এবং অধিকার নিয়ে জন্মগ্রহণ করে | তাঁদের
    বিবেক এবং বুদ্ধি আছে সুতরাং সকলেরই একে অপরের প্রতি ভ্রাতৃত্বসুলভ মনোভাব নিয়ে
    আচরণ করা উচিত্ |
</label>

<label>
    <input type="radio" bind:group={scripts} value={81} />
    বিয়াক মানুশ ইজ্‌জত এদ‌্দে অ়কর ই়শাবে আজাদ আর উ়য়াইন্‌না অ়ইয়েরে ফ়য়দা অ়য়। ই়তারাত্‌তু
    আহল এদ্‌দে বিবেক আছে ; এতল্‌লায় এজ্‌জন আরেজ্‌জনর উ়য়ারে ভাইয়ুর নান বেভার গরন
    দরহার।
</label>

<label>
    <input type="radio" bind:group={scripts} value={82} />
    सभी मनुष्यों को गौरव और अधिकारों के मामले में जन्मजात स्वतन्त्रता और समानता प्राप्त
    है। उन्हें बुद्धि और अन्तरात्मा की देन प्राप्त है और परस्पर उन्हें भाईचारे के
    भाव से बर्ताव करना चाहिए।
</label>

<label>
    <input type="radio" bind:group={scripts} value={83} />
    سٔری لُکھ چهہٕ حقوٗق تِہ عزت لِحاظٕ ہِہیٖ ژامِت. تِمن چه‍ہِ ضمير تِہ عَقل دِنِ
    آمٕژ. تٔوے پَزٕ تُمن بھٲئی برادری سانٛ روزُن.
</label>

<label>
    <input type="radio" bind:group={scripts} value={84} />
    Saf insān āzād wa ḥuqūq-ochay izzato ėʿtibāro sora barābaar paidā biti asuni.
    hetantey żamīr ôchay ʿaql ataa koronu biti sher. Hey bachen hetan taan muzhi
    brar gariyo sulūk korelik.
</label>

<label>
    <input type="radio" bind:group={scripts} value={85} />
    Hemû mirov azad û di weqar û mafan de wekhev tên dinyayê. Ew xwedî hiş û şuûr
    in û divê li hember hev bi zihniyeteke bratiyê bilivin.
</label>

<label>
    <input type="radio" bind:group={scripts} value={86} />
    ހުރިހާ އިންސާނުން ވެސް އުފަންވަނީ، ދަރަޖައާއި ޙައްޤުތަކުގައި މިނިވަންކަމާއި ހަމަހަމަކަން
    ލިބިގެންވާ ބައެއްގެ ގޮތުގައެވެ. އެމީހުންނަށް ހެޔޮ ވިސްނުމާއި، ހެޔޮ ބުއްދީގެ ބާރު
    ލިބިގެންވެއެވެ. އަދި އެމީހުން އެކަކު އަނެކަކާ މެދު މުޢާމަލާތް ކުރަންވާނީ، އުޚުއްވަތްތެރި
    ކަމުގެ ރޫޙެއްގައެވެ.
</label>

<label>
    <input type="radio" bind:group={scripts} value={87} />
    सर्व मनुष्यजात जन्मतःच स्वतंत्र आहे व सर्वजणांना समान प्रतिष्ठा व समान अधिकार
    आहेत. त्यांना विचारशक्ती व सदसद्विवेकबुद्धी लाभलेली आहे व त्यांनी एकमेकांशी बंधुत्वाच्या
    भावनेने आचरण करावे.
</label>

<label>
    <input type="radio" bind:group={scripts} value={88} />
    سگݪا مݨکه نے گورو ان ادهکاروں رے راسے مای جݪم سوں سوتنترا انے سمانتا پراپت چهے.
    وݨی رے گوڑے بده ان انتراتما ری پراپتی چهے ان وݨی نے بهیئیپاݪا بهاونا سو اےکبیجے
    رے سارو ورتن کرݨو جوییجے چهے.
</label>

<label>
    <input type="radio" bind:group={scripts} value={89} />
    सबै व्यक्तिहरू जन्मजात स्वतन्त्र हुन् ती सबैको समान अधिकार र महत्व छ। निजहरूमा
    विचार शक्ति र सद्विचार भएकोले निजहरूले आपस्तमा भ्रातृत्वको भावनाबाट व्यवहार गर्नु
    पर्छ।
</label>

<label>
    <input type="radio" bind:group={scripts} value={90} />
    ସବୁ ମନୁଷ୍ୟ ଜନ୍ମକାଳରୁ ସ୍ୱାଧୀନ. ସେମାନଙ୍କର ମର୍ଯ୍ୟାଦା ଓ ଅଧିକାର ସମାନ. ସେମାନଙ୍କଠାରେ
    ପ୍ରଜ୍ଞା ଓ ବିବେକ ନିହିତ ଅଛି. ସେମାନେ ପରସ୍ପର ପ୍ରତି ଭାତୃଭାବ ପୋଷଣ କରି କାର୍ଯ୍ୟ କରିବା
    ଦରକାର.
</label>

<label>
    <input type="radio" bind:group={scripts} value={91} />
    Адӕймӕгтӕ се 'ппӕт дӕр райгуырынц сӕрибарӕй ӕмӕ ӕмхуызонӕй сӕ барты. Уыдон ӕххӕст
    сты зонд ӕмӕ намысӕй, ӕмӕ кӕрӕдзийӕн хъуамӕ уой ӕфсымӕрты хуызӕн.
</label>

<label>
    <input type="radio" bind:group={scripts} value={92} />
    تمام افراد بشر آزاد به دنیا می آیند و از لحاظ حیثیت و حقوق با هم برابرند, همه
    دارای عقل و وجدان می باشند و باید نسبت به یک دیگر با روح برادری رفتار کنند.
</label>

<label>
    <input type="radio" bind:group={scripts} value={93} />
    ਸਾਰਾ ਮਨੁੱਖੀ ਪਰਿਵਾਰ ਆਪਣੀ ਮਹਿਮਾ, ਸ਼ਾਨ ਅਤੇ ਹੱਕਾਂ ਦੇ ਪੱਖੋਂ ਜਨਮ ਤੋਂ ਹੀ ਆਜ਼ਾਦ ਹੈ ਅਤੇ
    ਸੁਤੇ ਸਿੱਧ ਸਾਰੇ ਲੋਕ ਬਰਾਬਰ ਹਨ । ਉਨ੍ਹਾਂ ਸਭਨਾ ਨੂੰ ਤਰਕ ਅਤੇ ਜ਼ਮੀਰ ਦੀ ਸੌਗਾਤ ਮਿਲੀ ਹੋਈ
    ਹੈ ਅਤੇ ਉਨ੍ਹਾਂ ਨੂੰ ਭਰਾਤਰੀਭਾਵ ਦੀ ਭਾਵਨਾ ਰਖਦਿਆਂ ਆਪਸ ਵਿਚ ਵਿਚਰਣਾ ਚਾਹੀਦਾ ਹੈ ।
</label>

<label>
    <input type="radio" bind:group={scripts} value={94} />
    सर्वे मानवाः स्वतन्त्राः समुत्पन्नाः वर्तन्ते अपि च, गौरवदृशा अधिकारदृशा च समानाः
    एव वर्तन्ते। एते सर्वे चेतना-तर्क-शक्तिभ्यां सुसम्पन्नाः सन्ति। अपि च, सर्वेऽपि
    बन्धुत्व-भावनया परस्परं व्यवहरन्तु।
</label>

<label>
    <input type="radio" bind:group={scripts} value={95} />
    සියලූ මනුෂ්‍යයෝ නිදහස්ව උපත ලබා ඇත. ගරුත්වයෙන් හා අයිතිවාසිකම් සමාන වෙති. යුක්ති
    අයුක්ති පිළිබඳ හැඟීමෙන් හා හෘදය සාක්ෂියෙන් යුත් ඔවුනොවුන්වුන්ට සැළකිය යුත්තේ
    සහෝදරත්වය පිළිබඳ හැඟීමෙනි.
</label>

<label>
    <input type="radio" bind:group={scripts} value={96} />
    تمام انسان آزاد اور حقوق و عزت کے اعتبار سے برابر پیدا ہوۓ ہیں۔ انہیں ضمیر اور
    عقل ودیعت ہوئی ہے۔ اسلیۓ انہیں ایک دوسرے کے ساتھ بھائی چارے کا سلوک کرنا چاہیۓ۔
</label>

<label>
    <input type="radio" bind:group={scripts} value={97} />
    Omnes homines dignitate et iure liberi et pares nascuntur, rationis et conscientiae
    participes sunt, quibus inter se concordiae studio est agendum.
</label>

<label>
    <input type="radio" bind:group={scripts} value={98} />
    Toz os ombres naxen libres y iguals en dinidat y en dreitos. Adotatos de razón
    y de conzenzia, deben apachar-sen unos con atros d'una manera freternal.
</label>

<label>
    <input type="radio" bind:group={scripts} value={99} />
    Tuti iatsâli umineshtsâ s-fac liberi shi egali la nâmuzea shi-ndrepturli. Eali
    suntu hârziti cu fichiri shi sinidisi shi lipseashti un cu alantu sh-si poartâ
    tu duhlu-a frâtsâljiljei.
</label>

<label>
    <input type="radio" bind:group={scripts} value={100} />
    Tolos seres humanos nacen llibres y iguales en dignidá y drechos y, pola mor
    de la razón y la conciencia de so, han comportase hermaniblemente los unos colos
    otros.
</label>

<label>
    <input type="radio" bind:group={scripts} value={101} />
    Todos os seres humanos nascem livres e iguais em dignidade e direitos. São dotados
    de razão e consciência e devem agir em relação uns aos outros com espírito de
    fraternidade.
</label>

<label>
    <input type="radio" bind:group={scripts} value={102} />
    Tots els éssers humans neixen lliures i iguals en dignitat i en drets. Són dotats
    de raó i de consciència, i han de comportar-se fraternalment els uns amb els
    altres.
</label>

<label>
    <input type="radio" bind:group={scripts} value={103} />
    Tous les êtres humains naissent libres et égaux en dignité et en droits. Ils
    sont doués de raison et de conscience et doivent agir les uns envers les autres
    dans un esprit de fraternité.
</label>

<label>
    <input type="radio" bind:group={scripts} value={104} />
    Tous les êtres humains naissent libres et égaux en dignité et en droits. Ils
    sont doués de raison et de conscience et doivent agir les uns envers les autres
    dans un esprit de fraternité.
</label>

<label>
    <input type="radio" bind:group={scripts} value={105} />
    Tódolos seres humanos nacen libres e iguais en dignidade e dereitos e, dotados
    como están de razón e conciencia, díbense comportar fraternalmente uns cos outros.
</label>

<label>
    <input type="radio" bind:group={scripts} value={106} />
    Tutti gli esseri umani nascono liberi ed eguali in dignità e diritti. Essi sono
    dotati di ragione e di coscienza e devono agire gli uni verso gli altri in spirito
    di fratellanza.
</label>

<label>
    <input type="radio" bind:group={scripts} value={107} />
    Töcc i véser umà i nas líber e precís en dignità e diricc. I è dotacc de rizú
    e de coscenssa e i ga de comportà-s, de giü con l'óter, en spírit de fradelanssa.
</label>

<label>
    <input type="radio" bind:group={scripts} value={108} />
    Totes li hàmmes v'nàt au monde libes et égaux de la dignitè et da lo drâ. Ils
    so dotès de rahho et d'conscience et so t'nus d'se compoutè li ines enwoués lis
    autes da in esprit d'fraternitè.
</label>

<label>
    <input type="radio" bind:group={scripts} value={109} />
    Totas las personas nàisson liuras e parièras en dignitat e en dreches. Son cargadas
    de rason e de consciéncia e mai lor se cal comportar entre elas amb un eime de
    frairetat.
</label>

<label>
    <input type="radio" bind:group={scripts} value={110} />
    Tùit j'esse uman a nasso lìber e uguaj an dignità e an drit. A son dotà ‘d sust
    e ‘d consiensa e a dëvo agì j’un con j’àutri ant n’ëspìrit ëd fradlansa.
</label>

<label>
    <input type="radio" bind:group={scripts} value={111} />
    Todos os seres humanos nascem livres e iguais em dignidade e em direitos. Dotados
    de razão e de consciência, devem agir uns para com os outros em espírito de fraternidade.
</label>

<label>
    <input type="radio" bind:group={scripts} value={112} />
    Toate ființele umane se nasc libere și egale în demnitate și în drepturi. Ele
    sunt înzestrate cu rațiune și conștiință și trebuie să se comporte unele față
    de altele în spiritul fraternității.
</label>

<label>
    <input type="radio" bind:group={scripts} value={113} />
    Tutti l'omini nascinu libbiri cu a stissa dignità i diritti. Iddi hannu a raggiuni
    i cuscienza i hannu a travagghiari 'nzemmula cu spiritu di fratirnità.
</label>

<label>
    <input type="radio" bind:group={scripts} value={114} />
    Todos los seres humanos nacen libres e iguales en dignidad y derechos y, dotados
    como están de razón y conciencia, deben comportarse fraternalmente los unos con
    los otros.
</label>

<label>
    <input type="radio" bind:group={scripts} value={115} />
    Todos los seres humanos nacen libres e iguales en dignidad y derechos y, dotados
    como están de razón y conciencia, deben comportarse fraternalmente los unos con
    los otros.
</label>

<label>
    <input type="radio" bind:group={scripts} value={116} />
    Todos los seres humanos nacen libres e iguales en dignidad y derechos y, dotados
    como están de razón y conciencia, deben comportarse fraternalmente los unos con
    los otros.
</label>

<label>
    <input type="radio" bind:group={scripts} value={117} />
    Todos los seres humanos nacen libres e iguales en dignidad y derechos y, dotados
    como están de razón y conciencia, deben comportarse fraternalmente los unos con
    los otros.
</label>

<label>
    <input type="radio" bind:group={scripts} value={118} />
    Tots els éssers humans naixen lliures i iguals en dignitat i en drets i, dotats
    com estan de raó i de consciència, s’han de comportar fraternalment els uns amb
    els altres.
</label>

<label>
    <input type="radio" bind:group={scripts} value={119} />
    Tos lès-omes vinèt-st-å monde lîbes, èt so-l'minme pîd po çou qu'ènn'èst d'leu
    dignité èt d'leus dreûts. I n'sont nin foû rêzon èt-z-ont-i leû consyince po
    zèls, çou qu'èlzès deût miner a s'kidûre onk' po l'ôte tot come dès frés.
</label>

<label>
    <input type="radio" bind:group={scripts} value={120} />
    Usie ludzi naradžajucca svabodnymi i roŭnymi ŭ svajoj hodnaści i pravach. Jany
    nadzieleny rozumam i sumleńniem i pavinny stavicca adzin da adnaho ŭ duchu bractva.
</label>

<label>
    <input type="radio" bind:group={scripts} value={121} />
    Всички хора се раждат свободни и равни по достойнство и права. Tе са надарени
    с разум и съвест и следва да се отнасят помежду си в дух на братство.
</label>

<label>
    <input type="radio" bind:group={scripts} value={122} />
    Sva ljudska bića rađaju se slobodna i jednaka u dostojanstvu i pravima. Ona su
    obdarena razumom i sviješću i trebaju jedna prema drugima postupati u duhu bratstva.
</label>

<label>
    <input type="radio" bind:group={scripts} value={123} />
    Všichni lidé se rodí svobodní a sobě rovní co do důstojnosti a práv. Jsou nadáni
    rozumem a svědomím a mají spolu jednat v duchu bratrství.
</label>

<label>
    <input type="radio" bind:group={scripts} value={124} />
    Ситe чoвeчки суштeствa сe рaѓaaт слoбoдни и eднaкви пo дoстoинствo и прaвa. Tиe
    сe oбдaрeни сo рaзум и сoвeст и трeбa дa сe oднeсувaaт eдeн кoн друг вo дуxoт
    нa oпштo чoвeчкaтa припaднoст.
</label>

<label>
    <input type="radio" bind:group={scripts} value={125} />
    Wszyscy ludzie rodzą się wolni i równi w swojej godności i prawach. Są obdarzeni
    rozumem i sumieniem i powinni postępować wobec siebie w duchu braterstwa.
</label>

<label>
    <input type="radio" bind:group={scripts} value={126} />
    Все люди рождаются свободными и равными в своем достоинстве и правах. Они наделены
    разумом и совестью и должны поступать в отношении друг друга в духе братства.
</label>

<label>
    <input type="radio" bind:group={scripts} value={127} />
    Сва људска бића рађају се слободна и једнака у достојанству и правима. Она су
    обдарена разумом и свешћу и треба једни према другима да поступају у духу братства.
    | Sva ljudska bića rađaju se slobodna i jednaka u dostojanstvu i pravima. Ona
    su obdarena razumom i svešću i treba jedni prema drugima da postupaju u duhu
    bratstva.
</label>

<label>
    <input type="radio" bind:group={scripts} value={128} />
    Všetci ľudia sa rodia slobodní a sebe rovní, čo sa týka ich dostôjnosti a práv.
    Sú obdarení rozumom a majú navzájom jednať v bratskom duchu.
</label>

<label>
    <input type="radio" bind:group={scripts} value={129} />
    Vsi ljudje se rodijo svobodni in imajo enako dostojanstvo in enake pravice. Obdarjeni
    so z razumom in vestjo in bi morali ravnati drug z drugim kakor bratje.
</label>

<label>
    <input type="radio" bind:group={scripts} value={130} />
    Всі люди народжуються вільними і рівними у своїй гідності та правах. Вони наділені
    розумом і совістю і повинні діяти у відношенні один до одного в дусі братерства.
</label>

<label>
    <input type="radio" bind:group={scripts} value={131} />
    Gizon-emakume guztiak aske jaiotzen dira, duintasun eta eskubide berberak dituztela;
    eta ezaguera eta kontzientzia dutenez gero, elkarren artean senide legez jokatu
    beharra dute.
</label>

<label>
    <input type="radio" bind:group={scripts} value={132} />
    すべての人間は、生まれながらにして自由であり、かつ、尊厳と権利とについて平等である。人間は、理性と良心を授けられてあり、互いに同胞の精神をもって行動しなければならない。
</label>

<label>
    <input type="radio" bind:group={scripts} value={133} />
    모든 인간은 태어날 때부터 자유로우며 그 존엄과 권리에 있어 동등하다. 인간은 천부적으로
    이성과 양심을 부여받았으며 서로 형제애의 정신으로 행동하여야 한다.
</label>

<label>
    <input type="radio" bind:group={scripts} value={134} />
    ᠬᠦᠮᠦᠨ ᠪᠦᠷ ᠲᠥᠷᠥᠵᠦ ᠮᠡᠨᠳᠡᠯᠡᠬᠦ ᠡᠷᠬᠡ ᠴᠢᠯᠥᠭᠡ ᠲᠡᠢ᠂ ᠠᠳᠠᠯᠢᠬᠠᠨ ᠨᠡᠷ᠎ᠡ ᠲᠥᠷᠥ ᠲᠡᠢ᠂ ᠢᠵᠢᠯ ᠡᠷᠬᠡ ᠲᠡᠢ
    ᠪᠠᠢᠠᠭ᠃ ᠣᠶᠤᠨ ᠤᠬᠠᠭᠠᠨ᠂ ᠨᠠᠨᠳᠢᠨ ᠴᠢᠨᠠᠷ ᠵᠠᠶᠠᠭᠠᠰᠠᠨ ᠬᠦᠮᠦᠨ ᠬᠡᠭᠴᠢ ᠥᠭᠡᠷ᠎ᠡ ᠬᠣᠭᠣᠷᠣᠨᠳᠣ᠎ᠨ ᠠᠬᠠᠨ
    ᠳᠡᠭᠦᠦ ᠢᠨ ᠦᠵᠢᠯ ᠰᠠᠨᠠᠭᠠ ᠥᠠᠷ ᠬᠠᠷᠢᠴᠠᠬᠥ ᠤᠴᠢᠷ ᠲᠠᠢ᠃.
</label>

<label>
    <input type="radio" bind:group={scripts} value={135} />
    Wɔɑwo ɑdesɑmmɑ nyinɑɑ sɛ nnipɑ ɑ wɔwɔ ɑhofɑdi. Wɔn nyinɑɑ wɔ nidi ne kyɛfɑ koro.
    Wɔwɔ ɑdwene ne ɑhonim, nɑ ɛsɛ sɛ wobu wɔn ho wɔn ho sɛ ɑnuɑnom.
</label>

<label>
    <input type="radio" bind:group={scripts} value={136} />
    Doomi aadama yépp dañuy juddu, yam ci tawfeex ci sag ak sañ-sañ. Nekk na it ku
    xam dëgg te ànd na ak xelam, te war naa jëflante ak nawleem, te teg ko ci wàllu
    mbokk.
</label>

<label>
    <input type="radio" bind:group={scripts} value={137} />
    Semue orang ntu dilahirin bebas ame punye martabat dan hak-hak yang same. Mereka
    ntu dikasih akal ame ati nurani dan kudu bergaul satu ame lainnye dalem semangat
    persaudaraan.
</label>

<label>
    <input type="radio" bind:group={scripts} value={138} />
    Todo'l maga ser humano nace libre e igual en dignidad y maga derecho. Dotado
    con ellos el razon y conciencia y debe ellos comporta fraternalmente con el maga
    uno con el maga otro.
</label>

<label>
    <input type="radio" bind:group={scripts} value={139} />
    Evri man en mere olketa born frii en ikwol lo digniti en raits blo olketa. Olketa
    evriwan olketa garem maeni fo tingting en olketa sapos fo treatim isada wittim
    spirit blo bradahood.
</label>

<label>
    <input type="radio" bind:group={scripts} value={140} />
    လူတိုင်းသည် တူညီ လွတ်လပ်သော ဂုဏ်သိက္ခာဖြင့် လည်းကောင်း၊ တူညီလွတ်လပ်သော အခွင့်အရေးများဖြင့်
    လည်းကောင်း၊ မွေးဖွားလာသူများ ဖြစ်သည်။ ထိုသူတို့၌ ပိုင်းခြား ဝေဖန်တတ်သော ဉာဏ်နှင့်
    ကျင့်ဝတ် သိတတ်သော စိတ်တို့ရှိကြ၍ ထိုသူတို့သည် အချင်းချင်း မေတ္တာထား၍ ဆက်ဆံကျင့်သုံးသင့်၏။
</label>

<label>
    <input type="radio" bind:group={scripts} value={141} />
    人人生出嚟就係自由嘅，喺尊嚴同權利上一律平等。佢哋具有理性同良心，而且應該用兄弟間嘅關係嚟互相對待。
</label>

<label>
    <input type="radio" bind:group={scripts} value={142} />
    Monit hijan angbong kibi kethe kangtui kangdai pu ave. Arnam monit aphan kamathathek
    ajakong kipi. Lasi ning isivet pen dorapsi kachinghon chijinso pen donang ji.
</label>

<label>
    <input type="radio" bind:group={scripts} value={143} />
    人人生而自由﹐在尊嚴和權利上一律平等。他們賦有理性和良心﹐並應以兄弟關係的精神互相對待。
</label>

<label>
    <input type="radio" bind:group={scripts} value={144} />
    Wičháša na wíŋyaŋ otóiyohi iglúhapi na iyéhaŋyaŋ wówažapi. Tȟaŋmáhel slol'íč'iyapi
    na kičhíwičhowepi s'e kičhíčhuwapi kta héčha.
</label>

<label>
    <input type="radio" bind:group={scripts} value={145} />
    เราทุกคนเกิดมาอย่างอิสระ เราทุกคนมีความคิดและความเข้าใจเป็นของเราเอง เราทุกคนควรได้รับการปฏิบัติในทางเดียวกัน.
</label>

<label>
    <input type="radio" bind:group={scripts} value={146} />
    بوتون اينسانلار حيثييت و حاقلار باخيميندان دنك و اركين دوغولارلار.اوس و اويات
    ييهﺳﻴﺪيرلر و بير بيرلرينه قارشى قارداشليق روحو ايله داوراماليدرلار.
</label>

<label>
    <input type="radio" bind:group={scripts} value={147} />
    Бардык адамдар өз беделинде жана укуктарында эркин жана тең укуктуу болуп жаралат.
    Алардын аң -сезими менен абийири бар жана бири-бирине бир туугандык мамиле кылууга
    тийиш.
</label>

<label>
    <input type="radio" bind:group={scripts} value={148} />
    Bütün insanlar hür, haysiyet ve haklar bakımından eşit doğarlar. Akıl ve vicdana
    sahiptirler ve birbirlerine karşı kardeşlik zihniyeti ile hareket etmelidirler.
    | بتون انسانلر حر، حيشيت و حقلر باقمڭدن اشت طوغرلر. عقل و وجدانه صحبترلر و بربرلرينه
    قارشو قرداشلق ذهنيت ايله حركت اتمهلودرلر.
</label>

<label>
    <input type="radio" bind:group={scripts} value={149} />
    Хемме адамлар өз мертебеси ве хукуклары бюнча дең ягдайда дүнйә инйәрлер.Олара
    аң хем выждан берлендир ве олар бир-бирлери билен доганлык рухундакы гарайышда
    болмалыдырлар.
</label>

<label>
    <input type="radio" bind:group={scripts} value={150} />
    ﮬﻪﻣﻤﻪ ئادەم زاﻧﯩﺪﯨﻨﻼ ﺋﻪﺭﻛﯩﻦ، ﺋﯩﺰﺯﻩﺕ-ھۆرﻣﻪت ۋە ھوقۇقتا باپباراۋەر بولۇپ تۇغۇلغان.
    ئۇلار ﺋﻪﻗﯩﻠﮕﻪ ۋە ۋﯨﺠﺪﺍﻧﻐﺎ ﺋﯩﮕﻪ ﮬﻪﻣﺪﻩ ﺑﯩﺮ-ﺑﯩﺮﯨﮕﻪ ﻗﯧﺮﯨﻨﺪﺍﺷﻠﯩﻖ ﻣﯘﻧﺎﺳﯩﯟﯨﺘﯩﮕﻪ ﺧﺎﺱ
    ﺭﻭﮪ ﺑﯩﻠﻪﻥ ﻣﯘﺋﺎﻣﯩﻠﻪ ﻗﯩﻠﯩﺸﻰ ﻛﯧﺮەك.
</label>

<label>
    <input type="radio" bind:group={scripts} value={151} />
    H̡əmmə adəm zatidinla ərkin, izzət-h̡ɵrmət wə hok̡uk̡ta babbarawər bolup tuƣulƣan.
    Ular ək̡ilƣə wə wijdanƣa igə h̡əmdə bir-birigə k̡erindaxlik̡ munasiwitigə hax roh
    bilən mu’amilə k̡ilixi kerək.
</label>

<label>
    <input type="radio" bind:group={scripts} value={152} />
    Kõik inimesed sünnivad vabadena ja võrdsetena oma väärikuselt ja õigustelt. Neile
    on antud mõistus ja südametunnistus ja nende suhtumist üksteisesse peab kandma
    vendluse vaim.
</label>

<label>
    <input type="radio" bind:group={scripts} value={153} />
    Kaikki ihmiset syntyvät vapaina ja tasavertaisina arvoltaan ja oikeuksiltaan.
    Heille on annettu järki ja omatunto, ja heidän on toimittava toisiaan kohtaan
    veljeyden hengessä.
</label>

<label>
    <input type="radio" bind:group={scripts} value={154} />
    Minden emberi lény szabadon születik és egyenlő méltósága és joga van. Az emberek,
    ésszel és lelkiismerettel bírván, egymással szemben testvéri szellemben kell
    hogy viseltessenek.
</label>

<label>
    <input type="radio" bind:group={scripts} value={155} />
    Amād rovzt attõ sindõnd brīd ja īdlizt eņtš vǟrtitõks ja õigiztõks. Näntõn um
    andtõd mūoštõks ja sidāmtundimi, ja näntõn um īdtuoisõ tuoimõmõst veļkub vaimsõ.
</label>

<label>
    <input type="radio" bind:group={scripts} value={156} />
    Buot olbmot leat riegádan friddjan ja olmmošárvvu ja olmmošvuoigatvuođaid dáfus
    . Sii leat jierbmalaš olbmot geain lea oamedovdu ja sii gálggaše leat dego vieljačagat.
</label>

<!-- <h2 class="w-fit place-self-center mt-20">
    Importing audio from local audio file
</h2>
<audio controls preload="metadata">
    <source src={udhr_001} type="audio/mp3" />
</audio>

<h2 class="w-fit place-self-center mt-20">
    Importing audio from online audio file
</h2>
<audio controls preload="metadata">
    <source
        src="https://www.omniglot.com/soundfiles/udhr/udhr_so.mp3"
        type="audio/mp3"
    />
</audio>

<h2 class="w-fit place-self-center mt-20">
    Importing audio from base64 encoding in JSON file
</h2>

<audio controls preload="metadata">
    <source src={audio_json} type="audio/mp3" />
</audio>

<h2 class="w-fit place-self-center mt-20">
    Importing audio from base64 encoding in API
</h2> -->

<!-- Note: no need for an #each loop when calling API ending in `/1` -->
<!-- <p>id: {data_api.id} | name: {data_api.name} | script: {data_api.script}</p> -->
<!-- <div>
    {#await data_api then d}
        <audio
            controls
            preload="metadata"
            src={`data:audio/mp3;base64,${d.audio}`}
        />
    {/await}
</div> -->

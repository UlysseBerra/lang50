<script lang="ts">
</script>

<svelte:head>
    <title>Log in</title>
    <meta name="description" content="Authentication" />
</svelte:head>

<div class="text-column">
    <h1>Log in & Sign up</h1>

    <div class="card flex-shrink-0 w-full max-w-sm bg-base-100 text-center">
        <div class="card-body">
            <div class="form-control">
                <!-- svelte-ignore a11y-label-has-associated-control -->
                <label class="label">
                    <span class="label-text">Email</span>
                </label>
                <input
                    type="text"
                    placeholder="Your email address?"
                    class="input input-bordered text-center"
                />
            </div>
            <div class="form-control">
                <!-- svelte-ignore a11y-label-has-associated-control -->
                <label class="label">
                    <span class="label-text">Password</span>
                </label>
                <input
                    type="text"
                    placeholder="Your password?"
                    class="input input-bordered text-center"
                />
                <!-- svelte-ignore a11y-label-has-associated-control -->
                <label class="label">
                    <a href="." class="label-text-alt link link-hover"
                        >Forgot password?</a
                    >
                </label>
            </div>
            <div class="form-control mt-6">
                <button class="btn btn-primary">Log in</button>
            </div>
        </div>
    </div>
</div>

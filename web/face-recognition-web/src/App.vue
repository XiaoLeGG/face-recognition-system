<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
    <div class="main">
        <header>
            <div class="wrapper">    
                <a href="https://github.com/serengil/deepface/tree/master" target="_blank" class="logo-a">
                    <img src="./assets/logo.png" alt="logo" class="logo"/>
                    <h1>
                        DeepFace Recognition
                    </h1>
                </a>
                <nav>
                    <RouterLink to="/">About</RouterLink>
                    <RouterLink to="/register">Register</RouterLink>
                    <RouterLink to="/recognize">Recognize</RouterLink>
                    <RouterLink to="/verify">Verify</RouterLink>
                    <RouterLink to="/analyze">Analyze</RouterLink>
                </nav>
            </div>
        </header>
        <div class="body">
            <RouterView />
        </div>
    </div>
</template>

<style scoped>

.main {
    display: flex;
    justify-items: flex-start;
    flex-direction: column;
}

.logo-a {
    display: flex;
    align-items: center;
    gap: 2vh;
    justify-content: start;
}
.logo-a:hover {
    background-color: transparent;
    opacity: 0.5;
}

h1 {
    font-size: 5vh;
    color: var(--color-heading);
    flex-basis: max-content;
}

.logo {
    height: 8vh;
    width: auto;
    background-color: var(--color-background-soft);
    border-radius: 10%;
}

nav {
    display: flex;
    text-align: center;
    font-size: 3vh;
    flex-grow: 1;
    justify-content: end;
}

nav a.router-link-exact-active {
    color: var(--color-text);
}

nav a.router-link-exact-active:hover {
    background-color: transparent;
    opacity: 1;
}

nav a {
    display: inline-block;
    padding: 0 1rem;
    border-left: 1px solid var(--color-border);
    color: var(--color-heading);
}

nav a:hover {
    background-color: transparent;
    opacity: 0.7;
}

nav a:first-of-type {
    border: 0;
}

header {
    width: 100%;
    background-color: var(--color-background);
    padding: 1rem 1rem 1rem 1rem;
    position: fixed;
    z-index: 2002;
    top: 0;
    caret-color: transparent;
    user-select: none;
    border-bottom: 1px solid var(--color-border);

}

.body {
    margin-top: 11vh;
    padding: 5rem 5rem 5rem 5rem;
}

header .wrapper {
    display: flex;
    justify-content: start;
    align-items: center;
    gap: 2vh;
    width: 100%;
}
</style>

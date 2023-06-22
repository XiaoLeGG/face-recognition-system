<template>
  <div class="about">
    <h1>Welcome to DeepFace Recognition System</h1>
    <h2>This system is for simple face recognition application based on <a href="https://github.com/serengil/deepface/tree/master" target="_blank" rel="noopener">DeepFace</a>.</h2>
    <h2>You can access our system source code at <a href="https://github.com/XiaoLeGG/face-recognition-system" target="_blank">Github</a></h2>
  </div>
</template>

<style scoped>
.about {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 20vh;
}

.about > h1 {
    font-size: 5vh;
    color: var(--color-heading);
    flex-basis: max-content;
}

.about > h2 {
    font-size: 3vh;
    flex-basis: max-content;
}

</style>

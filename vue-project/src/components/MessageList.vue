<template>
    <ul>
        <li v-for="msg in messages" :key="msg">{{ msg }}</li>
    </ul>
</template>

<script setup>
defineProps({ messages: Array })
</script>

<script setup>
import { ref, onMounted, onUnmounted } from "vue";
import { connect, StringCodec } from "nats.ws";
import axios from 'axios';
import { useRoute } from 'vue-router'
import { geoStore } from "../stores/geo";
import {fetchGeo, updateColor} from "../services/api"
import {connectToNats} from "../services/nats"

const status = ref("déconnecté");
let nc = null;

const route = useRoute()
const username = route.params.username

async function connectNats() {
    status.value = "connexion en cours...";
    await connectToNats()
    status.value = "connecté";
}

onMounted(async () => {
    await fetchGeo();
    await connectNats();
});

onUnmounted(async () => {
    if (nc) {
        await nc.drain();
        nc = null;
    }
});
</script>


<template>
  <div>
    <h1>Dashboard de {{ username }}</h1>
    <h2>Geo List</h2>
    <ul>
      <li v-for="geo in geoStore.list" :key="geo.name">
        <span>{{ geo.name }} : </span>
        <input type="text" v-model="geo.color" />
        <button @click="updateColor(geo.name, geo.color)">Update</button>
      </li>
    </ul>
    <p>Status NATS : {{ status }}</p>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from "vue";
import MessageList from "../components/MessageList.vue"
import {sendDataToApi} from "../services/api"
import {connectToNats} from "../services/nats"
import { ChannelStore, Channel } from "../stores/channel"
import { MessageStore } from "../stores/message"
import {AddressbookStore} from "../stores/addressbook"
import {UserStore} from "../stores/user"
import { useRoute } from 'vue-router'

const status = ref("déconnecté");
let nc = null;
const route = useRoute()
const username = route.params.username
const messagesStore = MessageStore()


async function connectNats() {
    status.value = "connexion en cours...";
    for (const channel of ChannelStore.list)
    {
        console.log(`subscribing to ${channel.name}`)
        await connectToNats(channel.name, channel.handler, username)
    }
    status.value = "connecté";
}

onMounted(async () => {
    console.log(messagesStore.messages)
    const addressbook = AddressbookStore()
    const user = UserStore()
    ChannelStore.list.push(new Channel("addressbook", addressbook.handlerAddressBook))
    ChannelStore.list.push(new Channel(`user/${username}`, user.handlerUser))

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
      <div>
        <button @click="sendDataToApi(event={'event':'addressbook'})">addressbook</button>
      </div>
      <div>
        <p>user :  {{ username }}</p>
        <button @click="sendDataToApi(event={'event':'user', 'sender':username})">user</button>
      </div>
      <p>Status NATS : {{ status }}</p>
      <MessageList :messages="messagesStore.messages" />
    </div>
  </template>

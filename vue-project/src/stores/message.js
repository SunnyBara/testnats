import { defineStore } from "pinia"
import { ref } from "vue"

export const MessageStore = defineStore("message", () => {
    const messages = ref([])

    function addMessage(msg) {
        messages.value.push(msg)
    }

    function clearMessages() {
        messages.value = []
    }

    return { messages, addMessage, clearMessages }
})

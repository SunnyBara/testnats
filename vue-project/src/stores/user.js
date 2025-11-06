import { defineStore } from "pinia"
import { MessageStore } from "./message"

export const UserStore = defineStore("user", () => {

    function handlerUser(msg) {
        const messages = MessageStore()
        messages.addMessage(msg.message)
    }

    return { handlerUser }
})

import { defineStore } from "pinia"
import { MessageStore } from "./message"

export const AddressbookStore = defineStore("addressbook", () => {

    function handlerAddressBook(msg) {
        const messages = MessageStore()
        messages.addMessage(msg.message)
    }

    return { handlerAddressBook }
})

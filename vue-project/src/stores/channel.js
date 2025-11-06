import { reactive } from 'vue'
import { AddressbookStore } from './addressbook';

export class Channel {
    constructor(name, handler) {
        this.name = name
        this.handler = handler
    }
}
export const ChannelStore = reactive({
    list: [],

})

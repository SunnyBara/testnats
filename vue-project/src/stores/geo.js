import { reactive } from 'vue'

export const geoStore = reactive({
    list: [],

    setList(data) {
        this.list = data
    },

    updateColor(name, color) {
        const geo = this.list.find(g => g.name === name)
        if (geo) geo.color = color
    }
})

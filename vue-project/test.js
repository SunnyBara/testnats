import { ref } from 'vue'
import { connect, StringCodec } from "nats.ws";

const status = ref("déconnecté");
const isConnected = ref(false);
const messages = ref([]);

async function test() {
    const nc = await connect({ servers: "wss://demo.nats.io:8443" });

    const sc = StringCodec();

    const sub = nc.subscribe("foo");
    (async () => {
        for await (const m of sub) {
            const msg = sc.decode(m.data);
            console.log(`[${sub.getProcessed()}]: ${msg}`);
            messages.value.push(msg);
        }
        console.log("subscription closed");
    })();
    await nc.flush();

    status.value = "connecté";
    isConnected.value = true;
}

test()

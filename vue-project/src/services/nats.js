import { connect, StringCodec } from "nats.ws"
import { geoStore } from '../stores/geo.js'

let nc = null

export async function connectToNats(channelName, handler, username) {
    // const auth = await fetch("http://127.0.0.1:8000/nats/auth/", {
    //     credentials: "include"
    // }).then(r => r.json())

    // if (!auth.jwt) throw new Error("Unauthorized to access NATS")

    const nc = await connect({
        servers: "ws://localhost:9222",
        user: "a",
        password: "pwd1"
    })

    const sc = StringCodec();
    const sub = nc.subscribe(channelName);
    (async () => {
        for await (const m of sub) {
            const data = sc.decode(m.data)
            const dataParsed = JSON.parse(data);
            console.log(dataParsed)
            handler(dataParsed)
        }
    })();

    await nc.flush();
}

export async function disconnectNats() {
    if (nc) {
        await nc.drain()
        nc = null
    }
}

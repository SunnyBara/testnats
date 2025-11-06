import { geoStore } from '../stores/geo.js'

const API_BASE = 'http://127.0.0.1:8000'

export async function login(username, password) {
    const res = await fetch(`${API_BASE}/login/`, {
        method: 'POST',
        credentials: 'include', // ⬅️ important pour envoyer/recevoir les cookies
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
    })

    if (!res.ok) {
        console.error('Login failed', res.status, await res.text())
        throw new Error(`HTTP ${res.status}`)
    }

    const data = await res.json()
    console.log('login response', data)
    return data
}


export async function sendDataToApi(event) {
    const res = await fetch(`${API_BASE}/endpoint/`, {
        method: 'POST',
        credentials: 'include', // ⬅️ cookies inclus ici aussi
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ event }),
    })

    if (!res.ok) {
        console.error('endpoint failed', res.status, await res.text())
        throw new Error(`HTTP ${res.status}`)
    }

    const data = await res.json()
    console.log('endpoint response', data)
    return data
}


export async function fetchGeo() {
    const res = await fetch(`${API_BASE}/geo/`, {
        method: 'GET',
        credentials: 'include',
    })

    if (!res.ok) {
        console.error('geo fetch failed', res.status, await res.text())
        throw new Error(`HTTP ${res.status}`)
    }

    const data = await res.json()
    geoStore.setList(data.data)
}

export async function updateColor(name, color) {
    const res = await fetch(`${API_BASE}/geo/update/`, {
        method: 'POST',
        credentials: 'include',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name, color }),
    })

    if (!res.ok) {
        console.error('updateColor failed', res.status, await res.text())
        throw new Error(`HTTP ${res.status}`)
    }
}


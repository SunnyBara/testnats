<template>
    <div class="text-center">
      <h1>Connexion</h1>
      <form @submit.prevent="handleLogin" class="mt-4">
        <input v-model="username" placeholder="username" /><br />
        <input v-model="password" type="password" placeholder="password" /><br />
        <button type="submit">Connect</button>
      </form>
      <p v-if="error" class="text-red-500">{{ error }}</p>
    </div>
  </template>

  <script setup>
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  import { login as apiLogin } from '../services/api'

  const username = ref('')
  const password = ref('')
  const error = ref('')
  const router = useRouter()

  async function handleLogin() {
      try {
         await apiLogin(username.value, password.value)
          router.push(`/test/${username.value}`)
      } catch {
          error.value = 'Identifiants invalides'
      }
  }
  </script>

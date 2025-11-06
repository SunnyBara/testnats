import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'
import Dashboard from '../views/Dashboard.vue'
import Test from '../views/Test.vue'

const routes = [
    { path: '/', component: Login },
    { path: '/dashboard/:username', component: Dashboard, props: true },
    { path: '/test/:username', component: Test }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

router.beforeEach((to, from, next) => {
    const isAuthenticated = !!localStorage.getItem('token')
    if (to.path.startsWith('/test') && !isAuthenticated) {
        next('/')
    } else {
        next()
    }
})

export default router

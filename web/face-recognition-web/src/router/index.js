import { createRouter, createWebHistory } from 'vue-router'
import AboutView from '../views/AboutView.vue'
import RegisterView from '../views/RegisterView.vue'
import RecognizeView from '../views/RecognizeView.vue'
import VerifyView from '../views/VerifyView.vue'
import AnalyzeView from '../views/AnalyzeView.vue'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'about',
            component: AboutView
        },
        {
            path: '/register',
            name: 'register',
            component: RegisterView
        },
        {
            path: '/recognize',
            name: 'recognize',
            component: RecognizeView
        },
        {
            path: '/verify',
            name: 'verify',
            component: VerifyView
        },
        {
            path: '/analyze',
            name: 'analyze',
            component: AnalyzeView
        }
    ]
})

export default router

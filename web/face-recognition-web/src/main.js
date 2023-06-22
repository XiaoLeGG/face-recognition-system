import './assets/main.css'

import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import 'element-plus/theme-chalk/dark/css-vars.css'
import App from './App.vue'
import router from './router'
import { useDark, useToggle } from '@vueuse/core'
import { ElMessage, ElMessageBox } from 'element-plus'


// There is a small bug which causes the ElMessage does not immediately show up for the first time
ElMessage({
    message: 'Welcome to Face Recognition System',
    type: 'success',
    duration: 1
})

const isDark = useDark()
const toggleDark = useToggle(isDark)

const app = createApp(App)

app.use(ElementPlus)
app.use(router)

app.mount('#app')

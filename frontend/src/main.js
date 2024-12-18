import { createApp } from 'vue'
import App from './App.vue'

import axios from 'axios'

import ElementPlus from 'element-plus'

import 'element-plus/dist/index.css'

import { Plus, Delete, ChatSquare, ArrowDown } from '@element-plus/icons-vue'

import "./assets/css/global.css"


const app = createApp(App)

app.use(ElementPlus)
app.mount('#app')
app.config.globalProperties.$http = axios

app.component(Plus.name, Plus)
app.component(Delete.name, Delete)
app.component(ChatSquare.name, ChatSquare)
app.component(ArrowDown.name, ArrowDown)

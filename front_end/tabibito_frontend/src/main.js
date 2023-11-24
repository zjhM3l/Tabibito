import { createApp } from 'vue'
import App from './App.vue'
import router from "./router.js";
import {createPinia} from "pinia";
import naive from 'naive-ui'
import Toast from 'vue-toastification'
import 'vue-toastification/dist/index.css'
import { createI18n } from 'vue-i18n'
import enLocale from './i18n/en.js'
import zhLocale from './i18n/zh.js'
import axios from 'axios'




const app = createApp(App);
const pinia = createPinia();
axios.defaults.baseURL = 'http://127.0.0.1:5000';
axios.defaults.withCredentials = true;
// http://127.0.0.1:5137
// http://127.0.0.1:4523/m1/2418665-0-default
app.config.globalProperties.axios = axios;
app.config.globalProperties.$myApp = app;

const i18n = createI18n({
    locale: 'en',
    messages: {
        en: enLocale,
        zh: zhLocale
    },
    legacy: false
})
app.use(router);
app.use(pinia);
app.use(Toast);
app.use(i18n);
app.use(naive);
app.mount('#app')



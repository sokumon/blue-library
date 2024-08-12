// import './assets/main.css'
import './index.css'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import VueSweetalert2 from 'vue-sweetalert2';
import 'sweetalert2/dist/sweetalert2.min.css';



const app = createApp(App)
app.use(VueSweetalert2);
app.config.globalProperties.base_url = "http://localhost:5000"
app.use(router)

app.mount('#app')

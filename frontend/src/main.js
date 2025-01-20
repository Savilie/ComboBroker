import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

const clickOutside = {
  beforeMount: (el, binding) => {
      el.clickOutsideEvent = event => {
          if (!(el == event.target || el.contains(event.target))) {
              binding.value();
          }
      };
      document.addEventListener("click", el.clickOutsideEvent);
  },
  unmounted: el => {
      document.removeEventListener("click", el.clickOutsideEvent);
  },};

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
app.directive("click-outside", clickOutside)

import './assets/main.css'
import 'vue-final-modal/style.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { createVfm } from 'vue-final-modal'
import { useFeedbackStore } from './stores/form'

import App from './App.vue'
import router from './router'

const clickOutside = {
  beforeMount: (el, binding) => {
    el.clickOutsideEvent = (event) => {
      if (!(el == event.target || el.contains(event.target))) {
        binding.value()
      }
    }
    document.addEventListener('click', el.clickOutsideEvent)
  },
  unmounted: (el) => {
    document.removeEventListener('click', el.clickOutsideEvent)
  },
}

const app = createApp(App)
const vfm = createVfm()
app.use(createPinia())
app.use(router)

app.use(vfm).mount('#app')
app.directive('click-outside', clickOutside)

const store = useFeedbackStore()

export function changeNumber(number) {
  if (number.length < 15) {
    store.number = ''
  } else {
    store.number = '+7' + number
    console.log(store.number)
  }
}

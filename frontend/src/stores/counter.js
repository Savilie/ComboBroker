
import { defineStore } from 'pinia'
import axios from 'axios'

export const useFeedbackStore = defineStore('feedback', {
  state: () => {
    return { number: '', numberModal: '' , theme: 'Консультация по кредиту', preferedMessanger: 'WhatsApp' }
  },
  actions: {
    request(){
      console.log(this.number)
      if(this.number) {
        axios.post('https://xn--90aamrcjncbtd.xn--p1ai/api/feedback/', {number: this.number, theme: this.theme, messenger: this.preferedMessanger})
        .then(response => {console.log(response)
          alert('Спасибо за обращение! С вами свяжутся в течении суток')
        })
        .catch(error => console.log(error))
      } else {
        alert('Проверьте правильность написания номера телефона')
      }
    },
    requestModal(){
      console.log(this.numberModal)
      if(this.numberModal) {
        axios.post('https://xn--90aamrcjncbtd.xn--p1ai/api/feedback/', {number: this.numberModal, theme: this.theme, messenger: this.preferedMessanger})
        .then(response => {console.log(response)
          alert('Спасибо за обращение! С вами свяжутся в течении суток')
        })
        .catch(error => console.log(error))
      }else {
        alert('Проверьте правильность написания номера телефона')
      }
    }
  }
})


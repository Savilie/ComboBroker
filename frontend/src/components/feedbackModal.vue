<script setup>
import { VueFinalModal } from 'vue-final-modal'
import MaskInputComponent from '../../node_modules/my-mask-library/src/MaskInput.vue'
import radioButton from '@/components/RadioButton.vue'
import customSelect from '@/components/customSelect.vue'
import { useFeedbackStore } from '../stores/form.js'
import { ref } from 'vue'
defineProps({
  title: String,
})

const emit = defineEmits({
  e: 'confirm',
})
const maskedValue = ref('')
const store = useFeedbackStore()
function changeNumber() {
  if (maskedValue.value.length < 15) {
    store.numberModal = ''
  } else {
    store.numberModal = '+7' + maskedValue.value
  }
  console.log(store.numberModal)
}
function POSTrequest() {
  store.requestModal()
}
</script>

<template>
  <VueFinalModal
    class="confirm-modal"
    content-class="confirm-modal-content"
    overlay-transition="vfm-fade"
    content-transition="vfm-fade"
  >
    <div class="form-container-end">
      <h2>{{ title }}</h2>
      <div class="container-number">
        <h3>Номер телефона</h3>
        <div class="number-form">
          <h4 style="color: #fff; font-weight: normal">+7</h4>
          <MaskInputComponent
            @change="changeNumber"
            style="color: #fff; font-weight: normal; font-size: 18px"
            v-model="maskedValue"
            mask="(###) ###-##-##"
            type="text"
            className="masked-input"
          />
        </div>
      </div>
      <div class="">
        <h3>Тема вопроса</h3>
        <customSelect :options="['по кредиту', 'по ипотеке', 'по лечению кредитной истории', 'по бизнес кредитованию', 'по займу под залог недвижимости', 'другое']" />
      </div>
      <div class="container-number">
        <h3>Где вам удобнее общаться?</h3>
        <radioButton />
      </div>
      <!-- <button id="form-button" @click="emit('confirm')">Оставить заявку</button> -->
      <button id="form-button" @click="POSTrequest">Оставить заявку</button>
    </div>
  </VueFinalModal>
</template>

<style>
#form-button:hover {
  cursor: pointer;
}
.confirm-modal {
  display: flex;
  justify-content: center;
  align-items: center;
}
.confirm-modal-content {
  display: flex;
  flex-direction: column;
  border-radius: 0.5rem;
}
.confirm-modal-content > * + * {
  margin: 0.5rem 0;
}
.confirm-modal-content h1 {
  font-size: 1.375rem;
}
.dark .confirm-modal-content {
  background: #000;
}
</style>

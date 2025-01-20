<script setup>
import { ref } from 'vue'
import MaskInputComponent from '../../node_modules/my-mask-library/src/MaskInput.vue'
const maskedValue = ref('')
const questions = ref([
  {
    question: 'Какой тип недвижимости вас интересует',
    answers: [
      { id: 1, type: 'Первичка (новостройка, таунхаус, ДДУ, цессия)' },
      { id: 2, type: 'Вторичка (готовая квартира, дом, таунхаус от физ. лица)' },
      { id: 3, type: 'ИЖС (строительство дома)' },
      { id: 4, type: 'Коммерция' },
      { id: 5, type: 'Земельный участок' },
      { id: 6, type: 'Гараж/паркинг/машиноместо' },
    ],
  },
  {
    question: 'Стоимость обекта',
    range: 1000000,
    price: 100000,
  },
  {
    question: 'Первый взнос',
    range: 1000000,
    price: 100000,
  },
  {
    question: 'Тип программы',
    answers: [
      { id: 1, type: 'Стандарт (базовая)(базовая пониженная)' },
      { id: 2, type: 'Семейная ипотека' },
      { id: 3, type: 'Без подтверждения дохода' },
      { id: 4, type: 'Сельская ипотека' },
      { id: 5, type: 'IT ипотека' },
      { id: 6, type: 'Военная ипотека' },
      { id: 7, type: 'Дальневосточная/Арктическая ипотека' },
      { id: 8, type: 'Исламская ипотека' },
      { id: 9, type: 'Рефинансирование' },
    ],
  },
  {
    question: 'В каком регионе покупается недвижимость',
    cityVal: 'Москва',
    city: null,
  },
])
const currentPosition = ref(0)
const currentQuestion = ref(questions.value[currentPosition.value])

const result = ref([])

const selected = ref({
  button: null,
})
function logs(e) {
  if (selected.value.button) {
    selected.value.button.classList.remove('active')
  }

  e.target.classList.add('active')
  selected.value.button = e.target
}
const isQuizEnded = ref(false)
const rangeMax = ref(20000000)
function nextQuestion() {
  if (selected.value.button) {
    result.value.push(selected.value.button.innerHTML)
  } else if (currentQuestion.value.range) {
    result.value.push(currentQuestion.value.price)
    rangeMax.value = currentQuestion.value.price
    console.log(currentQuestion.value)
  } else if (currentQuestion.value.city) {
    result.value.push(currentQuestion.value.city)
  } else {
    currentPosition.value--
    alert('Выберите вариант')
  }
  console.log(currentQuestion.value)
  if (currentPosition.value < questions.value.length - 1) {
    currentPosition.value++
    currentQuestion.value = questions.value[currentPosition.value]
  } else {
    isQuizEnded.value = true
  }

  selected.value.button = null
  console.log(result.value)
}

function changer() {
  console.log(currentQuestion.value.price)
}

function addNumber() {
  if (maskedValue.value.length < 15) {
    document.querySelector('.number').style.transitionDuration = '0.2s'
    document.querySelector('.number').style.border = '1px solid #FF0000'
  } else {
    alert('Спасибо за прохождение опроса! С вами свяжутся в течении суток')
    result.value.push('+7' + maskedValue.value)
    console.log(result.value)
    document.querySelector('.number').style.transitionDuration = '0.2s'
    document.querySelector('.number').style.border = '1px solid #00FF26'
  }
}
</script>
<template>
  <div class="quiz" v-if="!isQuizEnded">
    <div class="header">
      <h1>{{ currentQuestion.question + '?' }}</h1>
    </div>
    <div v-if="currentQuestion.answers" class="questions">
      <button
        @click="logs($event)"
        v-for="question in currentQuestion.answers"
        class="question"
        :key="question.type"
        :id="question.id"
      >
        {{ question.type }}
      </button>
    </div>
    <div style="overflow: hidden" class="questions" v-else-if="currentQuestion.range">
      <div class="cont">
        <input
      class="number-input"
        type="number"
        step="100000"
        min="1000000"
        max="20000000"
        value="1000000"
        v-model="currentQuestion.price"
      />
      <input
      class="number-range"
        @change="changer"
        step="100000"
        type="range"
        min="1000000"
        :max="rangeMax"
        v-model="currentQuestion.price"
      />
      </div>

    </div>
    <div class="questions" style="overflow: hidden" v-else>
      <input class="number-input" type="text" placeholder="Введите город" v-model="currentQuestion.city" />
    </div>
    <div class="question" style="background-color: #5298ff; color: #fff" @click="nextQuestion">
      Следующий вопрос
    </div>
  </div>

  <div class="quiz" v-if="isQuizEnded">
    <header class="header">
        <h1>Осталось совсем немного, оставьте ваш номер телефона, чтобы мы смогли помочь вам</h1>
      </header>
    <div class="questions" style="justify-content: space-between; align-items: center; overflow: hidden; height:557px; margin-top: 0; padding-top: 0;">

      <div class="number" style="margin-top: 10px;">
        <h4>+7</h4>
        <MaskInputComponent
          v-model="maskedValue"
          mask="(###) ###-##-##"
          type="text"
          className="masked-input"
        />
      </div>
      <div class="question" style="background-color: #5298ff; color: #fff" @click="addNumber">Получить консультацию</div>
    </div>
  </div>
</template>

<style>
.cont {
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 0px;
}
input[type="range"]::range-progress{
  background-color: #000000;
  border-radius: 10px;
  height: 20px;
  width: 100%;
  box-shadow: 0 0 4px #5298ff

}
.number-range {
  border: 0;
  position: absolute;
  top: 20px;
  left: 0;
  width: 100%;
  height: 100%;
  cursor: pointer;
}
.number-input {
  width: 49vw;
  height: 20px;
  border: 1px solid #c6dcff;
  background-color: #ffffff;
  color: #000000;
  border-radius: 8px;
  padding: 10px;
  font-size: 16px;
}
.number-input:focus {
  width: 49vw;
  height: 20px;
  border: 1px solid #c6dcff;
  background-color: #ffffff;
  color: #000000;
  border-radius: 8px;
  padding: 10px;
  font-size: 16px;
}
.header {
  margin-top: 50px;
  width: 50vw;
  gap: 20px;
  margin-bottom: 20px;
}
.header h1 {
  font-size: 25px;
  color: #3359fd;
}
textarea:focus,
input:focus {
  outline: none;
}
.invalid {
  transition-duration: 0.2s;
  border: 1px solid rgb(141, 33, 33);
}
.number {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  border: 1px solid #c6dcff;
  border-radius: 8px;
  gap: 5px;
  padding: 10px;
  width: 20vw;
}
h4 {
  font-size: 16px;
  color: #5298ff;
}
.masked-input {
  width: 20vw;
  border: 0;
  padding: 0;
  margin: 0;
  font-size: 15px;
  background-color: #ececec00;
  font-weight: bold;
  color: #5298ff;
  overflow: none;
}
.select {
  user-select: none;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 50px;
  padding-left: 15px;
  padding-right: 50px;
  border-radius: 7px;
  background-color: #f1f1f100;
  border: 1px solid #353535;
}
.select:hover {
  cursor: pointer;
}
input::-webkit-calendar-picker-indicator {
  display: none;
}
.quiz {
  padding-left: 60px;
  padding-right: 60px;
  padding-top: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 60vw;
  padding-bottom: 40px;
  background-color: #ffffff;
  border: 1px solid #c8ddff;
  border-radius: 10px;
}

.questions::-webkit-scrollbar {
  width: 10px;
}

.questions::-webkit-scrollbar-track {
  -webkit-box-shadow: 5px 5px 5px -5px rgba(34, 60, 80, 0.2) inset;
  background-color: #f9f9fd;
  border-radius: 10px;
}

.questions::-webkit-scrollbar-thumb {
  border-radius: 10px;
  background: linear-gradient(180deg, #00c6fb, #005bea);
}

.questions {
  padding-top: 10px;
  padding-bottom: 10px;
  padding-right: 10px;
  padding-left: 10px;
  margin-left: 9px;
  margin-bottom: 10px;
  display: contents;
  overflow-y: scroll;
  height: 400px;
  margin-top: 20px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.question {
  box-shadow: 0px 3px 6px #c6dcff;
  display: flex;
  justify-content: center;
  font-size: 15px;
  cursor: pointer;
  user-select: none;
  transition-duration: 0.1s;
  font-weight: normal;
  color: #282828;
  background-color: #fff;
  border: 0px;
  padding-top: 20px;
  padding-bottom: 20px;
  border-radius: 7px;
  width: 50vw;
}
.active {
  box-shadow: 0px 3px 10px 1px #4189fd;
  background-color: #5298ff;
  color: #fff;
  transition-duration: 0.2s;
}
</style>

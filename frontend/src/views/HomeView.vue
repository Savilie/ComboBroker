<script setup>
import HeaderMain from '../components/HeaderMain.vue'
import QuizComponent from '@/components/QuizComponent.vue'
import MaskInputComponent from '../../node_modules/my-mask-library/src/MaskInput.vue'
import customSelect from '@/components/customSelect.vue'
import radioButton from '@/components/RadioButton.vue'
// Import Swiper Vue.js components
import { Swiper, SwiperSlide } from 'swiper/vue'
import { ref, onMounted } from 'vue'

// Import Swiper styles
import 'swiper/css'

const maskedValue = ref('')

const onSwiper = (swiper) => {
  console.log(swiper)
}
const onSlideChange = () => {
  console.log('slide change')
}
const slidePerView = ref(4)

onMounted(() => {
  if(window.innerWidth < 1500 && window.innerWidth > 500) {
    slidePerView.value = 3
  } else if(window.innerWidth < 1800 && window.innerWidth > 1500) {
    slidePerView.value = 4
  } else {
    slidePerView.value = 1
  }
})
window.addEventListener('resize', () => {
  if(window.innerWidth < 1500) {
    slidePerView.value = 3
  } else {
    slidePerView.value = 4
  }
} )
</script>

<template>
  <main>
    <div class="block1-container">
      <div class="block1-content">
        <HeaderMain />
        <div class="block1">
          <div class="Help_in_obligation_container">
            <div class="text_container">
              <h1 class="Help_in_obligation">
                Помощь в одобрении ипотеки и сопровождение сделки до результата<span class="dot"
                  >.</span
                >
              </h1>

              <p class="Help_in_obligation_p">
                Помогли одобрить и получить более 200 000 000 руб. за последний год
              </p>

              <button class="standard-button"><p>Получить консультацию</p></button>
            </div>
            <div class="img">
              <img
                src="../../public/Group 10.svg"
                alt="two persons sitting in front of each other just decoration"
                draggable="false"
              />
            </div>
          </div>

          <swiper
            :pagination="{
              clickable: true,
            }"
            :navigation="true"
            :loop="true"
            :slides-per-view="slidePerView"
            :space-between="0"
            @swiper="onSwiper"
            @slideChange="onSlideChange"
          >
            <swiper-slide
              ><img
                class="slider-image"
                src="../../public/sliderImage1.png"
                draggable="false"
                alt=""
            /></swiper-slide>
            <swiper-slide
              ><img
                class="slider-image"
                src="../../public/sliderImage2.png"
                draggable="false"
                alt=""
            /></swiper-slide>
            <swiper-slide
              ><img
                class="slider-image"
                src="../../public/sliderImage3.png"
                draggable="false"
                alt=""
            /></swiper-slide>
            <swiper-slide
              ><img
                class="slider-image"
                src="../../public/sliderImage4.png"
                draggable="false"
                alt=""
            /></swiper-slide>
            <swiper-slide
              ><img
                class="slider-image"
                src="../../public/sliderImage1.png"
                draggable="false"
                alt=""
            /></swiper-slide>
            <swiper-slide
              ><img
                class="slider-image"
                src="../../public/sliderImage2.png"
                draggable="false"
                alt=""
            /></swiper-slide>
            <swiper-slide
              ><img
                class="slider-image"
                src="../../public/sliderImage3.png"
                draggable="false"
                alt=""
            /></swiper-slide>
          </swiper>
          <div class="subBlock1">
            <h1>У нас вы сможете</h1>
            <div class="subBlock1-container">
              <div class="subBlock1-container__canWithUs">
                <div class="canWithUsIcon">
                  <img src="../../public/Phone_Icon.png" alt="" />
                </div>
                <h2>Получить консультацию по получению ипотеки</h2>
              </div>
              <div class="subBlock1-container__canWithUs">
                <div class="canWithUsIcon">
                  <img src="../../public/HomeKey_icon.png" alt="" />
                </div>
                <h2>Рассчитать и оформить страхование</h2>
              </div>
              <div class="subBlock1-container__canWithUs">
                <div class="canWithUsIcon">
                  <img src="../../public/Hand_Icon.png" alt="" />
                </div>
                <h2>Посмотреть свои стоп-факторы</h2>
              </div>
              <div class="subBlock1-container__canWithUs">
                <div class="canWithUsIcon">
                  <img src="../../public/Board_Icon.png" alt="" />
                </div>
                <h2>Сделать анализ кредитной истории</h2>
              </div>
              <div class="subBlock1-container__canWithUs">
                <div class="canWithUsIcon">
                  <img src="../../public/Home_Icon.png" alt="" />
                </div>
                <h2>Запросить отчет ЕГРН онлайн</h2>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="block2">
      <h1 class="block2-header">Никаких сюрпризов, мы гарантируем:</h1>
      <div class="whatWeGuarantee">
        <div class="whatWeGuaranteeBlock">
          <div class="OurGuarantee">
            <h2>Качественный разбор вашей кредитной истории</h2>
            <h3>
              Имеем большой опыт в сфере кредитования и точно сможем разобрать вашу кредитную
              историю
            </h3>
          </div>
          <img src="../../public/Guarantee.png" alt="" />
        </div>
        <div class="whatWeGuaranteeBlock">
          <img src="../../public/Guarantee.png" alt="" />
          <div class="OurGuarantee">
            <h2>Экономия на страховании</h2>
            <h3>Являемся аккредитованными партнерами крупных страховых компаний</h3>
          </div>
        </div>
        <div class="whatWeGuaranteeBlock">
          <div class="OurGuarantee">
            <h2>Грамотное юридическое сопровождение на всех этапах сделки</h2>
            <h3>
              От грамотной подачи, проверки недвижимости, подписания договора до получения ключей
            </h3>
          </div>
          <img src="../../public/Guarantee.png" alt="" />
        </div>
        <div class="whatWeGuaranteeBlock">
          <img src="../../public/Guarantee.png" alt="" />
          <div class="OurGuarantee">
            <h2>Безопасность ваших персональных данных</h2>
            <h3>
              Работаем только с данными с государственных структур, ваши данные в полной
              безопасности
            </h3>
          </div>
        </div>
      </div>
    </div>
    <div class="block3">
      <div class="styled-div">
        <div class="container-target">
          <h2>
            Пусть мечта о новом доме станет доступной целью,
            <span class="h1">а КомбоБрокер поможет вам в её достижении!</span>
          </h2>
          <button class="standard-button"><p>Получить консультацию</p></button>
        </div>
      </div>
    </div>
    <div class="form-container">
      <div class="form">
        <h1 class="h1">Получить кредитный отчёт</h1>
        <form action="">
          <div class="input-container">
            <input class="form-input" type="text" placeholder="ФИО" />
            <input class="form-input" type="text" placeholder="Регион" />
            <input class="form-input" type="text" placeholder="Серия и номер паспорта" />
          </div>
          <button>Узнать расшифровку кредитного отчёта</button>
        </form>
      </div>
      <div class="stops">
        <h2>Подскажем, есть ли у вас стоп-факторы</h2>
        <p>
          Lorem ipsum dolor sit amet consectetur. A in aliquet orci malesuada fusce risus tempus
          lectus. Ultrices eu sit pellentesque nisl cras dolor.Lorem ipsum dolor sit amet
          consectetur. A in aliquet orci malesuada fusce risus tempus lectus. Ultrices eu sit
          pellentesque nisl cras dolor.
        </p>
        <div class="services">
          <img class="service-icon" src="../../public/Service1_Icon.svg" alt="" />
          <img class="service-icon" src="../../public/Service2_Icon.svg" alt="" />
          <img class="service-icon" src="../../public/Service3_Icon.svg" alt="" />
        </div>
      </div>
    </div>
    <div class="block4">
      <div class="block4-container">
        <div class="services-that-we-use">
          <img draggable="false" src="../../public/fns.png" alt="" />
          <img draggable="false" src="../../public/fssp.png" alt="" />
          <img draggable="false" src="../../public/efrsb.png" alt="" />
        </div>
        <div class="stop-factors">
          <h2>
            Проверить себя или заемщика перед самостоятельной подачей заявки на
            <span>стоп факторы</span>
          </h2>
          <button class="blue-button">
            <p>Узнать стоп-факторы</p>
          </button>
        </div>
      </div>
    </div>
    <div class="block5">
      <div class="block5-container">
        <h1>Льготные программы</h1>
        <div class="programms">
          <img
            draggable="false"
            class="stock-block5"
            src="../../public/stock-image__block5.png"
            alt=""
          />
          <div class="programms__lgot">
            <div class="programm">
              <div class="programm-container">
                <div class="programm-image-container">
                  <img draggable="false" src="../../public/programm1.svg" alt="" />
                </div>
                <div class="programm-text">
                  <div class="programm-headers">
                    <h3>Семейная ипотека</h3>
                    <p>Ребёнок до 6 лет, или<br />Два несовершеннолетних ребёнка</p>
                  </div>
                  <div class="programm-percent"><p>6%</p></div>
                </div>
              </div>
            </div>
            <div class="programm">
              <div class="programm-container">
                <div class="programm-image-container">
                  <img draggable="false" src="../../public/programm2.svg" alt="" />
                </div>
                <div class="programm-text">
                  <div class="programm-headers">
                    <h3>Сельская ипотека</h3>
                    <p>Официальный доход<br />Стаж от трёх месяцев на текущем месте работы</p>
                  </div>
                  <div class="programm-percent"><p>3%</p></div>
                </div>
              </div>
            </div>
            <div class="programm">
              <div class="programm-container">
                <div class="programm-image-container">
                  <img draggable="false" src="../../public/programm3.svg" alt="" />
                </div>
                <div class="programm-text">
                  <div class="programm-headers">
                    <h3>IT ипотека</h3>
                    <p>Работникам it-компании<br />Стаж >= 2 года</p>
                  </div>
                  <div class="programm-percent"><p>6%</p></div>
                </div>
              </div>
            </div>
            <div class="programm">
              <div class="programm-container">
                <div class="programm-image-container">
                  <img draggable="false" src="../../public/programm4.svg" alt="" />
                </div>
                <div class="programm-text">
                  <div class="programm-headers">
                    <h3>Базовая ипотека</h3>
                    <p>Нет стоп-факторов</p>
                  </div>
                  <div class="programm-percent"><p>15%</p></div>
                </div>
              </div>
            </div>
            <div class="programm-button">
              <h2>Узнать какая подходит вам</h2>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="block6">
      <QuizComponent />
    </div>
    <div class="block7">
      <div class="form1">
        <div class="form-container-end">
          <h2>Остались вопросы?</h2>
          <div class="container-number">
            <h3>Номер телефона</h3>
            <div class="number-form">
              <h4 style="color: #fff; font-weight: normal">+7</h4>
              <MaskInputComponent
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
            <customSelect :options="['по кредиту', 'по ипотеке', 'почему', 'Другое']" />
          </div>
          <div class="container-number">
            <h3>Где вам удобнее общаться?</h3>
            <radioButton />
          </div>
          <button id="form-button">Оставить заявку</button>
        </div>
      </div>
    </div>
  </main>
  <footer>
    <div class="contacts-and-brand">
      <div class="contacts">
        <h4>+7 (917) 031-00-35</h4>
        <h3>Россия, Самарская обл.</h3>
        <p>Время работы: 8:00-20:00</p>
      </div>
      <div class="brand">
        <h1>Комбоброкер</h1>
        <div class="socials">
          <img draggable="false" src="../../public/Telegram_icon.svg" alt="" />
          <img draggable="false" src="../../public/WhatsUp_icon.svg" alt="" />
        </div>
        <p>©КомбоБрокер</p>
      </div>
    </div>
    <div class="tgchannel">
      <img draggable="false" src="../../public/Telegram_icon.svg" alt="" />
      <p>Наш канал в Telegram</p>
    </div>
  </footer>
</template>

<style lang="scss">
.tgchannel {
  height: 40px;
  p {
    color: #fff;
  }
  img{
    height:24px;
  }

  flex-direction: row;
  gap: 10px;
  margin-top: 26px;
}
.tgchannel:hover {
  cursor: pointer;
}
.contacts-and-brand {
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 17px;
  padding-left: 150px;
  .contacts {
    display: flex;
    flex-direction: column;
    gap: 7px;
  }
  .brand {
    display: flex;
    flex-direction: column;
    gap: 7px;
    h1 {
      font-weight: bold;
    }
    .socials {
      display: flex;
      flex-direction: row;
      gap: 55px;
      img:hover {
        cursor: pointer;
      }
    }
  }
  height: 250px;
}
  footer {
    display: grid;
    grid-template-columns: 1fr 2fr;
  

  img {
    width: 30px;
  }
  h1,
  h3,
  h4,
  p {
    color: #fff;
    font-weight: normal;
  }
  p {
    font-weight: 100;
    color: #9e9e9e;
  }
  h1 {
    font-weight: bold;
  }
  margin-top: 200px;
  height: 250px;
  background-color: #1f1f1f;
}
#form-button {
  background-color: #ffffff;
  color: #000000;
  border-radius: 9px;
  padding: 15px 30px;
  border: none;
}
.select-for-customSelect {
  margin-top: 10px;
}
.number-form {
  display: flex;
  flex-direction: row;
  align-items: center;

  border-bottom: 2px solid #c6dcff;
  gap: 5px;
  padding: 10px 0 10px 0;
  h4 {
    font-size: 18px;
  }
}
.form1 {
  margin-top: 150px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.form-container-end {
  display: flex;
  flex-direction: column;
  gap: 70px;
  height: 550px;
  background-color: #5298ff;
  padding: 40px;
  border-radius: 9px;
  h3 {
    color: #fff;
    font-weight: 300;
  }
  h2 {
    color: #fff;
    font-weight: 500;
  }
}
.block6 {
  display: flex;
  justify-content: center;
  align-items: center;
}

.programm-button:hover {
  cursor: pointer;
  box-shadow: 0 4 20px #1a72f76b;
  transition: all 0.2s ease;
}
.programm-button {
  display: flex;
  justify-content: center;
  align-items: center;
  transition: all 0.2s ease;
  h2 {
    color: #fff;
    font-weight: 500;
  }
  background-color: #458ffc;
  width: 100%;
  border-radius: 10px;
  height: 75px;
  box-shadow: 0 3px 7px 1px #458efc28;
}

.programm-percent {
  p {
    font-size: clamp(1.125rem, 0.104rem + 4.667vw, 2rem);
    color: #484848;
  }
}

.programm-text {
  .programm-headers {
    display: flex;
    flex-direction: column;
    gap: 5px;
    h3 {
      font-size: 20px;
      color: #484848;
      font-weight: normal;
    }
    p {
      font-size: 15px;
      color: #484848;
    }
  }
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 10px;
  justify-content: space-between;
}
.programm {
  padding-left: 15px;
  display: flex;
}
.programm-container {
  width: 100%;
  align-items: center;
  display: flex;
  flex-direction: row;

}
.programm-image-container {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #458ffc;
  width: 58px;
  height: 58px;
  border-radius: 10px;
}
.stock-block5 {
  box-shadow: 0 3px 7px 1px #458efc28;
  object-fit: cover;
  width: 40vw;
  border-radius: 10px;

}
.block5 {
display: flex;
flex-direction: column;
align-items: center;
}
.block5-container h1 {
  background: linear-gradient(90deg, #2b80ff 0%, #00a5e6 20%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.block5-container {
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.programms__lgot {
display: flex;
flex-direction: column;
gap: 20px;
}
.programms {
display: flex;
gap: 20px
}
.programm {
  background-color: #fff;
  border-radius: 10px;
  height: 90px;
  box-shadow: 0 3px 7px 1px #458efc28;
  padding-right: 10px;
}
.services-that-we-use {
  width: 50vw;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  img {
    width: 10vw;
    aspect-ratio: 1/1; 
    object-fit: contain;
  }
}
.blue-button {
  height: 53px;
  border-radius: 5px;
  border: 0;
  transition: all 0.3s ease;
  background-color: #458ffc;
  padding-left: 10px;
  padding-right: 10px;
}
.blue-button:hover {
  background-color: #5f9fff;
  box-shadow: 0 0 40px #458efc28;
  transition: all 0.2s ease;
  cursor: pointer;
}
.blue-button p {
  user-select: none;
  font-size: 16px;
  font-weight: 600;
  color: #fff;
}

.stop-factors {
  display: flex;
  flex-direction: column;
  gap: 30px;
  h2 {
    span {
      color: #458ffc;
    }
  }
}


.block4 {
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 500px;
}
.container-target {
  display: flex;
  flex-direction: column;
  gap: 30px;
  position: absolute;
  top: 42%;
  left: 37%;
  h2 {
    width: 60vw;
  }
}
.styled-div {
  position: relative;
  h2 {
    font-weight: normal;
    color: white;
    font-size: 40px;
  }
  span {
    font-weight: bold;
    color: white;
    font-size: 40px;
  }
}
.stops {
  flex-direction: column;
  justify-content: space-between;
  gap: 20px;
  height: 310px;
  p {
    font-size: 20px;
  }
}
.services {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  .service-icon {
    width: 100px;
  }
}
.input-container {
  padding-top: 40px;
  padding-bottom: 40px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.form-container {
  padding-top: 100px;
  height: 400px;
  display: flex;
  flex-direction: row;

  .stops {
    width: 800px;
  }
  .form {

    button {
      width: 100%;
      height: 50px;
      border-radius: 4px;
      border: 0;
      color: black;
      font-size: 15px;
      font-weight: 300;
      transition: all 0.2s ease;
    }
    button:hover {
      box-shadow: 0 0 40px #9cd2f1;
      transition: all 0.2s ease;
      cursor: pointer;
    }
    .form-input {
      background-color: #35353500;
      width: 100%;
      border: none;
      padding: 10px;
      border-bottom: 2.4px solid #fff;
      border-radius: 2px;
      padding: 0;
      padding-bottom: 5px;
      padding-top: 5px;
      font-size: 18px;
    }
    .form-input::placeholder {
      color: white;
      font-size: 18px;
      font-weight: lighter;
    }
  }
  * {
    color: white;
  }
}
.styled-div {
  width: 100%;
  height: 900px; /* Высота, аналогичная высоте SVG */
  background-color: #75a4eb; /* Цвет заливки */
  clip-path: path(
    'M65.3849 765.012C106.859 678.436 187.706 617.317 282.31 601.019V601.019C348.164 589.674 408.25 556.402 452.812 506.605L530.412 419.889C543.445 405.325 557.75 391.953 573.158 379.931V379.931C690.129 288.665 831.37 233.84 979.282 222.286L1172.61 207.186C1216.26 203.776 1258.49 190.15 1295.9 167.408L1391.82 109.101C1507.13 39.0011 1639.23 1.32002 1774.17 0.0317864L1777.5 0H1920V901.5H0L65.3849 765.012Z'
  );
}

.block3 {
  height: 893px;
  background-image: url('../../public/sec3house.png');
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  margin-top: 110px;
}
.section_3 {
  width: 100%;
}
.block2-header {
  background: linear-gradient(to right, #1974fd, #6616e7);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}



.block2 {
  position: relative;
  display: flex;
  justify-content: center;
  gap: 50px;
  height: 100%;
  margin-top: 120px;
}
.canWithUsIcon {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #75a4eb;
  border-radius: 8px;

}
.subBlock1-container {
  h2 {
    font-size: 18px;
    color: #363f4b;
  }
  width: 70vw;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  gap: 20px
}
.subBlock1-container__canWithUs {
  display: flex;
  flex-direction: column;
  gap: 30px;
  padding: 20px;

  background-color: #fff;
  border-radius: 8px;
  h2 {
    font-size: clamp(0.75rem, 0.596rem + 0.353vw, 1.125rem);
  }
}
.swiper {
  margin-top: 100px;
}
.swiper-wrapper {
  display: flex;
  align-items: center;

}

.img {
  user-select: none;
  right: 2vw;
  position: absolute;
  z-index: 12423;
  img {
    width: 35vw;
  }
}
.Help_in_obligation_container {
  position: relative;
  display: flex;
}
.text_container {
  display: flex;
  flex-direction: column;
  gap: 30px;
}
.dot {
  color: #e43737;
}

.Help_in_obligation {
  font-size: clamp(1.875rem, 1.591rem + 0.758vw, 2.5rem);
  font-weight: 700;
  line-height: 1.2;
  color: white;
}
.Help_in_obligation_p {
  font-size: 16px;
  font-weight: 300;
  color: white;
}
.block1-container {
  padding-bottom: 70px;
  background-color: #75a4eb;
  background-image: radial-gradient(circle at 0% 80%, #0af0ba81, transparent),
    radial-gradient(circle at 100% 0%, #b849fd91, transparent);
}
.block1-content,
.block2 {
  display: flex;
  flex-direction: column;
  gap: 100px;
  margin-left: 8vw;
  margin-right: 8vw;
}
</style>

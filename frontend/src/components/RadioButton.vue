<script>
export default {
  data() {
    return {
      option: 'WhatsApp',
    }
  },
  methods: {
    changeOption(messanger) {
      if (this.option !== messanger) {
        this.option = messanger
      }
    },
  },
}
</script>

<template>
  <div class="connect">

    <div class="radio-button" @click="changeOption(`WhatsApp`)">
      <div class="messanger-name">
        <img id="whatsapp-logo" src="../../public/WhatsUp_icon.svg" alt="">
        WhatsApp
    </div>
      <div class="circle">
        <div class="circle_inner"></div>
        <div class="circle_outer" v-if="option === 'WhatsApp'"></div>
      </div>
    </div>
    <div class="stick"></div>
  <div class="radio-button" @click="changeOption(`Telegram`)">
    <div class="messanger-name">
        <img id="telegram-logo" src="../../public/Telegram_icon.svg" alt="">
        Telegram</div>
    <div class="circle">
      <div class="circle_inner"></div>
      <div class="circle_outer" v-if="option === 'Telegram'"></div>
    </div>
  </div>

  </div>
</template>
<style lang="scss">
@media screen and (max-width: 1050px) and (min-width: 650px) {
    .radio-button {
        width: 20vw;
    }
  }
  @media screen and (max-width: 650px){
    .radio-button {
        width: 230px;
    }
}
.stick {
    border: 1px #fff;
    height: 40px;
    border-style: dashed;
    stroke-dasharray: 10 5;
}
#whatsapp-logo {
    width: 28px;

    margin-right: 10px;
}
#telegram-logo {
    width: 25px;

    margin-right: 10px
}

.messanger-name {
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 16px;
    font-weight: 300;
    color: #fff;
}

.connect {
    margin-top: 10px;
  display: flex;
  flex-direction: row;
  gap: 20px;
}
.radio-button {
    user-select: none;

  display: flex;
  flex-direction: row;
  justify-content: space-between;
  gap: 10px;
}
.radio-button:hover {
  cursor: pointer;
}
.circle {
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
    width: 20px;
    height: 40px;
}
.circle_inner {
  border-radius: 40px;
  width: 10px;
  height: 10px;
  background-color: #ffffff;
}
.circle_outer {
  border-radius: 40px;
  width: 16px;
  height: 16px;
  background-color: #ffffff00;
  border: 2px solid #fff;
  position: absolute;
  z-index: 34;


}
</style>

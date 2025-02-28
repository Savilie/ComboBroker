<script>
import { useFeedbackStore } from '../stores/form.js'

export default {
  props: {
    options: Array,
  },
  data() {
    return {
      store: useFeedbackStore(),
      isClicked: false,
      choosenOne: this.options[0],
    }
  },
  methods: {
    openSelect() {
      this.isClicked = !this.isClicked
    },
    chooseOption(option) {
      this.choosenOne = option
      this.isClicked = !this.isClicked
      this.store.theme = 'Консультация ' + option
      console.log(this.store.theme)
    },
    selectUnfocused() {
      switch (this.isClicked) {
        case true:
          this.isClicked = !this.isClicked
          break

        case false:
          break
      }
    },
  },
}
</script>

<template>
  <div class="select-for-customSelect">
    <button @click="openSelect" v-click-outside="selectUnfocused">
      {{ 'Консультация ' + choosenOne }}
    </button>
    <ul v-if="this.isClicked">
        <li @click="chooseOption(option)" v-for="(option, index) in this.options" :key="index">
        <p>{{ option }}</p>
      </li>
    </ul>
  </div>
</template>

<style scoped>
@media screen and (max-width: 650px) {
  button {
    width: 250px;
  }
}
@media screen and (max-width: 1050px) and (min-width: 650px) {
  button {
    width: 40vw;
  }
}
@media screen and (max-width: 2400px) and (min-width: 1050px) {
  button {
    width: 20vw;
  }
}
.select-for-customSelect {
  margin-top: 10px;
  position: relative;
}
button::-moz-focus-inner {
  border: 0;
}
button {
  background-color: #5298ff;

  height: 30px;
  border: 0;
  padding-bottom: 35px;
  border-bottom: 2px solid #ffffff;
  text-align: left;
  font-size: 18px;
  color: #fff;
  font-weight: 300;
}
button:hover {
  cursor: pointer;
}
ol {
  list-style-type: none;
}

ul {
  list-style-type: none;
}

li {
  display: flex;
  align-items: center;
  padding-left: 8px;
  height: 30px;
  text-align: left;
  width: 340px;
}
p {
  margin: 0;
}
li:hover {
  cursor: pointer;
  background-color: #dadada;
}

ul {
  background-color: #fff;
  position: absolute;
  display: flex;
  flex-direction: column;
  z-index: 23465;
  border-radius: 3px;
  padding-left: 0;
  padding-right: 0;
  padding-top: 5px;
  padding-bottom: 5px;
  margin-top: 5px;
  width: 348px;
}
</style>

<template>
 <header class="header" :style="backgroundColor">
   <div class="content">
     <!--   <div class="leftHeader">
     <div class="logoArea">
       <div class="logoIcon"></div>
       <div class="logoText"></div>
     </div>
     <div class="menu"></div>
   </div>-->
     <div class="logoArea" @click="this.$router.push('/')">
       <div class="logoIcon">
       </div>
       <div class="logoText">Tabibito</div>
     </div>
     <div class="actions" :style="currencyColor">
       <div class="simpleSettings">
<!--         @mouseenter="currency_is_shown = true" @mouseleave="currency_is_shown = false"-->
         <div class="actionButton currencyButton" @click="this.$router.push('/search_result')">
           <div class="actionIcon" id="currencyIcon" :style="currencyIcon1"></div>
           <div class="actionText" id="currencyText">{{ $t('navi.sear') }}</div>
         </div>
         <div class="divider"></div>

         <div class="actionButton currencyButton">


           <div class="actionIcon" id="currencyIcon" :style="currencyIcon2"></div>
           <n-dropdown trigger="click" style="z-index: 100000000 !important;" :options="options" @select="handleSelect">
             {{ $t('navi.chart') }}
           </n-dropdown>
         </div>
         <div class="divider"></div>

         <div class="actionButton currencyButton" @click="this.$router.push('/chat')">
           <div class="actionIcon" id="currencyIcon" :style="currencyIcon"></div>
           <div class="actionText" id="currencyText">{{ $t('navi.chat') }}</div>
         </div>
         <div class="divider"></div>

         <div class="actionButton currencyButton" @click="this.$router.push('/about')">
           <div class="actionIcon" id="currencyIcon" :style="currencyIcon3"></div>
           <div class="actionText" id="currencyText">{{ $t('navi.about') }}</div>
         </div>

         <transition name="fade">
           <drop-down
               @mouseenter="currency_is_shown = true"
               @mouseleave="currency_is_shown = false"
               :dropdown_item="currency_item"
               :is_currency="true"
               v-show="currency_is_shown"
               style="position: absolute; left: 10px; top: 60px"
               @change-currency="handleCurrencyChange"
           ></drop-down>
         </transition>
         <div class="divider"></div>
         <div class="actionButton languageButton" @click="changeLang()">
           <div class="actionIcon"></div>
           <div class="actionText">{{ $t('navi.lang') }}</div>
         </div>
       </div>
       <div class="accountButton" @mouseenter="user_is_shown = true" @mouseleave="user_is_shown = false">
         <transition name="fade">
           <drop-down
               @mouseenter="user_is_shown = true"
               @mouseleave="user_is_shown = false"
               :dropdown_item="login_item"
               :is_currency="false"
               v-show="user_is_shown"
               v-if="!user_is_logged_in"
               style="position: absolute; right: 100px; top: 60px"
               :style="dropDownPosition"
               @change-currency="handleCurrencyChange"
           ></drop-down>
         </transition>
           <transition name="fade">
           <user-drop-down
               @mouseenter="user_is_shown = true"
               @mouseleave="user_is_shown = false"
               style="position: absolute; right: 0; top: 60px"
               v-show="user_is_shown"
               v-if="user_is_logged_in"
           ></user-drop-down>
         </transition>
       </div>
     </div>
   </div>
 </header>

</template>

<script>
import {h, defineComponent, ref, onMounted} from "vue";
import DropDown from "./dropDown.vue";
import userDropDown from "./userDropDown.vue";
import {useStore, useLangStore} from "../../store.js";
import {getCurrentInstance} from 'vue'
import {useRouter} from 'vue-router';

import {useI18n} from "vue-i18n";
export default defineComponent({
  props: {
    isTransparent: Boolean,
    isIniTextWhite: Boolean
  },
  components: {DropDown, userDropDown},
  setup(props) {
    const route = useRouter();
    const store = useStore();
    let currency_is_shown = ref(false);
    let user_is_shown = ref(false);
    let user_is_logged_in = ref(false);
    const axios = getCurrentInstance().appContext.config.globalProperties.axios;
    axios.get('/user/login_status')
        .then((res)=>{
          user_is_logged_in.value = res.data.id !== null;
          if (user_is_logged_in.value){
            store.user_id = res.data.id;
            store.name = res.data.name
          }
          store.user_login_status = user_is_logged_in.value;
        })
    let currencyIcon = ref("background-image:url('src/assets/chat.png')");
    let currencyIcon1 = ref("background-image:url('src/assets/tour.png')");
    let currencyIcon2 = ref("background-image:url('src/assets/chart.png')");
    let currencyIcon3 = ref("background-image:url('src/assets/team.png')");

    let currencyText = ref('USD');
    let backgroundColor = ref("background-color: white;");
    let currencyColor = ref("")
    let dropDownPosition = ref("")
    if (props.isTransparent) {
      backgroundColor = ref("background-color: 00000000;");
      if (props.isIniTextWhite){
        currencyColor = ref("filter: invert(100%) sepia(0%) saturate(0%) hue-rotate(346deg) brightness(101%) contrast(104%);");
        dropDownPosition = ref("right: 100px;")
      }
      onMounted(() => {
        window.addEventListener("scroll", function () {
          let scrollTop = document.documentElement.scrollTop || document.body.scrollTop;

          if (scrollTop === 0) {
            backgroundColor.value = "background-color: 00000000; transition: .2s;";
            if (props.isIniTextWhite){
              currencyColor.value = "filter: invert(100%) sepia(0%) saturate(0%) hue-rotate(346deg) brightness(101%) contrast(104%); transition: .2s;";
              dropDownPosition.value = "right: 100px;"
            }
          } else {
            backgroundColor.value = "background-color: white; transition: .2s; box-shadow: 0px 10px 30px 0px #05103608;";
            currencyColor.value = "color: black; transition: .2s;";
            dropDownPosition.value = "right: 100px;"
          }
        }, true)
      })
    }else {
      backgroundColor = ref("background-color: white; box-shadow: 0px 10px 30px 0px #05103608;");
    }
    return {
      currency_is_shown,
      user_is_shown,
      currencyIcon,
      currencyIcon1,
      currencyIcon2,
      currencyIcon3,
      currencyText,
      user_is_logged_in,
      backgroundColor,
      currencyColor,
      dropDownPosition,
      options: [
        {
          label: "Reservation Rates",
          key: "rate"
        },
        {
          label: "Visual Travel Data",
          key: "data"
        },
        {
          label: "Tours Distribution",
          key: "map"
        }
      ],
      handleSelect(key) {
        if (key === "data"){
          route.push('/chartsData')
        } else if (key === "map"){
          route.push('/chartsMaps')
        } else if (key === "rate"){
          route.push('/chartsRates')
        }
      }
    };
  },
  data(){
    return{
      currency_item: ref([
        {icon: "background-image:url('src/assets/USD.svg')", text: this.$t('navi.chat')},
        // {icon: "background-image:url('src/assets/CNY.svg')", text: this.$t('navi.CNY')},
        // {icon: "background-image:url('src/assets/EUR.svg')", text: this.$t('navi.EUR')},
      ]),
      user_item: [
        {

        }
      ],
      login_item: [
        {icon: "background-image:url('src/assets/login.svg')", text: this.$t('navi.login'), path: '/login'},
        {icon: "background-image:url('src/assets/signup.svg')", text: this.$t('navi.signup'), path: '/register'}
      ]
    }
  },
  methods: {
    handleCurrencyChange(icon, text){
      this.currencyIcon = icon;
      this.currencyText = text;
    },
    changeLang() {
      const store = useLangStore();
      if (this.$i18n.locale === 'en') {
        this.$i18n.locale = 'zh'
        store.language = 'zh'
      } else {
        this.$i18n.locale = 'en';
        store.language = 'en'
      }
      let language;
      if (this.$i18n.locale === 'zh'){
        language = 'ch'
      }else {
        language = 'en'
      }
      this.axios.post('/user/set_language', {
        language: language
      })
    }
  }
});


</script>

<style scoped>
.header{
  width: 100vw;
  height: 90px;
  /*background-color: #13357B;*/
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-sizing: border-box;
  position: fixed;
  z-index: 10000;
}
@media screen and (max-height: 450px) {
  .header {
    height: 65px;
  }
}
.content{
  max-width: 1320px;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin: auto;
  box-sizing: border-box;
  padding-left: 30px;
  padding-right: 30px;
}
.leftHeader{
  width: auto;
  height: 100%;
  display: flex;
  flex-wrap: nowrap;
}
.logoArea{
  width: 160px;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: space-around;
  user-select: none;
}
.logoIcon{
  margin: 10px;
  height: 70px;
  width: 70px;
  background-repeat: no-repeat;
  background-size: contain;
  background-position: center;
  background-image: url("../../assets/logo.png");
}
.logoText{
  font-size: 20px;
}
.menu{
  width: 590px;
  height: 100%;
  background-color: aqua;
}
.actions{
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.simpleSettings{
  width: 490px;
  height: 30px;
  display: grid;
  grid-template-columns: 1fr 11px 1fr 11px 1fr 11px 1fr 11px 1fr;
  grid-template-rows: 1fr;
  align-items: center;
  box-sizing: border-box;
  position: relative;
}
.actionButton{
  width: calc(100% - 20px);
  height: 100%;
  display: flex;
  justify-content: space-around;
  align-items: center;
  position: relative;
  transition: .1s ease-in;
  border-radius: var(--border-radius);
  padding: 3px;
  cursor: pointer;
  outline: none;
}
.actionButton:hover{
  transition: .1s ease-out;
  background-color: rgba(46, 51, 56, .09);
}
.actionIcon{
  background-image: url('../../assets/USD.svg');
  background-position: center;
  background-repeat: no-repeat;
  background-size: contain;
  width: 24px;
  height: 24px;
}
.actionText{
  font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
}
.currencyButton{
  margin-left: 10px;
}
.languageButton{
  margin-right: 10px;
}
.languageButton .actionIcon{
  background-image: url('../../assets/language.svg');
}
.accountButton{
  width: 36px;
  height: 36px;
  border-radius: 400px;
  position: relative;
  box-sizing: border-box;
  background-image: url("../../assets/user.svg");
  background-size: 70%;
  background-repeat: no-repeat;
  background-position: center;
  cursor: pointer;
}
.accountButton:hover{
  background-color: rgba(46, 51, 56, .09);
  transition: .1s ease-out;
}
.divider{
  margin-left: 5px;
  margin-right: 5px;
  height: 80%;
  width: 1px;
  background-color: var(--border-color);
}
.fade-enter-active{
  transition:height .25s;
}
.fade-leave-active{
transition:opacity .25s
}
.fade-enter{
  height: 0;
}
.fade-leave-to {opacity:0}

@media screen and (max-width: 500px) {
  .actionButton{
    display: none;
  }
  .simpleSettings{
    width: 0;
  }
  .content{
    padding-left: 3px;
  }
}
</style>

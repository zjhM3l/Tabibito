<template>
  <n-config-provider :locale="naiveLang" :theme-overrides="themeOverrides">
    <n-message-provider>
      <router-view></router-view>
    </n-message-provider>
  </n-config-provider>
</template>

<script>
  import {zhCN, enUS} from "naive-ui"
  import {useLangStore} from "./store.js";
  import {useI18n} from "vue-i18n";
  import {ref} from "vue";
  import {getCurrentInstance} from 'vue'
  export default {
    name: 'App',
    setup(){
      const themeOverrides = {
        common: {
          primaryColor: '#3554D1',
          primaryColorHover: '#0a58ca',
          primaryColorPressed: '#051036',
          primaryColorSuppl: '#7E53F9'
        }
      }
      let langStore = useLangStore();
      let i18n = useI18n();
      let naiveLang = ref(enUS);
      const axios = getCurrentInstance().appContext.config.globalProperties.axios;
      axios.get('/user/get_language')
          .then((res) =>{
            i18n.locale = res.data.language;
            langStore.language = res.data.language;
            if (res.data.language === 'zh')
              naiveLang.value = zhCN;
            else {
              naiveLang.value = enUS;
            }
          })
      langStore.$subscribe((mutation, state) => {
        if (state.language === 'zh'){
          naiveLang.value = zhCN;
        }else {
          naiveLang.value = enUS;
        }
      })
      return{
        themeOverrides,
        langStore,
        zhCN,
      }
    },
  }
</script>

<style>
body {
  margin: 0;
  font-family: Jost, "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  font-size: 16px;
}
:root {
  --border-color: rgba(255, 255, 255, 0.2);
  --border-radius: 6px;
  --primary-color: #3554D1;
  --secondary-text-color: #697488;
  --text-color-dark: #051036;
}
@font-face {
  font-family: Jost;
  src: url("assets/fonts/Jost-VariableFont_wght.ttf") format("truetype");
}
@font-face {
  font-family: JostBlod;
  src: url("assets/fonts/Jost-Medium.ttf");
}

@font-face {
  font-family: JostLight;
  src: url("assets/fonts/Jost-Light.ttf");
}
@keyframes shake {
  0%{
    transform: translateX(0%);
  }
  15%{
    transform: translateX(-10px);
  }
  30%{
    transform: translateX(0%);
  }
  45%{
    transform: translateX(10px);
  }
  60%{
    transform: translateX(0%);
  }
  70%{
    transform: translateX(-5px);
  }
  80%{
    transform: translateX(0%);
  }
  90%{
    transform: translateX(5px);
  }
  100%{
    transform: translateX(0%);
  }
}
.n-upload-file-list .n-upload-file.n-upload-file--image-card-type{
  width: 180px;
  height: 180px;
}
.n-upload-file-list.n-upload-file-list--grid{
  grid-template-columns: repeat(auto-fill, 180px);
}
.n-upload-trigger.n-upload-trigger--image-card{
  width: 180px;
  height: 180px;
}
.n-upload-trigger.n-upload-trigger--image-card .n-base-icon{
  font-size: 50px;
}
.input_form .n-base-selection-label{
  height: 70px;
}
@media screen and (max-width: 550px) {
  .CRContainer .custom-arrow .custom-arrow--right{
    margin: 0;
  }
  .CRContainer .custom-arrow{
    justify-content:center;
  }
  .CRContainer .custom-dots{
    width: 100%;
    justify-content: center;
    /*margin-right: 188px; */
    margin-left: 0 !important;
  }
}
</style>

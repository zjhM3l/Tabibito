<template>
  <navigation-bar></navigation-bar>
  <div>
    <div v-if="isLoading" class="loading">
      <div class="logo_all">
        <img class=" aaa" src="../../assets/logo.jpg">
      </div>
      <div class="preloader_tit">Tabibito</div>
    </div>
    <div v-else>
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
      <!-- 网页内容 -->
    </div>
  </div>
</template>

<script>
import router from "../../router.js";
import NavigationBar from "../GeneralComponents/navigationBar.vue";

export default {
  components: {NavigationBar},
  data() {
    return {
      isLoading: true,
      isFirstLoad: true // 是否是第一次加载的标志变量

    };
  },

  mounted() {

    setTimeout(() => {
      this.$router.push('/');
    }, 1400); // 延时5秒

    if (window.location.href.indexOf("#reloaded") == -1) {
      window.location.href = window.location.href + "#reloaded";
      window.location.reload();
    }

  },
};
</script>

<style>
.loading {
  /* 设置加载页面的样式 */
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 5000;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  background-color: white;
  transition: opacity 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
}

.preloader_tit{
  font-size: 47px;
  font-weight: 600;
  line-height: 68px;
  letter-spacing: 0em;
  margin-top: 18px;
}

.logo_all{
  animation-name: box-moving;
  animation-duration: 2s;
  animation-timing-function: ease-in-out;
  animation-iteration-count: infinite;

  overflow: hidden;
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 132px;
  height: 132px;
  border-radius: 30px;
  background-color: white;
  box-shadow: 0px 2px 24px 0px #00000014;
}

.aaa {
  animation-name: img-moving;
  animation-duration: 2s;
  animation-timing-function: ease-in-out;
  animation-iteration-count: infinite;
  width: 112px;
  height: 112px;

}

@keyframes img-moving {
  0% {
    transform: translateY(60px) scale(1);
  }
  50% {
    transform: translateY(0px) rotate(10deg) scale(1.2);
  }
  100% {
    transform: translateY(-120px) rotateX(-20deg) scale(1);
  }
}

@keyframes box-moving {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.2);
  }
  100% {
    transform: scale(1);
  }
}

</style>

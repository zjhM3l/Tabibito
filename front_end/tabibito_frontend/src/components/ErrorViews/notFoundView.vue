<template>
  <navigation-bar></navigation-bar>
  <div class="container">
    <div class="cover"></div>
    <div class="texts">
      <div class="mainText">
        <span class="mainLeft">40</span>
        <span class="mainRight">4</span>
      </div>
      <div class="title">{{ $t('fourZeroFourPage.slogan')}}</div>
      <div class="description">{{ $t('fourZeroFourPage.subSlogan')}}</div>
      <div class="backButton" @click="this.$router.push('/')">{{ $t('fourZeroFourPage.button')}}</div>
    </div>
  </div>
  <footer-view></footer-view>
</template>

<script>
import NavigationBar from "../GeneralComponents/navigationBar.vue";
import FooterView from "../GeneralComponents/footerView.vue";
export default {
  name: "notFoundView",
  components: {FooterView, NavigationBar}

}
</script>

<style scoped>
.container{
  max-width: 1320px;
  box-sizing: border-box;
  padding: 200px 0;
  margin: 0 auto;
  display: flex;
}
.cover{
  background-image: url("../../assets/404.svg");
  background-size: contain;
  background-repeat: no-repeat;
  width: 660px;
  box-sizing: border-box;
  padding: 15px;
}
.texts{
  width: 550px;
  box-sizing: border-box;
  padding: 15px;
}
.mainText{
  font-size: 200px;
  line-height: 1.2;
}
.mainRight{
  color: var(--primary-color);
}
.title{
  font-size: 30px;
  margin: 0;
  line-height: 1.45;
}
.description{
  margin-top: 5px;
  color: var(--text-color-dark);
}
.backButton{
  margin-top: 40px;
  box-sizing: border-box;
  padding: 14px 30px;
  color: white;
  background-color: var(--primary-color);
  border-radius: 4px;
  width: fit-content;
  transition: all 0.3s cubic-bezier(0.165, 0.84, 0.44, 1);
  user-select: none;
}
.backButton:hover{
  background-color: var(--text-color-dark);
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.165, 0.84, 0.44, 1);
}
@media screen and (max-width: 1100px) {
  .cover {
    background-size: cover;
  }
  .container{
    padding-bottom: 100px;
    padding-top: 150px;
  }
}
@media screen and (max-width: 696px) {
  .container{
    padding-bottom: 50px;
    padding-top: 100px;
    flex-direction: column;
  }
  .cover{
    width: auto;
    display: none;
  }
  .texts{
    width: auto;
    margin: auto;
    padding: 20px;
  }
  .mainText{
    display: flex;
    font-size: 150px;
  }
}
</style>

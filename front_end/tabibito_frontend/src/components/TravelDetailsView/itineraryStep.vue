<template>
<div class="container">
  <div class="index">{{parseInt(index) + 1}}</div>
  <div class="information">
    <div class="title">{{item.description}}</div>
    <div class="time">{{item.time}}</div>
    <n-collapse-transition :show="show">
      <div class="picture" :style="'background-image: url(' + item.picture + ')'"></div>
      <div class="description">{{item.name}}</div>
    </n-collapse-transition>
    <div class="moreInfo" @click="handleInfo">{{moreInfoText}}</div>
  </div>
</div>
</template>

<script>
import {ref} from "vue";
export default {
  props: ['item', 'index'],
  name: "itineraryStep",
  setup(prop){
    console.log(prop.item)
    let show = ref(false);
    let moreInfoText = ref("See details & photo");
    return{
      show,
      moreInfoText,
      handleInfo(){
        if (show.value === false){
          show.value = true;
          moreInfoText.value = "See Less"
        }else {
          show.value = false;
          moreInfoText.value = "See details & photo"
        }
      }
    }
  }
}
</script>

<style scoped>
.container{
  width: 100%;
  display: flex;
}
.index{
  width: 40px;
  height: 40px;
  border-radius: 100%;
  color: var(--primary-color);
  font-size: 14px;
  font-weight: 500;
  line-height: 40px;
  text-align: center;
  background-color: #E5F0FD;
}
.information{
  margin-left: 20px;
}
.title{
  font-weight: 500;
  line-height: 1.5;
  font-size: 16px;
}
.time{
  color: var(--secondary-text-color);
  margin-top: 5px;
  font-size: 14px;
  line-height: 1.5;
}
.moreInfo{
  font-size: 15px;
  line-height: 1.5;
  color: var(--primary-color);
  cursor: pointer;
  user-select: none;
}
.picture{
  width: 290px;
  height: 130px;
  margin-top: 15px;
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
}
.description{
  font-size: 14px;
  margin-top: 15px;
  line-height: 1.7;
}
@media (min-width:576px){
  .container{
    max-width:540px
  }
}
@media (min-width:768px){
  .container{
    max-width:720px
  }
}
@media (min-width:992px){
  .container{
    max-width:960px
  }
}
@media (min-width:1200px){
  .container{
    max-width:1140px
  }
}
@media (min-width:1400px){
  .container{
    max-width:1320px
  }
}
</style>

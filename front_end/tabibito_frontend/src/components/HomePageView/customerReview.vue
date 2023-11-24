<template>
  <section class="block">

    <!--    背景图-->
    <div class="bgC">
    </div>

    <!--    文字标题部分-->
    <div class="CRContainer">
      <div class="tit">
        <h2 class="t1">{{$t('customerReview.title')}}</h2>
        <p class="t2">{{ $t('customerReview.showcase')}}</p>
      </div>

      <!--      图片+文字轮播图部分-->
      <n-carousel show-arrow >
        <div v-for="review in reviews" :key="review.id">
        <div class="con">
          <div class="img">
            <img src="../../assets/quote_bg.svg" alt="">
            <img :src="review.user_portrait" alt="">
          </div>

          <h4 class="tex1">{{ review.title }}</h4>
          <div class="tex2">{{ review.des }}</div>

          <div class="author">
<!--            <h5 class="tex3"> {{ review.user_portrait }} </h5>-->
            <div class="tex4">{{ review.date }}</div>
            <div class="tex4">{{ review.time }}</div>

          </div>
        </div>
        </div>

        <template #arrow="{ prev, next }">
          <div class="custom-arrow">
            <button type="button" class="custom-arrow--left" @click="prev">
              <n-icon><ArrowBack/></n-icon>
            </button>
            <button type="button" class="custom-arrow--right" @click="next">
              <n-icon><ArrowForward /></n-icon>
            </button>
          </div>
        </template>
        <template #dots="{ total, currentIndex, to }">
          <ul class="custom-dots">
            <li
                v-for="index of total"
                :key="index"
                :class="{ ['is-active']: currentIndex === index - 1 }"
                @click="to(index - 1)"
            />
          </ul>
        </template>

      </n-carousel>

    </div>


  </section>

</template>

<script>
import {ArrowBack, ArrowForward} from "@vicons/ionicons5";

export default {
  components: {ArrowBack, ArrowForward},
  name: "customerReview",
  data() {
    return {
      reviews: []  // 保存从后端获取到的数据
    }
  },
  mounted() {
    this.axios.get('/homepage/most_popular_comments')
        .then(response => {
          this.reviews = response.data.data;

          console.log(this.reviews)
        })
        .catch(error => {
          console.error(error);
        });
  }
}
</script>

<style scoped>
.block{
  position: relative;
  z-index: 0;

  padding-top: 120px;
  padding-bottom: 60px;

}

.bgC{
  position: absolute;
  top: 0;
  height: 100%;
  z-index: -1;

  flex:0 0 auto;
  /*width:100%;*/

  background-image: url('../../assets/customerBg.png');
  background-repeat: no-repeat;
  background-position: center center;
  width: 100%;
  /*height: 100vh;*/
}

.tit{
  justify-content: center !important;
  text-align: center;

  flex:0 0 auto;width:auto;
}

.t1{
  font-family: JostBlod;
  font-size: 30px;
}

.t2{
  color: #757272;
}

.CRContainer{
  /*width:100%;*/
  width: 500px;
  padding-right:15px;
  padding-left: 15px;
  margin-right:auto;
  margin-left:auto
}


@media (min-width:576px){
  .CRContainer{
    max-width:540px
  }
}

@media (min-width:768px){
  .CRContainer{max-width:720px}
}

@media (min-width:992px){
  .CRContainer{max-width:960px}
}

@media (min-width:1200px){
  .CRContainer{
    max-width:1140px
  }
}

@media (min-width:1400px){
  .CRContainer{
    max-width:1320px
  }
}


.img{
  display: flex;
  justify-content: center;
  align-items: center;
}

.img img:nth-child(2){
  position: absolute;
  z-index: 1;
  width: 96px;
  height: 96px;
  -o-object-fit: cover;
  object-fit: cover;
}

/*自定义轮播按键*/
.custom-arrow {
  display: flex;
  position: absolute;
  /*margin-left: 210px;*/
  margin-left: 150px;
  bottom: 4px;
}

.custom-arrow button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;

  /*margin-right: 12px;*/
  margin-right: 142px;
  color: #000;
  background-color: rgba(0, 0, 0, 0.1);
  border-width: 0;
  border-radius: 8px;
  transition: background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  cursor: pointer;
}

.custom-arrow button:hover {
  background-color: rgba(0, 0, 0, 0.2);
}

.custom-arrow button:active {
  transform: scale(0.95);
  transform-origin: center;
}

.custom-dots {
  display: flex;
  /*margin: 0;*/
  padding: 0;
  position: absolute;
  bottom: 0;
  margin-left: 188px;
  /*right: 0;*/
}

.custom-dots li {
  display: inline-block;
  width: 12px;
  height: 4px;
  margin: 0 3px;
  border-radius: 4px;
  background-color: rgba(0, 0, 0, 0.4);
  transition: width 0.3s, background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  cursor: pointer;
}

.custom-dots li.is-active {
  width: 40px;
  background: #3554D1;
}

.con{
  text-align: center;
  height: 490px;
}

.tex1{
  font-size: 16px;
  font-weight: 700;
  color: #3554D1;
}

.tex2{
  font-weight: 500;
  color: #051036;
  margin-top: 20px;
}

.author{
  margin-top: 40px
}

.tex3{
  font-size: 15px;
  line-height: 1.4 ;
  font-weight: 800;
}

.tex4{
  font-weight: 450;
  font-size: 14px;
  color: #697488;
  margin-top: 5px;
  font-family: JosT;
}

@media screen and (max-width: 550px) {
  .CRContainer{
    width: 100%;
    padding: 0;
  }
  .custom-arrow{
    width: 100%;
    margin: 0;
    position: static;
  }
  .tex2{
    padding: 15px
  }
}

</style>

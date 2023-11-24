<template>

<section class="mostPopularLayout-pt mostPopularLayout-pb">
  <div class="container">
    <div class="most-popular-contents" data-gap="30" data-slider-cols="xl-5 lg-4 md-2 sm-2 base-1" data-nav-prev="js-team-prev" data-pagination="js-team-pag" data-nav-next="js-team-next">
      <n-carousel :slides-per-view=slides_per_view :space-between=space_between :loop="false" show-arrow>
        <div v-for="item in discountData" class="tourItem">
          <n-carousel show-arrow autoplay :space-between="2">
          <img v-for="pic in item.banners"
              class="carousel-img"
              :src="pic"
          >
          <template #arrow="{ prev, next }">
            <div class="custom-arrow">
              <button type="button" class="custom-arrow--left" @click="prev">
                <n-icon><ArrowBack /></n-icon>
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
          <n-card>
            <div class="tourCardContent">
              <div class="tourCardTime">
                <div class="hours"></div>
                <div class="dot"></div>
                <div class="days">{{item.duration}}</div>
              </div>

              <h4 class="tourCardTitle" @click="this.$router.push('/trip/' + item.id)">
                <span>{{item.name}}</span>
              </h4>

              <p class="tourCardText">{{item.raw_pic}}</p>

              <div class="row starsLayout">
                <div class="col-auto">
                  <div class="starsBefore">
                    <div class="stars">

                      <div class="icon-star iconStar"></div>

                      <div class="icon-star iconStar"></div>

                      <div class="icon-star iconStar"></div>

                      <div class="icon-star iconStar"></div>

                      <div class="icon-star iconStar"></div>

                    </div>

                    <div class="review">{{item.reviews + $t('discount.review')}} </div>
                  </div>
                </div>

                <div class="col-auto">
                  <div class="footer">
                    {{ $t('discount.from') }}
                    <span class="price">{{'$' + item.price.toFixed(2)}}</span>
                  </div>
                </div>
              </div>
            </div>
          </n-card>
        </div>

      </n-carousel>
    </div>

  </div>



</section>

</template>

<script>
import { ArrowBack, ArrowForward } from '@vicons/ionicons5'
import {defineComponent, onMounted, ref} from 'vue'
export default {
  props:['discountData'],
  components: {
    ArrowBack,
    ArrowForward
  },
  name: "discountItems",

  data() {
    return {
      windowWidth: document.documentElement.clientWidth,
    }
  },
  setup() {
    let slides_per_view= ref(5);
    let space_between = ref(20);
    window.fullWidth = document.documentElement.clientWidth;
    if (window.fullWidth < 700) {
      slides_per_view.value = 2;
      space_between.value = 15;
    } else if (window.fullWidth < 768) {
      slides_per_view.value = 2;
      space_between.value = 20;
    } else if (window.fullWidth >= 768) {
      slides_per_view.value = 3;
      space_between.value = 20;
    }
    onMounted(()=>{
      window.addEventListener( 'resize', () => {
        window.fullWidth = document.documentElement.clientWidth;
        // that.windowWidth = window.fullWidth; // 宽
        if (window.fullWidth < 700) {
          slides_per_view.value = 2;
          space_between.value = 15;
        } else if (window.fullWidth < 768) {
          slides_per_view.value = 2;
          space_between.value = 20;
        } else if (window.fullWidth >= 768) {
          slides_per_view.value = 3;
          space_between.value = 20;
        }
      });
    })
    return{
      slides_per_view,
      space_between
    }
  },
}
</script>

<style scoped>
.carousel-img {
  border-radius: 8px;
  width: 243px;
  height: 243px;
  object-fit: cover;
}
.custom-arrow--right {
  display: flex;
  position: absolute;
  bottom: 113px;
  right: 0px;
}
.custom-arrow--left {
  display: flex;
  position: absolute;
  bottom: 113px;
  left: 10px;
}
.tourItem:hover .tourCardTitle span{
  background-image: linear-gradient(transparent 24px, black 20px);
  background-size: 100%;
  background-repeat: no-repeat;
  transition: background-size 0.3s cubic-bezier(0.785, 0.135, 0.15, 0.86) 0s;
}
.tourItem .carousel-img{
  border-radius: 4px;
  transition: scale 0.3s cubic-bezier(0.785, 0.135, 0.15, 0.86) 0s;
}
.tourItem:hover .carousel-img{
  scale: 1.15;
  transition: scale 0.3s cubic-bezier(0.785, 0.135, 0.15, 0.86) 0s;
}
/*@media (max-width: 1410px) {*/
/*  .carousel-img {*/
/*    width: 350px;*/
/*    height: 350px;*/
/*  }*/
/*  .custom-arrow--left {*/
/*    bottom: 175px;*/
/*    left: 7.5px;*/
/*  }*/
/*  .custom-arrow--right {*/
/*    bottom: 175px;*/
/*    right: 7.5px;*/
/*  }*/
/*}*/

/*@media (max-width: 1200px) {*/
/*  .carousel-img {*/
/*    width: 300px;*/
/*    height: 300px;*/
/*  }*/
/*  .custom-arrow--left {*/
/*    bottom: 150px;*/
/*    left: 7.5px;*/
/*  }*/
/*  .custom-arrow--right {*/
/*    bottom: 150px;*/
/*    right: 7.5px;*/
/*  }*/
/*}*/

/*@media (max-width: 1000px) {*/
/*  .carousel-img {*/
/*    width: 250px;*/
/*    height: 250px;*/
/*  }*/
/*  .custom-arrow--left {*/
/*    bottom: 125px;*/
/*    left: 7.5px;*/
/*  }*/
/*  .custom-arrow--right {*/
/*    bottom: 125px;*/
/*    right: 7.5px;*/
/*  }*/
/*}*/

/*@media (max-width: 780px) {*/
/*  .carousel-img {*/
/*    width: 200px;*/
/*    height: 200px;*/
/*  }*/
/*  .custom-arrow--left {*/
/*    bottom: 100px;*/
/*    left: 7.5px;*/
/*  }*/
/*  .custom-arrow--right {*/
/*    bottom: 100px;*/
/*    right: 7.5px;*/
/*  }*/
/*  .hours {*/
/*    font-size: 7px !important;*/
/*    color: #697488;*/
/*  }*/
/*  .dot {*/
/*    flex-shrink: 0;*/
/*    width: 1.5px;*/
/*    height: 1.5px;*/
/*    background-color: #697488 !important;*/
/*    border-radius: 100%;*/
/*    margin-left: 10px !important;*/
/*    margin-right: 10px !important;*/

/*  }*/
/*  .days {*/
/*    font-size: 7px !important;*/
/*    color: #697488;*/
/*  }*/
/*  .tourCardTitle {*/
/*    color: #051036;*/
/*    font-size: 9px !important;*/
/*    line-height: 1.6 !important;*/
/*    font-weight: 500;*/
/*  }*/
/*  .tourCardText {*/
/*    color: #697488;*/
/*    line-height: 1.4 !important;*/
/*    font-size: 7px !important;*/
/*    margin-top: 5px !important;*/
/*  }*/

/*}*/

.custom-arrow button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;
  margin-right: 12px;
  color: #000;
  background-color: #fff;
  border-width: 0;
  border-radius: 8px;
  transition: background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  cursor: pointer;
}

.custom-arrow button:hover {
  background-color: #3554D1;
}

.custom-arrow button:hover {
  color: #fff;
}

.custom-arrow button:active {
  transform: scale(0.95);
  transform-origin: center;
}

.custom-dots {
  display: flex;
  margin: 0;
  padding: 0;
  position: absolute;
  top: 20px;
  left: 20px;
}

.custom-dots li {
  display: inline-block;
  width: 12px;
  height: 4px;
  margin: 0 3px;
  border-radius: 4px;
  background-color: rgba(255, 255, 255, 0.4);
  transition: width 0.3s, background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  cursor: pointer;
}

.custom-dots li.is-active {
  width: 40px;
  background: #fff;
}

.row {
  --bs-gutter-x:30px;
  --bs-gutter-y:0;
  display:flex;
  flex-wrap:wrap;
  margin-top:calc(var(--bs-gutter-y)*-1);
  margin-right:calc(var(--bs-gutter-x)*-0.5);
  margin-left:calc(var(--bs-gutter-x)*-0.5)
}

.tourCardContent {
  margin-top: 10px !important;
}

.tourCardTime {
  display: flex !important;
  align-items: center !important;
  line-height: 1.4 !important;
  margin-bottom: 5px !important;
}

.hours {
  font-size: 14px;
  color: #697488;
}

.dot {
  flex-shrink: 0;
  width: 3px;
  height: 3px;
  background-color: #697488 !important;
  border-radius: 100%;
  margin-left: 10px !important;
  margin-right: 10px !important;

}

.days {
  font-size: 14px;
  color: #697488;
}

.tourCardTitle {
  color: #051036;
  font-size: 18px;
  line-height: 1.6 !important;
  font-weight: 500;
  cursor: pointer;
}
.tourCardTitle span{
  background-image: linear-gradient(transparent 24px, black 20px);
  background-size: 0;
  background-repeat: no-repeat;
  transition: background-size 0.3s cubic-bezier(0.785, 0.135, 0.15, 0.86) 0s;
}
.tourCardText {
  color: #697488;
  line-height: 1.4 !important;
  font-size: 14px;
  margin-top: 5px !important;
}

.starsLayout {
  justify-content: space-between;
  align-items: center;
  padding-top: 15px;
}

.starsBefore {
  display: flex !important;
  align-items: center !important;
}

.stars {
  display: flex !important;
  align-items: center !important;
  margin-left: -2.5px;
  margin-right: -2.5px;
}

.iconStar {
  color: #F8D448;
  font-size: 10px !important;
}

.review {
  font-size: 14px;
  color: #697488;
  margin-left: 10px;

}

.footer {
  font-size: 14px;
  color: #697488;
}

.price {
  font-size: 16px;
  font-weight: 500;
  color: #051036;
}

@media screen and (max-width: 1200px) {
  .mostPopularLayout-pb{
    margin-top: 20px;
  }
}
.container {
  width:770px;
  padding-right:var(--bs-gutter-x,15px);
  padding-left:var(--bs-gutter-x,15px);
  margin-right:auto;
  margin-left:auto
}

@media screen and (max-width: 1200px) {
  .container{
    width: 960px;
  }
  .carousel-img{
    width: 305px;
    height: 305px;
  }
}
@media screen and (max-width: 991px) {
  .container{
    width: 720px;
  }
  .carousel-img{
    width: 225px;
    height: 225px;
  }
}
@media screen and (max-width: 767px) {
  .container{
    width: 540px;
  }
  .carousel-img{
    width: 260px;
    height: 260px;
  }
}
@media screen and (max-width: 600px) {
  .container{
    padding: 0px;
  }
}
@media screen and (max-width: 550px) {
  .container{
    width: 450px;
  }
  .carousel-img{
    width: 215px;
    height: 215px;
  }
}
@media screen and (max-width: 480px) {
  .container{
    width: 420px;
  }
  .carousel-img{
    width: 200px;
    height: 200px;
  }
  .tourCardTitle{
    font-size: 14px;
    margin-top: 5px;
    margin-bottom: 5px;

  }
  .starsLayout{
    padding-top: 0px;
  }
  .review{
    margin-left: 5px;
  }
  .row.starsLayout{
    flex-direction: column;
    align-items: flex-start;
    margin-left: 0px;
  }
}
@media screen and (max-width: 430px) {
  .container{
    width: 350px;
  }
  .carousel-img{
    width: 168px;
    height: 168px;
  }

}
</style>

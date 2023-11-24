<template>

<section class="mostPopularLayout-pt mostPopularLayout-pb">
  <div class="container">
    <div class="mostPopularHead">
      <div class="col-auto">
        <div class="sectionTitle -md">
          <h2 class="sectionTitle__title">{{$t('mostPopularTours.most')}}</h2>
          <p class="sectionTitle__text">{{$t('mostPopularTours.choose')}}</p>
        </div>

        <div class="col-auto">
          <a class="button -md -blue-1 bg-blue-1-05 text-blue-1" @click="handleSearchPopular">
            {{ $t('mostPopularTours.more') }} <div class="icon"></div>
          </a>
        </div>
      </div>
    </div>

    <div class="most-popular-contents" data-gap="30" data-slider-cols="xl-5 lg-4 md-2 sm-2 base-1" data-nav-prev="js-team-prev" data-pagination="js-team-pag" data-nav-next="js-team-next">
      <n-carousel :slides-per-view=slides_per_view :space-between=space_between :loop="false" show-arrow>
        <div v-for="popular in populars" :key="popular.id">
          <n-carousel show-arrow autoplay :space-between="2">
            <img v-for="pic in popular.banners"
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
                <div class="hours">{{ popular.duration }}</div>
                <div class="dot"></div>
                <div class="days">{{ popular.types[0] }}</div>
              </div>

              <h4 class="tourCardTitle" @click="this.$router.push('/trip/' + popular.id)">
                <span>{{ popular.name }}</span>
              </h4>

              <p class="tourCardText">{{ popular.raw_loc }}</p>

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

                    <div class="review">{{ $t('mostPopularTours.reviews', {reviews: popular.reviews}) }}</div>
                  </div>
                </div>

                <div class="col-auto">
                  <div class="footer">
                    {{ $t('mostPopularTours.from') }}
                    <span class="price">US${{ popular.price.toFixed(2) }}</span>
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
import {getCurrentInstance} from 'vue'
import {defineComponent, onMounted, ref} from 'vue'
import {useRouter} from 'vue-router';
export default {
  components: {
    ArrowBack,
    ArrowForward
  },
  name: "mostPopularTours",
  data() {
    return {
      windowWidth: document.documentElement.clientWidth,
      populars: []
    }
  },
  setup() {
    let populars = ref({});
    const route = useRouter();
    const axios = getCurrentInstance().appContext.config.globalProperties.axios;
    axios.get('/homepage/most_popular_products')
        .then(response => {
          populars.value = response.data.products;
          for(let i = 0; i < populars.value.length; i++){
            let raw_time = populars.value[i].duration;
            let hour = Math.round(raw_time/3600);
            let day = Math.round(hour/24);
            if (hour > 24 && day === 1){
              populars.value[i].duration = '1 Day'
            }
            if (hour > 24 && day > 1){
              populars.value[i].duration = day + ' Days'
            }
            if (hour === 1){
              populars.value[i].duration = '1 Hour'
            }
            if (hour < 24 && hour !== 1){
              populars.value[i].duration = hour + ' Hours'
            }
          }
        })
        .catch(error => {
          console.error(error);
        });
    let slides_per_view= ref(3);
    let space_between = ref(20);
    window.fullWidth = document.documentElement.clientWidth;
    if (window.fullWidth < 550) {
      slides_per_view.value = 1;
      space_between.value = 0;
    } else if (window.fullWidth <= 700) {
      slides_per_view.value = 2;
      space_between.value = 13;
    } else if (window.fullWidth <= 900) {
      slides_per_view.value = 2;
      space_between.value = 15;
    } else if (window.fullWidth <= 1100) {
      slides_per_view.value = 3;
      space_between.value = 15;
    } else if (window.fullWidth >= 1100) {
      slides_per_view.value = 3;
      space_between.value = 20;
    }
    onMounted(()=>{
      window.addEventListener( 'resize', () => {
        window.fullWidth = document.documentElement.clientWidth;
        // that.windowWidth = window.fullWidth; // 宽
        if (window.fullWidth < 550) {
          slides_per_view.value = 1;
          space_between.value = 0;
        } else if (window.fullWidth <= 700) {
          slides_per_view.value = 2;
          space_between.value = 13;
        } else if (window.fullWidth <= 900) {
          slides_per_view.value = 2;
          space_between.value = 15;
        } else if (window.fullWidth <= 1100) {
          slides_per_view.value = 3;
          space_between.value = 15;
        } else if (window.fullWidth >= 1100) {
          slides_per_view.value = 3;
          space_between.value = 20;
        }
      });
    })
    return{
      slides_per_view,
      space_between,
      populars,
      route,
    }
  },
  methods: {
    handleSearchPopular() {
      this.route.push({ name: 'more', params: { type: 'popular' } });
    }
  }
}
</script>

<style scoped>
.carousel-img {
  border-radius: 8px;
  width: 427px;
  height: 450px;
  object-fit: cover;
}
.custom-arrow--right {
  display: flex;
  position: absolute;
  bottom: 225px;
  right: 10px;
}
.custom-arrow--left {
  display: flex;
  position: absolute;
  bottom: 225px;
  left: 10px;
}

.mostPopularHead {
  --bs-gutter-x:30px;
  --bs-gutter-y:0;
  display:flex;
  flex-wrap:wrap;
  margin-top:calc(var(--bs-gutter-y)*-1);
  margin-right:calc(var(--bs-gutter-x)*-0.5);
  margin-left:calc(var(--bs-gutter-x)*-0);
  margin-top: -10px;
  margin-bottom: -10px;
  justify-content: space-between !important;
  align-items: flex-end !important;
}

@media (max-width: 1399px) {
  .carousel-img {
    width: 367px;
    height: 367px;
  }
  .custom-arrow--left {
    bottom: 175px;
    left: 7.5px;
  }
  .custom-arrow--right {
    bottom: 175px;
    right: 7.5px;
  }
}

@media (max-width: 1200px) {
  .carousel-img {
    width: 306.66px;
    height: 300px;
  }
  .custom-arrow--left {
    bottom: 135px;
    left: 7.5px;
  }
  .custom-arrow--right {
    bottom: 135px;
    right: 7.5px;
  }
}

@media (max-width: 1000px) {
  .carousel-img {
    width: 228px;
    height: 228px;
  }
  .custom-arrow--left {
    bottom: 105px;
    left: 7.5px;
  }
  .custom-arrow--right {
    bottom: 105px;
    right: 7.5px;
  }
}

@media (max-width: 900px) {
  .carousel-img {
    width: 350px;
    height: 350px;
  }
  .custom-arrow--left {
    bottom: 155px;
    left: 7.5px;
  }
  .custom-arrow--right {
    bottom: 155px;
    right: 7.5px;
  }
  .hours {
    font-size: 7px !important;
    color: #697488;
  }
  .dot {
    flex-shrink: 0;
    width: 1.5px;
    height: 1.5px;
    background-color: #697488 !important;
    border-radius: 100%;
    margin-left: 10px !important;
    margin-right: 10px !important;

  }
  .days {
    font-size: 7px !important;
    color: #697488;
  }
  .tourCardTitle {
    color: #051036;
    font-size: 9px !important;
    line-height: 1.6 !important;
    font-weight: 500;
  }
  .tourCardText {
    color: #697488;
    line-height: 1.4 !important;
    font-size: 7px !important;
    margin-top: 5px !important;
  }
}

@media screen and (max-width: 768px) {
  .carousel-img {
    width: 260px;
    height: 260px;
  }
  .custom-arrow--left {
    bottom: 110px;
    left: 7.5px;
  }
  .custom-arrow--right {
    bottom: 110px;
    right: 7.5px;
  }
}

@media screen and (max-width: 650px) {
  .carousel-img {
    width: 262px;
    height: 262px;
  }
  .custom-arrow--left {
    bottom: 115px;
    left: 7.5px;
  }
  .custom-arrow--right {
    bottom: 115px;
    right: 7.5px;
  }
  .mostPopularHead {
  }
}

@media screen and (max-width: 550px) {
  .carousel-img {
    width: 398px;
    height: 398px;
  }
  .custom-arrow--left {
    bottom: 185px;
    left: 7.5px;
  }
  .custom-arrow--right {
    bottom: 185px;
    right: 7.5px;
  }
  .mostPopularHead {
    margin-left: -35px;
  }
  .sectionTitle__title {
    margin: auto;
  }
}

@media screen and (max-width: 450px) {
  .carousel-img {
    width: 300px;
    height: 300px;
  }
  .custom-arrow--left {
    bottom: 135px;
    left: 7.5px;
  }
  .custom-arrow--right {
    bottom: 135px;
    right: 7.5px;
  }
  .mostPopularHead {
    margin-left: 0px;
  }
}

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

.tourCardText {
  color: #697488;
  line-height: 1.4 !important;
  font-size: 14px;
  margin-top: 5px !important;
}

.starsLayout {
  justify-content: space-between !important;
  align-items: center !important;
  padding-top: 15px !important;
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
  font-size: 14px !important;
  color: #697488;
  margin-left: 10px !important;

}

.footer {
  font-size: 14px !important;
  color: #697488;
}

.price {
  font-size: 16px !important;
  font-weight: 500;
  color: #051036;
}

.most-popular-contents {
  overflow: hidden !important;
  padding-top: 40px !important;
}

.mostPopularLayout-pt {
  padding-top: 120px;
}

.mostPopularLayout-pb {
  padding-bottom: 60px;
}


@media (max-width: 767px) {
  .mostPopularLayout-pt {
    padding-top: 50px;
  }
  .mostPopularLayout-pb {
    padding-bottom: 100px;
  }
}

@media (max-width: 575px) {
  .mostPopularLayout-pt {
    padding-top: 20px;
  }
  .mostPopularLayout-pb {
    padding-bottom: 60px;
  }
}



.container {
  width:100%;
  padding-right:var(--bs-gutter-x,15px);
  padding-left:var(--bs-gutter-x,15px);
  margin-right:auto;
  margin-left:auto
}
@media (min-width:350px){
  .container{
    padding-left: 0px;
    max-width: 330px;
  }
}


@media (min-width:450px){
  .container{
    max-width:400px;
    padding-left: 20px;
  }
}
@media (min-width:550px){
  .container{
    max-width:540px;
    padding-left: 0px;
  }
}

@media (min-width:768px){
  .container{
    max-width:720px
  }
}

@media (min-width:1000px){
  .container{max-width:960px}
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

.sectionTitle.-md .sectionTitle__title {
  font-size: 30px;
}

@media (max-width: 767px) {
  .sectionTitle.-md .sectionTitle__title {
    font-size: 26px;
  }
}

.col-auto {
  flex:0 0 auto;
  width:auto
}

.sectionTitle__text {
  margin-top: 5px !important;
  color: #697488;
}

@media (max-width: 575px) {
  .sectionTitle__text {
    margin-top: 0px !important;
    color: #697488;
  }
}

.button {
  display: flex;
  align-items: center;
  justify-content: center;
  vertical-align: middle;
  text-align: center;
  line-height: 1;
  font-weight: 500;
  font-size: 15px;
  line-height: 1.2;
  border-radius: 4px;
  border: 1px solid transparent;
  transition: all 0.3s cubic-bezier(0.165, 0.84, 0.44, 1);
}

.button.-blue-1:hover {
  border-color: #3554D1;
  background-color: #3554D1 !important;
  color: white !important;
}

.button.-md {
  padding: 14px 30px;
}

.button.-blue-1:hover {
  border-color: #3554D1;
  background-color: #3554D1 !important;
  color: white !important;
}

.bg-blue-1-05 {
  background-color: rgba(53, 84, 209, 0.05);
}

.text-blue-1 {
  color: #3554D1;
}

</style>

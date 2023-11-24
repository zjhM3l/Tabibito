<template>

  <section class="chooseLayout-pt chooseLayout-pb" style="overflow: hidden">
    <div class="container">
      <div class="row chooseHead y-gap-20">
        <div class="col-auto">
            <h2 class="sectionTitle">{{ $t('chooseTourTypes.choose')}}</h2>
            <p class="sectionText">{{ $t('chooseTourTypes.choose1')}}</p>
        </div>
      </div>

      <div class="chooseCards">
        <n-carousel :slides-per-view=slides_per_view :space-between=space_between :loop="false">
          <div @click="handleWT">
          <n-card title="" class="tourTypeCard">
            <div class="cardContent">
              <a class="cardHref">
                <div class="tourTypeCardContent">
                  <n-icon class="icon"><Leaf /></n-icon>
                  <h4 class="cardText">{{ $t('chooseTourTypes.wildlifeTour') }}</h4>
                  <p class="cardPrice">{{ $t('chooseTourTypes.5ToursFrom550') }}</p>
                </div>
              </a>
            </div>
          </n-card>
          </div>
          <div @click="handleAT">
          <n-card title="" class="tourTypeCard">
            <div class="cardContent">
              <a class="cardHref">
                <div class="tourTypeCardContent">
                  <n-icon class="icon"><Bonfire /></n-icon>
                  <h4 class="cardText">{{ $t('chooseTourTypes.adventureTour') }}</h4>
                  <p class="cardPrice">{{ $t('chooseTourTypes.5ToursFrom550') }}</p>
                </div>
              </a>
            </div>
          </n-card>
          </div>
          <div @click="handleCT">
          <n-card title="" class="tourTypeCard">
            <div class="cardContent">
              <a class="cardHref">
                <div class="tourTypeCardContent">
                  <n-icon class="icon"><CarSport /></n-icon>
                  <h4 class="cardText">{{ $t('chooseTourTypes.cityTours') }}</h4>
                  <p class="cardPrice">{{ $t('chooseTourTypes.5ToursFrom550') }}</p>
                </div>
              </a>
            </div>
          </n-card>
          </div>
          <div @click="handleMT">
          <n-card title="" class="tourTypeCard" >
            <div class="cardContent">
              <a class="cardHref">
                <div class="tourTypeCardContent">
                  <n-icon class="icon"><Business /></n-icon>
                  <h4 class="cardText">{{ $t('chooseTourTypes.museumTours') }}</h4>
                  <p class="cardPrice">{{ $t('chooseTourTypes.5ToursFrom550') }}</p>
                </div>
              </a>
            </div>
          </n-card>
          </div>
          <div @click="handleBT">
          <n-card title="" class="tourTypeCard">
            <div class="cardContent">
              <a class="cardHref">
                <div class="tourTypeCardContent">
                  <n-icon class="icon"><Boat /></n-icon>
                  <h4 class="cardText">{{ $t('chooseTourTypes.beachesTour') }}</h4>
                  <p class="cardPrice">{{ $t('chooseTourTypes.5ToursFrom550') }}</p>
                </div>
              </a>
            </div>
          </n-card>
          </div>
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
      </div>
    </div>
  </section>

</template>

<script>
import { ArrowBack, ArrowForward, Leaf, Boat, Bonfire, Business, CarSport } from '@vicons/ionicons5'
import {defineComponent, onMounted, ref} from 'vue'
import {useRouter} from "vue-router";
export default {
  components: {
    ArrowBack,
    ArrowForward,
    Leaf,
    Boat,
    Bonfire,
    Business,
    CarSport
  },
  name: "chooseTourTypes",
  data() {
    return {
      windowWidth: document.documentElement.clientWidth,
    }
  },
  setup() {
    const route = useRouter();
    let slides_per_view= ref(5);
    let space_between = ref(20);
    window.fullWidth = document.documentElement.clientWidth;
    if (window.fullWidth < 500) {
      slides_per_view.value = 2;
      space_between.value = 7;
    } else if (window.fullWidth < 400) {
      slides_per_view.value = 2;
      space_between.value = 10;
    } else if (window.fullWidth < 500) {
      slides_per_view.value = 3;
      space_between.value = 10;
    } else if (window.fullWidth < 700) {
      slides_per_view.value = 3;
      space_between.value = 15;
    } else if (window.fullWidth < 900) {
      slides_per_view.value = 4;
      space_between.value = 15;
    } else if (window.fullWidth < 1100) {
      slides_per_view.value = 4;
      space_between.value = 20;
    } else if (window.fullWidth >= 1100) {
      slides_per_view.value = 5;
      space_between.value = 20;
    }
    onMounted(()=>{
      window.addEventListener( 'resize', () => {
        window.fullWidth = document.documentElement.clientWidth;
        // that.windowWidth = window.fullWidth; // 宽
        if (window.fullWidth < 400) {
          slides_per_view.value = 2;
          space_between.value = 10;
        } else if (window.fullWidth < 500) {
          slides_per_view.value = 3;
          space_between.value = 10;
        } else if (window.fullWidth < 700) {
          slides_per_view.value = 3;
          space_between.value = 15;
        } else if (window.fullWidth < 900) {
          slides_per_view.value = 4;
          space_between.value = 15;
        } else if (window.fullWidth < 1100) {
          slides_per_view.value = 4;
          space_between.value = 20;
        } else if (window.fullWidth >= 1100) {
          slides_per_view.value = 5;
          space_between.value = 20;
        }
      });
    })
    return{
      slides_per_view,
      route,
      space_between,
      handleWT() {
        this.route.push({
          path: '/moreView',
          query: {
            type: "type",
            value: "WildlifeTour"
          }
        })
      },
      handleAT() {
        this.route.push({
          path: '/moreView',
          query: {
            type: "type",
            value: "AdventureTour"
          }
        })
      },
      handleCT() {
        this.route.push({
          path: '/moreView',
          query: {
            type: "type",
            value: "CityTour"
          }
        })
      },
      handleMT() {
        this.route.push({
          path: '/moreView',
          query: {
            type: "type",
            value: "MuseumTour"
          }
        })
      },
      handleBT() {
        this.route.push({
          path: '/moreView',
          query: {
            type: "type",
            value: "BeachesTour"
          }
        })
      },
    }
  },

}

</script>

<style scoped>
.cardContent {
  width: auto;
  height: auto;
}

.tourTypeCardContent {
  text-align: center;
}

@media (max-width: 1050px) {
  .cardContent {
    /*width: 150px;*/
    height: 230px;
  }
  .cardText {
    color: #051036;
    font-size: 10px;
    font-weight: 300;
    margin-top: 50px;
  }
  .cardPrice {
    color: #697488;
    line-height: 1.4;
    font-size: 8px;
    margin-top: 5px;
  }
}

@media (max-width: 775px) {
  .cardContent {
    /*width: 100px;*/
    height: 230px;
  }
  .cardText {
    color: #051036;
    font-size: 8px;
    font-weight: 300;
    margin-top: 50px;
  }
  .cardPrice {
    color: #697488;
    line-height: 1.4;
    font-size: 5px;
    margin-top: 5px;
  }
}

.cardText {
  color: #051036;
  font-size: 18px;
  font-weight: 500;
  margin-top: 50px;
}

@media (max-width: 575px) {
  .cardContent {
    /*width: 75px;*/
    height: 230px;
  }

  .tourTypeCardContent {
    padding-top: 0px;
  }
  .cardText {
    color: #051036;
    font-size: 8px;
    font-weight: 300;
    margin-top: 20px;
  }
  .cardPrice {
    color: #697488;
    line-height: 1.4;
    font-size: 5px;
    margin-top: 5px;
  }
}

.cardText {
  color: #051036;
  font-size: 18px;
  font-weight: 500;
  margin-top: 50px;
}



.cardPrice {
  color: #697488;
  line-height: 1.4;
  font-size: 14px;
  margin-top: 5px;
}

.custom-arrow--right {
  display: flex;
  position: absolute;
  top: 10px;
  left: 180px;
}

.custom-arrow--left {
  display: flex;
  position: absolute;
  top: 10px;
  left: 10px;
}

.custom-dots {
  display: flex;
  margin: 0;
  padding: 0;
  position: absolute;
  top: 20px;
  left: 50px;
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
  color: rebeccapurple;
}

.custom-arrow button:active {
  transform: scale(0.95);
  transform-origin: center;
}

.custom-dots li {
  display: inline-block;
  width: 12px;
  height: 4px;
  margin: 0 3px;
  border-radius: 4px;
  background-color: gainsboro;
  transition: width 0.3s, background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  cursor: pointer;
}

.custom-dots li.is-active {
  width: 40px;
  background: #3d61f1;
}

.cardHref {
  text-decoration: none;
}

.icon {
  font-size: 60px !important;
  color: #3554D1;
}

@media (max-width: 575px) {
  .icon {
    font-size: 40px !important;
    color: #3554D1;
  }
}

.tourTypeCard {
  transition: all 0.3s cubic-bezier(0.165, 0.84, 0.44, 1);
  display: block !important;
  border-radius: 4px;
  background-color: rgba(53, 84, 209, 0.05);
}

.tourTypeCard:hover{
  background-color: #68abf6;
  transform: scale(1.08); /* 放大到 1.2 倍 */

}

.chooseCards {
  position: relative;
  overflow: hidden !important;
  padding-top: 40px !important;
}

@media (max-width: 575px) {
  .chooseCards {
    padding-top: 20px !important;
  }
  .tourTypeCardContent{
    padding-top: 25px;
  }
}

.chooseLayout-pt {
  padding-top: 60px;
}

.chooseLayout-pb {
  padding-bottom: 60px;
}

@media (max-width: 767px) {
  .chooseLayout-pt {
    padding-top: 60px;
  }
  .chooseLayout-pb {
    padding-bottom: 60px;
  }
}

@media (max-width: 575px) {
  .chooseLayout-pt {
    padding-top: 30px;
  }
  .chooseLayout-pb {
    padding-bottom: 30px;
  }
}

.container {
  width:100%;
  padding-right:var(--bs-gutter-x,15px);
  padding-left:var(--bs-gutter-x,15px);
  margin-right:auto;
  margin-left:auto
}

@media (min-width:576px){
  .container{
    width: 95%;
    max-width:540px
  }
}

@media (min-width:768px){
  .container{max-width:720px}
}

@media (min-width:992px){
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

.row {
  --bs-gutter-x:30px;
  --bs-gutter-y:0;
  display:flex;
  flex-wrap:wrap;
  margin-top:calc(var(--bs-gutter-y)*-1);
  margin-right:calc(var(--bs-gutter-x)*-0.5);
  margin-left:calc(var(--bs-gutter-x)*-0.5)
}

.chooseHead {
  justify-content: space-between !important;
  align-items: flex-end !important;
}

.y-gap-20 {
  margin-top: -10px;
  margin-bottom: -10px;
}

.y-gap-20 > * {
  padding-top: 10px;
  padding-bottom: 10px;
}

.col-auto {
  flex:0 0 auto;
  width:auto
}

.sectionTitle {
  font-size: 30px;
}

@media (max-width: 767px) {
  .sectionTitle {
    font-size: 26px;
  }
}

.sectionText {
  margin-top: 5px !important;
  color: #697488;
}

@media (max-width: 575px) {
  .sectionText {
    font-size: 0px;
    color: #697488;
  }
  .sectionTitle {
    margin-left: 20px;
  }
}

</style>

<template>
  <div class="container">
    <div class="chargeListTitle" v-if="hasVideo">{{ $t('projectDetailPage.ChargeList.video')}}</div>
    <iframe v-if="hasVideo" class="iframe" :width=frame_width :height=frame_height :src=" 'https://www.youtube.com/embed/' + videoLink" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    <div v-if="hasVideo" class="divider"></div>
    <div class="chargeListTitle">{{ $t('projectDetailPage.weatherReport') }}</div>
    <div class="chargeList">
      <div class="weatherPart" v-for="day in this.weather">
        <div class="weatherTitleBar">
          <div class="city">{{day.city}}</div>
          <div class="date">{{day.date}}</div>
        </div>
        <div class="weatherMain">
          <div class="temperature">{{day.avg_temp.toFixed(0) + '℃'}}</div>
          <img :src="day.img_url" alt="" class="weatherImg">
        </div>
        <div class="forecast">
          <div class="foreTemp">
            <div class="tempValue">{{day.max_temp.toFixed(0) + '℃'}}</div>
            <div class="tempType">{{ $t('projectDetailPage.max') }}</div>
          </div>
          <div class="foreTemp">
            <div class="tempValue">{{day.avg_temp.toFixed(0) + '℃'}}</div>
            <div class="tempType">{{ $t('projectDetailPage.avg') }}</div>
          </div>
          <div class="foreTemp">
            <div class="tempValue">{{day.min_temp.toFixed(0) + '℃'}}</div>
            <div class="tempType">{{ $t('projectDetailPage.min') }}</div>
          </div>
        </div>
      </div>
    </div>

  <div class="divider"></div>
    <div class="chargeListTitle">{{ $t('projectDetailPage.ChargeList.title')}}</div>
    <div class="chargeList">
      <n-card :title="item.name" hoverable v-for="item in this.chargeListData">
        {{item.description}}
      </n-card>
    </div>
  <div class="divider"></div>
  </div>
  <itinerary-part></itinerary-part>
</template>

<script>
import ItineraryPart from "./itineraryPart.vue";
import {useRoute, useRouter} from "vue-router";
import {onMounted, ref} from "vue";
export default {
  name: "chargeList",
  components: {ItineraryPart},
  setup() {
    let frame_width = ref(560);
    let frame_height = ref(315);
    window.fullWidth = document.documentElement.clientWidth;
    if (window.fullWidth < 700) {
      frame_width.value = 340;
      frame_height.value = 192;
    } else if (window.fullWidth >= 700) {
      frame_width.value = 560;
      frame_height.value = 315;
    }
    onMounted(() => {
      window.addEventListener('resize', () => {
        window.fullWidth = document.documentElement.clientWidth;
        // that.windowWidth = window.fullWidth; // 宽
        if (window.fullWidth < 700) {
          frame_width.value = 340;
          frame_height.value = 192;
        } else if (window.fullWidth >= 700) {
          frame_width.value = 560;
          frame_height.value = 315;
        }
      });
    })
    return {
      frame_width,
      frame_height,
    }
  },
  created() {
    const route = useRoute();
    const router = useRouter();
    this.axios.post('/product/charge_detail', {
        product_id: route.params.trip_id
      })
        .then((res) => {
          if (res.status === 200){
            this.chargeListData = res.data.charges;
          }else {
            router.push('/404');
          }
        })
    this.axios.post('/product/detail', {
      product_id: route.params.trip_id
    })
        .then((res) => {
              if (res.status === 200){
                this.axios.post('/third/weather_forecast', {
                  location: res.data.location
                })
                    .then((wres) => {
                      if (wres.status === 200) {
                        this.weather = wres.data.weather;
                      }
                    })
              }
        })
    this.axios.post('/product/video', {
      product_id: route.params.trip_id
    })
        .then((res) => {
          if (res.status === 200){
            this.hasVideo = true;
            this.videoLink = res.data.video_link
          }
        })
  },
  data(){
    return{
      chargeListData: [],
      weather: [],
      videoLink: "",
      hasVideo: false
    }
  }
}
</script>

<style scoped>
.container{
  width: 1320px;
  margin: 0 auto;
}
.chargeListTitle{
  font-weight: 500;
  font-size: 22px;
  line-height: 1.45;
  margin: 20px 0;
}
.chargeList{
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  width: 100%;
}
.weatherPart{
  width: calc((100% - 200px - 48px - 48px) * 0.33);
  height: 232px;
  transition: .2s ease-in;
  border-radius: 4px;
  cursor: pointer;
  box-sizing: border-box;
  padding: 12px;
  background-color: #2F80ED;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.weatherTitleBar{
  display: flex;
  align-items: flex-end;
}
.date{
  color: white;
}
.city{
  font-weight: bold;
  color: white;
  box-sizing: border-box;
  padding-right: 12px;
  display: flex;
  align-items: center;
  font-size: 20px;
}
.weatherMain{
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-sizing: border-box;
}
.temperature {
  font-size: 48px;
  color: white;
}
.weatherImg{
  width: 60px;
  height: 60px;
  object-fit: contain;
  object-position: center;
}
.forecast{
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
}
.foreTemp{
  background-color: rgba(255, 255, 255, 0.4);
  border-radius: 6px;
  width: 30%;
  height: 30px;
  display: flex;
  color: white;
  align-items: center;
  justify-content: space-around;
}
.tempValue{
  font-size: 14px;
}
.tempType{
  font-size: 10px;
}
.weatherPart:hover{
  transition: .2s ease-out;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.12) ;
}
.n-card{
  width: 270px;
  margin-bottom: 10px;
}
.divider{
  max-width: 1320px;
  border-top: 1px solid #DDDDDD;
  margin: 40px auto;
}
@media (min-width:360px){
  .container{
    max-width:350px
  }
  /*.iframe{*/
  /*  width: 330px;*/
  /*  height: auto;*/
  /*}*/
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

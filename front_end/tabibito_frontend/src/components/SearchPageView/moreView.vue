<template>
  <navigation-bar class="zup"></navigation-bar>

  <div class="halfMap">
    <div class="list_content">
      <div class="row y-gap-20 contents_wrap">

        <div class="col-12">

          <div class="content_wrap">
            <div class="row x-gap-20 y-gap-20 card" v-for="item in products" :key="item.id">
              <div class="col-md-auto">

                <div class="content_left ratio ratio-1:1">
                  <div class="cardImage_content">
                    <img class="cardImage col-12" :src="item.cover">
                  </div>

                  <div class="cardImage_wish">
                    <n-button :loading=false @click="handleClick" strong secondary circle type="info">
                      <template #icon>
                        <n-icon><HeartOutline /></n-icon>
                      </template>
                    </n-button>
                  </div>
                </div>
              </div>

              <div class="col-md">
                <div class="d-flex flex-column h-full justify-between">
                  <div class="">
                    <p class="text-14 lh-14 mb-5 text-light-1">{{  item.location }}</p>
                    <h3 class="text-16 lh-16 fw-500">{{  item.title }}<br> {{ $t('moreView.garden') }}</h3>

                    <div class="row x-gap-5 items-center pt-5">
                      <div class="col-auto">
                        <div class="text-14 text-light-1">{{ $t('moreView.2Guests') }}</div>
                      </div>
                      <div class="col-auto round">
                        <div class="size-3 rounded-full bg-light-1"></div>
                      </div>
                      <div class="col-auto">
                        <div class="text-14 text-light-1">{{ $t('moreView.1Bedroom') }}</div>
                      </div>
                      <div class="col-auto round">
                        <div class="size-3 rounded-full bg-light-1"></div>
                      </div>
                      <div class="col-auto">
                        <div class="text-14 text-light-1">{{ $t('moreView.1Bed') }}</div>
                      </div>
                    </div>
                  </div>

                  <div class="row x-gap-10 y-gap-10 pt-20">

                    <div class="col-auto">
                      <div class="border-light rounded-100 py-5 px-20 text-14 lh-14">{{ $t('moreView.breakfast') }}</div>
                    </div>

                    <div class="col-auto">
                      <div class="border-light rounded-100 py-5 px-20 text-14 lh-14">WiFi</div>
                    </div>

                    <div class="col-auto">
                      <div class="border-light rounded-100 py-5 px-20 text-14 lh-14">{{ $t('moreView.spa') }}</div>
                    </div>

                    <div class="col-auto">
                      <div class="border-light rounded-100 py-5 px-20 text-14 lh-14">{{ $t('moreView.bar') }}</div>
                    </div>

                  </div>
                </div>
              </div>

              <div class="col-md-auto content_right">
                <div class="review-and-grade row x-gap-10 y-gap-10 justify-end items-center md:justify-start">
                  <div class="col-auto">
                    <div class="text-14 lh-14 fw-500">{{ $t('moreView.exceptional') }}</div>
                    <div class="text-14 lh-14 text-light-1">{{ $t('moreView.3014Reviews') }}</div>
                  </div>
                  <div class="col-auto">
                    <div class="star">4.8</div>
                  </div>
                </div>

                <div class="from">{{ $t('discount.from') }}</div>
                <div class="price">US${{ item.price.toFixed(2) }}</div>
                <div class="per">{{ $t('moreView.perAdult') }}</div>


                <a class="button -dark-1 btn_detail" @click="this.$router.push('/trip/' + item.id)">
                  {{ $t('moreView.viewDetail') }} <n-icon class="margin"><ArrowForward /></n-icon>
                </a>

              </div>

            </div>
          </div>
        </div>
      </div>

      <n-pagination
          v-model:page="morePage"
          :page-count="morePages"
          v-model:page-size="morePageSize"
          @update:page="handleChangePage"></n-pagination>

    </div>

    <div class="map_content">
      <div class="map" id="map"></div>
    </div>
  </div>


</template>

<script>
import { defineComponent, ref, onMounted } from 'vue'
import { useRoute } from "vue-router";
import {Loader} from "@googlemaps/js-api-loader";
import { useMessage } from "naive-ui";
import { ArrowForward, Star, HeartOutline, LocationOutline, TodayOutline, CompassOutline, Search, StatsChartOutline } from "@vicons/ionicons5";
import {useLangStore} from "../../store.js";
import NavigationBar from "../GeneralComponents/navigationBar.vue";
import axios from 'axios';

export default defineComponent({
  name: "moreView",
  components: {
    NavigationBar,
    HeartOutline,
    LocationOutline,
    TodayOutline,
    CompassOutline,
    Search,
    StatsChartOutline,
    Star,
    ArrowForward
  },
  setup () {
    const morePage = ref(1);
    const morePages = ref(1);
    const moreNumber = 0;
    const morePageSize = ref(4);
    const route = useRoute();
    const type = ref(route.query.type);
    const value = ref(route.query.value);
    let project_loc = null;
    let project_zoom = 1;
    const locations = [];
    const products = ref([]);
    const langStore = useLangStore();
    let mapLanguage = 'en-US';
    if (langStore.language === 'zh'){
      mapLanguage = 'zh-CN'
    }
    const loadingRef = ref(false);
    const message = useMessage();
    // console.log(morePage.value);
    axios.post('/homepage/more_program_list',
        {
          type: type.value,
          value: value.value,
          page: morePage.value,
        }
    ).then((response) => {
      const code = response.status
      if (code === 200){
        products.value = response.data.products;
        for(let i = 0; i < products.length; i++){
          let raw_time = products[i].duration;
          let hour = Math.round(raw_time/3600);
          let day = Math.round(hour/24);
          if (hour > 24 && day === 1){
            products[i].duration = '1 Day'
          }
          if (hour > 24 && day > 1){
            products[i].duration = day + ' Days'
          }
          if (hour === 1){
            products[i].duration = '1 Hour'
          }
          if (hour < 24 && hour !== 1){
            products[i].duration = hour + ' Hours'
          }
        }
      }
      project_loc = {
        lat: products.value[0].latitude,
        lng: products.value[0].longitude
      }
      for (let i = 0; i < products.value.length; i++){
        locations.push({
          position: {lat: products.value[i].latitude, lng: products.value[i].longitude},
          title: products.value[i].title
        });
      }
      loadMap();
    })

    axios.post("/homepage/more",
        {
          type: type.value,
          value: value.value,
        }
    )
        .then((response)=>{
          // const code = response.status
          // if (code === 200){
          // console.log("in number get")
          const count = response.data.page_number
          morePages.value = count;
          // console.log(count, "+++", morePages.value)
          // }
        })
    const loadMap = () => {
      const loader = new Loader({
        apiKey: "AIzaSyBctzU8ocpP_0j4IdTRqA-GABIAnaXd0ow",
        version: "beta",
        libraries: ["marker"],
        language: mapLanguage
      });

      loader.load().then((google) => {
        const center = project_loc;
        let map = new google.maps.Map(document.getElementById("map"), {
          center: center,
          zoom: project_zoom,
          mapId: "jkhjkhkjhjkh"
        });
        const tourStops = locations;
        // Create an info window to share between markers.
        const infoWindow = new google.maps.InfoWindow();
        tourStops.forEach(({ position, title }, i) => {
          const pinView = new google.maps.marker.PinView({
            glyph: `${i + 1}`,
          });
          const marker = new google.maps.marker.AdvancedMarkerView({
            position,
            map,
            title: `${i + 1}. ${title}`,
            content: pinView.element,
          });

          // Add a click listener for each marker, and set up the info window.
          marker.addListener("click", ({ domEvent, latLng }) => {
            const { target } = domEvent;

            infoWindow.close();
            infoWindow.setContent(marker.title);
            infoWindow.open(marker.map, marker);
          });
        });

      });
    };
    return {
      morePage,
      morePages,
      moreNumber,
      morePageSize,
      loadMap,
      type,
      value,
      products,
      project_loc,
      project_zoom,
      locations,
      handleClick() {
        loadingRef.value = true
        setTimeout(() => {
          loadingRef.value = false
        }, 2000)
      },
      handleChangePage() {
        axios.post("/homepage/more_program_list", {
          type: type.value,
          value: value.value,
          page: morePage.value,
        })
            .then((response) => {
              const code = response.status;
              if (code === 200) {
                products.value = response.data.products;
                for(let i = 0; i < products.value.length; i++){
                  let raw_time = products.value[i].duration;
                  let hour = Math.round(raw_time/3600);
                  let day = Math.round(hour/24);
                  if (hour > 24 && day === 1){
                    products.value[i].duration = '1 Day'
                  }
                  if (hour > 24 && day > 1){
                    products.value[i].duration = day + ' Days'
                  }
                  if (hour === 1){
                    products.value[i].duration = '1 Hour'
                  }
                  if (hour < 24 && hour !== 1){
                    products.value[i].duration = hour + ' Hours'
                  }
                }
                project_loc = {
                  lat: products.value[0].map_latitude,
                  lng: products.value[0].map_longitude
                }
                for (let i = 0; i < products.value.length; i++){
                  locations.push({
                    position: {lat: products.value[i].map_latitude, lng: products.value[i].map_longitude},
                    title: products.value[i].title
                  });
                }
                loadMap();
              }
            });
      },
    }
  },
})

</script>

<style scoped>
.zup {
  position: fixed;
  top: 0;
}
.page{
  margin-top: 10px;
  margin-left: auto;
  margin-right: auto;
  width: 30%;
}
.halfMap {
  display: flex;
  width: 100%;
  min-height: calc(100vh - 90px);
  margin-top: 80px;
}

@media (max-width: 991px) {
  .halfMap {
    flex-direction: column;
    margin-top: 80px;
  }
}

@media (max-width: 767px) {
  .halfMap {
    margin-top: 80px;
  }
}
.dropdown {
  width: 160px !important;
  height: 40px;
  cursor: pointer;
  position: relative;
  display: flex;
  align-items: center;
}
.map_content {
  width: 100%;
  min-height: 100%;
}
@media (max-width: 991px) {
  .map_content {
    order: 1;
  }
}
.map {
  width: 100%;
  height: 100%;
  background-color: #a3a3a3;
}
.margin {
  margin-left: 15px;
}
.btn_detail {
  padding: 10px 24px !important;
  background-color: #3554D1 !important;
  color: #FFFFFF;
  margin-top: 15px !important;
  text-decoration: none;
}
.button.-dark-1:hover {
  border-color: #051036;
  color: white !important;
}
.button:hover {
  opacity: 0.7;
}
.button {
  color: white;
  text-transform: capitalize;
  font-weight: 700;
  transition: opacity 200ms ease;
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
.from {
  font-size: 14px;
  color: #697488;
  margin-top: 24px;
}
.price {
  font-size: 22px;
  line-height: 1.2;
  font-weight: 600;
}
.per {
  font-size: 14px;
  color: #697488;
}
.reviews {
  font-size: 14px;
  line-height: 1.4;
  color: #697488;
  margin-top: 10px;
}
.star {
  font-size: 10px;
  color: #F8D448;
}
.stars {
  display: flex !important;
  align-items: center !important;
  justify-content: flex-end !important;
}
.content_right {
  text-align: right;
}

.opt1 {
  font-size: 14px;
  line-height: 1.5 !important;
  font-weight: 500;
  margin-top: 20px;
}
.opt2 {
  font-size: 14px;
  color: #008009;
  font-weight: 500;
  line-height: 1.5 !important;
  margin-top: 3px !important;
}
.location {
  font-size: 14px;
  line-height: 1.4;
}
.title {
  font-size: 16px;
  line-height: 1.6 !important;
  font-weight: 500;
}
.hours {
  font-size: 14px;
  line-height: 1.4 !important;
  margin-bottom: 5px !important;
}

.card{
  padding-top: 20px;
  border-top: 1px solid #DDDDDD;
}
.cardImage_wish {
  position: absolute;
  top: 20px;
  right: 20px;
}
.cardImage {
  border-radius: 4px;
  height: auto;
  width: 100%;
  object-fit: contain;
}
.cardImage_content {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 0;
  border-radius: inherit;
}
.ratio {
  position: relative;
  display: block;
  overflow: hidden;
}

.ratio::before {
  display: block;
  width: 100%;
  content: "";
}

.ratio-1\:1::before {
  padding-bottom: 100%;
}
.content_left {
  position: relative;
  z-index: 0;
  width: 200px;
  max-width: 100%;
  border-radius: 4px;
}

.review-and-grade{
  justify-content: flex-end;
}
.text-light-1{
  color: #697488;
}
.mb-5{
  margin:0;
  margin-bottom: 5px;
}
.star{
  display: flex;
  justify-content: center;
  align-items: center;
  flex-shrink: 0;
  width: 40px;
  height: 40px;
  border-radius: 4px;
  color: white;
  background-color: #3554D1;
  font-weight: 600;
  font-size: 14px;
  box-sizing: border-box;
}
@media (max-width: 767px) {
  .content_left {
    width: 100% !important;
  }
  .content_right {
    text-align: left !important;
  }
  .stars {
    justify-content: flex-start !important;
  }
  .from {
    margin-top: 20px;
  }
}
.contents_wrap {
  padding-top: 20px;
}
.property_text {
  font-size: 18px;
}
.property_num {
  font-weight: 500;
}
.property {
  justify-content: space-between !important;
  align-items: center !important;
  padding-top: 20px !important;
}
.select_menu {
  padding-top: 20px !important;
}
.btn_search {
  flex-shrink: 0;
  width: 60px;
  height: 60px;
}
.icon_search {
  font-size: 20px;
}
.search_btn {
  border: none !important;
}
.guests_wrap {
  position: relative;
  padding-left: 30px;
  padding-right: 30px;
}
.date_wrap {
  position: relative;
  padding-left: 30px;
  padding-right: 30px;
}
.loc_margin {
  margin-left: 10px;
}
.loc_title {
  font-size: 15px;
  font-weight: 500;
  line-height: 1.6;
}
.loc_input {
  font-size: 15px;
  color: #697488;
  line-height: 1.6;
}
.icon_loc {
  font-size: 20px;
  color: #697488;
  margin-top: 5px;
}
.loc_head {
  display: flex !important;
}
.loc_wrap {
  position: relative;
  padding-right: 30px;
  padding-left: 20px;
}

.list_search {
  display: grid;
  grid-template-columns: 1fr 250px 290px auto;
  align-items: start !important;
}

.list_search > * + * {
  border-left: 1px solid #DDDDDD;
}


.list_search_wrap {
  position: relative;
  z-index: 20;
  background-color: #F5F5F5 !important;
  padding-top: 10px !important;
  padding-bottom: 10px !important;
  padding-right: 10px;
  border-radius: 4px;
}

.list_content {
  width: 865px;
  max-width: 100%;
  flex-shrink: 0;
  padding: 30px;
  min-height: 100%;
}


.row{
  --bs-gutter-x:30px;
  --bs-gutter-y:0;
  display:flex;
  flex-wrap:wrap;
  margin-top:calc(var(--bs-gutter-y)*-1);
  margin-right:calc(var(--bs-gutter-x)*-0.5);
  margin-left:calc(var(--bs-gutter-x)*-0.5)
}

.row>*{
  box-sizing:border-box;
  flex-shrink:0;
  width:100%;
  max-width:100%;
  padding-right:calc(var(--bs-gutter-x)*0.5);
  padding-left:calc(var(--bs-gutter-x)*0.5);
  margin-top:var(--bs-gutter-y)
}

.row-cols-auto>*{
  flex:0 0 auto;
  width:auto
}

.row-cols-1>*{
  flex:0 0 auto;
  width:100%
}

.row-cols-2>*{
  flex:0 0 auto;
  width:50%
}

.row-cols-3>*{
  flex:0 0 auto;
  width:33.33333%
}

.row-cols-4>*{
  flex:0 0 auto;
  width:25%
}

.row-cols-5>*{
  flex:0 0 auto;
  width:20%
}

.row-cols-6>*{
  flex:0 0 auto;
  width:16.66667%
}

.col-auto{
  flex:0 0 auto;
  width:auto
}

@media (min-width:576px){
  .row-cols-sm-auto>*{
    flex:0 0 auto;width:auto
  }
  .row-cols-sm-1>*{flex:0 0 auto;width:100%}
  .row-cols-sm-2>*{flex:0 0 auto;width:50%}
  .row-cols-sm-3>*{flex:0 0 auto;width:33.33333%}
  .row-cols-sm-4>*{flex:0 0 auto;width:25%}
  .row-cols-sm-5>*{flex:0 0 auto;width:20%}
  .row-cols-sm-6>*{flex:0 0 auto;width:16.66667%}
  .col-sm-6 {
    flex: 0 0 50%;
    max-width: 50%;
  }
}
.col-md, .col-md-auto,
.col-auto, .col-12 {
  position: relative;
  width: auto;
  /*padding-right: 15px;*/
  /*padding-left: 15px;*/
}

.rounded-full{
  width: 3px;
  height: 3px;
  border-radius: 100%;
  background-color: #697488;
  position: relative;
  top: 11px;
}

.round{
  padding-left: 0;
  padding-right: 0;
}

@media (min-width: 768px) {
  .col-md {
    flex-basis: 0;
    flex-grow: 1;
    max-width: 100%;
  }

  .row-cols-md-1 > * {
    flex: 0 0 100%;
    max-width: 100%;
  }

  .row-cols-md-2 > * {
    flex: 0 0 50%;
    max-width: 50%;
  }

  .row-cols-md-3 > * {
    flex: 0 0 33.3333333333%;
    max-width: 33.3333333333%;
  }

  .row-cols-md-4 > * {
    flex: 0 0 25%;
    max-width: 25%;
  }

  .row-cols-md-5 > * {
    flex: 0 0 20%;
    max-width: 20%;
  }

  .row-cols-md-6 > * {
    flex: 0 0 16.6666666667%;
    max-width: 16.6666666667%;
  }

  .col-md-auto {
    flex: 0 0 auto;
    width: auto;
    max-width: 100%;
  }

  .col-md-1 {
    flex: 0 0 8.3333333333%;
    max-width: 8.3333333333%;
  }

  .col-md-2 {
    flex: 0 0 16.6666666667%;
    max-width: 16.6666666667%;
  }

  .col-md-3 {
    flex: 0 0 25%;
    max-width: 25%;
  }

  .col-md-4 {
    flex: 0 0 33.3333333333%;
    max-width: 33.3333333333%;
  }

  .col-md-5 {
    flex: 0 0 41.6666666667%;
    max-width: 41.6666666667%;
  }

  .col-md-6 {
    flex: 0 0 50%;
    max-width: 50%;
  }

  .col-md-7 {
    flex: 0 0 58.3333333333%;
    max-width: 58.3333333333%;
  }

  .col-md-8 {
    flex: 0 0 66.6666666667%;
    max-width: 66.6666666667%;
  }

  .col-md-9 {
    flex: 0 0 75%;
    max-width: 75%;
  }

  .col-md-10 {
    flex: 0 0 83.3333333333%;
    max-width: 83.3333333333%;
  }

  .col-md-11 {
    flex: 0 0 91.6666666667%;
    max-width: 91.6666666667%;
  }

  .col-md-12 {
    flex: 0 0 100%;
    max-width: 100%;
  }
}

@media (min-width:768px){
  .row-cols-md-auto>*{flex:0 0 auto;width:auto}
  .row-cols-md-1>*{flex:0 0 auto;width:100%}
  .row-cols-md-2>*{flex:0 0 auto;width:50%}
  .row-cols-md-3>*{flex:0 0 auto;width:33.33333%}
  .row-cols-md-4>*{flex:0 0 auto;width:25%}
  .row-cols-md-5>*{flex:0 0 auto;width:20%}
  .row-cols-md-6>*{flex:0 0 auto;width:16.66667%}
  .col-md-6{flex:0 0 auto;width:50%}
  .col-md-auto {
    flex: 0 0 auto;
    width: auto;
    max-width: 100%;
  }
  .col-md {
    flex-basis: 0;
    flex-grow: 1;
    max-width: 100%;
  }
  .col-md{flex:1 0 0%}
}

@media (min-width:992px){
  .row-cols-lg-auto>*{flex:0 0 auto;width:auto}
  .row-cols-lg-1>*{flex:0 0 auto;width:100%}
  .row-cols-lg-2>*{flex:0 0 auto;width:50%}
  .row-cols-lg-3>*{flex:0 0 auto;width:33.33333%}
  .row-cols-lg-4>*{flex:0 0 auto;width:25%}
  .row-cols-lg-5>*{flex:0 0 auto;width:20%}
  .row-cols-lg-6>*{flex:0 0 auto;width:16.66667%}

}

@media (min-width:1200px){
  .row-cols-xl-auto>*{
    flex:0 0 auto;
    width:auto
  }
  .row-cols-xl-1>*{
    flex:0 0 auto;
    width:100%
  }
  .row-cols-xl-2>*{
    flex:0 0 auto;
    width:50%
  }
  .row-cols-xl-3>*{
    flex:0 0 auto;
    width:33.33333%
  }
  .row-cols-xl-4>*{
    flex:0 0 auto;
    width:25%
  }

  .row-cols-xl-5>*{
    flex:0 0 auto;
    width:20%
  }

  .row-cols-xl-6>*{
    flex:0 0 auto;
    width:16.66667%
  }

  .col-xl-3{flex:0 0 auto;width:25%}
  .col-xl-5{flex:0 0 auto;width:41.66667%}
}

@media (min-width:1400px){
  .row-cols-xxl-auto>*{
    flex:0 0 auto;width:auto}
  .row-cols-xxl-1>*{flex:0 0 auto;width:100%}
  .row-cols-xxl-2>*{flex:0 0 auto;width:50%}
  .row-cols-xxl-3>*{flex:0 0 auto;width:33.33333%}
  .row-cols-xxl-4>*{flex:0 0 auto;width:25%}
  .row-cols-xxl-5>*{flex:0 0 auto;width:20%}
  .row-cols-xxl-6>*{flex:0 0 auto;width:16.66667%}
}

.x-gap-10 {
  margin-left: -5px;
  margin-right: -5px;
}

.x-gap-10 > * {
  padding-left: 5px;
  padding-right: 5px;
}

.y-gap-10 {
  margin-top: -5px;
  margin-bottom: -5px;
}

.y-gap-10 > * {
  padding-top: 5px;
  padding-bottom: 5px;
}

.y-gap-20 {
  margin-top: -10px;
  margin-bottom: 10px;
}

.y-gap-20 > * {
  padding-top: 10px;
  padding-bottom: 10px;
}

.y-gap-30 {
  margin-top: -15px;
  margin-bottom: -15px;
}

.y-gap-30 > * {
  padding-top: 15px;
  padding-bottom: 15px;
}

.col-sm-6 {
  position: relative;
  width: 100%;
  padding-right: 15px;
  padding-left: 15px;
}

.col-12 {
  flex: 0 0 100%;
  max-width: 100%;
}

@media screen and (max-width: 1200px) {
  .loc_wrap{
    padding-right: 10px;
    padding-left: 10px;
  }
  .date_wrap{
    padding-right: 10px;
    padding-left: 10px;
  }
  .guests_wrap {
    padding-right: 10px;
    padding-left: 10px;
  }
  .list_search{
    grid-template-columns: 1fr 188px 192px auto
  }
}
@media (max-width: 991px) {
  .list_search {
    grid-template-columns: 1fr;
  }
  .list_search > * + * {
    border-left: 0;
    border-top: 1px solid #DDDDDD;
  }
  .loc_wrap {
    padding: 20px 0;
  }
  .date_wrap {
    padding: 20px 0px;
  }
  .guests_wrap {
    padding: 20px 0px;
  }
  .list_content {
    width: 660px;
  }
  .list_content {
    order: 2;
  }
  .list_search_wrap {
    width: 100%;
    border-radius: 4px !important;
    padding: 5px 20px 20px !important;
    background-color: #F5F5F5 !important;
  }
}

@media (max-width: 767px) {
  .list_content {
    padding: 20px;
    width: auto;
  }
  .list_search_wrap{
    width: auto;
  }
}
@media (max-width: 540px) {
  .from {
    margin-top: 5px;
  }
  .reviews {
    margin-top: 0;
  }
  .opt1 {
    margin-top: 5px;
  }
  .location{
    line-height: 0.5;
  }
}
</style>

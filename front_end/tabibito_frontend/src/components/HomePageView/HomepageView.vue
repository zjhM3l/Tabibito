<template>
  <navigation-bar :is-transparent="true"></navigation-bar>

  <section class="specialPart">
      <div class="specialBackgroundLeft"></div>
      <div class="specialPartCore">
        <div class="specialCoreContainer">
          <h1 class="specialTitle">{{ $t('homepage.searchPart.slogan1') }}
            <span class="specialTitleTail">{{ $t('homepage.searchPart.slogan2') }}
              <span class="specialTitleDecoration">
                <img class="decorationImg" src="../../assets/line.png"/>
              </span>
            </span>
          </h1>
          <p class="specialSlogan">{{ $t('homepage.searchPart.sloganDescription')}}</p>
          <div class="searchBar">
            <div class="search">
              <div class="locationOption">
                <div class="optionName">{{ $t('homepage.searchPart.loc')}}</div>
                <n-dropdown
                  trigger="click"
                  placement="bottom-start"
                  :options="locationOptions"
                  @select="handleSelectLocation"
                >
                  <div class="optionValue" id="locationValue">{{currentLocation}}</div>
                </n-dropdown>
              </div>
              <div class="durationOption">
                <div class="optionName">{{ $t('homepage.searchPart.stet')}}</div>
<!--                <div class="optionValue" id="durationValue" @click="handleSelectTime">{{currentTimePeriod}}</div>-->
                <div class="dataPickers">
                  <n-date-picker v-model:value="startTime" type="date" :is-date-disabled="secureStartTime" size="small" clearable :placeholder="$t('homepage.searchPart.st')"/>
                  <span>-</span>
                  <n-date-picker v-model:value="endTime" type="date" placement="bottom-end" :is-date-disabled="secureEndTime" size="small" clearable :placeholder="$t('homepage.searchPart.et')"/>

                </div>
              </div>
              <div class="tagOption">
                <div class="optionName">{{ $t('homepage.searchPart.tags')}}</div>
<!--                <div class="optionValue" id="tagValue">fdsfds</div>-->
                <n-select
                    class="selector"
                    v-model:value="tagValue"
                    multiple
                    :render-tag="renderTag"
                    :options="tags"
                    max-tag-count="responsive"
                />
              </div>
              <div class="searchButton" @click="handleSearchProject">
                <div class="searchButtonContent">
                  <div class="searchButtonIcon"></div>
                  <div class="searchButtonText">{{ $t('homepage.searchPart.button')}}</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="specialBackgroundRight"></div>
    </section>


  <most-popular-tours></most-popular-tours>
  <choose-tour-types></choose-tour-types>
  <hot-location></hot-location>

  <section class="discountPart" style="overflow: hidden">
    <div class="discountTitleArea">
      <div class="discountTitle">{{ $t('homepage.discountPart.title')}}</div>
      <div class="discountSlogan">{{ $t('homepage.discountPart.slogan')}}</div>
    </div>
    <div class="discountMain">
      <div class="discountCover">
        <div class="discountCoverTextArea">
          <div class="discountCoverTitle1">{{ $t('homepage.discountPart.period')}}</div>
          <div class="discountCoverTitle2">{{ $t('homepage.discountPart.bookTitle')}}</div>
          <div class="discountCoverBookButton" @click="handleMore()">{{ $t('homepage.discountPart.button')}}</div>
        </div>
      </div>
      <discount-items :discount-data="discountData"></discount-items>
    </div>
  </section>

  <section class="statistics">
    <div class="figure">
      <n-number-animation show-separator
                          :from="0"
                          :to="this.figures.review_count"></n-number-animation>
      <div class="figureName">{{ $t('homepage.figurePart.reviews')}}</div>
    </div>
    <div class="figure">
      <n-number-animation show-separator
                          :from="0"
                          :to="this.figures.product_count"></n-number-animation>
      <div class="figureName">{{ $t('homepage.figurePart.travelProjects')}}</div>
    </div>
    <div class="figure">
      <n-number-animation show-separator
                          :from="0"
                          :to="this.figures.happy_customer_count"></n-number-animation>
      <div class="figureName">{{ $t('homepage.figurePart.happyCustomers')}}</div>
    </div>
    <div class="figure">
      <n-number-animation show-separator
                          :from="0"
                          :to="this.figures.order_count"></n-number-animation>
      <div class="figureName">{{ $t('homepage.figurePart.orders')}}</div>
    </div>
  </section>

  <section class="whyChooseUsSection">
    <div class="whyChooseImg"></div>
    <div class="whyChooseCore">
      <div class="whyChooseContent">
        <h2 class="whyChooseTitle">{{ $t('homepage.whyChoosePart.title')}}</h2>
        <div class="whyChooseSlogan">{{ $t('homepage.whyChoosePart.slogan')}}</div>
        <div class="whyChooseFeatures">
          <div class="whyChooseFeature">
            <div class="featureIcon shieldIcon"></div>
            <div class="featureTextArea">
              <h4 class="featureName">{{ $t('homepage.whyChoosePart.attr1')}}</h4>
              <div class="featureText">{{ $t('homepage.whyChoosePart.val1')}}</div>
            </div>
          </div>
          <div class="whyChooseFeature">
            <div class="featureIcon bookingIcon"></div>
            <div class="featureTextArea">
              <h4 class="featureName">{{ $t('homepage.whyChoosePart.attr2')}}</h4>
              <div class="featureText">{{ $t('homepage.whyChoosePart.val2')}}</div>
            </div>
          </div>
          <div class="whyChooseFeature">
            <div class="featureIcon careIcon"></div>
            <div class="featureTextArea">
              <h4 class="featureName">{{ $t('homepage.whyChoosePart.attr3')}}</h4>
              <div class="featureText">{{ $t('homepage.whyChoosePart.val3')}}</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <customer-review></customer-review>
  <inspiration></inspiration>
  <not-a-member></not-a-member>
  <footer-view></footer-view>
</template>

<script>
import NavigationBar from "../GeneralComponents/navigationBar.vue";
import {h, onBeforeMount, onMounted, ref} from "vue";
import {NIcon, NTag} from "naive-ui";
import {Location} from "@vicons/ionicons5";
import MostPopularTours from "./mostPopularTours.vue";
import DiscountItems from "./discountItems.vue";
import ChooseTourTypes from "./chooseTourTypes.vue";
import HotLocation from "./hotLocation.vue";
import CustomerReview from "./customerReview.vue";
import Inspiration from "./inspiration.vue";
import FooterView from "../GeneralComponents/footerView.vue";
import NotAMember from "./notMember.vue";
import {useRouter} from 'vue-router';
import {getCurrentInstance} from 'vue'
const renderIcon = (icon) => {
  return () => {
    return h(NIcon, null, {
      default: () => h(icon)
    });
  };
};
export default {
  name: "HomepageView",
  components: {
    NotAMember,
    FooterView,
    Inspiration, CustomerReview, HotLocation, ChooseTourTypes, DiscountItems, MostPopularTours, NavigationBar},
  setup(){
    let figures = ref({});
    const route = useRouter();
    const axios = getCurrentInstance().appContext.config.globalProperties.axios;
    let locationOptions = [];
    axios.get('/homepage/all_location')
        .then((res) =>{
          if (res.status === 200){
            for (let loc of res.data.locations){
              locationOptions.push(
                  {
                    label: loc,
                    key: loc,
                    icon: renderIcon(Location)
                  }
              )
            }

          }
        })
    axios.get('/homepage/four_number')
        .then(function (response) {
          figures.value = response.data
        })
    let discountData = ref({});
    axios.get('/homepage/lowest_discount')
        .then(function (res){
          discountData.value = res.data.products
          console.log(discountData.value)
          for(let i = 0; i < discountData.value.length; i++){
            let raw_time = discountData.value[i].duration;
            let hour = Math.round(raw_time/3600);
            let day = Math.round(hour/24);
            if (hour > 24 && day === 1){
              discountData.value[i].duration = '1 Day'
            }
            if (hour > 24 && day > 1){
              discountData.value[i].duration = day + ' Days'
            }
            if (hour === 1){
              discountData.value[i].duration = '1 Hour'
            }
            if (hour < 24 && hour !== 1){
              discountData.value[i].duration = hour + ' Hours'
            }
          }
        })
    let startTime = ref();
    let endTime = ref();
    let currentLocation = ref("select");
    const renderTag = ({ option, handleClose }) => {
      return h(
          NTag,
          {
            type: option.type,
            closable: true,
            onMousedown: (e) => {
              e.preventDefault();
            },
            onClose: (e) => {
              e.stopPropagation();
              handleClose();
            }
          },
          { default: () => option.label }
      );
    };
    return{
      locationOptions,
      route,
      currentLocation,
      startTime,
      endTime,
      figures,
      discountData,
      range: ref([]),
      tagValue: ref([]),
      tags: [
        {
          label: "Wild Life Tour",
          value: "WildlifeTour",
          type: "success"
        },
        {
          label: "Adventure Tour",
          value: "AdventureTour",
          type: "warning"
        },
        {
          label: "City Tour",
          value: "CityTour",
          type: "success"
        },
        {
          label: "Museum Tour",
          value: "MuseumTour",
          type: "error"
        },
        {
          label: "Beaches Tour",
          value: "BeachesTour",
          type: "warning"
        }
      ],
      renderTag,
      handleSelectLocation(val){
        currentLocation.value = val;
      },
      secureStartTime(ts) {
        if (endTime.value != null){
          return ts < Date.now() || ts > endTime.value;
        }
        else {
          return ts < Date.now();
        }
      },
      secureEndTime(ts){
        if (startTime.value != null){
          return ts < Date.now() || ts < startTime.value;
        }
        else {
          return ts < Date.now();
        }
      },
      handleSearchProject() {
        if (startTime.value === 0 || startTime.value === null || endTime.value === null || endTime.value === 0 || currentLocation.value === "select"){
          return;
        }
        /*axios.post("http://127.0.0.1:5000/homepage/search",
            {
              start_time: startTime.value,
              end_time: endTime.value,
              location: currentLocation.value,
              tags: this.tagValue
            }
        )
            .then(function (response){
              if (response.data.code === 200){
                this.router.push('/search_result')
              }
            })*/

       this.route.push({
          path: '/search_result',
          query: {
            start_time: startTime.value,
            end_time: endTime.value,
            location: currentLocation.value,
            tags: this.tagValue
          }
        })
      }
    }
  },
  methods: {
    handleMore() {
      this.$router.push({name: 'search'})
    }
  }
}
</script>

<style scoped>
  .specialPart{
    position: relative;
    padding-top: 260px;
    padding-bottom: 200px;
    box-sizing: border-box;
  }
  .specialBackgroundLeft{
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    width: 58%;
    z-index: -1;
    background-image: url("../../assets/homeheadbg.svg");
    background-size: cover;
  }
  .specialBackgroundRight{
    position: absolute;
    top: 0;
    right: 0;
    height: 100%;
    width: 42%;
    z-index: -2;
    background-image: url("../../assets/beach.jpg");
    background-size: cover;
    background-position: center;
  }
  .specialPartCore{
    max-width: 1140px;
    width: 100%;
    padding-left: 15px;
    padding-right: 15px;
    margin-left: auto;
    margin-right: auto;
    box-sizing: border-box;
  }
  .specialCoreContainer{
    flex: 0 0 auto;
    width: 75%;
    box-sizing: border-box;
    max-width: 100%;
  }
  .specialTitle{
    font-size: 60px;
    margin: 0;
    line-height: 1.45;
    font-weight: 600;
  }
  .specialTitleTail{
    color: #3554D1;
    position: relative;
  }
  .specialSlogan{
    margin-top: 20px;
    font-size: 16px;
    color: var(--secondary-text-color);
    line-height: 1.875;
  }
  .searchBar{
    border-radius: 4px;
    background-color: white;
    margin-top: 35px;
    padding: 20px 20px 20px 0;
    position: relative;
    box-sizing: border-box;
    box-shadow: 0px 20px 40px 0px #05103612;
  }
  .search{
    display: grid;
    grid-template-columns: 1fr 260px 280px auto;
    align-items: center;
  }
  .locationOption{
    padding-left: 30px;
    padding-right: 30px;
    position: relative;
    box-sizing: border-box;

  }
  .dataPickers{
    display: flex;
  }
  .durationOption,.tagOption{
    border-left: 1px solid #DDDDDD;
    padding-left: 30px;
    padding-right: 30px;
    position: relative;
    box-sizing: border-box;
  }
  .searchButton{
    border: none;
    background-color: #3554D1;
    cursor: pointer;
    border-radius: 4px;
    transition: .3s ease-in;
  }
  .searchButton:hover{
    transition: all 0.3s cubic-bezier(0.165, 0.84, 0.44, 1);
    background-color: #051036;
  }
  .searchButtonContent{
    height: 60px;
    padding: 15px 35px 15px 35px;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    box-sizing: border-box;
    color: white;
  }
  .searchButtonIcon{
    width: 20px;
    height: 20px;
    background-image: url("../../assets/search_white.svg");
    background-repeat: no-repeat;
    background-position: center;
    background-size: contain;
  }

  @media screen and (max-width: 1200px) {
    .specialPart{
      padding-top: 150px;
      padding-bottom: 150px;
    }
    .specialCoreContainer{
      width: 80%;
      margin-left: 50px;
    }
  }

  @media screen and (max-width: 1050px) {
    .specialPart{
      padding-top: 100px;
    }
    .specialCoreContainer{
      width: 75%;
      margin: auto;
    }
    .specialTitle{
      font-size: 40px;
    }
    .search{
      grid-template-columns: 1fr;
      margin-left: 20px;
    }
    .locationOption{
      padding: 20px 0px;
    }
    .optionName{

    }
    .durationOption{
      padding: 20px 0px;
      border-left: 0px;
      border-top: 1px solid #DDDDDD;
    }
    .tagOption{
      padding: 20px 0px;
      border-left: 0px;
      border-top: 1px solid #DDDDDD;
    }
    .searchButton{
    }
  }
  @media screen and (max-width: 575px) {
    .selector {
      width: 92%;
    }
  }
  @media screen and (max-width: 500px) {
    .specialBackgroundLeft{
      width: 100%;
    }
    .specialPart{
      padding-top: 100px;
      padding-bottom: 20px;
    }
    .specialCoreContainer {
      margin: auto;
      width: 95%;
    }
    .specialTitle{
      font-size: 30px;
    }
  }
  .optionName{
    font-weight: 500;
    line-height: 1.6;
    font-size: 15px;
  }
  .optionValue{
    color: var(--secondary-text-color);
    line-height: 1.6;
    font-size: 15px;
    cursor: pointer;
  }
  .specialTitleDecoration{
    position: absolute;
    bottom: -40%;
    left: 0;
    width: 100%;
  }
  .decorationImg{
    width: 100%;
    max-width: 100%;
    height: auto;
    object-fit: cover;
  }
  .statistics{
    margin: 60px auto 120px auto;
    max-width: 1140px;
    box-sizing: border-box;
    padding-left: 15px;
    padding-right: 15px;
    display: flex;
    justify-content: center;
  }
  @media screen and (max-width: 800px){
    .statistics{
      margin-bottom: 80px;
    }
  }
  @media screen and (max-width: 600px){
    .statistics{
      margin-bottom: 55px;
    }
  }
  @media screen and (max-width: 450px){
    .statistics{
      margin-bottom: 30px;
    }
  }
  .figure{
    padding: 15px;
    box-sizing: border-box;
    width: 25%;
    text-align: center;
    font-weight: 600;
    line-height: 1.3;
    font-size: 40px;
    color: #3554D1;
  }
  .figureName{
    font-size: 14px;
    color: var(--secondary-text-color);
    margin-top: 5px;
    line-height: 1.4;
    font-weight: 400;
  }
  .whyChooseUsSection{
    position: relative;
    padding-bottom: 120px;
    padding-top: 120px;
    box-sizing: border-box;
    background-color: rgba(53, 84, 209, 0.05);
  }
  .whyChooseImg{
    width: 41.66667%;
    position: absolute;
    box-sizing: border-box;
    height: 100%;
    right: 0;
    top: 0;
    background-repeat: no-repeat;
    background-position: center;
    background-size: cover;
    background-image: url("../../assets/mountain-fuji.jpg");
  }
  .whyChooseCore{
    max-width: 1320px;
    padding-left: 15px;
    padding-right: 15px;
    margin: 0 auto;
    display: flex;
    flex-wrap: wrap;
    box-sizing: border-box;
  }
  .whyChooseContent{
    width: 430px;
    flex: 0 0 auto;
    box-sizing: border-box;
    padding-left: 15px;
    padding-right: 15px;
    max-width: 100%;

  }
  .whyChooseTitle{
    font-weight: 600;
    font-size: 30px;
    line-height: 1.45;
    box-sizing: border-box;
    margin: 0;
  }
  .whyChooseSlogan{
    margin-top: 5px;
    color: var(--secondary-text-color);
  }
  .whyChooseFeatures{
    margin-top: 45px;
  }
  .whyChooseFeature{
    padding: 15px 45px 15px 15px;
    flex:  0 0 auto;
    width: 100%;
    max-width: 100%;
    box-sizing: border-box;
    display: flex;
  }
  .featureIcon{
    width: 50px;
    height: 50px;
    box-sizing: border-box;
    background-repeat: no-repeat;
    background-position: center;
    background-size: cover;
    flex-shrink: 0;
  }
  .shieldIcon{
    background-image: url("../../assets/shield.svg");
  }
  .bookingIcon{
    background-image: url("../../assets/easy_booking.svg");
  }
  .careIcon{
    background-image: url("../../assets/care.svg");
  }
  .featureTextArea{
    margin-left: 15px;
    box-sizing: border-box;
  }
  .featureName{
    font-weight: 500;
    font-size: 18px;
    box-sizing: border-box;
    margin: 0;
  }
  .featureText{
    margin-top: 10px;
    font-size: 15px;
    box-sizing: border-box;
    color: var(--secondary-text-color);
  }
  .discountPart{
    margin: 60px auto 60px auto;
    box-sizing: border-box;
    padding-left: 15px;
    padding-right: 15px;
    max-width: 1320px;
  }
  .discountTitle{
    font-size: 30px;
    margin: 0;
    line-height: 1.45;
    font-weight: 600;
  }
  .discountSlogan{
    margin-top: 5px;
    color: var(--secondary-text-color);
    line-height: 1.875;
  }
  .discountMain{
    margin-top: 25px;
    display: flex;
    flex-wrap: nowrap;
  }
  .discountCover{
    width: 41.66667%;
    box-sizing: border-box;
    margin-right: 15px;
    padding: 50px;
    background-image: url("../../assets/cherry.jpg");
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    border-radius: 4px;
    position: relative;
  }
  .discountCoverTextArea{
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    position: relative;
    z-index: 1;
  }
  .discountCover::after{
    content: '';
    position: absolute;
    z-index: 0;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: block;
    background: linear-gradient(180deg, rgba(5, 16, 54, 0.7) 0%, rgba(5, 16, 54, 0) 100%);
  }
  .discountCoverTitle1{
    color: white;
    margin-bottom: 10px;
    font-weight: 500;
    font-size: 15px;
  }
  .discountCoverTitle2{
    color: white;
    font-size: 30px;
    margin: 0;
    line-height: 1.45;
    font-weight: 600;
  }
  .discountCoverBookButton{
    margin-top: 30px;
    min-width: 180px;
    color: #051036;
    background-color: white;
    padding-top: 15px;
    padding-bottom: 15px;
    font-weight: 500;
    line-height: 1.2;
    text-align: center;
    border-radius: 4px;
    cursor: pointer;
    transition: all 0.3s cubic-bezier(0.165, 0.84, 0.44, 1);
  }
  .discountCoverBookButton:hover{
    background-color: var(--primary-color);
    color: white;
    transition: all 0.3s cubic-bezier(0.165, 0.84, 0.44, 1);
  }
  @media screen and (max-width: 1200px) {
    .discountTitleArea{
      width: 960px;
      margin: auto;
    }
    .discountMain{
      flex-direction: column;
    }
    .discountCover{
      width: 960px;
      margin: auto;
    }
  }
  @media screen and (max-width: 991px) {
    .discountTitleArea{
      width: 720px;
      margin: auto;
    }
    .discountMain{
      flex-direction: column;
    }
    .discountCover{
      width: 720px;
      margin: auto;
    }
  }
  @media screen and (max-width: 767px) {
    .discountTitleArea{
      width: 540px;
      margin: auto;
    }
    .discountMain{
      flex-direction: column;
    }
    .discountCover{
      width: 540px;
      margin: auto;
    }
  }
  @media screen and (max-width: 550px) {
    .discountTitleArea{
      width: 450px;
      margin: auto;
    }
    .discountMain{
      flex-direction: column;
    }
    .discountCover{
      width: 450px;
      margin: auto;
    }
  }
  @media screen and (max-width: 480px) {
    .discountPart{
      padding: 0px;
    }
    .discountTitleArea{
      width: 420px;
      margin: auto;
    }
    .discountMain{
      flex-direction: column;
    }
    .discountCover{
      width: 420px;
      margin: auto;
    }
  }
  @media screen and (max-width: 430px) {
    .discountPart{
      padding: 0px;
    }
    .discountTitleArea{
      width: 350px;
      margin: auto;
    }
    .discountMain{
      flex-direction: column;
    }
    .discountCover{
      width: 350px;
      margin: auto;
    }
  }


  @media screen and (max-width: 700px) {
    .whyChooseContent{
      width: 60%;
    }
    .whyChooseFeature{
      padding-right: 0px;
      padding-left: 0px;
    }
    .whyChooseFeatures{
      margin-top: 20px;
    }
  }
  @media screen and (max-width: 600px) {
    .whyChooseContent{
      width: 60%;
      padding-left: 0px;
    }
    .whyChooseFeature{
      padding-right: 0px;
      padding-left: 0px;
    }
    .whyChooseFeatures{
      margin-top: 20px;
    }
    .whyChooseUsSection{
      padding-top: 60px;
    }
    .whyChooseTitle{
      margin-left: 10px;
    }
    .whyChooseSlogan{
      margin-left: 10px;
    }
  }
  @media screen and (max-width: 550px) {
    .whyChooseImg{
      position: static;
      width: 100%;
      height: 400px;
    }
    .whyChooseUsSection{
      padding-top: 0px;
      padding-bottom: 20px;
    }
    .whyChooseCore{
      margin-top: 40px;
    }
    .whyChooseContent{
      width: 100%;
      margin: auto;
      padding-right: 0;
    }
  }
  @media screen and (max-width:480px) {
    .whyChooseImg{
      position: static;
      width: 100%;
      height: 400px;
    }
    .whyChooseUsSection{
      padding-top: 0px;
      padding-bottom: 20px;
    }
    .whyChooseCore{
      margin-top: 40px;
    }
    .whyChooseContent{
      width: 100%;
      margin: auto;
      padding-right: 0;
    }
  }
</style>

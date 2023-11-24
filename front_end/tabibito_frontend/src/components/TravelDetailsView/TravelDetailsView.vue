<template>
  <navigation-bar></navigation-bar>

  <section class="pd" >
    <div class="TDCon" style="margin-top: 80px;">
      <div class="space">
        <div class="TDTit">
          <h1 class="TDT">{{ details.name }}</h1>

          <div class="lower">
            <div class="TDRow">
              <!--       星级评分       -->
              <n-rate size="small" readonly allow-half :value="details.mark" />

            </div>
            <div class="TDReview">{{ $t('mostPopularTours.reviews', {reviews: details.reviews}) }}</div>

            <img class="loc" src="../../assets/location.svg" alt="">
            <div class="TDLoc">{{ details.location }}</div>

            <button class="map">{{ $t('traveldetails.showOnMap') }}</button>

          </div>

        </div>
      </div>
    </div>
  </section>

  <section class="pd">
    <div class="TDCon">
      <div class="DTCols1">

        <div class="TDInput_border">

          <button type="submit" class="TDAdd_btn" @click="showModal = true">
            {{ $t('traveldetails.seeAllPhotos') }}
            <div class="icon_add"></div>
          </button>

          <button type="submit" class="TDmodel">
            {{ $t('traveldetails.seeModel') }}
            <div class="icon_add"></div>
          </button>
          <button type="submit" class="TDmodel" @click="toggleModel" :disabled="!details.model">
            {{ details.model ? (showModalModel ? 'Hide Model' : 'See Model') : 'No Model'}}
            <div class="icon_add"></div>
          </button>
          <iframe v-show="showModalModel" allowfullscreen class ="model" loading="lazy" frameborder="0" :src="details.model"></iframe>


          <!--     显示图片     -->
          <div v-if="showModal" class="modal">
            <div class="modal-container">
              <div class="close-button" @click="showModal = false">X</div>
              <img :src="imageList[currentIndex]" :key="currentIndex" class="enlarge-image">
              <div class="image-buttons">
                <div class="prev-button" @click="prevImage">&lt;-</div>
                <div class="next-button" @click="nextImage">-></div>
              </div>
            </div>
          </div>
        </div>

        <n-carousel show-arrow class="TDImg" draggable>
          <img
              class="carousel-img"
              :src="details.cover_image"
          >

          <div v-for="imgURL in details.banner_image">
            <img
                class="carousel-img"
                :src="imgURL"
            >
          </div>

        </n-carousel>

        <h3 class="TDTex1">
          {{ $t('traveldetails.tourSnapshot') }}
        </h3>

        <div class="TDRow1">
          <div class="TDR1">
            <img class="TDIcon1" src="../../assets/time_icon.svg" alt="">
            <div class="TDT1">
              {{ $t('traveldetails.duration') }}<br> {{ $t('traveldetails.day', {duration: duration}) }}
            </div>
          </div>

          <div class="TDR1">
            <img class="TDIcon1" src="../../assets/group.svg" alt="">
            <div class="TDT1">
              {{ $t('traveldetails.groupSize') }}<br> {{ details.group_number }}
            </div>
          </div>

          <div v-for="tag in details.tags">
          <div class="TDR1">
            <img class="TDIcon1" src="../../assets/TDtag.svg" alt="">
            <div class="TDT1">
              {{ tag.key }}: <br>{{ tag.value }}
            </div>
          </div>

        </div>

        </div>

        <!--Draw a line to separate-->
        <div class="TDLine"></div>

        <div class="TDOverview">
          <h3 class="TDTex2">{{ $t('traveldetails.overview') }}</h3>

          <p class="TDTex3">
            {{ details.description }}
          </p>
        </div>

        <!--Leave a space to separate-->
        <div class="TDSpace"></div>

<!--        <div class="TDOverview">-->
<!--          <h3 class="TDTex2">Fee Description</h3>-->

<!--          <div v-for="fee in details.fee_des">-->
<!--            <p class="TDTex3 head">-->
<!--              {{ fee.name }}-->
<!--            </p>-->
<!--            <br>-->

<!--            <p class="TDTex3">-->
<!--              {{ fee.description }}-->
<!--            </p>-->
<!--          </div>-->
<!--        </div>-->


      </div>

      <!--   The slide block  -->
      <div class="TDConBox" :style="{top: blockTop}">
        <div class="TDBox">
          <div class="TDTex5">
            {{ $t('traveldetails.price') }} <span class="TDTex6">US${{ details.price }}</span>
          </div>


          <!--     date chosen     -->
          <div class="TDDate">
            <div class="TDOptionName">{{ $t('traveldetails.date') }}</div>
            <div class="TDDataPickers">
              {{ details.start_time }}
              <span>—</span>
              {{ details.end_time }}
            </div>
          </div>

          <!--     number     -->
          <div class="TDDate">
            <div class="TDOptionName">{{ $t('traveldetails.numberOfTravelers') }}</div>
            <n-space vertical>
              <n-input-number
                  v-model:value="groupNum"
                  :placeholder="$t('traveldetails.groupNumber')"
                  :min="1"
                  :max="details.group_number"
                  size="large"
              />
            </n-space>
          </div>

          <div class="book">
            <div class="input_border">
              <button type="submit" class="add_step_btn c" @click="handleClickProject">
                {{ $t('homepage.discountPart.button') }}
              </button>
            </div>
          </div>

          <div class="com">
            <img class="love" src="../../assets/love4.svg">
            <div class="TDTex7">{{ $t('traveldetails.moreThanHalfOfTravelersRecommendThisTrip') }}</div>
          </div>

        </div>

        <div class="TDTex4">{{ $t('traveldetails.notSureYouCanCancelThisReservationUpTo24HoursInAdv') }}</div>
        </div>
    </div>

    <!--Draw a line to separate-->
    <div class="TDLine full"></div>

  </section>

  <charge-list></charge-list>

  <div class="TDLine full"></div>

  <guest-reviews></guest-reviews>

  <div class="TDLine full"></div>

  <leave-reply></leave-reply>

  <div class="TDLine full"></div>

  <similar-experiences></similar-experiences>

  <footer-view></footer-view>
</template>

<script>
import ChargeList from "./chargeList.vue";
import GuestReviews from "./guestReviews.vue";
import LeaveReply from "./leaveReply.vue";
import SimilarExperiences from "./similarExperiences.vue";
import NavigationBar from "../GeneralComponents/navigationBar.vue";
import footerView from "../GeneralComponents/footerView.vue";
import {ref} from "vue";
import { useToast } from "vue-toastification";
import {useRoute} from "vue-router";
import {useStore} from "../../store.js";
import { getCurrentInstance } from 'vue';

export default {
  name: "TravelDetailsView",
  components: {NavigationBar, SimilarExperiences, LeaveReply, GuestReviews, ChargeList, footerView},

  data() {
    star: ref()
    id1: ref()
    return {
      showModalPhotos: false,
      showModalModel: false,
      showModal: false,
      currentIndex: 0,
      imageList: ref(),

      blockHeight: 310, // 制作区块高度
      threshold: 490, // 页面滚动的阈值
      scrollTop: 0, // 页面滚动距离

      // 后端拿到的数据
      details: [],
      duration: 0,
      id: 0,
    };
  },

  setup(){
    const instance = getCurrentInstance();
    const id1 = instance.data.id1;
    let store = useStore();
    let startTime = ref();
    let endTime = ref();
    let groupNum = ref();
    const axios = getCurrentInstance().appContext.config.globalProperties.axios;
    const toast = useToast();


    let user_log_in = ref(false);

    user_log_in.value = store.user_login_status;

    return{
      startTime,
      endTime,
      groupNum,
      toast,
      user_log_in,
      id1,

      handleClickProject() {
        let self = this;

        if (store.user_id === 0){
          self.toast.warning("Please login first",{
            position: "bottom-right",
          });
          } else if (this.groupNum == null ) {
          self.toast.warning("Please enter the number of the travelers first",{
            position: "bottom-right",
          });
        } else {


          axios.post("/order/create_order",
              {
                product_id: this.id1,
                groupNum: this.groupNum,
                user_id: store.user_id
              }
          )
              .then(function (response) {
                if (response.data.code === 200) {
                  self.toast.success("Successfully Reservation", {
                    position: "bottom-right",
                  });
                } else {
                  self.toast.warning("You have already booked this trip", {
                    position: "bottom-right",
                  });
                }
              })
        }
    }
    }
  },

  created() {
    let route = useRoute();
    this.id1 = route.params.trip_id
    this.axios.post('/product/detail', {
      product_id: route.params.trip_id
    })
        .then(response => {
          this.details = response.data.product;
          // console.log(this.details)

          const num1 = new Date(this.details.end_time).getTime()
          const num2 = new Date(this.details.start_time).getTime()
          let diffMs = num1-num2
          // 将毫秒数转换为天数
          this.duration = Math.floor(diffMs / (1000 * 60 * 60 * 24))

          this.star = this.details.mark

          this.imageList = this.details.gallery
        })
        .catch(error => {
          console.error(error);
        });
  },

  mounted() {
    window.addEventListener("scroll", this.handleScroll);

  },
  destroyed() {
    window.removeEventListener("scroll", this.handleScroll);
  },
  methods: {
    toggleModel() {
      this.showModalModel = !this.showModalModel;
    },
    handleScroll() {
      this.scrollTop =
          window.pageYOffset || document.documentElement.scrollTop;
    },
    prevImage() {
      this.currentIndex = (this.currentIndex - 1 + this.imageList.length) % this.imageList.length;
    },
    nextImage() {
      this.currentIndex = (this.currentIndex + 1) % this.imageList.length;
    },
  },
  computed: {
    blockTop() {
      if (this.scrollTop > this.threshold) {
        return `${this.threshold+182 -this.scrollTop}px`;
      } else if (this.scrollTop > this.blockHeight-182) {
        return "182px";
      } else {
        return `${this.blockHeight - this.scrollTop}px`;
      }
    },
  },
}
</script>

<style scoped>
.model {
  width: 640px;
  height: 480px;
}

iframe {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 9999; /* 设置z-index属性来保证iframe浮动在页面最顶层 */
}

.pd{
  padding-top: 40px !important;
}

.space{
  display:flex;
  flex-wrap:wrap;
  justify-content: space-between !important;
  align-items: flex-end !important;
}

.TDTit{
  flex:0 0 auto;
  width:auto;
}

.TDT{
  font-weight: 100;
  font-size: 30px;
  font-family: JostBlod;
}

.lower{
  display:flex;
  flex-wrap:wrap;
  align-items: center !important;
  padding-top: 10px !important;
}

.TDRow{
  flex:0 0 auto;
  width:auto;
  display:flex!important;
  align-items: center !important;
}

.star{
  width: 13px;
  margin-right: 3px;
}

.loc{
  width: 16px;
  margin-left: 18px;
}

.TDReview{
  font-size: 14px;
  color: #697488;
  margin-left: 10px !important;
}

.TDLoc{
  font-size: 14px;
  color: #697488;
  margin-left: 5px;
}

.map{
  color: #3554D1;
  font-size: 14px;
  text-decoration: underline;
  border: none;
  background-color: transparent;
  margin-left: 10px;
  font-family: Jost;
}

.TDImg{
  //display:flex;
  height: 502px;
  flex-wrap:wrap;
  flex:0 0 auto;
  border-radius: 3px;
}

.TDInput_border{
  flex:0 0 auto;
  width:100%;
  margin-top: 20px;
}
.TDmodel{
  position: absolute;
  font-weight: 900;
  font-size: 16px;
  line-height: 1.2;
  border-radius: 4px;
  border: 1px solid transparent;
  transition: all 0.3s cubic-bezier(0.165, 0.84, 0.44, 1);

  padding-top: 15px !important;
  padding-bottom: 15px !important;

  margin-top: 380px;
  margin-left: 20px;
  z-index: 100;


  background-color: white !important;
  color: #3554D1;
  width:170px;
  text-decoration:none;
  font-family: Jost;
}

.TDmodel:hover{
  background-color: #3554D1 !important;
  color: white !important;
}
.TDAdd_btn{
  position: absolute;
  font-weight: 900;
  font-size: 16px;
  line-height: 1.2;
  border-radius: 4px;
  border: 1px solid transparent;
  transition: all 0.3s cubic-bezier(0.165, 0.84, 0.44, 1);

  padding-top: 15px !important;
  padding-bottom: 15px !important;

  margin-top: 440px;
  margin-left: 20px;
  z-index: 100;


  background-color: white !important;
  color: #3554D1;
  width:170px;
  text-decoration:none;
  font-family: Jost;
}

.TDAdd_btn:hover{
  background-color: #3554D1 !important;
  color: white !important;
}

.carousel-img {
  width: 100%;
  height: 502px;
  object-fit: cover;
}

.TDTex1{
  font-size: 22px;
  font-weight: 500;
  margin-top: 25px !important;
}

.TDRow1{
  display:flex;
  flex-wrap:wrap;
  justify-content: space-between !important;
  width: 100%;
}

.TDR1{
  flex:0 0 auto;
  width: auto;
  display: flex !important;
}

.TDT1{
  font-size: 15px;
  line-height: 1.5 !important;
  font-family: JostLight;
  font-weight: 900;
}

.TDIcon1{
  width: 26px;
  margin-right: 10px !important;
  margin-top: -20px;
}

.TDLine{
  border-top: 1px solid #DDDDDD;
  margin-top: 40px !important;
  margin-bottom: 40px !important;
  width: 100%;
}

.TDSpace{
  margin-top: 20px !important;
  margin-bottom: 40px !important;
  width: 100%;
}

.full{
  margin-top: 40px !important;
  margin-bottom: 40px !important;
  margin-left: auto;
  margin-right: auto;
  max-width: 1320px;
}

.TDOverview{
  //display:flex;
  flex-wrap:wrap;

  flex:0 0 auto;
  width: 100%;
}

.TDTex2{
  font-size: 22px;
  font-weight: 500;
  margin: 0;
}

.TDTex3{
  color: #051036;
  font-size: 15px;
  margin: 20px 0 0;
  line-height: 2.5;
}

.head{
  font-size: 17px;
  font-weight: 700;
}

.DTCols1{
  /*//display:flex;*/
  /*//flex-wrap:wrap;*/
  flex:0 0 auto;
  width: 850px;
}

.TDBox{
  flex:0 0 auto;

  justify-content: flex-end !important;

  flex-direction:column!important;
  align-items: center !important;

  border-radius: 4px;
  padding: 30px !important;
  border: 1px solid #DDDDDD !important;
  background-color: #FFFFFF;
  box-shadow: 0 10px 60px 0 #0510360D;

  width: 300px;
  height: 380px;
}

.TDConBox{
  position: fixed;
  display:flex;
  flex-wrap:wrap;
  margin-left: 935px;
  flex-direction: column;
}

.TDTex4{
  padding-left: 30px !important;
  padding-right: 30px !important;
  font-size: 14px;
  color: #697488;
  margin-top: 30px !important;
}

.TDTex5{
  font-size: 15px;
  color: #697488;
}

.TDTex6{
  font-size: 20px;
  font-weight: 500;
  color: #051036;
  margin-left: 5px !important;
  font-family: JostBlod;
}

.TDDate{
  margin-top: 30px;
}

.book{
  margin-top: 25px;
}

.com{
  display:flex!important;
  align-items: center !important;
  padding-top: 20px !important;
}

.TDOptionName{
  margin-bottom: 10px;
  font-size: 17px;
}

.TDDataPickers{
  display: flex;
  text-align: center;
  margin-right: auto;
  margin-left: auto;
  color: #464649;
}

.input_border{
  flex:0 0 auto;
  width:100%;
}

.love{
  display: flex;
  justify-content: center;
  align-items: center;

  height: 35px;
}

.TDTex7{
  font-size: 14px;
  line-height: 1.6 !important;
  margin-left: 10px !important;
  font-family: JostLight;
  font-weight: 900;
}


.add_step_btn{
  font-family: Jost;
  display: flex;
  align-items: center;
  justify-content: center;
  vertical-align: middle;
  text-align: center;
  font-weight: 500;
  font-size: 16px;
  line-height: 1.2;
  border-radius: 4px;
  border: 1px solid transparent;
  transition: all 0.3s cubic-bezier(0.165, 0.84, 0.44, 1);

  width: 100%;
  padding-top: 15px !important;
  padding-bottom: 15px !important;

  background-color: #3554D1 !important;
  color: #FFFFFF;

  text-decoration:none;
}

.add_step_btn.c:after{
  content: '»';
  opacity: 0;
  margin-left: 17px;
  transition: 0.5s;
  font-size: 23px;
}


.add_step_btn.c:hover:after {
  opacity: 1;
  right: 0;
  padding-left: 17px;
}

.add_step_btn:hover{
  border-color:  #051036;
  background-color: #051036 !important;
  color: white !important;
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: black;
  opacity: 0.88;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 10000000 !important;
}

.modal-container {
  background-color: transparent;
//padding: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 44%;
  background-repeat: no-repeat;
  background-size: cover;
}

.enlarge-image {
  width: 100%;
  height: 600px;
  border: none;
}

.image-buttons {
  display: flex;
  justify-content: space-between;
  margin-top: 10px;
  width: 100%;
}

.prev-button,
.next-button,
.close-button {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background-color: rgba(255, 255, 255, 0.5);
  cursor: pointer;
  transition: all 0.3s ease-in-out;
  font-weight: bold;
}

.prev-button:hover,
.next-button:hover,
.close-button:hover {
  background-color: rgba(255, 255, 255, 0.8);
}

.prev-button {
  margin-right: 10px;
}

.close-button {
  position: absolute;
  top: 10px;
  right: 10px;
}

.TDCon{
  width:100%;
  //width: 500px;
  padding-right:15px;
  padding-left: 15px;
  margin-right:auto;
  margin-left:auto;

  display: flex;
  flex-wrap:wrap;
}
@media (min-width:370px){
  .TDCon{
    max-width:350px
  }
  .TDConBox{
    position: static;
    margin-left: 0px;
    justify-content: center;
    flex-direction: row;
    width: 100%;
  }
  .DTCols1{
    width: 100%;
  }
  .TDBox{
    width: 75%;
  }
  .TDTex4{
    width: 75%;
    text-align: center;
  }
}


@media (min-width:576px){
  .TDCon{
    max-width:540px
  }
  .TDConBox{
    position: static;
    margin-left: 0px;
    justify-content: center;
    flex-direction: row;
    width: 100%;
  }
  .DTCols1{
    width: 100%;
  }
  .TDBox{
    width: 75%;
  }
  .TDTex4{
    width: 75%;
    text-align: center;
  }
}

@media (min-width:768px){
  .TDCon{max-width:720px}
}

@media (min-width:992px){
  .TDCon{max-width:960px}
}

@media (min-width:1200px){
  .TDCon{
    max-width:1140px
  }

}

@media (min-width:1400px){
  .TDCon{
    max-width:1320px
  }
  .TDConBox{
    position: fixed;
    margin-left: 935px;
    justify-content: flex-start;
    width: auto;
  }
  .DTCols1{
    width: 850px;
  }
  .TDBox{
    width: 300px;
  }
  .TDTex4{
    text-align: start;
    width: 300px;
  }
}

</style>

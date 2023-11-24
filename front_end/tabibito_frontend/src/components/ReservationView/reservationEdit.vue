<template>
  <div class="bg">
    <div class="container">
      <div class="titlePart">
        <div class="titleMain">
          <h1 class="mainTitle">{{ $t('reservationEdit.editReservation') }}</h1>
          <div class="slogan">{{ $t('reservationEdit.editTheReservationDetailsAndAnnounceTheChangesToTh') }}</div>
        </div>
      </div>
      <div class="settings">
        <n-tabs
            v-model:value="tabValue"
            class="card-tabs"
            size="large"
            animated
            style="margin: 0 -4px"
            pane-style="padding-left: 4px; padding-right: 4px; box-sizing: border-box;">


          <n-tab-pane name="Basic Information" tab="1. Basic Information">
            <div class="tabInnerContainer">

              <div class="inputTitle">{{ $t('reservationEdit.travelTimeDetail') }}</div>

              <div class="dataPickers">
                <n-date-picker v-model:value="startTime" type="date" :is-date-disabled="secureStartTime" size="large" clearable :placeholder="$t('homepage.searchPart.st')"/>
                <n-date-picker v-model:value="endTime" type="date" placement="bottom-end" :is-date-disabled="secureEndTime" size="large" clearable :placeholder="$t('homepage.searchPart.et')"/>
              </div>
            </div>
            <p class="note"> {{ $t('reservationEdit.newTravelTimeWillBeAnnouncedToTheBookingHolderOnce') }}</p>

          </n-tab-pane>

          <n-tab-pane name="Route" tab="2. Route">
            <div class="inputTitle">{{ $t('reservationEdit.totalDayNumber') }}</div>
            <div class="input_form">
              <input type="text" v-model="totalDayNumber" :disabled="totalDayNumberDisabled" required @change="checkAddStepStatus" @blur="validateInteger($event, totalDayNumber, 'totalDayNumber')" @focus="resetInput($event)">
              <label class="input_label">{{ $t('reservationEdit.totalDayNumber') }}</label>
            </div>
            <button type="submit" class="add_step_btn" :class="add_step_status" @click="addStep">
              <div class="icon_add"></div>
              {{ $t('reservationEdit.addStep') }}
            </button>
            <div v-for="(routeData, index) in routeDatas">
              <route-step :step-data="routeData" :step-index="index" @delete-step="handleDeleteStep(index)"></route-step>
            </div>
          </n-tab-pane>


          <n-tab-pane name="Price" tab="3. Price" >
            <div class="inputTitle">{{ $t('reservationEdit.originalPrice') }}</div>
            <div class="input_form">
              <input type="text" v-model="originalPrice" required :style="originalPriceStyle" @blur="validateNumber($event, originalPrice, 'originalPrice')" @focus="resetInput($event)">
              <label class="input_label">{{ $t('reservationEdit.originalPrice') }}</label>
              <n-select
                  v-model:value="currencyType"
                  size="large"
                  :options="currencyOptions"
                  :placeholder="$t('traveldetails.selectCurrencyUnit')"
                  style="width: 200px; margin-left: 10px"
              />
            </div>
            <div class="inputTitle">{{ $t('reservationEdit.discount') }}</div>
            <div class="input_form">
              <input type="text" v-model="discount" required @blur="validateNumber($event, discount, 'discount')" @focus="resetInput($event)">
              <label class="input_label">{{ $t('reservationEdit.discount') }}</label>
            </div>
            <button type="submit" class="add_step_btn" @click="addCharge">
              <div class="icon_add"></div>
              {{ $t('reservationEdit.addCharge') }}
            </button>
            <div v-for="(chargeData, index) in chargeDatas">
              <price-item :item-data="chargeData" :item-index="index" @delete-charge="handleDeleteCharge(index)"></price-item>
            </div>
          </n-tab-pane>

          <n-tab-pane name="Location" tab="4. Reason">
            <div class="tabInnerContainer">
              <div class="inputTitle">{{ $t('reservationEdit.reason') }}</div>
              <div class="input_form">
                <input type="text" v-model="locationText" required>
                <label class="input_label">{{ $t('reservationEdit.reasonsForChangingTheReservation') }}</label>
              </div>

            </div>
          </n-tab-pane>

          <n-tab-pane name="Submit" tab="5. Submit">
            <button type="submit" class="add_step_btn" @click="submitForm">
              {{ $t('reservationEdit.submit') }}
              <div class="icon_submit"></div>
            </button>
          </n-tab-pane>
        </n-tabs>
      </div>
    </div>
  </div>
</template>

<script>
import {ref} from "vue";
import {useMessage} from "naive-ui";
import RouteStep from "../PMDetailView/routeStep.vue";
import PriceItem from "../PMDetailView/priceItem.vue";
import { useToast } from "vue-toastification";

export default {
  name: "projectManagementDetailView",
  components: {PriceItem, RouteStep},
  // beforeRouteEnter(to, from, next){
  //   next((vm) => {
  //     vm.axios.get('/user/login_status')
  //         .then((res) =>{
  //           if (res.data.job === 'Staff'){
  //           }else {
  //             vm.$router.push('/forbidden')
  //           }
  //         })
  //         .catch((e) => {
  //           vm.$router.push('/forbidden')
  //         })
  //   })
  // },
  setup(){
    // General
    let tabValue = ref("Basic Information");
    const message = useMessage();

    // Tab 1
    // let durationMode = ref("Day/Night Mode");
    let startTime = ref(null);
    let endTime = ref(null);
    let tags = ref([
      {
        key: null,
        value: ""
      },
      {
        key: null,
        value: ""
      },
      {
        key: null,
        value: ""
      },
    ]);
    let coverImage = null;
    const handleFinishCover = ({file,event}) => {
      console.log(event);
      let res = (event?.target).response;
      coverImage = res;
    };
    let bannerImages = [];
    const handleFinishBanner = ({file,event}) => {
      console.log(event);
      let res = (event?.target).response;
      bannerImages.push(res);
    };
    let galleryImages = [];
    const handleFinishGallery = ({file,event}) => {
      console.log(event);
      let res = (event?.target).response;
      galleryImages.push(res);
    };
    // Tab 3
    let routeDatas = ref([]);
    let add_step_status = ref("disabled_btn");
    let totalDayNumber = ref();
    let totalDayNumberDisabled = ref(false);

    //Tab 4
    let chargeDatas = ref([]);


    return{
      // General
      tabValue,
      resetInput(e){
        if (e.currentTarget.classList.contains("invalidInput")){
          e.currentTarget.classList.remove("invalidInput");
        }
      },

      // Tab 1
      // durationMode,
      startTime,
      endTime,
      tags,
      coverImageList: ref([]),
      bannerImageList: ref([]),
      galleryList: ref([]),
      coverImage,
      handleFinishCover,
      bannerImages,
      handleFinishBanner,
      galleryImages,
      handleFinishGallery,
      async beforeUpload(data) {
        let reg = /image/
        let fileType = data.file.file?.type
        if (!reg.test(fileType)) {
          message.error("You can only upload images.");
          return false;
        }
        return true;
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
      tagOptions: ref([
        {
          label: "Price",
          value: "Price"
        },
        {
          label: "Hotel",
          value: "Hotel"
        },
        {
          label: "Scenery",
          value: "Scenery"
        },
        {
          label: "Transportation Method",
          value: "Transportation Method"
        },
        {
          label: "Country",
          value: "Country"
        }
      ]),

      // Tab 3
      routeDatas,
      totalDayNumber,
      totalDayNumberDisabled,
      add_step_status,
      checkAddStepStatus(){
        if (totalDayNumber.value !== null && totalDayNumber.value !== 0 && totalDayNumber.value !== '0'){
          let pattern = new RegExp('\\D');
          if (pattern.test(totalDayNumber.value)){
            add_step_status.value = "disabled_btn"
          }else {
            add_step_status.value = ""
          }
        }else {
          add_step_status.value = "disabled_btn"
        }
      },
      addStep(){
        if (add_step_status.value === "disabled_btn"){
          message.error("Please Enter total day number at first.")
        }else {
          if (routeDatas.value.length === 0) {
            totalDayNumberDisabled.value = true;
          }
          routeDatas.value.push({
            totalDayNumber: totalDayNumber.value,
            activityName: "",
            exactLocation: "",
            mapLatitude: "",
            mapLongitude: "",
            mapZoom: "",
            dayNumber: null,
            periodValue: "Morning",
            exactTime: null,
            activityPic: ""
          })
        }
      },

      // Tab 4
      chargeDatas,
      currencyType: ref("USD"),
      currencyOptions: ref([
        {
          label: "USD",
          value: "USD"
        },
        {
          label: "EUR",
          value: "EUR"
        },
        {
          label: "CNY",
          value: "CNY"
        },
      ]),
      addCharge(){
        chargeDatas.value.push({
          chargeName: "",
          chargeDescription: ""
        })
      },
    }
  },
  data() {
    return {
      projectName: null,
      projectNameStyle: null,
      projectDescription: null,
      /*morningNumber: null,
      nightNumber: null,
      dayNumber: null,
      hourNumber: null,*/
      groupNumber: null,
      typeList: [],
      cutoffDate: null,
      locationText: null,
      mapLatitude: null,
      mapLongitude: null,
      mapZoom: null,
      originalPrice: null,
      discount: null,
      originalPriceStyle: null,
    }
  },
  methods:{
    validateInteger(e, value, key){
      let pattern = new RegExp('\\D');
      if (pattern.test(value)){
        this[key] = "";
        e.currentTarget.classList.add("invalidInput");
      }
    },
    validateNumber(e, value, key){
      let reg = /^[0-9]+([.]{1}[0-9]+){0,1}$/
      if (!reg.test(value)){
        this[key] = "";
        e.currentTarget.classList.add("invalidInput");
      }
    },
    handleChooseType(type, e){
      if (this.typeList.indexOf(type) !== -1){
        e.currentTarget.classList.remove('selectedType');
        this.typeList.splice(this.typeList.indexOf(type), 1);
      }else {
        e.currentTarget.classList.add('selectedType');
        this.typeList.push(type);
      }
    },
    /*changeDurationMode(value){
      if (value === "Day/Night Mode"){
        this.dayNumber = "";
        this.hourNumber = "";
        this.durationMode = "Day/Night Mode";
      }
      if (value === "Day/Hour Mode"){
        this.morningNumber = "";
        this.nightNumber = "";
        this.durationMode = "Day/Hour Mode";
      }
    },*/
    handleDeleteStep(index){
      this.routeDatas.splice(index, 1);
      if (this.routeDatas.length === 0){
        this.totalDayNumberDisabled = false;
      }
    },
    handleDeleteCharge(index){
      this.chargeDatas.splice(index, 1);
    },
    submitForm(){
      console.log("ese")
      const toast = useToast();
      if (this.tags[0].value === "" || this.tags[1].value === "" || this.tags[2].value === ""){
        this.tabValue = "Basic Information";
        toast.error("Please enter all the three tags");
        return;
      }
      if(this.projectName === null || this.projectName === ""){
        this.tabValue = "Basic Information";
        this.projectNameStyle = "invalidInput";
        return;
      }
      if(this.originalPrice === null || this.originalPrice=== ""){
        this.tabValue = "Price";
        this.originalPriceStyle = "invalidInput"
        return;
      }
      let trips = [];
      for (let index = 0; index < this.routeDatas.length; index++){
        console.log(this.routeDatas)
        trips.push({
          location: {
            exact: this.routeDatas[index].exactLocation,
            map_latitude: this.routeDatas[index].mapLatitude,
            map_longitude: this.routeDatas[index].mapLongitude,
            map_zoom: this.routeDatas[index].mapZoom
          },
          time: this.routeDatas[index].exactTime,
          activity: this.routeDatas[index].activityName,
          picture: this.routeDatas[index].activityPic,
          day: this.routeDatas[index].dayNumber,
          time_of_day: this.routeDatas[index].periodValue
        })
      }
      let fees = [];
      for (let index = 0; index < this.chargeDatas.length; index++){
        fees.push({
          name: this.chargeDatas[index].chargeName,
          description: this.chargeDatas[index].chargeDescription
        })
      }
      this.axios.post('/product/add', {
        name: this.projectName,
        description: this.projectDescription,
        group_number: this.groupNumber,
        location: {
          raw_loc: this.locationText,
          map_latitude: this.mapLatitude,
          map_longitude: this.mapLongitude,
          map_zoom: this.mapZoom
        },
        discount: this.discount,
        ori_price: this.originalPrice,
        currency: this.currencyType,
        tags: this.tags,
        cover_image: this.coverImage,
        banner_image: this.bannerImages,
        gallery: this.galleryImages,
        start_time: this.startTime,
        end_time: this.endTime,
        app_ddl: this.cutoffDate,
        fee_des: fees,
        trips: trips,
        types: this.typeList
      })
    }
  }
}
</script>

<style scoped>
template{
  background-color: #F5F5F5;
}
.bg{
  width: 100%;
  height: 100vh;
  background-color: #F5F5F5;
}
.container{
  width: 100%;
  padding: 60px 60px 60px 60px;
  box-sizing: border-box;
  background-color: #F5F5F5;
}
.titlePart{
  display: flex;
  box-sizing: border-box;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: flex-end;
  margin-bottom: 50px;
  line-height: 1.875;
}
.titleMain{
  margin: 10px 15px;
  flex: 0 0 auto;
  width: auto;
  box-sizing: border-box;
}
.mainTitle{
  margin: 0;
  font-weight: 600;
  line-height: 1.4;
  font-size: 30px;
}
.slogan{
  font-size: 15px;
  color: var(--secondary-text-color);
}
.settings{
  padding: 30px;
  box-sizing: border-box;
  background-color: white;
}
.tabInnerContainer{
  width: 83.33%;
}
.inputTitle{
  margin: 10px 0;
  font-weight: 500;
  font-size: 18px;
  line-height: 1.875;
}
.input_form{
  position: relative;
  transition: all 0.2s cubic-bezier(0.165, 0.84, 0.44, 1);
  display: flex;
  margin: 10px;
}
.inner_input_form{
  position: relative;
  transition: all 0.2s cubic-bezier(0.165, 0.84, 0.44, 1);
  display: flex;
  width: 30%;
}
.input_label{
  line-height: 1 !important;
  font-size: 14px !important;
  color: #697488;
}

.input_form label {
  position: absolute;
  top: 26px;
  padding: 0 15px;
  pointer-events: none;
  font-size: 14px;
  transition: all 0.2s cubic-bezier(0.165, 0.84, 0.44, 1);
}

.input_form input,textarea {
  border: 1px solid #DDDDDD;
  width: 100%;
  font-size: 15px;
  border-radius: 4px;
  /*padding: 0 15px;*/
  padding-top: 20px;
  padding-left: 15px;
  min-height: 48px;
  transition: all 0.2s cubic-bezier(0.165, 0.84, 0.44, 1);
}

.input_form textarea{
  min-height: 80px;
}

.input_form input:focus,textarea:focus {
  outline: 2px solid #000000 !important;
}

.input_form input:focus ~ label, .input_form input:valid ~ label {
  transform: translateY(-10px);
}
.input_form textarea:focus ~ label, .input_form textarea:valid ~ label {
  transform: translateY(-10px);
}
.input_form textarea{
  box-sizing: border-box;
  padding-top: 35px;
}
.dataPickers{
  display: flex;
  margin:0 10px;
  justify-content: space-between;
}

.note{
  margin-top: 40px;
  color: #757272;
}

.n-date-picker{
  width: 49%;
}

.add_step_btn{
  display: flex;
  align-items: center;
  justify-content: center;
  vertical-align: middle;
  text-align: center;
  font-weight: 500;
  font-size: 17px;
  line-height: 1.2;
  border-radius: 4px;
  border: 1px solid transparent;
  transition: all 0.3s cubic-bezier(0.165, 0.84, 0.44, 1);
  margin-bottom: 10px;
  padding-top: 20px !important;
  padding-bottom: 20px !important;
  cursor: pointer;
  background-color: #3554D1;
  color: #FFFFFF;

  width:100%;

  text-decoration:none;

}

.add_step_btn:hover{
  border-color:  #051036;
  background-color: #051036;
  color: white !important;
}

.icon_add{
  background-image: url("../../assets/AddCircle.svg");
  margin-right: 15px !important;
  background-position: center;
  background-repeat: no-repeat;
  background-size: contain;
  width: 20px;
  height: 20px;
}
.icon_submit{
  background-image: url("../../assets/arrow.svg");
  margin-left: 15px !important;
  background-position: center;
  background-repeat: no-repeat;
  background-size: contain;
  width: 20px;
  height: 20px;
}
.disabled_btn{
  background-color: #DDDDDD;
  cursor: no-drop;
}
.disabled_btn:hover{
  border-color: #DDDDDD;
  background-color: #DDDDDD;
}
.invalidInput{
  border: 1px solid #D03050 !important;
  animation: shake .5s ease-in-out;
}
.typesContainer{
  margin-left: 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.type{
  width: 150px;
  height: 150px;
  border-radius: 4px;
  background-color: #E5F0FD;
  display: flex;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.165, 0.84, 0.44, 1);
}
.typeTitle{
  font-size: 20px;
  margin: auto;
}
.type:hover{
  background-color: var(--primary-color);
  color: white;
  transition: all 0.3s cubic-bezier(0.165, 0.84, 0.44, 1);
}
.selectedType{
  background-color: var(--primary-color);
  color: white;
}
</style>

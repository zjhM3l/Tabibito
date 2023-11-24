<template>
  <div class="bg">
    <div>
      <side-bar-view></side-bar-view>
    </div>
    <div class="container">
      <div class="titlePart">
        <div class="titleMain">
          <h1 class="mainTitle">{{ $t('PMDV.addTravelProject') }}</h1>
          <div class="slogan">{{ $t('traveldetails.addANewTourismProject') }}</div>
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
              <div class="inputTitle">{{ $t('traveldetails.introduction') }}</div>
              <div class="input_form">
                <input type="text" v-model="projectName" required :class="projectNameStyle" @focus="resetInput($event)">
                <label class="input_label">{{ $t('traveldetails.projectName') }}</label>
              </div>
              <div class="input_form">
                <textarea v-model="projectDescription" required></textarea>
                <label class="input_label">{{ $t('traveldetails.projectDescription') }}</label>
              </div>
              <div class="inputTitle">{{ $t('searchPage.duration') }}</div>
<!--              <n-tabs
                  class="card-tabs"
                  size="large"
                  animated
                  v-model:value="durationMode"
                  :on-before-leave="changeDurationMode"
                  style="padding: 0 10px 10px; height: 160px; box-sizing: border-box; border: 1px solid #DDDDDD; border-radius: 4px;"
                  pane-style="padding-left: 4px; padding-right: 4px; box-sizing: border-box;">
                <n-tab-pane name="Day/Night Mode" tab="Day/Night Mode">
                  <div class="input_form" style="justify-content: space-between;">
                    <div class="inner_input_form" style="width: calc(50% - 5px)">
                      <input type="text" v-model="morningNumber" required @blur="validateInteger($event, morningNumber, 'morningNumber')" @focus="resetInput($event)">
                      <label class="input_label">Day Number</label>
                    </div>
                    <div class="inner_input_form" style="width: calc(50% - 5px)">
                      <input type="text" v-model="nightNumber" required @blur="validateInteger($event, nightNumber, 'nightNumber')" @focus="resetInput($event)">
                      <label class="input_label">Night Number</label>
                    </div>
                  </div>
                </n-tab-pane>
                <n-tab-pane name="Day/Hour Mode" tab="Day/Hour Mode" display-directive="if">
                  <div class="input_form" style="justify-content: space-between;">
                    <div class="inner_input_form" style="width: calc(50% - 5px)">
                      <input type="text" v-model="dayNumber" required @blur="validateInteger($event, dayNumber, 'dayNumber')" @focus="resetInput($event)">
                      <label class="input_label">Days</label>
                    </div>
                    <div class="inner_input_form" style="width: calc(50% - 5px)">
                      <input type="text" v-model="hourNumber" required @blur="validateInteger($event, hourNumber, 'hourNumber')" @focus="resetInput($event)">
                      <label class="input_label">Hours</label>
                    </div>
                  </div>
                </n-tab-pane>
              </n-tabs>-->
              <div class="dataPickers">
                <n-date-picker v-model:value="startTime" type="date" :is-date-disabled="secureStartTime" size="large" clearable :placeholder="$t('homepage.searchPart.st')"/>
                <n-date-picker v-model:value="endTime" type="date" placement="bottom-end" :is-date-disabled="secureEndTime" size="large" clearable :placeholder="$t('homepage.searchPart.et')"/>
                <n-date-picker v-model:value="cutoffDate" type="date" placement="bottom-end" size="large" clearable :placeholder="$t('traveldetails.cutoffDate')"/>
              </div>
              <div class="inputTitle">{{ $t('traveldetails.groupNumber') }}</div>
              <div class="input_form">
                <input v-model="groupNumber" required @blur="validateInteger($event, groupNumber, 'groupNumber')" @focus="resetInput($event)"/>
                <label class="input_label" >{{ $t('traveldetails.groupNumber') }}</label>
              </div>
              <div class="inputTitle">{{ $t('traveldetails.youtubeVideo') }}</div>
              <div class="input_form">
                <input v-model="videoLink" required @focus="resetInput($event)"/>
                <label class="input_label" >{{ $t('traveldetails.videoLink') }}</label>
              </div>
              <div class="inputTitle">{{ $t('traveldetails.coverImage') }}</div>
              <n-upload
                  :action="imageAPI"
                  v-model:file-list="coverImageList"
                  list-type="image-card"
                  style="margin-left: 10px"
                  @before-upload="beforeUpload"
                  accept="image/*"
                  @finish="handleFinishCover"
                  @remove="handleRemoveImage"
                  :max=1
              />
              <div class="inputTitle">{{ $t('traveldetails.bannerImage') }}</div>
              <n-upload
                  :action="imageAPI"
                  v-model:file-list="bannerImageList"
                  list-type="image-card"
                  style="margin-left: 10px"
                  @before-upload="beforeUpload"
                  accept="image/*"
                  @finish="handleFinishBanner"
                  @remove="handleRemoveImage"
                  :max=4
              />
              <div class="inputTitle">{{ $t('traveldetails.gallery') }}</div>
              <n-upload
                  :action="imageAPI"
                  v-model:file-list="galleryImageList"
                  list-type="image-card"
                  style="margin-left: 10px"
                  @before-upload="beforeUpload"
                  accept="image/*"
                  @finish="handleFinishGallery"
                  @remove="handleRemoveImage"
              />
              <div class="inputTitle">{{ $t('homepage.searchPart.tags') }}</div>
              {{tags}}
              <div class="input_form" v-for="tag in tags">
                <n-select
                    v-model:value="tag.key"
                    size="large"
                    :options="tagOptions"
                    :placeholder="$t('traveldetails.selectATagType')"
                    style="width: 250px; margin-right: 10px"
                />
                <input type="text" v-model="tag.value" required @focus="resetInput($event)">
                <label class="input_label tag_input_label" style="left: 200px">{{ $t('traveldetails.tagValue') }}</label>
              </div>

              <div class="inputTitle">{{ $t('traveldetails.types') }}</div>

              <div class="typesContainer">
                <div class="type" @click="handleChooseType('WildlifeTour', $event)">
                  <div class="typeTitle">{{ $t('chooseTourTypes.wildlifeTour') }}</div>
                </div>
                <div class="type" @click="handleChooseType('AdventureTour', $event)">
                  <div class="typeTitle">{{ $t('chooseTourTypes.adventureTour') }}</div>
                </div>
                <div class="type" @click="handleChooseType('CityTour', $event)">
                  <div class="typeTitle">{{ $t('traveldetails.cityTour') }}</div>
                </div>
                <div class="type" @click="handleChooseType('MuseumTour', $event)">
                  <div class="typeTitle">{{ $t('traveldetails.museumTour') }}</div>
                </div>
                <div class="type" @click="handleChooseType('BeachesTour', $event)">
                  <div class="typeTitle">{{ $t('chooseTourTypes.beachesTour') }}</div>
                </div>
              </div>
            </div>
          </n-tab-pane>


          <n-tab-pane name="Location" tab="2. Location">
            <div class="tabInnerContainer">
              <div class="inputTitle">{{ $t('homepage.searchPart.loc') }}</div>
              <div class="input_form">
                <input type="text" v-model="locationText" required>
                <label class="input_label">{{ $t('PMDV.locationText') }}</label>
              </div>
              <div class="input_form" style="justify-content: space-between;">
                <div class="inner_input_form">
                  <input type="text" v-model="mapLatitude" required @blur="validateInteger($event, mapLatitude, 'mapLatitude')" @focus="resetInput($event)">
                  <label class="input_label">{{ $t('routeStep.mapLatitude') }}</label>
                </div>
                <div class="inner_input_form">
                  <input type="text" v-model="mapLongitude" @blur="validateInteger($event, mapLongitude, 'mapLongitude')" required @focus="resetInput($event)">
                  <label class="input_label">{{ $t('routeStep.mapLongitude') }}</label>
                </div>
                <div class="inner_input_form">
                  <input type="text" v-model="mapZoom" @blur="validateInteger($event, mapZoom, 'mapZoom')" required @focus="resetInput($event)">
                  <label class="input_label">{{ $t('routeStep.mapZoom') }}</label>
                </div>
              </div>
            </div>
          </n-tab-pane>


          <n-tab-pane name="Route" tab="3. Route">
            <div class="inputTitle">{{ $t('traveldetails.totalDayNumber') }}</div>
            <div class="input_form">
              <input type="text" v-model="totalDayNumber" :disabled="totalDayNumberDisabled" required @keyup="checkAddStepStatus" @blur="validateInteger($event, totalDayNumber, 'totalDayNumber')" @focus="resetInput($event)">
              <label class="input_label">{{ $t('reservationEdit.totalDayNumber') }}</label>
            </div>
            <div class="inputTitle">{{ $t('reservationEdit.flightNumber') }}</div>
            <div class="input_form" style="justify-content: space-between;">
              <div class="inner_input_form">
                <input type="text" v-model="flight_numbers[0]" required>
                <label class="input_label">{{ $t('reservationEdit.flightNumber1') }}</label>
              </div>
              <div class="inner_input_form">
                <input type="text" v-model="flight_numbers[1]" required>
                <label class="input_label">{{ $t('reservationEdit.flightNumber2') }}</label>
              </div>
              <div class="inner_input_form">
                <input type="text" v-model="flight_numbers[2]" required>
                <label class="input_label">{{ $t('reservationEdit.flightNumber3') }}</label>
              </div>

            </div>
            <button type="submit" class="add_step_btn" :class="add_step_status" @click="addStep">
              <div class="icon_add"></div>
              {{ $t('traveldetails.addStep') }}
            </button>
            <div v-for="(routeData, index) in routeDatas">
              <route-step :step-data="routeData" :step-index="index" @delete-step="handleDeleteStep(index)"></route-step>
            </div>
          </n-tab-pane>


          <n-tab-pane name="Price" tab="4. Price" >
            <div class="inputTitle">{{ $t('traveldetails.originalPrice') }}</div>
            <div class="input_form">
              <input type="text" v-model="originalPrice" required :style="originalPriceStyle" @blur="validateNumber($event, originalPrice, 'originalPrice')" @focus="resetInput($event)">
              <label class="input_label">{{ $t('traveldetails.originalPrice') }}</label>
              <n-select
                  v-model:value="currencyType"
                  size="large"
                  :options="currencyOptions"
                  :placeholder="$t('traveldetails.selectCurrencyUnit')"
                  style="width: 200px; margin-left: 10px"
              />
            </div>
            <div class="inputTitle">{{ $t('traveldetails.discount') }}</div>
            <div class="input_form">
              <input type="text" v-model="discount" required @blur="validateNumber($event, discount, 'discount')" @focus="resetInput($event)">
              <label class="input_label">{{ $t('reservationEdit.discount') }}</label>
            </div>
            <button type="submit" class="add_step_btn" @click="addCharge">
              <div class="icon_add"></div>
              {{ $t('traveldetails.addCharge') }}
            </button>
            <div v-for="(chargeData, index) in chargeDatas">
              <price-item :item-data="chargeData" :item-index="index" @delete-charge="handleDeleteCharge(index)"></price-item>
            </div>
          </n-tab-pane>

<!--          <n-tab-pane name="Notification" tab="5. Notification">
            <div class="inputTitle">{{ $t('traveldetails.title') }}</div>
            <div class="input_form">
              <input type="text" @focus="resetInput($event)">
              <label class="input_label">{{ $t('traveldetails.title') }}</label>
            </div>
            <div class="inputTitle">{{ $t('homepage.searchPart.tags') }}</div>

            <div class="input_form" style="justify-content: space-between;">
              <n-select
                  style="margin-right: 20px"
                  v-model:value="tagValue"
                  multiple
                  :render-tag="renderTag"
                  :options="noticeTags"
                  max-tag-count="1"
              />
              <n-input :placeholder="$t('traveldetails.newTag')" style="margin-right: 20px"></n-input>
              <n-button type="primary">{{ $t('traveldetails.add') }}</n-button>
            </div>

            <div class="inputTitle">{{ $t('traveldetails.content') }}</div>
            <div class="input_form">
              <textarea v-model="projectDescription" required></textarea>
              <label class="input_label">{{ $t('traveldetails.content') }}</label>
            </div>
          </n-tab-pane>-->


          <n-tab-pane name="Submit" tab="5. Submit">
            <button type="submit" class="add_step_btn" @click="submitForm">
              {{ $t('traveldetails.submit') }}
              <div class="icon_submit"></div>
            </button>
          </n-tab-pane>
        </n-tabs>
      </div>
    </div>
  </div>
</template>

<script>
import {h, ref} from "vue";
import {NTag, useMessage} from "naive-ui";
import RouteStep from "./routeStep.vue";
import PriceItem from "./priceItem.vue";
import { useToast } from "vue-toastification";
import {useRoute} from "vue-router";
import {getCurrentInstance} from 'vue'
import SideBarView from "../StaffPortalView/sideBarView.vue";
export default {
  name: "projectManagementDetailView",
  components: {SideBarView, PriceItem, RouteStep},
  /*beforeRouteEnter(to, from, next){
    next((vm) => {
      vm.axios.get('/user/login_status')
          .then((res) =>{
            if (res.data.job === 'Staff'){
            }else {
                // vm.$router.push('/forbidden')
            }
          })
          .catch((e) => {
              vm.$router.push('/forbidden')
          })
    })
    /!*axios.get('http://127.0.0.1:5000/user/login_status')
        .then((res) =>{
          if (res.data.job === 'Staff'){
            return;
          }else {
            next((vm) =>{
              vm.$router.push('/forbidden')
            })
          }
        })
        .catch((e) => {
          next((vm) =>{
            vm.$router.push('/forbidden')
          })
        })*!/
  },*/
  setup(){
    // General
    const axios = getCurrentInstance().appContext.config.globalProperties.axios;
    let tabValue = ref("Basic Information");
    const message = useMessage();
    const baseURL = getCurrentInstance().appContext.config.globalProperties.axios.defaults.baseURL;
    const imageAPI = baseURL + '/product/uploadpicture';
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
    let coverImageList = ref([]);
    let bannerImageList = ref([]);
    let galleryImageList = ref([]);
    const handleFinishCover = ({file,event}) => {
      let res = (event?.target).response;
      file.url = res;
    };
    const handleFinishBanner = ({file,event}) => {
      let res = (event?.target).response;
      file.url = res;
    };
    const handleFinishGallery = ({file,event}) => {
      let res = (event?.target).response;
      file.url = res;
    };
    const handleRemoveImage = ({file, fileList}) => {
      let fileIndex = -1;
      for (let i = 0; i < fileList.length; i++){
        if (file.id === fileList[i].id){
          fileIndex = i
        }
      }
      axios.post('/product/deletepicture', {
        url: fileList[fileIndex].url
      })
          .then((res) => {
            if (res.status === 200){
              fileList.splice(fileIndex, 1);
              return true;
            }
          })
    };
    // Tab 3
    let routeDatas = ref([]);
    let add_step_status = ref("disabled_btn");
    let totalDayNumber = ref();
    let totalDayNumberDisabled = ref(false);

    //Tab 4
    let chargeDatas = ref([]);

    //Tab 5
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
      // General
      tabValue,
      imageAPI,
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
      coverImageList,
      bannerImageList,
      galleryImageList,
      handleFinishCover,
      handleFinishBanner,
      handleFinishGallery,
      handleRemoveImage,
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
        if (totalDayNumber.value !== null && totalDayNumber.value !== 0 && totalDayNumber.value !== '0' && totalDayNumber.value !== ''){
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
      ]),
      addCharge(){
        chargeDatas.value.push({
          chargeName: "",
          chargeDescription: ""
        })
      },

      // Tab 5
      renderTag,
      tagValue: ref([]),
    }
  },
  created() {
    const route = useRoute();
    if (route.params.id !== null){
      this.axios.post('', )
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
      videoLink: '',
      typeList: [],
      cutoffDate: null,
      locationText: null,
      mapLatitude: null,
      mapLongitude: null,
      mapZoom: null,
      flight_numbers: ['', '', ''],
      originalPrice: null,
      discount: null,
      originalPriceStyle: null,
      noticeTags: [
      {
        label: "Flight Change",
        value: "value1",
        type: "success"
      },
      {
        label: "Time Change",
        value: "value2",
        type: "warning"
      },
      {
        label: "Other change",
        value: "value3",
        type: "error"
      },
    ]
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
  let coverImage = this.coverImageList[0].url;
  let bannerImages = [];
  for (let file of this.bannerImageList){
    bannerImages.push(file.url)
  }
  let galleryImages = [];
  for (let file of this.bannerImageList){
    galleryImages.push(file.url)
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
    total_day_number: this.totalDayNumber,
    discount: this.discount,
    ori_price: this.originalPrice,
    currency: this.currencyType,
    tags: this.tags,
    cover_image: coverImage,
    banner_image: bannerImages,
    gallery: galleryImages,
    start_time: this.startTime,
    end_time: this.endTime,
    app_ddl: this.cutoffDate,
    fee_des: fees,
    trips: trips,
    types: this.typeList,
    flight_numbers: this.flight_numbers,
    video_link: this.videoLink,
    url_3d: null
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
    height: fit-content;
    background-color: #F5F5F5;
    display: flex;
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
  @media screen and (max-width: 1150px) {
    .tabInnerContainer{
      width: 100%;
    }
  }
  @media screen and (max-width: 980px) {
    .container{
      padding-left: 30px;
      padding-right: 30px;
    }
    .typesContainer{
      flex-wrap: wrap;
    }
    .type{
      margin: 3px;
      width: 120px;
      height: 120px;
    }
    .typeTitle {
      font-size: 18px;
    }
  }
  @media screen and (max-width: 920px) {
    .typesContainer {
      justify-content: flex-start;
    }
    .type {
      margin: 5px;
      width: 110px;
      height: 110px;
    }
    .typeTitle{
      font-size: 16px;
    }
  }
  @media screen and (max-width: 670px) {
    .tag_input_label{
      left: 170px !important;
    }
  }

  @media screen and (max-width: 430px) {
    .tag_input_label{
      left: 120px !important;
    }
  }
</style>

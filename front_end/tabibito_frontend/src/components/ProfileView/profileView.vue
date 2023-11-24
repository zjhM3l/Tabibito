<template>
<navigation-bar></navigation-bar>
  <div class="bg">
    <div class="container">
      <div class="titlePart">
        <div class="titleMain">
          <h1 class="mainTitle">{{ $t('profile.personalCenter') }}</h1>
          <div class="slogan">{{ $t('profile.manageAllTheInformationYouNeedHere') }}</div>
        </div>
      </div>
      <div class="settings">
        <n-modal v-model:show="showModal">
          <div class="modalBody">
            <div class="orderBasic">
              <div class="attrTitle">{{ $t('profile.travelName') }}</div>
              <div class="attrValue">{{ modalData.name}}</div>
              <div class="attrTitle">{{ $t('homepage.searchPart.stet') }}</div>
              <div class="attrValue">{{modalData.startTime + " - " + modalData.endTime}}</div>
              <div class="attrTitle">{{ $t('profile.travelDetail') }}</div>
              <div class="attrValue link" @click="this.$router.push('/trip/' + modalData.trip_id)">{{ $t('profile.goToTravelDetail') }}</div>
            </div>
            <div class="itinerary">
              <div class="attrTitle">{{ $t('profile.itinerary') }}</div>
              <n-timeline v-for="step in modalData.trip" style="margin-left: 12px; margin-top: 12px;">
                <n-timeline-item
                    :type="step.finished"
                    :title="step.title"
                    :content="step.content"
                    :time="'day ' + step.day + ' ' + step.time_of_day + ', ' + step.time"
                />
              </n-timeline>
            </div>
          </div>

        </n-modal>
        <n-tabs
            v-model:value="tabValue"
            class="card-tabs"
            size="large"
            animated
            style="margin: 0 -4px"
            pane-style="padding-left: 4px; padding-right: 4px; box-sizing: border-box;">

          <n-tab-pane name="Dashboard" tab="Dashboard" display-directive="show:lazy">
            <div class="helloSection">
              <img :src="basicInfo.avatar_url" class="helloAvatar">
              <div class="greeting">{{ $t('profile.hello', {expr: 'Hello, ' + basicInfo.username + '. Which trip do you want to enjoy today?'}) }}</div>
            </div>
            <div class="recentTrip" v-for="trip in recentTrips">
              <div class="recentTripTitleBar">
                <div class="recentTripName">{{trip.name}}</div>
                <div class="recentTripMore" @click="this.$router.push('/trip/' + trip.trip_id)">{{ $t('hotLocation.more') }}</div>
              </div>
              <div class="recentTripBody">
                <img class="tripCover" :src="trip.cover_url"/>
                <n-modal v-model:show="showWeatherModel">

                </n-modal>
                <div class="weatherPart">
                  <div class="city">{{trip.weather.city}}</div>
                  <div class="weatherMain">
                    <div class="temperature">{{ $t('profile.temp', {expr: trip.weather.temp.toFixed(0) + '℃'}) }}</div>
                    <img :src="trip.weather.img_url" alt="" class="weatherImg">
                  </div>
                  <div class="forecast">
                    <div class="foreTemp">
                      <div class="tempValue">{{ $t('profile.maxtemp', {expr: trip.weather.max_temp.toFixed(0) + '℃'}) }}</div>
                      <div class="tempType">{{ $t('profile.max') }}</div>
                    </div>
                    <div class="foreTemp">
                      <div class="tempValue">{{ $t('profile.avgtemp', {expr: trip.weather.avg_temp.toFixed(0) + '℃'}) }}</div>
                      <div class="tempType">{{ $t('profile.avg') }}</div>
                    </div>
                    <div class="foreTemp">
                      <div class="tempValue">{{ $t('profile.mintemp', {expr: trip.weather.min_temp.toFixed(0) + '℃'}) }}</div>
                      <div class="tempType">{{ $t('profile.min') }}</div>
                    </div>
                  </div>
                </div>
                <div class="aeroPart">
                  <div class="flightTitle">{{ $t('profile.flightInformation') }}</div>
                  <div class="flightStatus">{{trip.flightInfo.status}}</div>
                  <div class="infoColumn">
                    <div class="airportNo">{{trip.flightInfo.departure.airport_no}}</div>
                    <div class="airportNo">{{trip.flightInfo.arrival.airport_no}}</div>
                  </div>
                  <div class="infoColumn">
                    <div class="airportLoc">{{trip.flightInfo.departure.airport_loc}}</div>
                    <div class="airportLoc">{{trip.flightInfo.arrival.airport_loc}}</div>
                  </div>
                  <div class="infoColumn">
                    <div class="airDes">{{ $t('profile.takesOffFrom') }}</div>
                    <div class="airDes">{{ $t('profile.landingAt') }}</div>
                  </div>
                  <div class="infoColumn">
                    <div class="airportName">{{trip.flightInfo.departure.airport_name}}</div>
                    <div class="airportName">{{trip.flightInfo.arrival.airport_name}}</div>
                  </div>
                  <div class="infoColumn">
                    <div class="date">{{trip.flightInfo.departure.date}}</div>
                    <div class="date">{{trip.flightInfo.arrival.date}}</div>
                  </div>
                  <div class="infoColumn">
                    <div class="time">{{trip.flightInfo.departure.time}}</div>
                    <div class="time">{{trip.flightInfo.arrival.time}}</div>
                  </div>
                </div>
              </div>
            </div>
            <div class="footPrintMap" id="map"></div>
          </n-tab-pane>

          <n-tab-pane name="Profile" tab="Profile" display-directive="show:lazy">
<!--            <div class="infoCard">-->
<!--              <img class="avatar" :src="basicInfo.avatar_url">-->
<!--              <div class="cardText">-->
<!--                <div class="nameBar">-->
<!--                  <div class="userName">{{basicInfo.username}}</div>-->
<!--                  <div class="edit" @click="this.$router.push(this.$route.path + '/edit')">-->
<!--                    {{ $t('profile.editInfo') }}-->
<!--                  </div>-->
<!--                </div>-->
<!--                <div class="userDescription">{{basicInfo.description}}</div>-->
<!--              </div>-->
<!--            </div>-->
<!--            <div class="attrTitle">{{ $t('profile.realName') }}</div>-->
<!--            <div class="attrValue">{{basicInfo.first_name + ' ' + basicInfo.last_name}}</div>-->
<!--            <div class="attrTitle">{{ $t('login.email') }}</div>-->
<!--            <div class="attrValue">{{basicInfo.email}}</div>-->
<!--            <div class="attrTitle">{{ $t('profile.phoneNumber') }}</div>-->
<!--            <div class="attrValue">{{basicInfo.phone_number}}</div>-->
<!--            <div class="attrTitle">{{ $t('profile.birthday') }}</div>-->
<!--            <div class="attrValue">{{basicInfo.birthday}}</div>-->
            <right-setting-view></right-setting-view>
          </n-tab-pane>

          <n-tab-pane name="Orders" tab="Orders" display-directive="show:lazy">
            <n-tabs
                v-model:value="orderType"
                class="card-tabs"
                size="large"
                animated
                pane-style="padding-left: 4px; padding-right: 4px; box-sizing: border-box;"
            >
              <n-tab-pane name="In Progress" tab="In Progress">
                <n-data-table
                    :columns="inProgressColumns"
                    :data="inProgressData"
                />
              </n-tab-pane>

              <n-tab-pane name="Completed" tab="Completed">
                <n-data-table
                    :columns="completedColumns"
                    :data="completedData"
                />
              </n-tab-pane>

              <n-tab-pane name="Cancelled" tab="Cancelled">
                <n-data-table
                    :columns="cancelledColumns"
                    :data="cancelledData"
                />
              </n-tab-pane>

            </n-tabs>
          </n-tab-pane>

          <n-tab-pane name="Your Comments" tab="Your Comments" display-directive="show:lazy">
            <div v-for="comment in this.comments" class="comment">
              <div class="commentHead">
                <div class="leftCommentHead">
                  <img class="commentAvatar" :src="comment.user_portrait">
                  <div class="commentHeadTexts">
                    <div class="commentName">{{comment.user_name}}</div>
                    <div class="commentTime">{{comment.datetime}}</div>
                  </div>
                </div>
                <n-popconfirm
                    @positive-click="handleDeleteComment"
                >
                  <template #trigger>
                    <div class="commentAction">{{ $t('profile.delete') }}</div>
                  </template>
                  {{ $t('profile.areYouSureYouWantToDeleteYourComment') }}
                </n-popconfirm>
              </div>
              <div class="commentScore">{{comment.score}}</div>
              <p class="commentDescription">{{comment.des}}</p>
              <div class="commentPictures">
                <img v-for="pic in comment.pics" class="commentPicture" :src="pic">
              </div>
            </div>
            <n-pagination
                v-model:page="commentPage"
                :page-count="commentPages"
                v-model:page-size="commentPageSize"
                @update:page-size="handleChangePageSize"
                @update:page="handleChangePage"
                show-size-picker
                :page-sizes="[10, 20, 30, 40]"></n-pagination>
          </n-tab-pane>

          <n-tab-pane name="Notices" tab="Notices" display-directive="show:lazy">
            <div class="notice" v-for="notice in newNotices">
              <div class="noticeTitleBar">
                <div class="noticeTitleLeft">
                  <div class="noticeTitle">{{notice.title}}</div>
                  <div class="noticeType">{{ notice.type }}</div>
                  <div class="noticeBadge"></div>
                  <div class="noticeTime">{{notice.time}}</div>
                </div>
                <div class="noticeCheckBt" @click="handleCheck(notice.id)">{{ $t('profile.check') }}</div>
              </div>
              <div class="noticeContent">{{notice.content}}</div>
            </div>
            <div class="notice" v-for="notice in oldNotices">
              <div class="noticeTitleBar">
                <div class="noticeTitleLeft">
                  <div class="noticeTitle">{{notice.title}}</div>
                  <div class="noticeType">{{ notice.type }}</div>
                  <div class="noticeTime">{{notice.time}}</div>
                </div>
                <div class="noticeCheckBt" @click="handleUncheck(notice.id)">{{ $t('profile.uncheck') }}</div>
              </div>
              <div class="noticeContent">{{notice.content}}</div>
            </div>
          </n-tab-pane>

<!--          <n-tab-pane name="Your Blogs" tab="Your Blogs">
            <div class="blog">
              <n-popconfirm
                  @positive-click="handleDeleteBlog"
              >
                <template #trigger>
                  <div class="blogAction">delete</div>
                </template>
                Are you sure you want to delete your blog?
              </n-popconfirm>

              <img class="blogCover">
              <div class="blogInfo">
                <div class="blogDate">April 06, 2022</div>
                <div class="blogTitle">fsdf sdfsdffd fsdfsdfsdf</div>
                <div class="blogDescription">sdfsdf sdfdsfdsfsd fsdf sdfsdffd fsdfsdfsdf sdfdsfdsfsd fsdf sdfsdffd fsdfsdfsdf sdfdsfdsfsd fsdf sdfsdffd fsdfsdfsdf sdfdsfdsfsd </div>
              </div>
            </div>
          </n-tab-pane>-->

<!--          <n-tab-pane name="Preference" tab="Preference">
            <div class="attrTitle">Language</div>
            <n-select v-model:value="chosenLanguage" :options="languageOptions" />
          </n-tab-pane>-->
        </n-tabs>
      </div>
    </div>
  </div>
</template>

<script>
import NavigationBar from "../GeneralComponents/navigationBar.vue";
import {getCurrentInstance, h, ref} from "vue";
import { NButton } from "naive-ui";
import {Loader} from "@googlemaps/js-api-loader";
import * as regionLookupClient from "@googlemaps/region-lookup";
import {useLangStore} from "../../store.js";
import * as RegionLookup from "@googlemaps/region-lookup";
import RightSettingView from "./rightSettingView.vue";

const createInProgressColumns = ({ cancel, viewDetail }) => {
  return [
    {
      title: "Travel Name",
      key: "travelName"
    },
    {
      title: "Start Date",
      key: "startDate"
    },
    {
      title: "End Date",
      key: "endDate"
    },
    {
      title: "Create Date",
      key: "createDate"
    },
    {
      title: "Paid",
      key: "paid",
      sorter: {
        compare: (a, b) => a.paid - b.paid
      }
    },
    {
      title: "Cancel",
      key: "cancel",
      render(row) {
        return h(
            NButton,
            {
              strong: true,
              secondary: true,
              type: 'error',
              onClick: () => cancel(row)
            },
            { default: () => "cancel"}
        )
      }
    },
    {
      title: "View Detail",
      key: "viewDetail",
      render(row) {
        return h(
            NButton,
            {
              strong: true,
              secondary: true,
              type: 'info',
              onClick: () => viewDetail(row)
            },
            {default: () => "view detail"}
        )
      }
    },
  ]
}
const createCompletedColumns = ({ viewDetail }) => {
  return [
    {
      title: "Travel Name",
      key: "travelName"
    },
    {
      title: "Start Date",
      key: "startDate"
    },
    {
      title: "End Date",
      key: "endDate"
    },
    {
      title: "Create Date",
      key: "createDate"
    },
    {
      title: "Paid",
      key: "paid",
      sorter: {
        compare: (a, b) => a.paid - b.paid
      }
    },
    {
      title: "View Detail",
      key: "viewDetail",
      render(row) {
        return h(
            NButton,
            {
              strong: true,
              secondary: true,
              type: 'info',
              onClick: () => viewDetail(row)
            },
            {default: () => "view detail"}
        )
      }
    },
  ]
}
const createCancelledColumns = ({ viewDetail }) => {
  return [
    {
      title: "Travel Name",
      key: "travelName"
    },
    {
      title: "Start Date",
      key: "startDate"
    },
    {
      title: "End Date",
      key: "endDate"
    },
    {
      title: "Create Date",
      key: "createDate"
    },
    {
      title: "Paid",
      key: "paid",
      sorter: {
        compare: (a, b) => a.paid - b.paid
      }
    },
    {
      title: "View Detail",
      key: "viewDetail",
      render(row) {
        return h(
            NButton,
            {
              strong: true,
              secondary: true,
              type: 'info',
              onClick: () => viewDetail(row)
            },
            {default: () => "view detail"}
        )
      }
    },
  ]
}
export default {
  name: "profileView",
  components: {RightSettingView, NavigationBar},

  setup() {
    const langStore = useLangStore();
    let mapLanguage = 'en-US';
    if (langStore.language === 'zh') {
      mapLanguage = 'zh-CN'
    }
    const axios = getCurrentInstance().appContext.config.globalProperties.axios;
    const inProgressData = ref([]);
    let modalData = ref({
      name: '',
      startTime: '',
      endTime: '',
      trip_id: 0,
      trip: [
        {
          finished: 'false',
          title: '',
          content: '',
          day: 0,
          time_of_day: '',
          time: ''
        }
      ]
    });
    let showModal = ref(false);
    axios.post('/user/get_user_order', {
      // user_id: this.$route.params.uid,
      order_status: 'Processing'
    })
        .then((res) => {
          if (res.status === 200) {
            for (const item of res.data.all_orders) {
              inProgressData.value.push({
                id: item.id,
                travelName: item.name,
                startDate: item.start_time,
                endDate: item.end_time,
                createDate: item.res_time,
                paid: (item.price * item.discount).toFixed(2)
              })
            }
          }
        })
    return {
      mapLanguage,
      inProgressData,
      showModal,
      modalData,
      tabValue: ref("Dashboard"),
      dashboardValue: ref("Recent Trips"),
      orderType: ref("In Progress"),
      inProgressColumns: createInProgressColumns({
        cancel(row) {

          axios.post('/staff_portal/product_status?apifoxApiId=75345235', {
            id: row.id,
            operation: 'Cancelled',
          })
              .then((res) => {
                for (let item of inProgressData.value) {
                  if (item.id === row.id) {
                    inProgressData.value.splice(inProgressData.value.indexOf(item), 1)
                  }
                }
              })
        },
        viewDetail(row) {

          axios.post('/user/get_order_detail', {
            id: row.id
          })
              .then((res) => {
                if (res.status === 200) {
                  modalData.value = res.data
                  console.log(modalData.value)
                }
              })
          showModal.value = true;
        }
      }),
      completedColumns: createCompletedColumns({
        viewDetail(row) {
          axios.post('/user/get_order_detail', {
            id: row.id
          })
              .then((res) => {
                if (res.status === 200) {
                  modalData.value = res.data
                  console.log(modalData.value)
                }
              })
          showModal.value = true;
        }
      }),
      cancelledColumns: createCancelledColumns({
        viewDetail(row) {
          axios.post('/user/get_order_detail', {
            id: row.id
          })
              .then((res) => {
                if (res.status === 200) {
                  modalData.value = res.data
                  console.log(modalData.value)
                }
              })
          showModal.value = true;
        }
      }),
      /*loadMap() {
        const headers = {
          "X-Goog-Api-Key": "AIzaSyBctzU8ocpP_0j4IdTRqA-GABIAnaXd0ow",
        };

        const data = {
          search_values: [
            {
              "address": "2627 N Hollywood Way, Burbank, CA",
              "place_type": "ADMINISTRATIVE_AREA_LEVEL_1",
              "region_code": "us"

            },
          ],
        };
        const response = regionLookupClient.searchRegion({headers, data});

        let placeID;
        response.then((res) => {
          placeID = res.data.matches[0].matchedPlaceId;
          console.log(placeID)
          const loader = new Loader({
            apiKey: "AIzaSyBctzU8ocpP_0j4IdTRqA-GABIAnaXd0ow",
            version: "weekly",
            libraries: ["marker", "drawing", "visualization", "geometry", "localContext", "places"],
            language: mapLanguage
          });
          let featureLayer;
          loader.load().then((google) => {
            // const center = this.project_loc;
            console.log(document.getElementById('map'));
            let map = new google.maps.Map(document.getElementById("map"), {
              center: {lat: 20.773, lng: -156.01},
              zoom: 1,
              mapId: "83a836f63edecc9b"
            });
            featureLayer = map.getFeatureLayer("ADMINISTRATIVE_AREA_LEVEL_1");
            console.log(featureLayer)
            const featureStyleOptions = {
              strokeColor: "#810FCB",
              strokeOpacity: 1.0,
              strokeWeight: 3.0,
              fillColor: "#810FCB",
              fillOpacity: 0.5,
            };
            featureLayer.style = (options) => {
              if (options.feature.placeId === "ChIJPV4oX_65j4ARVW8IJ6IJUYs") {
                return featureStyleOptions;
              }
            };

          });
        })


      },*/

    }
  },
  data() {
    return {
      recentTrips: [],
      basicInfo: {},
      completedData: [],
      cancelledData: [],
      commentPage: ref(1),
      commentPages: ref(20),
      commentPageSize: ref(10),
      commentNumber: 0,
      comments: [],
      newNotices: ref([]),
      oldNotices: ref([]),
      footPrints: {
        search_values: [],
      }
    }
  },
  methods: {
    handleCancel(row) {

    },
    initMap(){
      const headers = {
        "X-Goog-Api-Key": "AIzaSyBctzU8ocpP_0j4IdTRqA-GABIAnaXd0ow",
      };

      /*let instance = axios.create();
      instance.headers = headers;
      instance.data = d;
      instance.defaults.withCredentials = false;*/
      const data = this.footPrints;
      const response = regionLookupClient.searchRegion({headers, data, withCredentials: false});
      let placeIDs;
      response.then((res) => {
        placeIDs = res.data.matches;
        let map;
        map = new google.maps.Map(document.getElementById('map'), {
          center: {lat: 20, lng: 0},
          zoom: 2,
          mapId: "353522139b1baa35",
        })
        let featureLayer = map.getFeatureLayer('ADMINISTRATIVE_AREA_LEVEL_1');
        const featureStyleOptions = {
          strokeColor: "#810FCB",
          strokeOpacity: 1.0,
          strokeWeight: 3.0,
          fillColor: "#810FCB",
          fillOpacity: 0.5,
        };
        featureLayer.style = (options) => {
          for (let obj of placeIDs){

            if (options.feature.placeId === obj.matchedPlaceId) {

              return featureStyleOptions;
            }
          }
        };

      })
    },
    handleChangePageSize(pageSize) {
      this.commentPages = Math.ceil(this.commentNumber / this.commentPageSize);
      this.axios.post('/comment/get_page', {
        page_number: this.commentPage,
        page_size: this.commentPageSize
      })
          .then((res) => {
            if (res.status === 200) {
              this.comments = res.data.comments
            }
          })
    },
    handleChangePage() {
      this.axios.post('/comment/get_page', {
        page_number: this.commentPage,
        page_size: this.commentPageSize
      })
          .then((res) => {
            if (res.status === 200) {
              this.comments = res.data.comments
            }
          })
    },
    handleDeleteComment(id) {
      this.axios.post('/comment/delete', {
        id: id
      })
          .then((res) => {
            if (res.status === 200) {
              this.axios.post('/comment/get_page', {
                page_number: this.commentPage,
                page_size: this.commentPageSize
              })
                  .then((res) => {
                    if (res.status === 200) {
                      this.comments = res.data.comments
                    }
                  })
            }
          })
    },
    handleCheck(id) {
      this.axios.post('/user/check_notice', {
        id: id,
        new_status: 'old'
      })
          .then((res) => {
            if (res.status === 204) {
              let index = -1
              for (let i = 0; i < this.newNotices.length; i++) {
                if (this.newNotices[i].id === id) {
                  index = i
                }
              }
              this.oldNotices.push(this.newNotices[index]);
              this.newNotices.splice(index, 1);
            }
          })
    },
    handleUncheck(id) {
      this.axios.post('/user/check_notice', {
        id: id,
        new_status: 'new'
      })
          .then((res) => {
            if (res.status === 204) {
              let index = -1
              for (let i = 0; i < this.oldNotices.length; i++) {
                if (this.oldNotices[i].id === id) {
                  index = i
                }
              }
              this.newNotices.unshift(this.oldNotices[index]);
              this.oldNotices.splice(index, 1);
            }
          })
    }
  },
  created() {

    // this.loadMap();
    this.axios.post('/user/dashboard/get_recent_trips')
        .then((res) => {
          if (res.status === 200) {
            this.recentTrips = res.data.recentTrips
            for (let trip of this.recentTrips) {
              this.axios.post('/third/weather', {
                location: trip.raw_loc
              })
                  .then((res) => {
                    if (res.status === 200) {
                      trip.weather = res.data;
                    }
                  })
              console.log()
              if (trip.flight_numbers !== null){
                this.axios.post('/third/flight', {
                  flight_numbers: trip.flight_numbers
                })
                    .then((res) => {
                      if (res.status === 200) {
                        trip.flightInfo = res.data
                      }
                    })
              }

            }
          }
        })
    this.axios.post('/user/getprofile', {
      user_id: this.$route.params.uid
    })
        .then((res) => {
          this.basicInfo = res.data
        })

    this.axios.post('/comment/user_all_number')
        .then((res) => {
          if (res.status === 200) {
            this.commentNumber = res.data.number;
            this.commentPages = Math.ceil(this.commentNumber / this.commentPageSize)
          }
        })
    this.axios.post('/comment/get_page', {
      page_number: this.commentPage,
      page_size: this.commentPageSize
    })
        .then((res) => {
          if (res.status === 200) {
            this.comments = res.data.comments
          }
        })
    this.axios.post('/user/get_user_order', {
      user_id: this.$route.params.uid,
      order_status: 'Completed'
    })
        .then((res) => {
          if (res.status === 200) {
            for (const item of res.data.all_orders) {
              this.completedData.push({
                id: item.id,
                travelName: item.name,
                startDate: item.start_time,
                endDate: item.end_time,
                createDate: item.res_time,
                paid: (item.price * item.discount).toFixed(2)
              })
            }
          }
        })
    this.axios.post('/user/get_user_order', {
      user_id: this.$route.params.uid,
      order_status: 'Cancelled'
    })
        .then((res) => {
          if (res.status === 200) {
            for (const item of res.data.all_orders) {
              this.cancelledData.push({
                id: item.id,
                travelName: item.name,
                startDate: item.start_time,
                endDate: item.end_time,
                createDate: item.res_time,
                paid: (item.price * item.discount).toFixed(2)
              })
            }
          }
        })
    this.axios.post('/user/get_notices', {
      status: 'new'
    })
        .then((res) => {
          if (res.status === 200) {
            this.newNotices = res.data.notices;
          }
        })
    this.axios.post('/user/get_notices', {
      status: 'old'
    })
        .then((res) => {
          if (res.status === 200) {
            this.oldNotices = res.data.notices;
          }
        })
    this.axios.get('/third/getfootprint')
        .then((res) => {
          if (res.status === 200){
            for (let item of res.data.locations){
              this.footPrints.search_values.push({
                "address": item,
                "place_type": "ADMINISTRATIVE_AREA_LEVEL_1",
              })
            }
          }
        })
  },
  mounted() {
    let script = document.createElement('script');
    script.type = 'text/javascript';
    script.src = 'https://maps.googleapis.com/maps/api/js?key=AIzaSyBctzU8ocpP_0j4IdTRqA-GABIAnaXd0ow&callback=initMap&v=beta&language=' + this.mapLanguage;
    document.body.appendChild(script);
    window.initMap = this.initMap
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
  box-sizing: border-box;
  padding-top: 90px;
  padding-bottom: 90px;
  background-color: #F5F5F5;
}
.container{
  max-width: 1260px;
  padding: 60px 0 0 0;
  margin: auto;
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
  max-width: 100%;
}
.tabInnerContainer{
  width: 83.33%;
}
.helloSection{
  margin: 24px;
  height: 140px;
  display: grid;
  grid-template-columns: 140px 1fr;
  grid-template-rows: 1fr;
  border-radius: 4px;
  box-shadow: 0 1px 10px rgba(0, 0, 0, 0.08) ;
}
.helloAvatar{
  width: 100px;
  height: 100px;
  border-radius: 100%;
  margin: 20px;
}
.greeting{
  font-size: 24px;
  font-weight: 500;
  display: flex;
  align-items: center;
}
.recentTrip{
  margin: 24px;
  height: 340px;
  border-radius: 4px;
  box-shadow: 0 1px 10px rgba(0, 0, 0, 0.08);
}
.recentTripTitleBar{
  width: 100%;
  height: 60px;
  display: flex;
  justify-content: space-between;
  box-sizing: border-box;
  align-items: center;
  padding: 0 24px;
}
.recentTripName{
  font-size: 24px;
}
.recentTripMore{
  font-size: 20px;
  color: var(--primary-color);
  text-decoration: underline;
  cursor: pointer;
}
.recentTripBody{
  height: 280px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-shrink: 0;
  box-sizing: border-box;
  padding: 24px;
}
.tripCover{
  width: 200px;
  height: 232px;
  object-fit: cover;
  object-position: center;
  border-radius: 4px;
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
.aeroPart{
  width: calc((100% - 200px - 48px - 48px) * 0.67);
  height: 232px;
  border-radius: 4px;
  transition: .2s ease-in;
  cursor: pointer;
  padding: 12px;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  background: linear-gradient(rgba(255, 255, 255, 0.5), rgba(255, 255, 255, 0.5)), url("../../assets/airplane_bg.jpg") no-repeat 50% 50%/ cover;
}
.aeroPart:hover{
  transition: .2s ease-out;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.12) ;
}
.flightTitle{
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 4px;
  position: relative;
}
.flightStatus{
  width: fit-content;
  padding: 0 6px;
  background-color: #2F80ED;
  border-radius: 4px;
  color: white;
}
.infoColumn{
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 16px;
}
.airportNo{
  font-size: 17px;
}
.airportLoc{
  font-size: 16px;
  font-weight: bold;
}
.airDes{
  font-size: 12px;
}
.airportName{
  text-decoration-line: underline;
  color: #2F80ED;
}
.flightStatus{
  font-size: 14px;
}
.footPrintMap{
  margin: 24px;
  height: 500px;
  border-radius: 4px;
}
.infoCard{
  width: 100%;
  box-sizing: border-box;
  padding: 12px;
  display: flex;
}
.avatar{
  margin-right: 24px;
  width: 100px;
  height: 100px;
  object-fit: cover;
  object-position: top;
}
.nameBar{
  display: flex;
  justify-content: space-between;
}
.userName{
  margin: 6px 0;
  font-size: 20px;
}
.edit{
  width: 100px;
  height: auto;
  background-color: var(--primary-color);
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 4px;
  transition: .1s ease-out;
  cursor: pointer;
}
.edit:hover{
  background-color: #0d2857;
  transition: .1s ease-in;
}
.description{
  color: var(--secondary-text-color);
}
.modalBody{
  background-color: white;
  box-sizing: border-box;
  padding: 12px;
  max-height: 600px;
  overflow-y: auto;
  border-radius: 4px;
}
.attrTitle{
  margin-left: 12px;
  width: fit-content;
  font-size: 20px;
  border-bottom: var(--primary-color) 2px solid;
}
.attrValue{
  margin: 12px 0 12px 16px;
}
.link{
  color: var(--primary-color);
  text-decoration: underline;
  cursor: pointer;
}
.comment{
  width: 100%;
  box-sizing: border-box;
  padding: 12px;
  margin-bottom: 30px;
}
.commentHead{
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.leftCommentHead{
  display: flex;
}
.commentAvatar{
  object-fit: contain;
  border-radius: 100%;
  width: 60px;
  height: 60px;
}
.commentHeadTexts{
  margin: auto auto auto 12px;
}
.commentName{
  margin: 4px 0;
}
.commentTime{
  font-size: 14px;
  color: var(--secondary-text-color);
}
.commentAction{
  width: 100px;
  height: 44px;
  background-color: rgb(247, 222, 227);
  color: rgb(208, 48, 80);
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 4px;
  transition: .1s ease-out;
  cursor: pointer;
  user-select: none;
}
.commentAction:hover{
  background-color: rgb(208, 48, 80);
  color: rgb(247, 222, 227);
}
.commentScore{
  margin: 12px 0;
  color: var(--primary-color);
  font-size: 20px;
}
.commentDescription{
  line-height: 1.875;
  margin: 0;
}
.commentPictures{
  display: flex;
  flex-wrap: wrap;

}
.commentPicture{
  border-radius: 4px;
  object-fit: contain;
  object-position: center;
  height: 110px;
  width: 110px;
  margin-right: 30px;
}
.notice{
  width: 100%;
  box-sizing: border-box;
  padding: 12px;
  margin-bottom: 30px;
  height: 160px;
}
.noticeTitleBar{
  display: flex;
  justify-content: space-between;
  height: 40px;
}
.noticeTitleLeft{
  display: flex;
  align-items: center;
}
.noticeCheckBt{
  color: var(--primary-color);
  text-decoration: underline;
  cursor: pointer;
}
.noticeTitle{
  font-size: 20px;
  margin-right: 12px;
}
.noticeType{
  box-sizing: border-box;
  border-radius: 16px;
  padding: 0 10px;
  height: 20px;
  font-size: 12px;
  background-color: rgb(219, 235, 253);
  color: var(--primary-color);
  display: flex;
  align-items: center;
  margin-right: 12px;
}
.noticeBadge{
  margin-right: 12px;
  height: 5px;
  width: 5px;
  border-radius: 100%;
  background-color: red;
}
.noticeTime{
  color: var(--secondary-text-color);
  font-size: 12px;
}
.noticeContent{
  height: 120px;
  overflow-y: auto;
}
.blog{
  display: flex;
  margin-bottom: 30px;
  height: 250px;
  overflow: hidden;
  text-overflow: ellipsis;
  position: relative;
}
.blogAction{
  position: absolute;
  right: 0;
  width: 100px;
  height: 44px;
  background-color: rgb(247, 222, 227);
  color: rgb(208, 48, 80);
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 4px;
  transition: .1s ease-out;
  cursor: pointer;
  user-select: none;
}
.blogAction:hover{
  background-color: rgb(208, 48, 80);
  color: rgb(247, 222, 227);
}
.blogCover{
  margin-right: 30px;
  min-width: 250px;
  height: 250px;
  object-fit: cover;
  object-position: center;
  border-radius: 4px;
}
.blogInfo{
  margin: auto 0;
}
.blogDate{
  color: var(--secondary-text-color);
  font-size: 15px;
}
.blogTitle{
  margin-top: 10px;
  font-size: 22px;
  line-height: 1.45;
}
.blogDescription{
  font-size: 15px;
  color: var(--secondary-text-color);
  margin-top: 10px;
}
@media screen and (max-width: 1300px) {
  .container{
    padding-left: 15px;
    padding-right: 15px;
  }
}
</style>

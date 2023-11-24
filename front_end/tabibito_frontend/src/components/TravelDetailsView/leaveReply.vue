<template>

  <section>
    <div class="container">
      <div class="row y-gap-30 leave_message_wrap">
        <div class="col-xl-3">
          <div class="row">
            <div class="col-auto">
              <h3 class="lm_left_title">
                {{ $t('leaveReply.leaveAReply') }}
              </h3>
              <p class="lm_left_subtitle">
                {{ $t('leaveReply.yourEmailAddressWillNotBePublished') }}
              </p>
            </div>
          </div>
          <div class="row y-gap-30 lm_left_stars">
            <div class="col-sm-6">
              <div class="star_title">
                {{ $t('homepage.searchPart.loc') }}
              </div>
              <div class="star_wrap">
                <template v-for="index in 10" :key="index">
                  <n-icon class="star" @click="setRating('location', index)">
                    <star :class="{ filled: isLocationActive(index) }" />
                  </n-icon>
                </template>
              </div>
            </div>
            <div class="col-sm-6">
              <div class="star_title">
                {{ $t('leaveReply.staff2') }}
              </div>
              <div class="star_wrap">
                <template v-for="index in 10" :key="index">
                  <n-icon class="star" @click="setRating('staff', index)">
                    <star :class="{ filled: isStaffActive(index) }" />
                  </n-icon>
                </template>
              </div>
            </div>
            <div class="col-sm-6">
              <div class="star_title">
                {{ $t('leaveReply.cleanliness2') }}
              </div>
              <div class="star_wrap">
                <template v-for="index in 10" :key="index">
                  <n-icon class="star" @click="setRating('cleanliness', index)">
                    <star :class="{ filled: isCleanlinessActive(index) }" />
                  </n-icon>
                </template>
              </div>
            </div>
            <div class="col-sm-6">
              <div class="star_title">
                {{ $t('leaveReply.valueForMoney2') }}
              </div>
              <div class="star_wrap">
                <template v-for="index in 10" :key="index">
                  <n-icon class="star" @click="setRating('value_for_money', index)">
                    <star :class="{ filled: isValueForMoneyActive(index) }" />
                  </n-icon>
                </template>
              </div>
            </div>
            <div class="col-sm-6">
              <div class="star_title">
                {{ $t('leaveReply.comfort2') }}
              </div>
              <div class="star_wrap">
                <template v-for="index in 10" :key="index">
                  <n-icon class="star" @click="setRating('comfort', index)">
                    <star :class="{ filled: isComfortActive(index) }" />
                  </n-icon>
                </template>
              </div>
            </div>
            <div class="col-sm-6">
              <div class="star_title">
                {{ $t('leaveReply.facilities2') }}
              </div>
              <div class="star_wrap">
                <template v-for="index in 10" :key="index">
                  <n-icon class="star" @click="setRating('facilities', index)">
                    <star :class="{ filled: isFacilitiesActive(index) }" />
                  </n-icon>
                </template>
              </div>
            </div>
            <div class="col-sm-6">
              <div class="star_title">
                {{ $t('leaveReply.freeWifi2') }}
              </div>
              <div class="star_wrap">
                <template v-for="index in 10" :key="index">
                  <n-icon class="star" @click="setRating('free_wifi', index)">
                    <star :class="{ filled: isFreeWifiActive(index) }" />
                  </n-icon>
                </template>
              </div>
            </div>
          </div>
        </div>

        <div class="list_wrap">
          <n-space vertical>
            <div class="form_input">
              <n-input v-model:value="title" type="text" size="large" :placeholder="$t('leaveReply.title')" clearable
                       show-count
                       :maxlength="12"
                       :count-graphemes="countGraphemes"/>
            </div>
            <div class="form_input">
              <n-input
                  v-model:value="des"
                  type="textarea"
                  size="large"
                  :placeholder="$t('leaveReply.writeYourComment')"
                  clearable
                  show-count
                  :maxlength="200"
                  :count-graphemes="countGraphemes"
              />
            </div>
            <n-button strong secondary type="info" size="large" icon-placement="right" @click="handleComment"
                      :disabled="isButtonDisabled || !locationRated || !staffRated || !cleanlinessRated || !valueForMoneyRated || !comfortRated || !facilitiesRated || !freeWifiRated">
              <template #icon>
                <n-icon>
                  <ArrowForwardOutline />
                </n-icon>
              </template>
              {{ $t('leaveReply.postComment') }}
            </n-button>
          </n-space>

        </div>

      </div>
    </div>
  </section>

</template>

<script>
import { defineComponent, ref, computed } from 'vue'
import {StarHalf as star} from "@vicons/ionicons5";
import {ArrowForwardOutline} from "@vicons/ionicons5";
import axios from 'axios'
export default defineComponent({
  name: "leaveReply",
  components: {
    star,
    ArrowForwardOutline
  },
  data() {
    return {
      value: ref(null),
      locationRating: 0,
      staffRating: 0,
      cleanlinessRating: 0,
      valueForMoneyRating: 0,
      comfortRating: 0,
      facilitiesRating: 0,
      freeWifiRating: 0,
      locationRated: false,
      staffRated: false,
      cleanlinessRated: false,
      valueForMoneyRated: false,
      comfortRated: false,
      facilitiesRated: false,
      freeWifiRated: false,
    }
  },
  methods: {
    setRating(category, rating) {
      // Update the corresponding rating property based on the category
      switch (category) {
        case 'location':
          this.locationRating = rating;
          this.locationRated = true;
          break;
        case 'staff':
          this.staffRating = rating;
          this.staffRated = true;
          break;
        case 'cleanliness':
          this.cleanlinessRating = rating;
          this.cleanlinessRated = true;
          break;
        case 'value_for_money':
          this.valueForMoneyRating = rating;
          this.valueForMoneyRated = true;
          break;
        case 'comfort':
          this.comfortRating = rating;
          this.comfortRated = true;
          break;
        case 'facilities':
          this.facilitiesRating = rating;
          this.facilitiesRated = true;
          break;
        case 'free_wifi':
          this.freeWifiRating = rating;
          this.freeWifiRated = true;
          break;
        default:
          break;
      }
    },
  },
  computed: {
    isLocationActive() {
      return (index) => index <= this.locationRating;
    },
    isStaffActive() {
      return (index) => index <= this.staffRating;
    },
    isCleanlinessActive() {
      return (index) => index <= this.cleanlinessRating;
    },
    isValueForMoneyActive() {
      return (index) => index <= this.valueForMoneyRating;
    },
    isComfortActive() {
      return (index) => index <= this.comfortRating;
    },
    isFacilitiesActive() {
      return (index) => index <= this.facilitiesRating;
    },
    isFreeWifiActive() {
      return (index) => index <= this.freeWifiRating;
    },
  },
  setup () {
    const title = ref("");
    const des = ref("");

    const isButtonDisabled = computed(() => {
      return !title.value || !des.value;
    });

    const handleComment = async () => {
          if (!isButtonDisabled.value) {
            try {
              const response = await axios.post("/comment/add_comment", {
                title: title.value,
                des: des.value,
                user_id: null,
                product_id: 9,
                location_grade: this.locationRating,
                staff_grade: this.staffRating,
                cleanliness_grade: this.cleanlinessRating,
                value_for_money_grade: this.valueForMoneyRating,
                comfort_grade: this.comfortRating,
                facilities_grade: this.facilitiesRating,
                free_wifi_grade: this.freeWifiRating,
                pics: [],
              });
              console.log(response.data); // 输出后端返回的数据
            } catch (error) {
              console.error(error);
            }
          }
    };

    return {
      title,
      isButtonDisabled,
      des,
      handleComment}
  },
})
</script>

<style scoped>
.form_input {
  position: relative;
  transition: all 0.2s cubic-bezier(0.165, 0.84, 0.44, 1);
  display: flex;
}

.list_wrap {
  margin-top: -15px;
  margin-bottom: -15px;
}

.star {
  /* 未选中状态的星星样式 */
  color: gray;
}

.filled {
  /* 选中状态的星星样式 */
  color: #FF8F00;
}

.star_wrap {
  display:flex;
  margin-left: -2.5px;
  margin-right: -2.5px;
  align-items: center;
  padding-top: 10px;
}

.star_title {
  font-size: 15px;
  line-height: 1;
  font-weight: 500;
}

.lm_left_stars {
  padding-top: 30px;
}
.lm_left_subtitle {
  font-size: 15px;
  color: #051036;
  margin-top: 5px;
}

.lm_left_title {
  font-size: 22px;
  font-weight: 500;
}

.leave_message_wrap {
  justify-content: space-between !important;
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
    max-width:300px
  }
}

@media (min-width:450px){
  .container{
    max-width:400px
  }
}
@media (min-width:550px){
  .container{
    max-width:540px
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

@media (min-width:768px){
  .row-cols-md-auto>*{flex:0 0 auto;width:auto}
  .row-cols-md-1>*{flex:0 0 auto;width:100%}
  .row-cols-md-2>*{flex:0 0 auto;width:50%}
  .row-cols-md-3>*{flex:0 0 auto;width:33.33333%}
  .row-cols-md-4>*{flex:0 0 auto;width:25%}
  .row-cols-md-5>*{flex:0 0 auto;width:20%}
  .row-cols-md-6>*{flex:0 0 auto;width:16.66667%}
  .col-md-6{flex:0 0 auto;width:50%}
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

.y-gap-20 {
  margin-top: -10px;
  margin-bottom: -10px;
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

</style>

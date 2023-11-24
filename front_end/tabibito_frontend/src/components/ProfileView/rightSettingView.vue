<template>
  <div class="tabInnerContainer">
    <div class="tabs_content">
      <div class="row y-gap-30 tab_main">
        <div class="col-auto">
          <div class="avatar_container">
            <img :src="avatar" alt="avatar" style="
              position: absolute;
              top: 30px;
              left: 30px;
              width: 180px;
              height: 180px;
              -o-object-fit: cover;
              /*object-fit: cover;*/
              border-radius: 4px;"
            />
            <n-upload
                action="/profile/uploadavatar"
                :default-file-list="coverImageList"
                list-type="image-card"
                style="position: relative;
                       top: -15px;
                       left: 30px;
                       width: 200px;
                       height: 200px;
                       -o-object-fit: cover;
                       object-fit: cover;
                       border-radius: 4px;"
                @before-upload="beforeUpload"
                accept="image/*"
                @finish="handleFinishAvatar"
                :max=1
                :disabled="!isEditing"
            />
          </div>
        </div>

        <div class="col-auto">
          <h4 class="avatar_title">{{ $t('rightSetting.yourAvatar') }}</h4>
          <div class="avatar_text">{{ $t('rightSetting.pngOrJpgNoBiggerThan800pxWideAndTall') }}</div>
        </div>
      </div>

      <div class="line"></div>

      <div class="col-xl-9">
        <div class="row x-gap-20 y-gap-20">
          <div class="col-12">

            <div class="input_form">
              <input type="text" v-model="gender" :readonly="!isEditing" required>
              <label class="label">{{ $t('rightSetting.gender') }}</label>
            </div>

          </div>

          <div class="col-12">

            <div class="input_form">
              <input type="text" v-model="u_name" :readonly="!isEditing" required>
              <label class="label">{{ $t('rightSetting.userName') }}</label>
            </div>

          </div>

          <div class="col-md-6">

            <div class="input_form">
              <input type="text" v-model="f_name" :readonly="!isEditing" required>
              <label class="label">{{ $t('reg.fir') }}</label>
            </div>

          </div>

          <div class="col-md-6">

            <div class="input_form">
              <input type="text" v-model="l_name" :readonly="!isEditing" required>
              <label class="label">{{ $t('reg.las') }}</label>
            </div>

          </div>

          <div class="col-md-6">

            <div class="input_form">
              <input type="text" v-model="email" :readonly="true" required>
              <label class="label">{{ $t('login.email') }}</label>
            </div>

          </div>

          <div class="col-md-6">

            <div class="input_form">
              <input type="text" v-model="phone" :readonly="!isEditing" required>
              <label class="label">{{ $t('rightSetting.phoneNumber') }}</label>
            </div>

          </div>

          <div class="col-12">

            <div class="input_form">
              <input type="text" v-model="birthday" :readonly="!isEditing" required>
              <label class="label">{{ $t('rightSetting.birthday') }}</label>
            </div>

          </div>

          <div class="col-12">

            <div class="input_form">
              <textarea v-model="about" :readonly="!isEditing" required rows="5"></textarea>
              <label class="label">{{ $t('rightSetting.aboutYourself') }}</label>
            </div>

          </div>
        </div>
      </div>

      <div class="btn_container">
        <a class="button px-24 -dark-1 btn_bg" @click="toggleEdit">
          {{ buttonText }} <div class="icon-arrow-top-right ml-15"></div>
        </a>
      </div>

    </div>
  </div>

</template>

<script>
import { defineComponent, ref } from 'vue'
import {ArrowForwardOutline} from "@vicons/ionicons5";
import axios from 'axios';

export default defineComponent({
  name: "rightSettingView",
  components: {
    ArrowForwardOutline
  },
  created() {
    this.axios.get('/profile/info').then(res => {
      this.avatar = res.data.avatar;
      this.gender = res.data.gender;
      this.u_name = res.data.u_name;
      this.f_name = res.data.f_name;
      this.l_name = res.data.l_name;
      this.email = res.data.email;
      this.phone = res.data.phone;
      this.birthday = res.data.birthday;
      this.about = res.data.about;
    })
  },
  data() {
    return {
      isEditing: false,
      avatar: '',
      gender: '',
      u_name: '',
      f_name: '',
      l_name: '',
      email: '',
      phone: '',
      birthday: '',
      about: ''
    }
  },
  computed: {
    buttonText() {
      return this.isEditing ? 'Save' : 'Edit';
    },
  },
  methods: {
    toggleEdit() {
      this.isEditing = !this.isEditing;
      if (!this.isEditing) {
        axios.post('/profile/update_info', {
          u_name: this.u_name,
          gender: this.gender,
          f_name: this.f_name,
          l_name: this.l_name,
          email: this.email,
          phone: this.phone,
          birthday: this.birthday,
          about: this.about,
        });
      }
    },
  },
})
</script>

<style scoped>
.btn_container {
  display:inline-block!important;
  padding-top: 30px !important;
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
  border-radius: 4px;
  border: 1px solid transparent;
  transition: all 0.3s cubic-bezier(0.165, 0.84, 0.44, 1);
  height: 50px !important;
  padding-left: 24px !important;
  padding-right: 24px !important;
}
.button.-dark-1:hover {
  border-color: #051036;
  background-color: #051036 !important;
  color: white !important;
}
.btn_bg {
  background-color: #3554D1 !important;
  color: #FFFFFF;
}
.label {
  line-height: 1 !important;
  font-size: 16px !important;
  color: #697488;
}
.input_form {
  position: relative;
  transition: all 0.2s cubic-bezier(0.165, 0.84, 0.44, 1);
  display: flex;
}
.input_form label {
  position: absolute;
  top: 0;
  top: 26px;
  padding: 0 15px;
  pointer-events: none;
  font-size: 14px;
  transition: all 0.2s cubic-bezier(0.165, 0.84, 0.44, 1);
}

.input_form textarea,
.input_form input {
  width: 100%;
  border: 1px solid #DDDDDD;
  border-radius: 4px;
  padding: 25px 15px 0;
  min-height: 50px;
  transition: all 0.2s cubic-bezier(0.165, 0.84, 0.44, 1);
}

.input_form textarea:focus,
.input_form input:focus {
  border: 2px solid #051036 !important;
}

.input_form textarea:focus ~ label, .input_form textarea:valid ~ label,
.input_form input:focus ~ label, .input_form input:valid ~ label {
  transform: translateY(-10px);
}
.line {
  border-top: 1px solid #DDDDDD;
  margin-top: 30px !important;
  margin-bottom: 30px !important;
}
.avatar_title {
  font-size: 16px;
  font-weight: 500;
}
.avatar_text {
  font-size: 14px;
  margin-top: 5px;
}
.avatar_container {
  display: flex !important;
  padding-bottom: 0;
  width: 200px;
  max-width: 100%;
}
.tab_main {
  align-items: center;
}
.tabs_content {
  position: relative;
  padding-top: 30px !important;
}
.tabInnerContainer {
  padding: 30px !important;
  border-radius: 4px;
  background-color: #FFFFFF !important;
  box-shadow: 0px 10px 30px 0px #05103608;
}




.x-gap-20 {
  margin-left: -10px;
  margin-right: -10px;
}

.x-gap-20 > * {
  padding-left: 10px;
  padding-right: 10px;
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

.col-12{
  flex:0 0 auto;
  width:100%
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
  .col-xl{flex:1 0 0%}
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
  .col-xl-9{flex:0 0 auto;width:75%}
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
</style>

<template>
  <navigation-bar></navigation-bar>

  <div class="bg">

    <div class="container">

      <n-card class="card">

        <div class="border">

          <h1 class="font_login">{{ $t('forget.res')}}</h1>
          <p class="font_acc">{{ $t('forget.rem')}}
            <router-link to="/login" class="font_blue">{{ $t('forget.log')}}</router-link></p>

          <form autocomplete="off">

            <!--          账号部分-->
            <div class="input_border">

              <div class="input_form">
                <input type="text" v-model="inputE" required>
                <label class="input_label">{{ $t('forget.email')}}</label>
              </div>

            </div>

            <!--          验证码部分-->
            <div class="input_border">

              <div class="input_form">

                <div class="half_1">
                  <input type="text" v-model="code" required>
                  <label class="input_label">{{ $t('forget.veri')}}</label>
                </div>

                <div class="half_2">
                  <!--          验证码按钮-->
                  <a class="add_step_btn verify" @click="startCountdown" v-show="!countingDown">
                    {{ $t('forget.get')}}
                  </a>
                  <a class="add_step_btn verify" v-if="countingDown">{{ remainingTime }} s </a>
                </div>
              </div>


            </div>


            <!--          按钮-->
            <div class="input_border">

              <button type="submit" class="add_step_btn c" @click="verify">
                {{ $t('forget.conti')}}
              </button>

            </div>

          </form>

          <!--          其他登陆方式-->
          <div class="input_border">
            <div class="text_center">{{ $t('forget.or')}}</div>

            <button class="other_login_btn">
              <i class="google_icon"></i>
              {{ $t('forget.Google')}}
            </button>

          </div>

          <div class="input_border">

            <div class="text_note">{{ $t('forget.reset')}}</div>


          </div>


        </div>

      </n-card>

    </div>



  </div>

  <footer-view></footer-view>


</template>

<script>

import navigationBar from "../GeneralComponents/navigationBar.vue";
import FooterView from "../GeneralComponents/footerView.vue";
import {getCurrentInstance} from 'vue'
import {useToast} from "vue-toastification";

export default {
  setup() {
    const axios = getCurrentInstance().appContext.config.globalProperties.axios;
    // axios.defaults.withCredentials = true;
    // Get toast interface
    const toast = useToast();

    // Make it available inside methods
    return { toast }
  },
  components: {FooterView, navigationBar},
  name: "forgetPasswordView",
  data() {
    return {
      countingDown: false,
      remainingTime: 60,
      countdownInterval: null,

      inputE: '',
      code:''
    };
  },
  methods: {
    startCountdown() {
      let self = this;

      this.countingDown = true;
      this.remainingTime = 60; // add this line to reset remainingTime to 60
      this.countdownInterval = setInterval(() => {
        if (this.remainingTime > 0) {
          this.remainingTime--;
        } else {
          clearInterval(this.countdownInterval);
          this.countingDown = false;
        }
      }, 1000);

      let emailValue = this.inputE;

      const tester = /^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/;
      if (!tester.test(emailValue)) {
        self.toast.error("This email is not valid");
      } else {

        this.toast.success("Captcha sends successfully");

        this.axios.post('/user/captcha', {
          email: emailValue,

        }).then(function (response) {
          let code = response.data['code'];
          let message = response.data['message'];
          if (code === 200) {
            self.toast.success("Captcha sends successfully");
          } else if (code === 400) {
            if (message === 'email') {
              self.toast.error("Email is not registered");
            }
          }
        }).catch(function (error) {
          console.log(error);
        });
      }
    },

    verify(){
      let self = this;
      let emailValue = this.inputE;
      let codeValue = this.code;

      if (this.inputE === ''){
        this.toast.error("The email can't be blank");
      }

      const tester = /^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/;
      if (!tester.test(this.inputEmail1)){
        this.toast.error("This email is not valid");
      }

      this.axios.post('/user/forget_form_email', {
        email: emailValue,
        verifyCode: codeValue

      }).then(function (response){
        let code=response.data['code'];
        let message=response.data['message'];
        if (code === 200){
          console.log("成功")
          self.$router.push('/reset');
        } else if (code === 400){
          if (message === 'captcha'){
            self.toast.error("The verification code is not correctly");
          }
          if (message === 'email'){
            self.toast.error("This email is not valid");
          }
        }
      }).catch(function (error) {
        console.log(error);
      });
    }


  }

}
</script>

<style scoped>

@font-face {
  font-family: myFont;
  src: url("../../assets/fonts/Jost-Regular.ttf");
}

.bg{
  background-image: url("../../assets/img.png");

  /*background-image: url("../../assets/loginBg.jpg");*/
  background-repeat: no-repeat;
  /*height: 100vh;*/
  min-height: 975px;

  background-size: 100% 100%;

  font-family: myFont;
}

.container{
  display: flex;
  padding: 90px 0;
  box-sizing: border-box;
  justify-content: center;
}

.card{

  width: 628px;

  /*height: calc(100vh - 300px);*/

  height: 740px;

  top: 80px;

  background-color: #ffffff;
}

.font_login{
  font-size: 23px !important;

  margin-top: -10px;
  margin-bottom: -10px;
  font-weight: 600;
  flex:0 0 auto;width:100%
}

.border{
  margin: 30px 15px;
}

.font_acc{
  margin-top: 25px !important;
  color: #757272;
  font-size: 15px;
}

.font_blue{
  color: #3554D1;
  text-decoration:none;
}

.input_border{
  flex:0 0 auto;
  width:100%;
  margin-top: 40px;
}

.half_1{
  display: inline-block;


  width: 50%;
}

.half_2{

  display: inline-block;

  margin-left: 60px;
  /*margin-top: -10px;*/

  width: 40%;
}

.input_form{
  position: relative;
  transition: all 0.2s cubic-bezier(0.165, 0.84, 0.44, 1);
  display: flex;
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

.input_form input {
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

.input_form input:focus {
  outline: 2px solid #000000 !important;
}

.input_form input:focus ~ label, .input_form input:valid ~ label {
  transform: translateY(-10px);
}

.forget_link{
  font-size: 15px !important;
  font-weight: 500;
  color: #3554D1;
  text-decoration: underline;
}

.add_step_btn{

  display: flex;
  align-items: center;
  justify-content: center;
  vertical-align: middle;
  text-align: center;
  font-weight: 500;
  font-size: 19px;
  line-height: 1.2;
  border-radius: 4px;
  border: 1px solid transparent;
  transition: all 0.3s cubic-bezier(0.165, 0.84, 0.44, 1);

  margin-top: 70px;

  width: 100%;
  padding-top: 20px !important;
  padding-bottom: 20px !important;

  background-color: #3554D1 !important;
  color: #FFFFFF;

  text-decoration:none;
}

.add_step_btn.c:after{
  content: '»';
  opacity: 0;
  margin-left: 20px;
  transition: 0.5s;
  font-size: 23px;
}


.add_step_btn.c:hover:after {
  opacity: 1;
  right: 0;
  padding-left: 20px;

}

.add_step_btn.verify{
  background-color: #ffffff !important;
  color: #3554D1;

  border: 1.2px solid #3554D1;

  margin-top: 5px;
  font-size: 17px;
}

.add_step_btn.verify:hover{
  border-color:  #3d61f1;
  background-color: #3d61f1 !important;
  color: white !important;
}

.add_step_btn:hover{
  border-color:  #051036;
  background-color: #051036 !important;
  color: white !important;
}

.icon_add{
  background-image: url("../../assets/arrow.svg");
  margin-left: 15px !important;

  background-position: center;
  background-repeat: no-repeat;
  background-size: contain;
  width: 20px;
  height: 20px;
}

.text_center{
  text-align: center;
  font-size: 17px;
}

.text_note{
  text-align: center;
  font-size: 17px;
  padding-left: 30px !important;
  padding-right: 30px !important;
}

.other_login_btn{
  background-color: #FFFFFF;
  color: #D93025;
  display: flex;
  align-items: center;
  justify-content: center;
  vertical-align: middle;
  text-align: center;
  font-weight: 500;
  font-size: 16px;
  line-height: 1.2;
  border: 1px solid #D93025;
  transition: all 0.3s cubic-bezier(0.165, 0.84, 0.44, 1);

  flex:0 0 auto;width:100%;

  padding-top: 15px !important;
  padding-bottom: 15px !important;

  border-radius: 8px;

  margin-top: 10px !important;
}

.other_login_btn:hover{
  background-color: #ce2821;
  border-color: transparent;
  color: white !important;
}

.other_login_btn:hover .google_icon{
  background-image: url("../../assets/google_white.svg");
}

.google_icon{
  background-image: url("../../assets/google.svg");
  background-position: center;
  background-repeat: no-repeat;
  background-size: contain;

  margin-right: 10px !important;

  width: 20px;
  height: 20px;
}

@media screen and (max-width: 750px) {
  .bg{
    background-image: url("../../assets/img.png");

    /*background-image: url("../../assets/loginBg.jpg");*/
    background-repeat: no-repeat;
    /*height: 100vh;*/
    min-height: 690px;

    background-size: 100% 100%;

    font-family: myFont;
  }

  .container{
    display: flex;

    justify-content: center;
  }

  .card{

    width: 90%;

    /*height: calc(100vh - 300px);*/

    height: 610px;

    top: 40px;

    background-color: #ffffff;
  }

  .font_login{
    font-size: 23px !important;

    margin-top: -10px;
    margin-bottom: -10px;
    font-weight: 600;
    flex:0 0 auto;width:100%
  }

  .border{
    margin: 30px 15px;
  }

  .font_acc{
    margin-top: 25px !important;
    color: #757272;
    font-size: 15px;
  }

  .font_blue{
    color: #3554D1;
    text-decoration:none;
  }

  .input_border{
    flex:0 0 auto;
    width:100%;
    margin-top: 20px;
  }

  .half_1{
    display: inline-block;


    width: 50%;
  }

  .half_2{

    display: inline-block;

    margin-left: 40px;
    /*margin-top: -10px;*/

    width: 40%;
  }

  .input_form{
    position: relative;
    transition: all 0.2s cubic-bezier(0.165, 0.84, 0.44, 1);
    display: flex;
  }

  .input_label{
    line-height: 1 !important;
    font-size: 14px !important;
    color: #697488;
  }

  .input_form label {
    position: absolute;
    top: 22px;
    padding: 0 15px;
    pointer-events: none;
    font-size: 14px;
    transition: all 0.2s cubic-bezier(0.165, 0.84, 0.44, 1);
  }

  .input_form input {
    border: 1px solid #DDDDDD;
    width: 100%;
    font-size: 15px;
    border-radius: 4px;
    /*padding: 0 15px;*/
    padding-top: 20px;
    padding-left: 15px;
    min-height: 35px;
    transition: all 0.2s cubic-bezier(0.165, 0.84, 0.44, 1);
  }

  .input_form input:focus {
    outline: 2px solid #000000 !important;
  }

  .input_form input:focus ~ label, .input_form input:valid ~ label {
    transform: translateY(-10px);
  }

  .forget_link{
    font-size: 15px !important;
    font-weight: 500;
    color: #3554D1;
    text-decoration: underline;
  }

  .add_step_btn{

    display: flex;
    align-items: center;
    justify-content: center;
    vertical-align: middle;
    text-align: center;
    font-weight: 500;
    font-size: 19px;
    line-height: 0.95;
    border-radius: 4px;
    border: 1px solid transparent;
    transition: all 0.3s cubic-bezier(0.165, 0.84, 0.44, 1);

    margin-top: 35px;

    padding-top: 20px !important;
    padding-bottom: 20px !important;

    background-color: #3554D1 !important;
    color: #FFFFFF;

    text-decoration:none;
  }

  .add_step_btn.c:after{
    content: '»';
    opacity: 0;
    margin-left: 20px;
    transition: 0.5s;
    font-size: 23px;
  }


  .add_step_btn.c:hover:after {
    opacity: 1;
    right: 0;
    padding-left: 20px;

  }

  .add_step_btn.verify{
    background-color: #ffffff !important;
    color: #3554D1;

    border: 1.2px solid #3554D1;

    margin-top: 0px;
    font-size: 17px;
  }

  .add_step_btn.verify:hover{
    border-color:  #3d61f1;
    background-color: #3d61f1 !important;
    color: white !important;
  }

  .add_step_btn:hover{
    border-color:  #051036;
    background-color: #051036 !important;
    color: white !important;
  }

  .icon_add{
    background-image: url("../../assets/arrow.svg");
    margin-left: 15px !important;

    background-position: center;
    background-repeat: no-repeat;
    background-size: contain;
    width: 20px;
    height: 20px;
  }

  .text_center{
    text-align: center;
    font-size: 17px;
  }

  .text_note{
    text-align: center;
    font-size: 15px;
    padding-left: 0px !important;
    padding-right: 0px !important;
  }

  .other_login_btn{
    background-color: #FFFFFF;
    color: #D93025;
    display: flex;
    align-items: center;
    justify-content: center;
    vertical-align: middle;
    text-align: center;
    font-weight: 500;
    font-size: 16px;
    line-height: 1.2;
    border: 1px solid #D93025;
    transition: all 0.3s cubic-bezier(0.165, 0.84, 0.44, 1);

    flex:0 0 auto;width:100%;

    padding-top: 15px !important;
    padding-bottom: 15px !important;

    border-radius: 8px;

    margin-top: 10px !important;
  }

  .other_login_btn:hover{
    background-color: #ce2821;
    border-color: transparent;
    color: white !important;
  }

  .other_login_btn:hover .google_icon{
    background-image: url("../../assets/google_white.svg");
  }

  .google_icon{
    background-image: url("../../assets/google.svg");
    background-position: center;
    background-repeat: no-repeat;
    background-size: contain;

    margin-right: 10px !important;

    width: 20px;
    height: 20px;
  }
}



</style>

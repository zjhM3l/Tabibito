<template>
  <navigation-bar></navigation-bar>

  <div class="bg">

    <div class="container">

      <n-card class="card">

        <div class="border">

          <h1 class="font_login">{{ $t('reg.sign')}}
          </h1>
          <p class="font_acc">{{ $t('reg.alr')}}
            <router-link to="/login" class="font_blue">{{ $t('reg.log')}}</router-link></p>

          <form autocomplete="off" >

          <!--          name部分-->
          <div class="input_border">

            <div class="input_form">
              <input type="text" v-model="inputFirst" required>
              <label class="input_label">{{ $t('reg.fir')}}</label>
            </div>

          </div>

          <div class="input_border">

            <div class="input_form">
              <input type="text" v-model="inputLast" required>
              <label class="input_label">{{$t('reg.las')}}</label>
            </div>

          </div>

          <!--          账号部分-->
          <div class="input_border">

            <div class="input_form">
              <input type="text" v-model="inputEmail1" required>
              <label class="input_label">{{ $t('reg.email')}}</label>
            </div>

          </div>

          <!--          密码部分-->
          <div class="input_border">

            <div class="input_form">
              <input type="password" v-model="inputPassword1" required>
              <label class="input_label">{{ $t('reg.pass')}}</label>
            </div>

          </div>

          <!--          确认密码部分-->
          <div class="input_border">

            <div class="input_form">
              <input type="password" v-model="inputConfirm" required>
              <label class="input_label">{{ $t('reg.con')}}</label>
            </div>

          </div>

          <!--          验证码部分-->
          <div class="input_border">

            <div class="input_form">
              <div class="half_1">
                <input type="text" v-model="inputCode" required>
                <label class="input_label">{{ $t('reg.ver')}}</label>
              </div>

              <div class="half_2">
                <!--          验证码按钮-->
                <a class="add_step_btn verify" @click="startCountdown" v-show="!countingDown">
                  {{ $t('reg.get')}}
                </a>
                <a class="add_step_btn verify" v-if="countingDown">{{ remainingTime }} s </a>
              </div>
            </div>

          </div>

          <!--          按钮-->
          <div class="input_border">

            <button type="submit" class="add_step_btn" @click="checkRegister">
              {{$t('reg.sig')}} <div class="icon_add"></div>
            </button>

          </div>

          </form>

          <!--          其他登陆方式-->
          <div class="input_border">
            <div class="text_center">{{ $t('reg.or')}}</div>

            <button class="other_login_btn">
              <i class="google_icon"></i>
              {{ $t('reg.goo')}}
            </button>

          </div>

          <div class="input_border">

            <div class="text_note">{{$t('reg.by')}}</div>

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
import {useToast} from "vue-toastification";

export default {
  setup() {
    // Get toast interface
    const toast = useToast();

    // or with options
    // toast.success("My toast content", {
    //   timeout: 2000
    // });

    // These options will override the options defined in the "app.use" plugin registration for this specific toast

    // Make it available inside methods
    return { toast }
  },
  components: {FooterView, navigationBar},
  name: "loginView",
  data() {
    return {
      countingDown: false,
      remainingTime: 60,
      countdownInterval: null,

      inputFirst: '',
      inputLast:'',
      inputEmail1: '',
      inputPassword1:'',
      inputConfirm:'',
      inputCode:'',
    };
  },
  methods: {
    startCountdown() {
      let self = this;

      if (this.inputFirst === ''){
        this.toast.error("First name can't be blank");
      }
      const tester = /^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/;
      if (!tester.test(this.inputEmail1)){
        this.toast.error("This email is not valid");
      }

      if (this.inputLast === ''){
        this.toast.error("Last name can't be blank");
      }
      if (this.inputEmail1 === ''){
        this.toast.error("Email can't be blank");
      }
      if (this.inputPassword1 === ''){
        this.toast.error("Password can't be blank");
      }
      if (this.inputPassword1.length > 20){
        this.toast.error("Your password is too long");
      }
      if (this.inputPassword1.length < 5){
        this.toast.error("Your password is too easy");
      }
      if (this.inputConfirm === ''){
        this.toast.error("Please confirm your password");
      }
      if (this.inputPassword1 !== this.inputConfirm){
        this.toast.error("The passwords are not the same");
      }
      if (this.inputEmail1 === '' || this.inputPassword1 === '' || this.inputFirst === '' || this.inputLast === '' || this.inputConfirm === '' ){
        this.toast.error("Please finish the information above first");
      } else {
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

        let emailValue = this.inputEmail1;

        self.toast.success("Captcha send Successfully.");

        this.axios.post('/user/captcha', {
          email: emailValue,

        }).then(function (response) {
          let code = response.data['code'];
          let message = response.data['message'];
          if (code === 200) {
            self.toast.success("Register successfully. You can login now!");
          } else if (code === 400) {
            if (message === 'invalidSignUpEmail') {
              self.toast.error("The email is not available");
            }
          }
        }).catch(function (error) {
          console.log(error);
        });
      }
    },

    checkRegister() {
      let self = this;

      if (this.inputFirst === ''){
        this.toast.error("First name can't be blank");
      }
      const tester = /^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/;
      if (!tester.test(this.inputEmail1)){
        this.toast.error("This email is not valid");
      }

      if (this.inputLast === ''){
        this.toast.error("Last name can't be blank");
      }
      if (this.inputEmail1 === ''){
        this.toast.error("Email can't be blank");
      }
      if (this.inputPassword1 === ''){
        this.toast.error("Password can't be blank");
      }
      if (this.inputPassword1.length > 20){
        this.toast.error("Your password is too long");
      }
      if (this.inputPassword1.length < 5){
        this.toast.error("Your password is too easy");
      }
      if (this.inputConfirm === ''){
        this.toast.error("Please confirm your password");
      }
      if (this.inputCode === ''){
        this.toast.error("Please verify your email first");
      }
      if (this.inputPassword1 !== this.inputConfirm){
        this.toast.error("The passwords are not the same");
      }
      if (this.inputEmail1 === '' || this.inputPassword1 === '' || this.inputFirst === '' || this.inputLast === '' || this.inputConfirm === '' || this.inputCode === ''){
      } else {
        let firstValue = this.inputFirst;
        let lastValue = this.inputLast;
        let emailValue = this.inputEmail1;
        let passwordValue = this.inputPassword1;
        let confirmValue = this.inputConfirm;
        let codeValue = this.inputCode;
        this.axios.post('/user/register_form', {
          first: firstValue,
          last: lastValue,
          email: emailValue,
          password: passwordValue,
          confirm: confirmValue,
          code: codeValue,
        })
            .then(function (response){
              let code=response.data['code'];
              let message=response.data['message'];
              if (code === 200){
                self.$router.push('/login');
              } else if (code === 400) {
                if (message === 'invalidSignUpEmail') {
                  self.toast.error("This email is already registered");
                }
                if (message === 'invalidSignUpCaptcha') {
                  self.toast.error("The Verification Code is not correct");
                }
              }
            })
            .catch(function (error) {
              console.log(error);
            });
      }

    }

  }

}
</script>

<style scoped>

@font-face {
  font-family: Jost;
  src: url("../../assets/fonts/Jost-Regular.ttf");
}

.bg{
  background-image: url("../../assets/img.png");
  /*background-image: url("../../assets/loginBg.jpg");*/
  background-repeat: no-repeat;
  /*height: 100vh;*/
  min-height: 1200px;

  background-size: 100% 100%;

  font-family: Jost;
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

  height: 970px;

  top: 80px;

  /*display: flex;*/
  /*align-items: center;*/

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
  font-size: 16px;
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

  .add_step_btn.verify:hover{
    border-color:  #3d61f1;
    background-color: #3d61f1 !important;
    color: white !important;
  }

.add_step_btn{
  margin-top: 35px;
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

  padding-top: 20px !important;
  padding-bottom: 20px !important;

  background-color: #3554D1 !important;
  color: #FFFFFF;

  width: 100%;

  text-decoration:none;

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

.text_center{
  text-align: center;
  margin-top: 40px;
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

  flex:0 0 auto;

  width:100%;

  padding-top: 15px !important;
  padding-bottom: 15px !important;

  border-radius: 8px;

  margin-top: 10px !important;
}

.other_login_btn:hover .google_icon{
  background-image: url("../../assets/google_white.svg");
}

.other_login_btn:hover{
  background-color: #ce2821;
  border-color: transparent;
  color: white !important;
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
    min-height: 870px;

    background-size: 100% 100%;

    font-family: Jost;
  }

  .container{
    display: flex;

    justify-content: center;
  }

  .card{

    width: 90%;

    /*height: calc(100vh - 300px);*/

    height: 850px;

    top: 40px;

    /*display: flex;*/
    /*align-items: center;*/

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
    margin: 10px 0px;
  }

  .font_acc{
    margin-top: 25px !important;
    color: #757272;
    font-size: 16px;
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

    margin-left: 39px;
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


  .add_step_btn{
    margin-top: 15px;
    display: flex;
    align-items: center;
    justify-content: center;
    vertical-align: middle;
    text-align: center;
    font-weight: 500;
    font-size: 17px;
    line-height: 0.9;
    border-radius: 4px;
    border: 1px solid transparent;
    transition: all 0.3s cubic-bezier(0.165, 0.84, 0.44, 1);

    padding-top: 20px !important;
    padding-bottom: 20px !important;

    background-color: #3554D1 !important;
    color: #FFFFFF;

    text-decoration:none;

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


  .add_step_btn.verify{
    background-color: #ffffff !important;
    color: #3554D1;

    border: 1.2px solid #3554D1;



    margin-top: 0px;
    font-size: 17px;
  }

  .text_center{
    text-align: center;
    margin-top: 20px;
    font-size: 17px;
  }



  .text_note{
    text-align: center;
    font-size: 17px;
    padding-left: 10px !important;
    padding-right: 10px !important;
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

  .other_login_btn:hover .google_icon{
    background-image: url("../../assets/google_white.svg");
  }

  .other_login_btn:hover{
    background-color: #ce2821;
    border-color: transparent;
    color: white !important;
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

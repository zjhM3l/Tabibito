<template>
  <navigation-bar></navigation-bar>

  <div class="bg">

    <div class="container">

      <n-card class="card">

        <div class="border">

          <h1 class="font_login">{{ $t('reset.reset')}}</h1>
          <p class="font_acc">{{ $t('reset.rem')}}
            <router-link to="/login" class="font_blue">{{ $t('reset.log')}}</router-link></p>

          <form autocomplete="off"  >

            <!--          账号部分-->
            <div class="input_border">

              <div class="input_form">
                <input type="password" v-model="p1" required>
                <label class="input_label">{{ $t('reset.enter')}}</label>
              </div>

            </div>

            <!--          密码部分-->
            <div class="input_border">

              <div class="input_form">

                  <input type="password" v-model="p2" required>
                  <label class="input_label">{{ $t('reset.con')}}</label>
              </div>
            </div>


            <!--          按钮-->
            <div class="input_border">

              <div class="add_step_btn c" @click="reset">
                {{ $t('reset.res')}}
                <!--                <div class="icon_login"></div>-->
              </div>

            </div>

          </form>

          <!--          其他登陆方式-->
          <div class="input_border">
            <div class="text_center">{{ $t('reset.or')}}</div>

            <button class="other_login_btn">
              <i class="google_icon"></i>
              {{ $t('reset.goo')}}
            </button>

          </div>

          <div class="input_border">

            <div class="text_note">{{ $t('reset.rese')}}</div>


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

export default {
  components: {FooterView, navigationBar},
  name: "loginView",
  setup(){
    const axios = getCurrentInstance().appContext.config.globalProperties.axios;
    // axios.defaults.withCredentials = true;
  },
  data() {
    return {
      countingDown: false,
      remainingTime: 60,
      countdownInterval: null,

      p1:'',
      p2:'',
    };
  },
  methods: {
    reset(){
      let self = this;
      if (this.p1 === ''){
        this.toast.error("Password name can't be blank");
      }
      if (this.p2 === ''){
        this.toast.error("Please confirm your password");
      }
      if (this.p1 !== this.p2){
        this.toast.error("The passwords are not the same");
      }

      let passwordValue = this.p1;
      let confirmValue = this.p2;
      this.axios.post('/user/reset_password', {
        password: passwordValue,
        confirm: confirmValue
      }).then(function (response){
        let code=response.data['code'];
        let message=response.data['message'];
        if (code === 200){
          self.$router.push('/login');
        } else if (code === 400){
          if (message === 'email'){
            self.toast.error("Email is not registered");
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
  width: 100%;

  margin-top: 70px;

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
    min-height: 660px;

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

    height: 580px;

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

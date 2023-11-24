<template>
<navigation-bar></navigation-bar>

  <div class="bg">

    <div class="container">

      <n-card class="card">

        <div class="border">

          <h1 class="font_login">{{ $t('login.welcome') }}</h1>
<!--          <h1 class="font_login">Welcome back</h1>-->
          <p class="font_acc">{{ $t('login.noAccount')}}
            <router-link to="/register" class="font_blue">{{ $t('login.signup')}}</router-link></p>

          <form autocomplete="off">

          <!--账号部分-->
          <div class="input_border">

            <div class="input_form">
              <input type="text" v-model="inputEmail" required>
              <label class="input_label">{{ $t('login.email') }}</label>
            </div>

          </div>

          <!--密码部分-->
          <div class="input_border">

            <div class="input_form">
              <input type="password" v-model="inputPassword" required>
              <label class="input_label">{{ $t('login.password')}}</label>
            </div>

          </div>

          <!--忘记密码-->
          <div class="input_border">
            <router-link to="/forget" class="forget_link">{{ $t('login.forget')}}</router-link>
          </div>

          <!--按钮-->
          <div class="input_border">

            <button type="submit" class="add_step_btn" @click="checkLogin">
              {{ $t('login.signin')}}
              <div class="icon_add"></div>
            </button>
          </div>

          </form>

<!--          其他登陆方式-->
          <div class="input_border">
            <div class="text_center">{{ $t('login.signin2') }}</div>

            <button class="other_login_btn" @click="googleLogin">
              <i class="google_icon"></i>
              {{$t("login.google")}}
            </button>

          </div>

          <div class="input_border">

            <div class="text_note">{{$t('login.agree')}}</div>



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

import { useToast } from "vue-toastification";



export default {
  setup() {
    // Get toast interface
    const toast = useToast();
    const axios = getCurrentInstance().appContext.config.globalProperties.axios;
    // axios.defaults.withCredentials = true;
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
  data(){
    return {
      inputEmail: '',
      inputPassword:'',
      from: '',
    };
  },
  beforeRouteEnter(to, from, next){
    next(vm =>{
      vm.from = from;
    })
  },
  methods: {

    checkLogin() {
      event.preventDefault();
      let self = this;

      if (this.inputEmail === ''){
        this.toast.error("Email can't be blank");
      }
      if (this.inputPassword === ''){
        this.toast.error("Password can't be blank");
      }
      if (this.inputEmail === '' || this.inputPassword === ''){
      } else {
        let emailValue = this.inputEmail;
        let passwordValue = this.inputPassword;
        this.axios.post('/user/login_form', {
          email: emailValue,
          password: passwordValue
        }).then(function (response){
              let code=response.data['code'];
              let message=response.data['message'];
              if (code === 200){
                if (response.data.job === "Customer"){
                  if (self.from.path === '/login' || self.from.path === '/register' || self.from.path === '/forbidden' || self.from.name === 'NotFound'){
                    self.$router.push('/');
                  }else
                    self.$router.push(self.from.path);
                }else {
                  self.$router.push('/management')
                }
              } else if (code === 400){
                if (message === 'email'){
                  self.toast.error("Email is not correct");
                }else if (message === 'password'){
                  self.toast.error("Password is not correct");
                }
              }
            })
            .catch(function (error) {
              console.log(error);
            });
      }

    },
    googleLogin(){
      this.axios.post('/user/authorize', {
      }).then(function (response){

      });
    }
  }
}
</script>

<style scoped>

.bg{
  background-image: url("../../assets/img.png");

  /*background-image: url("../../assets/loginBg.jpg");*/
  background-repeat: no-repeat;
  /*height: 100vh;*/
  min-height: 975px;

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

  height: 740px;

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
  font-size: 15px;
}

.font_blue{
  color: #3554D1;
  text-decoration:none;
}

.input_border{
  flex:0 0 auto;
  width:100%;
  margin-top: 30px;
  display: inline-block;
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
  font-size: 17px;
  line-height: 1.2;
  border-radius: 4px;
  border: 1px solid transparent;
  transition: all 0.3s cubic-bezier(0.165, 0.84, 0.44, 1);

  padding-top: 20px !important;
  padding-bottom: 20px !important;

  background-color: #3554D1 !important;
  color: #FFFFFF;

  width:100%;

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

@media screen and (max-width: 700px) {
  .bg{
    background-image: url("../../assets/img.png");

    /*background-image: url("../../assets/loginBg.jpg");*/
    background-repeat: no-repeat;
    /*height: 100vh;*/
    min-height: 730px;

    background-size: 100% 100%;

    font-family: Jost;
  }

  .container{
    display: flex;

    justify-content: center;
  }

  .card{

    width: 90%;
    padding: 0;
    /*height: calc(100vh - 300px);*/

    height: 630px;

    top: 50px;

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
    margin: 30px 0px;
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
    min-height: 38px;
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
    font-size: 17px;
    line-height: 1.2;
    border-radius: 4px;
    border: 1px solid transparent;
    transition: all 0.3s cubic-bezier(0.165, 0.84, 0.44, 1);

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

  .text_center{
    text-align: center;
    font-size: 17px;
  }

  .text_note{
    text-align: center;
    font-size: 16px;
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

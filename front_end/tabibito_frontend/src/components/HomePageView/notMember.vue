<template>
  <section class="nCon">
    <div class="notContainer">
      <div class="nLine">
        <div class="nTex">
          <h2 class="nTex1">{{ $t('notMember.not')}}</h2>
          <div class="slogan">{{ $t('notMember.slogan')}}</div>
        </div>

        <div class="but">
          <button class="nBtn nBtn1" @click="this.$router.push('/login')">
            {{ $t('notMember.sign')}}
            <div class="icon_add"></div>
          </button>

          <button class="nBtn nBtn2" @click="this.$router.push('/register')">
            {{ $t('notMember.reg')}}
            <div class="icon_add"></div>
          </button>

        </div>

      </div>

    </div>
  </section>

</template>

<script>
export default {
  name: "notAMember"
}
</script>

<style scoped>
.nCon{
  padding-top: 60px;
  padding-bottom: 120px;

}

.nLine{
  display:flex;
  flex-wrap:wrap;
  margin: -15px;

  justify-content: space-between !important;
  align-items: flex-end !important;
}

.nTex{
  /*flex:0 0 auto;*/
  width:auto;
}

.nTex1{
  font-size: 30px;
  font-family: JostBlod;
}

.nTex2{
  color: #051036;
  font-weight: 100;
  margin-top: -15px;
}

.but{
  flex:0 0 auto;
  width:auto;

  display:flex;
  flex-wrap:wrap;
}

.nBtn{
  display: flex;
  align-items: center;
  justify-content: center;
  vertical-align: middle;
  text-align: center;
  font-weight: 500;
  font-size: 15px;
  line-height: 1.2;
  border-radius: 4px;
  /*border: 1px solid transparent;*/
  transition: all 0.3s cubic-bezier(0.165, 0.84, 0.44, 1);

  padding-left: 40px ;
  padding-right: 40px;

  height: 60px !important;

  /*控制按钮和字体在一行用的，可以删掉，但是那样就对不齐了*/
  margin-top: -80px;
}

.nBtn1{
  background-color: #3554D1;
  color: white;
  border: 1px solid #3554D1;
}

.nBtn1:hover{
  background-color: #FBFCFF;
  color: #051036;
}

.nBtn2{
  background-color: #FBFCFF;
  color: #051036;
  border: 1px solid #3554D1;
  margin-left: 20px;
  padding-left: 33px ;
  padding-right: 33px;
}

.nBtn2:hover{
  background-color: #3554D1;
  color: white;
}

.nBtn1 .icon_add{
  background-image: url("../../assets/arrow.svg");
  margin-left: 15px !important;

  background-position: center;
  background-repeat: no-repeat;
  background-size: contain;
  width: 20px;
  height: 20px;
}

.nBtn2 .icon_add{
  background-image: url("../../assets/arrow_blue.svg");
  margin-left: 15px !important;

  background-position: center;
  background-repeat: no-repeat;
  background-size: contain;
  width: 20px;
  height: 20px;
}

.nBtn1:hover .icon_add{
  background-image: url("../../assets/arrow_blue.svg");
}

.nBtn2:hover .icon_add{
  background-image: url("../../assets/arrow.svg");
}

.notContainer{
  width:100%;
  padding-right:15px;
  padding-left:15px;
  margin-right:auto;
  margin-left:auto;
}
@media (min-width: 370px) {
  .notContainer{
    max-width: 350px;
    padding-right:0px;
    padding-left:0px;
  }
  .nBtn{
    margin-top: 0px;
  }
  .but{
    margin-top: 30px;
  }
  .nTex1{
    margin-bottom: 10px;
  }
  .nLine{
    margin: 0px;
  }
}
@media (min-width: 450px) {
  .notContainer{
    max-width: 430px;
  }
  .nLine{
    margin: -15px
  }
}
@media (min-width:576px){
  .notContainer{
    max-width:540px
  }
  .nBtn{
    margin-top: 0px;
  }
  .but{
    margin-top: 30px;
  }
  .nTex1{
    margin-bottom: 10px;
  }

}

@media (min-width:768px){
  .notContainer{
    max-width:720px
  }
  .nBtn{
    margin-top: 0px;
  }
  .but{
    margin-top: 30px;
  }
  .nTex1{
    margin-bottom: 10px;
  }
}

@media (min-width:992px){
  .notContainer{
    max-width:960px
  }
  .nBtn{
    margin-top: -80px;
  }
}

@media (min-width:1200px){
  .notContainer{
    max-width:1140px
  }
}

@media (min-width:1400px){
  .notContainer{
    max-width:1320px
  }
}

</style>

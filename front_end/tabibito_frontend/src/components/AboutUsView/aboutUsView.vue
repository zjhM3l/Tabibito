<template>
  <navigation-bar :is-ini-text-white="false" :is-transparent="false"></navigation-bar>
  <div style="height: 91px; z-index: -100"></div>
 <div class="cover">
   <div class="coverSlogans">
     <h1 class="mainSlogan">{{ $t('aboutUsPage.mainSlogan')}}</h1>
     <div class="subSlogan">{{ $t('aboutUsPage.subSlogan')}}</div>
   </div>
 </div>
  <div class="whyChooseUsSection">
    <div class="whyChooseTextContainer">
      <div class="whyChooseTextArea">
        <h2 class="whyChooseTitle">{{ $t('aboutUsPage.whyChooseTitle')}}</h2>
        <div class="whyChooseSlogan">{{ $t('aboutUsPage.whyChooseSlogan')}}</div>
      </div>
    </div>
    <div class="advantages">
      <div class="advantage">
        <div class="advantageIcon shieldIcon"></div>
        <h4 class="advantageName">{{ $t('aboutUsPage.advantageName1')}}</h4>
        <div class="advantageText">{{ $t('aboutUsPage.advantageText1')}}</div>
      </div>
      <div class="advantage">
        <div class="advantageIcon bookingIcon"></div>
        <h4 class="advantageName">{{ $t('aboutUsPage.advantageName2')}}</h4>
        <div class="advantageText">{{ $t('aboutUsPage.advantageText2')}}</div>
      </div>
      <div class="advantage">
        <div class="advantageIcon careIcon"></div>
        <h4 class="advantageName">{{ $t('aboutUsPage.advantageName3')}}</h4>
        <div class="advantageText">{{ $t('aboutUsPage.advantageText3')}}</div>
      </div>
    </div>
  </div>
  <div class="companyIntroSection">
    <div class="companyIntroTexts">
      <h2 class="companyIntroTitle">{{ $t('aboutUsPage.companyIntroTitle')}}</h2>
      <div class="companyIntroSlogan">{{ $t('aboutUsPage.companyIntroSlogan')}}</div>
      <div class="companyIntroDescription">{{ $t('aboutUsPage.intro1')}}<br/><br/>

        {{ $t('aboutUsPage.intro2')}}

        <br><br/>{{ $t('aboutUsPage.intro3')}}
        <br><br/>{{ $t('aboutUsPage.intro4')}}
        <br><br/>{{ $t('aboutUsPage.intro5')}}    </div>
    </div>
    <div class="companyIntroImage"></div>

  </div>
  <div class="statistics">
    <div class="figure">
      <n-number-animation show-separator
                          :from="0"
                          :to="0"
                          class="mainFigure"></n-number-animation>
      <div class="figureName">{{ $t('aboutUsPage.reviews') }}</div>
    </div>
    <div class="figure">
      <n-number-animation show-separator
                          :from="0"
                          :to="0"
                          class="mainFigure"></n-number-animation>
      <div class="figureName">{{ $t('aboutUsPage.travelProjects') }}</div>
    </div>
    <div class="figure">
      <n-number-animation show-separator
                          :from="0"
                          :to="0"
                          class="mainFigure"></n-number-animation>
      <div class="figureName">{{ $t('aboutUsPage.happyCustomers') }}</div>
    </div>
    <div class="figure">
      <n-number-animation show-separator
                          :from="0"
                          :to="0"
                          class="mainFigure"></n-number-animation>
      <div class="figureName">{{ $t('aboutUsPage.monthlyIncome') }}</div>
    </div>
  </div>

  <n-divider />
  <our-team-view></our-team-view>
  <overheard-from-travelers-view></overheard-from-travelers-view>
  <footer-view></footer-view>
</template>

<script>
import NavigationBar from "../GeneralComponents/navigationBar.vue";
import {onMounted, ref} from "vue";
import OurTeamView from "./ourTeamView.vue";
import OverheardFromTravelersView from "./overheardFromTravelersView.vue";
import FooterView from "../GeneralComponents/footerView.vue";

export default {
  name: "aboutUsView",
  components: {FooterView, OverheardFromTravelersView, OurTeamView, NavigationBar},
  setup() {
    const numberAnimationInstRef = ref(null);
    return {
      numberAnimationInstRef,
      handleClick() {
        numberAnimationInstRef.value?.play();
      }
    };
  }
}
</script>

<style scoped>
.cover{
  width: 100vw;
  height: 343px;
  background-image: url("../../assets/aboutus_cover.png");
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  display: flex;
}
.coverSlogans{
  margin: auto;
}
.mainSlogan{
  font-weight: 600;
  font-size: 40px;
  color: white;
  margin: 0;
}
.subSlogan{
  color: white;
  margin-top: 15px;
  font-size: 16px;
  text-align: center;
}
.whyChooseUsSection{
  margin-top: 120px;
  margin-bottom: 60px;
  max-width: 1140px;
  box-sizing: border-box;
  margin-left: auto;
  margin-right: auto;
  padding-left: 15px;
  padding-right: 15px;
}
.whyChooseTextContainer{
  display: flex;
}
.whyChooseTextArea{
  margin-left: auto;
  margin-right: auto;
  width: auto;
  text-align: center;
}
.whyChooseTitle{
  font-size: 30px;
  margin: 0;
}
.whyChooseSlogan{
  margin-top: 5px;
  color: var(--secondary-text-color);
}
.advantages{
  margin-top: -20px;
  margin-bottom: -20px;
  box-sizing: border-box;
  padding-top: 50px;
  display: flex;
  justify-content: space-between;
}
.advantage{
  padding: 20px 15px 20px 15px;
  box-sizing: border-box;
  width: 25%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.advantageIcon{
  width: 70px;
  height: 70px;
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center;
}
.shieldIcon{
  background-image: url("../../assets/shield.svg");
}
.bookingIcon{
  background-image: url("../../assets/easy_booking.svg");
}
.careIcon{
  background-image: url("../../assets/care.svg");
}
.advantageName{
  margin: 30px 0 0 0;
  text-align: center;
  font-weight: 500;
  font-size: 18px;
}
.advantageText{
  font-size: 15px;
  margin-top: 10px;
  color: var(--secondary-text-color);
  text-align: center;
}
.companyIntroSection{
  margin-top: 60px;
  max-width: 1140px;
  padding-left: 15px;
  padding-right: 15px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-left: auto;
  margin-right: auto;
}
.companyIntroTexts{
  padding: 15px;
  width: 41.66667%;
  box-sizing: border-box;
}
.companyIntroImage{
  margin-top: 150px;
  padding: 15px;
  box-sizing: border-box;
  width: 50%;
  border-radius: 4px;
  background-image: url("../../assets/mountain-fuji.jpg");
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  height:630px;
}
.companyIntroTitle{
  margin: 0;
  font-weight: 600;
  font-size: 30px;
}
.companyIntroSlogan{
  color: var(--secondary-text-color);
  margin-top: 5px;
}
.companyIntroDescription{
  color: var(--text-color-dark);
  margin-top: 60px;
}
.statistics{
  margin: 60px auto 40px auto;
  max-width: 1140px;
  box-sizing: border-box;
  padding-left: 15px;
  padding-right: 15px;
  display: flex;
  justify-content: center;
}
.figure{
  padding: 15px;
  box-sizing: border-box;
  width: 25%;
  text-align: center;
  font-weight: 600;
  line-height: 1.3;
  font-size: 40px;
}
.figureName{
  font-size: 14px;
  color: var(--secondary-text-color);
  margin-top: 5px;
  line-height: 1.4;
  font-weight: 400;
}

@media screen and (max-width: 750px) {
  .cover{
    width: 100vw;
    height: 200px;
    background-image: url("../../assets/aboutus_cover.png");
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    display: flex;
  }
  .coverSlogans{
    margin: auto;
  }
  .mainSlogan{
    font-weight: 600;
    font-size: 40px;
    color: white;
    margin: 0;
  }
  .subSlogan{
    color: white;
    margin-top: 15px;
    font-size: 16px;
    text-align: center;
  }
  .whyChooseUsSection{
    margin-top: 40px;
    margin-bottom: 60px;
    max-width: 1140px;
    box-sizing: border-box;
    margin-left: auto;
    margin-right: auto;
    padding-left: 15px;
    padding-right: 15px;
  }
  .whyChooseTextContainer{
    display: flex;
  }
  .whyChooseTextArea{
    margin-left: auto;
    margin-right: auto;
    width: auto;
    text-align: center;
  }
  .whyChooseTitle{
    font-size: 30px;
    margin: 0;
  }
  .whyChooseSlogan{
    margin-top: 5px;
    color: var(--secondary-text-color);
  }
  .advantages{
    margin-top: -20px;
    margin-bottom: -20px;
    box-sizing: border-box;
    flex-direction: column;
    padding-top: 50px;
    display: flex;
    justify-content: space-between;
  }
  .advantage{
    padding: 20px 15px 20px 15px;
    box-sizing: border-box;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .advantageIcon{
    width: 70px;
    height: 70px;
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
  }
  .shieldIcon{
    background-image: url("../../assets/shield.svg");
  }
  .bookingIcon{
    background-image: url("../../assets/easy_booking.svg");
  }
  .careIcon{
    background-image: url("../../assets/care.svg");
  }
  .advantageName{
    margin: 30px 0 0 0;
    text-align: center;
    font-weight: 500;
    font-size: 18px;
  }
  .advantageText{
    font-size: 15px;
    margin-top: 10px;
    color: var(--secondary-text-color);
    text-align: center;
  }
  .companyIntroSection{
    margin-top: 60px;
    max-width: 1140px;
    padding-left: 15px;
    padding-right: 15px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    margin-left: auto;
    margin-right: auto;
  }
  .companyIntroTexts{
    padding: 15px;
    width: 100%;
    box-sizing: border-box;
  }
  .companyIntroImage{
    margin-top: 10px;
    padding: 15px;
    box-sizing: border-box;
    width: 100%;
    border-radius: 4px;
    background-image: url("../../assets/mountain-fuji.jpg");
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    height:390px;
  }
  .companyIntroTitle{
    margin: 0;
    font-weight: 600;
    font-size: 30px;
  }
  .companyIntroSlogan{
    color: var(--secondary-text-color);
    margin-top: 5px;
  }
  .companyIntroDescription{
    color: var(--text-color-dark);
    margin-top: 30px;
  }
  .statistics{
    margin: 20px auto 10px auto;
    max-width: 1140px;
    box-sizing: border-box;
    padding-left: 15px;
    padding-right: 15px;
    display: flex;
    justify-content: center;
  }
  .figure{
    padding: 15px;
    box-sizing: border-box;
    width: 25%;
    text-align: center;
    font-weight: 600;
    line-height: 1.3;
    font-size: 40px;
  }
  .figureName{
    font-size: 14px;
    color: var(--secondary-text-color);
    margin-top: 5px;
    line-height: 1.4;
    font-weight: 400;
  }
}
</style>

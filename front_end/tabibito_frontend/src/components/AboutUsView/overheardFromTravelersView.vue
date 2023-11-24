<template>

  <section class="sectionBg layoutPt layoutPb" style="overflow: hidden">
    <div class="sectionItemBg sectionMx"></div>

    <div class="container">
      <div class="row sectionTitleLayout">
        <div class="col-auto">
          <div class="sectionTitle -md">
            <h2 class="sectionOverheardTitle">{{ $t('overheard.overheard')}}</h2>
            <p class="sectionOverheardText">{{ $t('overheard.these')}}</p>
          </div>
        </div>
      </div>

      <n-carousel
          effect="card"
          prev-slide-style="transform: translateX(-150%) translateZ(-800px);"
          next-slide-style="transform: translateX(50%) translateZ(-800px);"
          id="carousel"
          :show-dots="false"
      >
        <n-carousel-item :style="{ width: '50%'}">
          <n-card
              size="large"
              :segmented="{
            content: true,
            footer: 'soft'}"
          >
            <h4 class="commentTitle">{{ $t('overheard.hotelEquatorialMelaka') }}</h4>

            <p class="commentText"> {{ $t('overheard.ourFamilyWasTravelingViaBulletTrainBetweenCitiesIn') }}</p>
            <div class="commentFooter">
              <div class="col-auto">
                <img class="commentAvatar" src="../../assets/avatars/1.png" :alt="$t('overheard.image')">
              </div>

              <div class="col-auto">
                <div class="commentName">{{ $t('overheard.courtneyHenry') }}</div>
                <div class="commentJob">{{ $t('overheard.webDesigner') }}</div>
              </div>
            </div>
          </n-card>
        </n-carousel-item>
        <n-carousel-item :style="{ width: '50%'}">
          <n-card
              size="large"
              :segmented="{
            content: true,
            footer: 'soft'}"
          >
            <h4 class="commentTitle">{{ $t('overheard.hotelEquatorialMelaka') }}</h4>

            <p class="commentText"> {{ $t('overheard.ourFamilyWasTravelingViaBulletTrainBetweenCitiesIn') }}</p>
            <div class="commentFooter">
              <div class="col-auto">
                <img class="commentAvatar" src="../../assets/avatars/1.png" :alt="$t('overheard.image')">
              </div>

              <div class="col-auto">
                <div class="commentName">{{ $t('overheard.courtneyHenry') }}</div>
                <div class="commentJob">{{ $t('overheard.webDesigner') }}</div>
              </div>
            </div>
          </n-card>
        </n-carousel-item>
        <n-carousel-item :style="{ width: '50%'}">
          <n-card
              size="large"
              :segmented="{
            content: true,
            footer: 'soft'}"
          >
            <h4 class="commentTitle">{{ $t('overheard.hotelEquatorialMelaka') }}</h4>

            <p class="commentText"> {{ $t('overheard.ourFamilyWasTravelingViaBulletTrainBetweenCitiesIn') }}</p>
            <div class="commentFooter">
              <div class="col-auto">
                <img class="commentAvatar" src="../../assets/avatars/1.png" :alt="$t('overheard.image')">
              </div>

              <div class="col-auto">
                <div class="commentName">{{ $t('overheard.courtneyHenry') }}</div>
                <div class="commentJob">{{ $t('overheard.webDesigner') }}</div>
              </div>
            </div>
          </n-card>
        </n-carousel-item>
        <n-carousel-item :style="{ width: '50%'}">
          <n-card
              size="large"
              :segmented="{
            content: true,
            footer: 'soft'}"
          >
            <h4 class="commentTitle">{{ $t('overheard.hotelEquatorialMelaka') }}</h4>

            <p class="commentText"> {{ $t('overheard.ourFamilyWasTravelingViaBulletTrainBetweenCitiesIn') }}</p>
            <div class="commentFooter">
              <div class="col-auto">
                <img class="commentAvatar" src="../../assets/avatars/1.png" :alt="$t('overheard.image')">
              </div>

              <div class="col-auto">
                <div class="commentName">{{ $t('overheard.courtneyHenry') }}</div>
                <div class="commentJob">{{ $t('overheard.webDesigner') }}</div>
              </div>
            </div>
          </n-card>
        </n-carousel-item>
      </n-carousel>

<!--      <div class="row sectionOverheardAnalysis pt40 smallPt20">
        <div class="columAnalysis">
          <div class="row analysisRow">
            <div class="analysisColumn">
              <div class="analysisNum">13m+</div>
              <div class="analysisText">Happy People</div>
            </div>

            <div class="analysisColumn">
              <div class="analysisNum">4.88</div>
              <div class="analysisText">Overall rating</div>

              <div class="iconStars">

                <div class="icon-star iconStar"></div>

                <div class="icon-star iconStar"></div>

                <div class="icon-star iconStar"></div>

                <div class="icon-star iconStar"></div>

                <div class="icon-star iconStar"></div>

              </div>
            </div>
          </div>
        </div>

        <div class="overheardAssociation">
          <div class="row associationItems">

            <div class="colAuto colSm">
              <div class="associationIcon">
                <img src="../../assets/clients/1.svg" alt="image">
              </div>
            </div>

            <div class="colAuto colSm">
              <div class="associationIcon">
                <img src="../../assets/clients/2.svg" alt="image">
              </div>
            </div>

            <div class="colAuto colSm">
              <div class="associationIcon">
                <img src="../../assets/clients/3.svg" alt="image">
              </div>
            </div>

            <div class="colAuto colSm">
              <div class="associationIcon">
                <img src="../../assets/clients/4.svg" alt="image">
              </div>
            </div>

          </div>
        </div>
      </div>-->
    </div>

  </section>

</template>

<script>
export default {
  name: "overheardFromTravelersView"
}
</script>

<style scoped>
#carousel {
  height: 240px;
}
@media(max-width: 1000px) {
  .commentName {
    font-size: 0 !important;
  }

  .commentJob {
    font-size: 0 !important;
  }

  .commentAvatar {
    visibility: hidden;
  }
}

@media screen and (max-width: 500px) {
  #carousel {
    height: 500px;
  }
}
.commentName {
  font-size: 15px !important;
  font-weight: 500;
  line-height: 1.4 !important;
}

.commentJob {
  font-size: 14px !important;
  line-height: 1.4 !important;
  color: #697488;
  margin-top: 5px !important;
}

.commentAvatar {
  flex-shrink: 0;
  width: 60px;
  height: 60px;
}

.commentFooter {
  margin-left: -10px;
  margin-right: -10px;
  margin-top: -10px;
  margin-bottom: -10px;
  align-items: center !important;
}

.commentText {
  line-height: 1.8;
  font-weight: 500;
  color: #051036;
}

.commentTitle {
  font-size: 16px !important;
  font-weight: 500;
  color: #3554D1;
  margin-bottom: 20px !important;
}

@media screen and (max-width: 500px) {
  .commentText {
    line-height: 1.5;
  }
  .commentTitle {

  }
}

@media (min-width:768px) {
  .colAuto {
    flex:0 0 auto;
    width:auto
  }
}

@media (min-width:576px) {
  .colSm {
    flex:0 0 auto;
    width:50%
  }
}


@media (min-width:1200px){
  .overheardAssociation {
    flex:0 0 auto;
    width:66.66667%
  }
}

.associationItems {
  margin-top: -15px;
  margin-bottom: -15px;
  justify-content: space-between !important;
  align-items: center !important;
}

.associationIcon {
  display: flex !important;
  justify-content: center !important;
}


.iconStars {
  display: flex !important;
  margin-left: -2.5px;
  margin-right: -2.5px;
  align-items: center !important;
  padding-top: 10px !important;
}

.iconStar {
  color: #051036;
  font-size: 10px !important
}

.analysisColumn {
  flex:0 0 auto;
  width:50%
}

@media (min-width: 576px) {
  .analysisColumn {
    flex: 0 0 auto;
    width: 41.66667%
  }
}

.analysisRow {
  margin-top: -15px;
  margin-bottom: -15px;
  color: #051036;
}

.sectionOverheardAnalysis {
  margin-top: -15px;
  margin-bottom: -15px;
  align-items: center !important;
}

.pt40 {
  padding-top: 40px !important;
}

.analysisNum {
  font-size: 30px !important;
  line-height: 1.5 !important;
  font-weight: 600;
}

.analysisText {
  line-height: 1.5 !important;
}

@media (min-width:1200px){
  .columAnalysis {
    flex: 0 0 auto;
    width: 33.33333%
  }
}

@media (max-width: 575px) {
  .smallPt20 {
    padding-top: 20px !important;
  }
}

.sectionTitleLayout {
  justify-content: center !important;
  text-align: center;
}

.container {
  width: 100%;
  padding-right: var(--bs-gutter-x,15px);
  padding-left: var(--bs-gutter-x,15px);
  margin-right: auto;
  margin-left: auto
}

.row {
  --bs-gutter-x:30px;
  --bs-gutter-y:0;
  display:flex;
  flex-wrap:wrap;
  margin-top:calc(var(--bs-gutter-y)*-1);
  margin-right:calc(var(--bs-gutter-x)*-0.5);
  margin-left:calc(var(--bs-gutter-x)*-0.5)
}

.col-auto{
  flex:0 0 auto;
  width:auto
}

.sectionOverheardTitle {
  font-size: 30px;
}

@media (max-width: 767px) {
  .sectionOverheardTitle {
    font-size: 26px;
  }
}

@media (max-width: 575px) {
  .sectionOverheardTitle {
    margin-top: 0 !important;
  }
}

.sectionOverheardText {
  margin-top: 5px !important;
}

@media (min-width:768px){
  .container{
    max-width: 720px
  }
}

@media (min-width:576px){
  .container{
    max-width: 540px
  }
}

@media (min-width:992px){
  .container{
    max-width: 960px
  }
}

@media (min-width:1200px){
  .container{
    max-width: 1140px
  }
}

@media (min-width:1400px){
  .container{
    max-width: 1320px
  }
}

.sectionBg {
  position: relative;
  z-index: 0;
}

.layoutPt {
  padding-top: 120px;
}

.layoutPb {
  padding-bottom: 120px;
}

.sectionItemBg {
  position: absolute;
  top: 0;
  height: 100%;
  z-index: -1;
  background-color: #F5F5F5 !important;
}

.sectionMx {
  left: 20px;
  right: 20px;
}

@media (max-width: 767px) {
  .sectionMx {
    left: 0;
    right: 0;
  }
}

@media (max-width: 767px) {
  .layoutPt {
    padding-top: 100px;
  }
  .layoutPb {
    padding-bottom: 100px;
  }
}

@media (max-width: 575px) {
  .layoutPt {
    padding-top: 60px;
  }
  .layoutPb {
    padding-bottom: 60px;
  }
}
</style>

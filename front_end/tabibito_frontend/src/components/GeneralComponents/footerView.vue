<template>
  <body style="overflow: hidden">

  <section class="layout-journey-start-pt layout-journey-start-pb layout-journey-bg">
    <div class="container">
      <div class="row journey-start-nav">
        <div class="col-auto">
          <div class="row journey-start-left">
            <div class="col-auto">
              <div class="icon"></div>
            </div>

            <div class="col-auto">
              <div class="journey-start-title">{{ $t('footer.journey1')}}</div>
              <div class="journey-start-text">{{$t('footer.journey2')}}</div>
            </div>
          </div>
        </div>

<!--        <div class="col-auto">-->
<!--          <div class="single-field -w-410 journey-start-right">-->
<!--            <div>-->
<!--              <input class="journey-start-right-input" type="text" placeholder="Your Email">-->
<!--            </div>-->

<!--            <div>-->
<!--              <button class="button -md button-else">Subscribe</button>-->
<!--            </div>-->
<!--          </div>-->
<!--        </div>-->
      </div>
    </div>
  </section>

  <footer class="footer -type-1">
    <div class="container">
      <div class="layout-footer">
        <div class="row layout-footer-contents xl:justify-start">
          <div class="col-xl col-lg col-sm">
            <h5 class="footer-h">{{ $t('footer.contact') }}</h5>

            <div class="mt-30">
              <div class="text-14 mt-30">{{ $t('footer.toll') }}</div>
              <a href="#" class="contact-href">{{ $t('footer.tele') }}</a>
            </div>

            <div class="mt-35">
              <div class="text-14 mt-30">{{ $t('footer.supp') }}</div>
              <a href="#" class="contact-href">hi@tabibito.com</a>
            </div>
          </div>

          <div class="col-xl col-lg col-sm">
            <h5 class="footer-h">{{ $t('footer.comp') }}</h5>
            <div class="contact-title">
              <a @click="this.$router.push('/about')" class="link">{{ $t('footer.about') }}</a>
              <a href="#" class="link">{{ $t('footer.carr') }}</a>
              <a href="#" class="link">{{ $t('footer.blog') }}</a>
              <a href="#" class="link">{{ $t('footer.press') }}</a>
              <a href="#" class="link">{{ $t('footer.gift') }}</a>
              <a href="#" class="link">{{ $t('footer.maga') }}</a>
            </div>
          </div>

          <div class="col-xl col-lg col-sm">
            <h5 class="footer-h"></h5>
            <div class="contact-title">
              <a href="#" class="link">{{ $t('footer.cont') }}</a>
              <a href="#" class="link">{{ $t('footer.legal') }}</a>
              <a href="#" class="link">{{ $t('footer.priva') }}</a>
              <a href="#" class="link">{{ $t('footer.terms') }}</a>
              <a href="#" class="link">{{ $t('footer.site') }}</a>
            </div>
          </div>

          <div class="col-xl col-lg col-sm">
            <h5 class="footer-h">{{ $t('footer.other') }}</h5>
            <div class="contact-title">
              <a href="#" class="link">{{ $t('footer.carh') }}</a>
              <a href="#" class="link">{{ $t('footer.acti') }}</a>
              <a href="#" class="link">{{ $t('footer.tour') }}</a>
              <a href="#" class="link">{{ $t('footer.fligh') }}</a>
              <a href="#" class="link">{{ $t('footer.crui') }}</a>
              <a href="#" class="link">{{ $t('footer.holi') }}</a>
              <a href="#" class="link">{{ $t('footer.travel') }}</a>
            </div>
          </div>
        </div>
      </div>

      <div class="contact-foot-layout">
        <div class="row contact-foot">
          <div class="col-auto">
            <div class="row contact-foot-sub">
              <div class="col-auto">
                <div class="contact-foot-text">
                  {{ $t('footer.reser') }}
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>
  </footer>
  </body>
</template>

<script>
export default {
  name: "footerView"
}
</script>

<style scoped>
.link {
  text-decoration: none;
  color: #000000;
}

.link:hover {
  color: #428bca;
}

.layout-journey-bg {
  background-color: #0D2857 !important;
}

.layout-journey-start-pt {
  padding-top: 60px;
}

.layout-journey-start-pb {
  padding-bottom: 60px;
}

.container{
  width:100%;
  padding-right:var(--bs-gutter-x,15px);
  padding-left:var(--bs-gutter-x,15px);
  margin-right:auto;
  margin-left:auto;
}

.row {
  --bs-gutter-x:30px;
  --bs-gutter-y:0;
  width: 100%;
  display:flex;
  flex-wrap:wrap;
  margin-top:calc(var(--bs-gutter-y)*-1);
  margin-right:calc(var(--bs-gutter-x)*0.5);
  margin-left:calc(var(--bs-gutter-x)*0.5)
}

.journey-start-nav {
  margin-top: -15px;
  margin-bottom: -15px;
  justify-content: space-between !important;
  align-items: center !important;
}

.col-auto{
  flex:0 0 auto;
  width:auto
}

.journey-start-left {
  margin-top: -10px;
  margin-bottom: -10px;
  margin-right: 10px;
  flex-wrap: wrap;
  align-items: center !important;
}

.journey-start-title {
  margin-top: 20px;
  font-size: 26px;
  color: #FFFFFF;
  font-weight: 600;

}

.journey-start-text {
  color: #FFFFFF;
  margin-bottom: 20px;
}

.journey-start-right {
  display: flex !important;
  margin-left: -5px;
  margin-right: -5px;
  margin-top: -10px;
  margin-bottom: -10px;
}

.journey-start-right-input {
  background-color: #FFFFFF !important;
  height: 60px !important;
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
  line-height: 1.2;
  border-radius: 4px;
  border: 1px solid transparent;
  transition: all 0.3s cubic-bezier(0.165, 0.84, 0.44, 1);
}

.button.-md {
  padding: 14px 30px;
}

.button-else {
  height: 60px !important;
  background-color: #3554D1 !important;
  color: #FFFFFF;
}

.layout-footer {
  padding-top: 60px !important;
  padding-bottom: 60px !important;
}

.layout-footer-contents {
  margin-top: -20px;
  margin-bottom: -20px;
  justify-content: space-between !important;
}

.footer-h {
  font-size: 16px !important;
  font-weight: 500;
  margin-bottom: 30px !important;
}

.mt-30 {
  margin-top: 30px !important;
}

.mt-35 {
  margin-top: 35px !important;
}

.text-14 {
  font-size: 14px !important;
}

.text-24 {
  font-size: 24px !important;
}

.contact-href {
  font-size: 18px !important;
  font-weight: 500;
  color: #3554D1;
  margin-top: 5px !important;
}

.contact-title {
  display: flex !important;
  margin-top: -5px;
  margin-bottom: -5px;
  flex-direction: column;
}

.contact-apple {
  display: flex !important;
  align-items: center !important;
  padding-left: 20px !important;
  padding-right: 20px !important;
  padding-top: 10px !important;
  padding-bottom: 10px !important;
  border-radius: 4px;
  border: 1px solid #DDDDDD !important;
}

.icon-apple-ml {
  margin-left: 20px !important;
}

.icon-apple-text1 {
  font-size: 14px !important;
  color: #697488;
}

.icon-apple-text2 {
  font-size: 15px !important;
  line-height: 1 !important;
  font-weight: 500;
}

.contact-google {
  display: flex !important;
  align-items: center !important;
  padding-left: 20px !important;
  padding-right: 20px !important;
  padding-top: 10px !important;
  padding-bottom: 10px !important;
  border-radius: 4px;
  border: 1px solid #DDDDDD !important;
  margin-top: 20px !important;
}

.contact-foot-layout {
  padding-top: 20px !important;
  padding-bottom: 20px !important;
  border-top: 1px solid #DDDDDD;
}

.contact-foot {
  justify-content: space-between !important;
  align-items: center !important;
  margin-top: -5px;
  margin-bottom: -5px;
}

.contact-foot-sub {
  margin-left: -15px;
  margin-right: -15px;
  margin-top: -5px;
  margin-bottom: -5px;
}

.contact-foot-text {
  display: flex !important;
  align-items: center !important;
}

.contact-foot-att {
  display: flex !important;
  margin-left: -7.5px;
  margin-right: -7.5px;
}

.contact-foot-sub2 {
  margin-top: -5px;
  margin-bottom: -5px;
  align-items: center !important;
}

.contact-foot-sub2-in {
  display: flex !important;
  align-items: center !important;
}

.contact-foot-sub2-btn {
  display: flex !important;
  align-items: center !important;
  font-size: 14px !important;
  font-weight: 500;
  color: #051036;
  margin-right: 10px !important;
  border: none;
  background: none;
}

.contact-foot-sub2-icon {
  font-size: 16px !important;
  margin-right: 10px !important;
}

.underline {
  text-decoration: underline;
}

.contact-foot-sub2-btn2 {
  display: flex !important;
  align-items: center !important;
  font-size: 14px !important;
  font-weight: 500;
  color: #051036;
  border: none;
  background: none;
}

.contact-foot-icons {
  display: flex !important;
  margin-left: -10px;
  margin-right: -10px;
  align-items: center !important;
}

@media (max-width: 767px) {
  .layout-journey-start-pt {
    padding-top: 60px;
  }
  .layout-journey-start-pb {
    padding-bottom: 60px;
  }
}

@media (max-width: 575px) {
  .layout-journey-start-pt {
    padding-top: 30px;
  }
  .layout-journey-start-pb {
    padding-bottom: 30px;
  }
  .col-auto{
    margin-left: -8px;
  }
}

@media (min-width:576px){
  .container{
    max-width:540px
  }
}

@media (min-width:768px){
  .container{
    max-width:720px
  }
}

@media (min-width:992px){
  .container{
    max-width:960px
  }
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

.col-sm {
  flex: 0 0 auto;
  width: 100%;
}

@media (min-width: 576px) {
  .col-sm {
    flex: 0 0 auto;
    width: 50%;
  }
}

@media (min-width:992px) {
  .col-lg {
    flex: 0 0 auto;
    width: 33.33333%;
  }
}


@media (min-width: 1200px) {
  .col-xl {
    flex: 0 0 auto;
    width: 16.66667%;
  }
}

@media (max-width: 1199px) {
  .xl\:justify-start {
    justify-content: flex-start !important;
  }
}

@media screen and (max-width: 420px) {
  .journey-start-title {
    font-size: 24px;
  }
  .contact-foot-sub{
    margin-left: 0;
  }
}

</style>

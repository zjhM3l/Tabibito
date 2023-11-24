<template>
  <section class="header">
    <div class="container">
      <div class="row y-gap-10 header_wrap">
        <div class="col-auto">
          <div class="row x-gap-10 y-gap-5 header_text">
            <div class="col-auto">
              <div class="">Europe</div>
            </div>
            <div class="col-auto">
              <div class="">></div>
            </div>
            <div class="col-auto">
              <div class="">United Kingdom (UK)</div>
            </div>
            <div class="col-auto">
              <div class="">></div>
            </div>
            <div class="col-auto">
              <div class="header_loc">London</div>
            </div>
          </div>
        </div>

        <div class="col-auto">
          <a href="#" class="header_link">London Tourism: Best of London</a>
        </div>
      </div>
    </div>
  </section>

  <section class="blogs_wrap">
    <div class="container">
      <div class="row title">
        <div class="col-auto">
            <h2 class="sectionTitle_title">Travel articles</h2>
            <p class="sectionTitle_text">blablablablablablablabla blablablabla</p>
        </div>
      </div>

      <div class="tabs_container">
        <div class="row x-gap-10 tabs_wrap">

          <div class="col-auto">
            <n-button class="tabs__button tabs_btn is-active">
              Art and culture
            </n-button>
          </div>

          <div class="col-auto">
            <n-button class="tabs__button tabs_btn">
              Beaches
            </n-button>
          </div>

          <div class="col-auto">
            <n-button class="tabs__button tabs_btn">
              Adventure travel
            </n-button>
          </div>

          <div class="col-auto">
            <n-button class="tabs__button tabs_btn">
              Explore
            </n-button>
          </div>

          <div class="col-auto">
            <n-button class="tabs__button tabs_btn">
              Family holidays
            </n-button>
          </div>

          <div class="col-auto">
            <n-button class="tabs__button tabs_btn">
              Air travel
            </n-button>
          </div>

          <div class="col-auto">
            <n-button class="tabs__button tabs_btn">
              Food and drink
            </n-button>
          </div>
        </div>

        <div class="tabs_content">
          <div class="tabs_pane is-active">
            <div class="row y-gap-30">

              <div v-for="i in 9" :key="i" class="col-lg-4 col-sm-6">

                <n-card hoverable>
                  <template #cover>
                    <img class="blogCard_image" src="https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg">
                  </template>
                  <div class="card_text">
                    <h4 class="card_text_main">10 European ski destinations you should visit this winter</h4>
                    <div class="card_text_date">April 06, 2022</div>
                  </div>
                </n-card>

              </div>

            </div>
          </div>
        </div>
      </div>

    </div>
  </section>
</template>

<script>
export default {
  name: "blogListView"
}
</script>

<style scoped>
.card_text_date {
  color: #697488;
  font-size: 15px !important;
  line-height: 1.4 !important;
  margin-top: 5px !important;
}
.card_text {
  padding-top: 20px !important;
}
.card_text_main {
  color: #051036;
  font-size: 18px !important;
  font-weight: 500;
}
.blogCard_image {
  display: block;
  width: 100%;
  content: "";
  border-radius: 8px;
}
.tabs_pane {
  position: absolute;
  top: 0;
  visibility: hidden;
  transition: none;
  opacity: 0;
}

.tabs_pane.is-active {
  transition: opacity 0.3s cubic-bezier(0.165, 0.84, 0.44, 1) 0.1s;
  position: relative;
  opacity: 1;
  visibility: visible;
}
.tabs_content {
  position: relative;
  padding-top: 30px !important;
}
.n-card {
  max-width: 300px;
}
.tabs_container .tabs_wrap .tabs__button {
  transition: all 0.2s cubic-bezier(0.165, 0.84, 0.44, 1);
}
.tabs_container .tabs_wrap .tabs__button:hover {
  color: #13357B !important;
}
.tabs_container .tabs_wrap .tabs__button.is-active {
  color: #FFFFFF !important;
  background-color: #13357B !important;
}
.tabs_btn {
  font-size: 14px;
  font-weight: 500;
  padding: 10px 20px !important;
  border-radius: 4px;
  background-color: #F5F5F5 !important;
}
.tabs_wrap {
  position: relative;
  overflow: auto;
  -ms-scroll-snap-type: x mandatory;
  scroll-snap-type: x mandatory;
  white-space: nowrap;
  justify-content: center !important;
}
.tabs_wrap > div {
  scroll-snap-align: center;
}
.tabs_container {
  padding-top: 30px !important;
}
.sectionTitle_text {
  margin-top: 5px !important;
}
@media (max-width: 575px) {
  .sectionTitle_text {
    margin-top: 0px !important;
  }
}
.sectionTitle_title {
  font-size: 30px;
}
@media (max-width: 767px) {
  .sectionTitle_title {
    font-size: 26px;
  }
}
.title {
  justify-content: center !important;
  text-align: center;
}
.blogs_wrap {
  padding-top: 60px;
  padding-bottom: 120px;
}
@media (max-width: 575px) {
  .blogs_wrap {
    padding-top: 30px;
    padding-bottom: 30px;
  }
}
@media (max-width: 767px) {
  .blogs_wrap {
    padding-top: 60px;
    padding-bottom: 60px;
  }
}
.header_link {
  font-size: 14px;
  color: #697488;
}
.header_loc {
  color: #051036;
}
.header_text {
  align-items: center !important;
  font-size: 14px;
  color: #697488;
}
.header_wrap {
  align-items: center !important;
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
.header {
  display:flex!important;
  align-items: center !important;
  padding-top: 15px !important;
  padding-bottom: 15px !important;
  border-top: 1px solid #DDDDDD;
}
.x-gap-10 {
  margin-left: -5px;
  margin-right: -5px;
}
.x-gap-10 > * {
  padding-left: 5px;
  padding-right: 5px;
}
.y-gap-10 {
  margin-top: -5px;
  margin-bottom: -5px;
}
.y-gap-5 {
  margin-top: -2.5px;
  margin-bottom: -2.5px;
}
.y-gap-5 > * {
  padding-top: 2.5px;
  padding-bottom: 2.5px;
}
.y-gap-10 > * {
  padding-top: 5px;
  padding-bottom: 5px;
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
.col-lg-4, .col-sm-6 {
  position: relative;
  width: 100%;
  padding-right: 15px;
  padding-left: 15px;
}
@media (min-width: 576px) {
  .col-sm-6 {
    flex: 0 0 50%;
    max-width: 50%;
  }
}
@media (min-width: 992px) {
  .col-lg-4 {
    flex: 0 0 33.3333333333%;
    max-width: 33.3333333333%;
  }
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
<template>

  <div class="container">
    <div class="row y-gap-30 guest_reviews_wrap">
      <div class="col-xl-3">
        <h3 class="gr_title">
          {{ $t('guestReviews') }}
        </h3>

        <div class="exceptional">
          <div class="ex_point">{{ scores.exceptional }}</div>
          <div class="ex_sub_wrap">
            <div class="ex_text">
              {{ $t('moreView.exceptional') }}
            </div>
            <div class="ex_sta">
              {{ $t('reviews', {reviews_num: reviews.reviews_num}) }}
            </div>
          </div>
        </div>

        <div class="row y-gap-20 bars">
          <div class="col-12">
            <div class="">
              <div class="bar_head">
                <div class="bar_title">
                  {{ $t('homepage.searchPart.loc') }}
                </div>
                <div class="bar_score">
                  {{ scores.location }}
                </div>
              </div>

              <div class="bar_progress">
                <n-progress
                    type="line"
                    :show-indicator="false"
                    :percentage="percentages.location"
                    processing
                />
              </div>

            </div>
          </div>
          <div class="col-12">
            <div class="">
              <div class="bar_head">
                <div class="bar_title">
                  {{ $t('staff') }}
                </div>
                <div class="bar_score">
                  {{ scores.staff }}
                </div>
              </div>

              <div class="bar_progress">
                <n-progress
                    type="line"
                    :show-indicator="false"
                    :percentage="percentages.staff"
                    processing
                />
              </div>

            </div>
          </div>
          <div class="col-12">
            <div class="">
              <div class="bar_head">
                <div class="bar_title">
                  {{ $t('cleanliness') }}
                </div>
                <div class="bar_score">
                  {{ scores.cleanliness }}
                </div>
              </div>

              <div class="bar_progress">
                <n-progress
                    type="line"
                    :show-indicator="false"
                    :percentage="percentages.cleanliness"
                    processing
                />
              </div>

            </div>
          </div>
          <div class="col-12">
            <div class="">
              <div class="bar_head">
                <div class="bar_title">
                  {{ $t('valueForMoney') }}
                </div>
                <div class="bar_score">
                  {{ scores.value_for_money }}
                </div>
              </div>

              <div class="bar_progress">
                <n-progress
                    type="line"
                    :show-indicator="false"
                    :percentage="percentages.value_for_money"
                    processing
                />
              </div>

            </div>
          </div>
          <div class="col-12">
            <div class="">
              <div class="bar_head">
                <div class="bar_title">
                  {{ $t('comfort') }}
                </div>
                <div class="bar_score">
                  {{ scores.comfort }}
                </div>
              </div>

              <div class="bar_progress">
                <n-progress
                    type="line"
                    :show-indicator="false"
                    :percentage="percentages.comfort"
                    processing
                />
              </div>

            </div>
          </div>
          <div class="col-12">
            <div class="">
              <div class="bar_head">
                <div class="bar_title">
                  {{ $t('facilities') }}
                </div>
                <div class="bar_score">
                  {{ scores.facilities }}
                </div>
              </div>

              <div class="bar_progress">
                <n-progress
                    type="line"
                    :show-indicator="false"
                    :percentage="percentages.facilities"
                    processing
                />
              </div>

            </div>
          </div>
          <div class="col-12">
            <div class="">
              <div class="bar_head">
                <div class="bar_title">
                  {{ $t('freeWifi') }}
                </div>
                <div class="bar_score">
                  {{ scores.free_wifi }}
                </div>
              </div>

              <div class="bar_progress">
                <n-progress
                    type="line"
                    :show-indicator="false"
                    :percentage="percentages.free_wifi"
                    processing
                />
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="col-xl-8">
        <div class="row y-gap-30">
          <div class="col-12" v-for="comment in comments">

            <div class="row y-gap-20 x-gap-20 comment_head">
              <div class="col-auto">
                <img :src="comment.user_portrait" class="avatar">
              </div>
              <div class="col-auto">
                <div class="user_name">{{ comment.user_name }}</div>
                <div class="date">{{ comment.date_time }}</div>
              </div>
            </div>


            <h5 class="comment_title">
              {{ comment.title }}
            </h5>

            <p class="comment_content">
              {{ comment.des }}
            </p>

            <div class="row x-gap-20 y-gap-30 comment_photos" v-for="p in comment.pic">
              <div class="col-auto">
                <img :src="p" class="photo">
              </div>
            </div>

<!--            <div class="comment_foot x-gap-20">-->
<!--              <n-button text :loading="loading" @click="handleClick">-->
<!--                <template #icon>-->
<!--                  <n-icon size="16px">-->
<!--                    <ThumbsUp />-->
<!--                  </n-icon>-->
<!--                </template>-->
<!--                {{ $t('helpful') }}-->
<!--              </n-button>-->

<!--              <n-button text :loading="loading" @click="handleClick">-->
<!--                <template #icon>-->
<!--                  <n-icon size="16px">-->
<!--                    <ThumbsDown />-->
<!--                  </n-icon>-->
<!--                </template>-->
<!--                {{ $t('notHelpful') }}-->
<!--              </n-button>-->
<!--            </div>-->
          </div>

          <n-pagination
              v-model:page="commentPage"
              :page-count="commentPages"
              v-model:page-size="commentPageSize"
              @update:page="handleChangePage"></n-pagination>


        </div>
      </div>

    </div>
  </div>

</template>

<script>
import { defineComponent, ref } from 'vue';
import { useRoute } from 'vue-router';
import {ThumbsUp, ThumbsDown, ArrowForwardOutline} from "@vicons/ionicons5";

export default defineComponent({
  name: "guestReviews",
  components: {
    ThumbsUp,
    ThumbsDown,
    ArrowForwardOutline
  },
  setup () {
    const loadingRef = ref(false)
    return {
      handleClick () {
        loadingRef.value = true
        setTimeout(() => {
          loadingRef.value = false
        }, 2000)
      },
      loading: loadingRef
    }
  },
  data() {
    return {
      percentages: {},
      commentPage: ref(1),
      commentPages: ref(20),
      commentPageSize: ref(10),
      comments:[
        {
        },
      ],
      scores: {
      },
      percentage: {},
      reviews: {
      },
    }
  },
  methods: {
    handleChangePage() {
      this.axios.post('/product/get_comment', {
        page_number: this.commentPage,
        product_id: route.params.trip_id,
      })
          .then((res) => {
            if (res.status === 200) {
              this.comments = res.data.comments
            }
          })
    },
  },
  created() {
    var self = this;
    let route = useRoute();
    console.log(route.params.trip_id);
    this.axios.post('/product/get_comment',{
      page: this.commentPage,
      product_id: route.params.trip_id,
    })
        .then((response)=>{
          const code = response.status
          if (code === 200){
            self.comments = response.data.comments
          }
        })

    this.axios.post('/product/get_reviews',
        {
          product_id: route.params.trip_id
        })
        .then((response)=>{
          const code = response.status
          if (code === 200){
            const count = response.number
            this.commentPages  = Math.floor(count / 10) + (count % 10 > 0 ? 1 : 0);
          }
        })
  },
  mounted() {
    let route = useRoute();
    for (const [key, value] of Object.entries(this.scores)) {
      this.$set(this.percentage, key, Math.round(value * 10));
    }
    var self = this;
    this.axios.post('/product/get_product_grade',
        {
          // 暂时给定值，不知道怎么拿到id
          product_id: route.params.trip_id
        }
    )
        .then(function (response){
          self.scores = response.data;
          for (const [key, value] of Object.entries(self.scores)) {
            self.percentages[key] = Math.round(value * 20);
          }
        })
        .catch(error => {
          console.error(error);
        });
    this.axios.post('/product/get_reviews',
        {
          product_id: route.params.trip_id
        }
    )
        .then(function (response){
          self.reviews = response.data;
        })
        .catch(error => {
          console.error(error);
        });
  },
})
</script>

<style scoped>
.avatar {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  object-fit: cover;
}
.comment_foot {
  display: flex !important;
  align-items: center !important;
  padding-top: 20px !important;
}

.comment_title {
  font-size: 20px;
  font-weight: 500;
  color: #3554D1;
  margin-top: 20px;
}

.comment_content {
  font-size: 15px;
  color: #051036;
  margin-top: 10px;
}

.comment_photos {
  padding-top: 20px;
}

.user_name {
  font-weight: 500;
  line-height: 1.5;
}

.date {
  font-size: 14px;
  line-height: 1.5;
  color: #697488;
}

.photo {
  border-radius: 4px;
  height: 110px;
  width: 110px;
  object-fit: contain;
}

.comment_head {
  align-items: center !important;
}

.bar_head {
  display:flex!important;
  align-items: center !important;
  justify-content: space-between !important;
}

.bar_title {
  font-size: 15px;
  font-weight: 500;
}

.bar_score {
  font-size: 15px;
  color: #697488;
}

.bars {
  padding-top: 20px;
}
.ex_point {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #3554D1;
  border-radius: 4px;
  flex-shrink: 0;
  width: 70px;
  height: 70px;
  font-size: 22px !important;
  font-weight: 600;
  color: #FFFFFF;
}

.ex_sub_wrap {
  margin-left: 20px;
}

.ex_text {
  font-size: 16px;
  font-weight: 500;
  line-height: 1.4;
  color: #051036;
}

.ex_sta {
  font-size: 15px;
  margin-top: 4px;
  line-height: 1.4;
  color: #697488;
}

.exceptional {
  display: flex;
  align-items: center;
  margin-top: 20px;
}

.gr_title {
  font-size: 22px;
  font-weight: 500;
}

.guest_reviews_wrap {
  justify-content: space-between;

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
  .col-sm-6 {
    flex: 0 0 50%;
    max-width: 50%;
  }
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

  .col-xl-8{flex:0 0 auto;width:66.66667%}
  .col-xl-3{flex:0 0 auto;width:25%}
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

.y-gap-20 {
  margin-top: -10px;
  margin-bottom: -10px;
}

.y-gap-20 > * {
  padding-top: 10px;
  padding-bottom: 10px;
}

.x-gap-20 {
  margin-left: -10px;
  margin-right: -10px;
}

.x-gap-20 > * {
  padding-left: 10px;
  padding-right: 10px;
}

.y-gap-30 {
  margin-top: -15px;
  margin-bottom: -15px;
}

.y-gap-30 > * {
  padding-top: 15px;
  padding-bottom: 15px;
}

.col-12{
  flex:0 0 auto;
  width:100%
}

.col-12, .col-xl-8 {
  position: relative;
  width: 100%;
  padding-right: 15px;
  padding-left: 15px;
}
</style>

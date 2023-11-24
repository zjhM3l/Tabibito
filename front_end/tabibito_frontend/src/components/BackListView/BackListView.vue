<template>
  <navigation-bar :is-transparent="true" class="zup"></navigation-bar>

  <div class="TManager">
    <div>
      <side-bar-view></side-bar-view>
    </div>
    <div class="TCon">
      <div class="TTit">
        <div class="TCol">
          <h1 class="TTex1">{{ $t('backList.travelProgramsList') }}</h1>
          <div class="TTex2">{{ $t('backList.manageTheTourismPrograms') }}</div>

        </div>

        <div class="TAuto">
          <div class="but">
            <router-link to="/management" style="text-decoration: none">
              <button class="nBtn nBtn1">
                {{ $t('backList.backToDashboard') }}
              </button>
            </router-link>

            <router-link to="/management/project_detail/add" style="text-decoration: none">
              <button class="nBtn nBtn2">
                {{ $t('backList.addNewProgram') }}
              </button>
            </router-link>

          </div>

        </div>
      </div>

      <div class="TTable">

          <div class="main">
            <div class="tableArea">
              <n-scrollbar x-scrollabl trigger="none" >
              <div class="mainTable">
                <n-data-table
                    :columns="columns"
                    :data="data"
                    :pagination="pagination"
                    @update:sorter="handleUpdateSorter"
                />
              </div>
              </n-scrollbar>
            </div>

          </div>
      </div>

      <!--      footer 部分，直接从footerView中抄过来的-->
      <footer class="footer -type-1">
        <div class="container">
          <div class="contact-foot-layout">
            <div class="row contact-foot">
              <div class="col-auto">
                <div class="row contact-foot-sub">
                  <div class="col-auto">
                    <div class="contact-foot-text">
                      {{ $t('backList.TabibitoAllRightsReserved') }}
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </footer>


    </div>
  </div>


</template>

<script>

import { h, ref, computed } from 'vue'
import { NButton, useMessage } from 'naive-ui'
import {useRouter} from 'vue-router';

import {useToast} from "vue-toastification";
import NavigationBar from "../GeneralComponents/navigationBar.vue";
import SideBarView from "../StaffPortalView/sideBarView.vue";
import axios from 'axios';

export default {
  name: "staffView",
  components: {
    SideBarView,
    NavigationBar
  },

  setup () {

    let data = ref()

    const toast = useToast();

    const route = useRouter();

    const sortStatesRef = ref([])
    const sortKeyMapOrderRef = computed(() =>
        sortStatesRef.value.reduce((result, { columnKey, order }) => {
          result[columnKey] = order
          return result
        }, {})
    )
    const paginationRef = ref({ pageSize: 10, onUpdatePage: page, pageCount:2 })

    const columnsRef = computed(() => [
      {
        title: 'Tourism Title',
        key: 'name'
      },
      {
        title: 'Start Time',
        key: 'start_time',
        // sortOrder: sortKeyMapOrderRef.value.start_time || false,
        // sorter (rowA, rowB) {
        //   return rowA.start_time - rowB.start_time
        // },

      },
      {
        title: 'End Time',
        key: 'end_time',
        // sortOrder: sortKeyMapOrderRef.value.end_time || false,
        // sorter: {
        //   compare: (a, b) => a.end_time - b.end_time,
        //   multiple: 3
        // }
      },
      {
        title: 'Deadline',
        key: 'app_ddl',
        // sortOrder: sortKeyMapOrderRef.value.app_ddl || false,
        // sorter: {
        //   compare: (a, b) => a.app_ddl - b.app_ddl,
        //   multiple: 2
        // }
      },
      {
        title: 'Price',
        sortOrder: sortKeyMapOrderRef.value.price || false,
        key: 'price',
        sorter: {
          compare: (a, b) => a.price - b.price,
          multiple: 1
        }
      },
      {
        title: 'Discount',
        sortOrder: sortKeyMapOrderRef.value.discount || false,
        key: 'discount',
        sorter: {
          compare: (a, b) => a.discount - b.discount,
          multiple: 1
        }
      },{
        title: 'Mark',
        sortOrder: sortKeyMapOrderRef.value.mark || false,
        key: 'mark',
        sorter: {
          compare: (a, b) => a.mark - b.mark,
          multiple: 1
        }
      },{
        title: 'Status',
        sortOrder: sortKeyMapOrderRef.value.status || false,
        key: 'status',
      },
      {
        title: 'Launch',
        key: 'actions',
        render (row) {
          return h(
              NButton,
              {
                strong: true,
                size: 'large',
                type: "success",
                bordered: true,
                secondary: true,
                onClick: () => launch(row)
              },
              { default: () => 'Launch' }
          )
        },
      }, {
        title: 'Delist',
        key: 'actions',
        render (row) {
          return h(
              NButton,
              {
                strong: true,
                size: 'large',
                type: "warning",
                bordered: true,
                secondary: true,
                onClick: () => delist(row)
              },
              { default: () => 'Delist' }
          )
        },
      },{
        title: 'Edit',
        key: 'actions',
        render (row) {
          return h(
              NButton,
              {
                strong: true,
                size: 'large',
                type: "info",
                bordered: true,
                secondary: true,
                onClick: () => edit(row)
              },
              { default: () => 'Edit' }
          )
        },
      }
    ])

    function handleUpdateSorter (sorters) {
      console.log(sorters)
      sortStatesRef.value = [].concat(sorters)
    }

    function launch(row){
      axios.post('/staff_portal/product_status',{
        operation: "Launched",
        id: `${row.id}`,
      }).then((response)=>{
        const code = response.data['code']
        if (code === 200){
          toast.success("This program is launched successfully",{
            position: "bottom-right",

          })
        } else {
          toast.warning("This program has already been launched",{
            position: "bottom-right",

          })
        }
      })
      // console.log( `${row.key}`)
    }

    function delist(row){
      axios.post('/staff_portal/product_status',{
        operation: "Delisted",
        id: `${row.id}`,
      }).then((response)=>{
        const code = response.data['code']
        if (code === 200){
          toast.success("This program is delisted successfully",{
            position: "bottom-right",

          })
        } else {
          toast.warning("This program has already been delisted",{
            position: "bottom-right",

          })
        }
      })
      // console.log( `${row.key}`)
    }
    function edit(row){
      route.push('/management/project_detail/'+`${row.id}`)
      // console.log( `${row.key}`)
    }

    function page(newPage){}

    return {
      route,
      columns: columnsRef,
      handleUpdateSorter,
      data,
      pagination: paginationRef,
      toast,
    }
  },

  created() {
    this.axios.post('/staff_portal/product_list',{
      page: 1
    }).then((response)=>{
      const code = response.status
      if (code === 200){
        this.data = response.data.products

      }
    })
  },

  methods:{
  }

}
</script>

<style scoped>
.zup {
  position: fixed;
  top: 0;
}
.TManager{
  /*overflow: hidden;*/
  width: 100%;
  margin-top: 80px;
  background-color: #F5F5F5;

  /*使用侧边栏前后变化 300px*/
  //padding-left: 300px;
  will-change: padding-left;
  transition: all 0.5s cubic-bezier(0.215, 0.61, 0.355, 1);

  display: flex;
}

.TCon{
  width: 100%;
  padding: 60px;
  padding-bottom: 0;

  overflow: hidden;
  will-change: padding-left;
  transition: all 0.5s cubic-bezier(0.215, 0.61, 0.355, 1);
}



.TTit{
  display:flex;
  flex-wrap:wrap;
  margin: -10px -15px;

  justify-content: space-between;
  align-items: flex-end;
  padding-bottom: 60px;
  //padding-bottom: 40px;
}

.TCol{
  flex:0 0 auto;
  width:auto;
  margin-left: 20px;
  margin-right: 20px;
}

.TTex1{
  font-family: JostBlod;
  font-size: 30px;
  line-height: 1.4;
  font-weight: 100;
}

.TTex2{
  font-size: 15px;
  color: #697488;
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

  padding-left: 44px ;
  padding-right: 44px;

  height:60px;

}

.nBtn1{
  background-color: #3554D1;
  color: white;
  border: 1px solid #3554D1;
  padding-left: 33px ;
  padding-right: 33px;
}

.nBtn1:hover{
  background-color: #FBFCFF;
  color: #051036;
}

.nBtn2{
  background-color: #FBFCFF;
  color: #051036;
  border: 1px solid #3554D1;
  margin-left: 40px;
  padding-left: 33px ;
  padding-right: 33px;
}

.nBtn2:hover{
  background-color: #3554D1;
  color: white;
}

.nBtn1 .icon_login{
  background-image: url("../../assets/arrow.svg");
  margin-left: 15px !important;

  background-position: center;
  background-repeat: no-repeat;
  background-size: contain;
  width: 20px;
  height: 20px;
}

.nBtn2 .icon_login{
  background-image: url("../../assets/arrow_blue.svg");
  margin-left: 15px !important;

  background-position: center;
  background-repeat: no-repeat;
  background-size: contain;
  width: 20px;
  height: 20px;
}

.nBtn1:hover .icon_login{
  background-image: url("../../assets/arrow_blue.svg");
}

.nBtn2:hover .icon_login{
  background-image: url("../../assets/arrow.svg");
}


.TAuto{
  flex:0 0 auto;
  width:auto;
  margin-left: 20px;
  margin-top: 15px;
}

.TTable{
  padding: 30px;
  border-radius: 4px;
  background-color: #FFFFFF;
  width: 95%;
  overflow-x: auto;
}

.main{
  margin-left: auto;
  margin-right: auto;
  background-color: white;
  width: 100%;
  height: 820px;
}

.tableArea{
  display: flex;
  margin-top: 30px;
}

.mainTable{
  min-width: 850px;
  height: 800px;
  margin-left: auto;
  margin-right: auto;
  /*overflow-x: hidden !important;*/
}

.page{
  margin-left: auto;
  margin-right: auto;
  width: 30%;
}

/*下方开始，都是footerView中超过来的代码*/
.container{
  padding-right:var(--bs-gutter-x,15px);
  padding-left:var(--bs-gutter-x,15px);
  //margin-right:auto;
  //margin-left:auto;
}

.row {
  --bs-gutter-x:30px;
  --bs-gutter-y:0;
  width: 90%;
  display:flex;
  flex-wrap:wrap;
  margin-top:calc(var(--bs-gutter-y)*-1);
  margin-right:calc(var(--bs-gutter-x)*0.5);
  margin-left:calc(var(--bs-gutter-x)*0.5)
}

.col-auto{
  flex:0 0 auto;
  width:auto
}

.text-14 {
  font-size: 14px !important;
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

@media screen and (max-width: 1100px) {
  .TCon{
    padding-left: 30px;
    padding-right: 30px;
  }
  .TTable{
    padding: 20px;
  }
}

@media screen and (max-width: 768px) {
  .TCon{
    padding-left: calc(7rem);
  }
}
@media screen and (max-width: 560px) {
  .but{
    flex-direction: column;
  }
  .nBtn2 {
    margin-top: 10px;
    margin-left: 0px;
    margin-right: 0px;
    width: 100%;
  }
}
@media screen and (max-height: 450px) {
  .TManager{
    margin-top: 65px;
  }
}
</style>

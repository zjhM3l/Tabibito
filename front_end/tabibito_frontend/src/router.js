import {createRouter, createWebHashHistory} from 'vue-router'
const profileView = () =>  import("./components/ProfileView/profileView.vue");
const loginView = () =>  import("./components/LoginView/loginView.vue");
const registerView = () => import("./components/RegisterView/registerView.vue");
const aboutUsView = () => import("./components/AboutUsView/aboutUsView.vue");
const forgetPasswordView = () => import("./components/ForgetPasswordView/forgetPasswordView.vue");
const resetView = () => import("./components/ForgetPasswordView/resetView.vue");
const homepageView = () => import("./components/HomepageView/HomepageView.vue");
const backListView = () => import("./components/BackListView/BackListView.vue");
const reservationView = () => import("./components/ReservationView/reservationView.vue");
const projectManagementDetailView = () => import("./components/PMDetailView/projectManagementDetailView.vue");
const TravelDetailsView = () => import("./components/TravelDetailsView/TravelDetailsView.vue");
const leftListView = () => import("./components/SearchPageView/leftListView.vue");
const StaffPortalView = () => import("./components/StaffPortalView/staffPortalView.vue");
const notFoundView = () => import("./components/ErrorViews/notFoundView.vue");
const forbiddenView = () => import("./components/ErrorViews/forbiddenView.vue");
const reservationEdit = () => import("./components/ReservationView/reservationEditNew.vue");
const moreView = () => import("./components/SearchPageView/moreView.vue");
const rightSettingView = () => import("./components/ProfileView/rightSettingView.vue");
const chatView = () => import("./components/ChatView/chatView.vue");
const chartsView = () => import("./components/ChartsView/chartsViewData.vue");
const chartsView1 = () => import("./components/ChartsView/chartViewMaps.vue");
const chartsView2 = () => import("./components/ChartsView/chartViewRates.vue");
const loadView = () => import("./components/LoadView/load.vue");

const routes = [
    { path: '/', component: homepageView, meta: {title: 'home - Tabibito'} },
    { path: '/:pathMatch(.*)*', name: 'NotFound', component: notFoundView, meta: {title: '404 - Tabibito'} },
    { path: '/forbidden', name: 'Forbidden', component: forbiddenView, meta: {title: '403 - Tabibito'} },
    { path: '/login', component: loginView, meta: {title: 'login - Tabibito'} },
    { path: '/register', component: registerView, meta: {title: 'register - Tabibito'} },
    { path: '/forget', component: forgetPasswordView, meta: {title: 'forget - Tabibito'}},
    { path: '/about', component: aboutUsView, meta: {title: 'about us - Tabibito'}},
    { path: '/reset', component: resetView,
        beforeEnter: (to, from) => {
        if (from.path !== '/forget'){
            return {name: 'Forbidden'};
        }else
            return true;
        },
        meta: {title: 'reset - Tabibito'}
    },
    { path: '/management', component: StaffPortalView, meta: {title: 'staff portal - Tabibito'}},
    { path: '/management/project_list', component: backListView, meta: {title: 'project list - Tabibito'}},
    { path: '/management/reservation_list', component: reservationView, meta: {title: 'reservation list - Tabibito'}},
    { path: '/management/reservation_detail/:id', component: reservationEdit, meta: {title: 'reservation detail - Tabibito'}},
    { path: '/management/project_detail/:id', component: reservationEdit, meta: {title: 'project detail - Tabibito'}},
    { path: '/management/project_detail/add', component: projectManagementDetailView, meta: {title: 'add project - Tabibito'}},
    { path: '/trip/:trip_id', component: TravelDetailsView, meta: {title: 'project detail - Tabibito'}},
    { path: '/search_result', name: 'search', component: leftListView, meta: {title: 'search result - Tabibito'}},
    { path: '/user/profile/:uid', component: profileView, meta: {title: 'profile - Tabibito'}},
    { path: '/user/profile/:uid/edit', component: rightSettingView, meta: {title: 'edit profile - Tabibito'}},
    { path: '/chat', component: chatView, meta: {title: 'chat - Tabibito'}},
    { path: '/moreView', name:'more', component: moreView, meta: {title: 'more View - Tabibito'}},
    { path: '/chartsData', component: chartsView, meta: {title: 'charts View - Tabibito'}},
    { path: '/chartsMaps', component: chartsView1, meta: {title: 'charts View - Tabibito'}},
    { path: '/chartsRates', component: chartsView2, meta: {title: 'charts View - Tabibito'}},
    { path: '/load', component: loadView, meta: {title: 'Loading View - Tabibito'}},
]

const router = createRouter({
    history: createWebHashHistory(),
    routes,})

router.beforeEach((to, from) => {
    if (to.meta.title){
        document.title = to.meta.title;
    }
})
export default router;

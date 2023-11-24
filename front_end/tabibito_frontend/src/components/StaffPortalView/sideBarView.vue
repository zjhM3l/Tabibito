<template>
  <head>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
  </head>
  <body style="height:100%">

  <aside :class="`${is_expanded && 'is-expanded'}`">
    <div class="logo">
    </div>

    <div class="menu-toggle-wrap">
      <button class="menu-toggle" @click="ToggleMenu">
        <span class="material-symbols-outlined">keyboard_double_arrow_right</span>
      </button>
    </div>

    <h3>{{ $t('sidebarView.menu') }}</h3>
    <div class="menu">
      <router-link class="button" to="/management">
        <img class="material-symbols-outlined" src="../../assets/dashboard/sidebar/compass.svg" :alt="$t('rightContentView.icon')">
        <span class="text">{{ $t('rightContentView.dashboard') }}</span>
      </router-link>
      <router-link class="button" to="/chat">
        <img class="material-symbols-outlined iconC" src="../../assets/Chat.svg" :alt="$t('rightContentView.icon')">
        <span class="text">{{ $t('navi.chat') }}</span>
      </router-link>
      <router-link class="button" to="/management/project_list">
        <img class="material-symbols-outlined" src="../../assets/dashboard/sidebar/booking.svg" :alt="$t('rightContentView.icon')">
        <span class="text">{{ $t('sidebarViewprograms') }}</span>
      </router-link><router-link class="button" to="/management/reservation_list">
      <img class="material-symbols-outlined" src="../../assets/dashboard/sidebar/bookmark.svg" :alt="$t('rightContentView.icon')">
      <span class="text">{{ $t('sidebarViewreservations') }}</span>
    </router-link><router-link class="button" to="/">
      <img class="material-symbols-outlined" src="../../assets/dashboard/sidebar/gear.svg" :alt="$t('rightContentView.icon')">
      <span class="text">{{ $t('sidebarViewsettings') }}</span>
    </router-link><router-link class="button" to="/">
      <img class="material-symbols-outlined" src="../../assets/dashboard/sidebar/log-out.svg" :alt="$t('rightContentView.icon')">
      <span class="text">{{ $t('sidebarViewlogout') }}</span>
    </router-link>
    </div>
  </aside>
  </body>
</template>

<script setup>
import { ref } from 'vue'
import {  } from '@vicons/ionicons5'

const is_expanded = ref(false)

const ToggleMenu = () => {
  is_expanded.value = !is_expanded.value
}
</script>

<style scoped>

/*@media (max-width: 991px) {*/
/*  .portal_sidebar {*/
/*    transform: translateX(-100%);*/
/*  }*/
/*}*/

/*@media (max-width: 767px) {*/
/*  .portal_sidebar {*/
/*    width: 80%;*/
/*    height: calc(100% - 80px);*/
/*  }*/
/*}*/

/*.portal_sidebar {*/
/*  position: fixed;*/
/*  bottom: 0;*/
/*  left: 0;*/
/*  z-index: 100;*/
/*  width: var(--dashboard-width);*/
/*  height: calc(100% - 90px);*/
/*  padding: 30px;*/
/*  padding-top: 60px;*/
/*  padding-bottom: 40px;*/
/*  will-change: transform;*/
/*  transition: all 0.5s cubic-bezier(0.215, 0.61, 0.355, 1);*/
/*  background-color: #FFFFFF !important;*/
/*}*/

:root {
  --primary: #4ade80;
  --grey: #64748b;
  --dark: #1e293b;
  --dark-alt: #334155;
  --light: #f1f5f9;
  --sidebar-width: 300px;
}

aside {
  display: flex;
  flex-direction: column;
  width: calc(2rem + 2rem);
  min-height: 100%;
  overflow: hidden;
  padding: 1rem;
  background-color: #fff;
  color: #1e293b;
  transition: 0.3s ease-out;
}

aside .logo {
  margin-bottom: 1rem;
}

aside .logo img {
  width: 4rem;
}

aside .menu-toggle-wrap {
  display: flex;
  justify-content: flex-end;
  margin-bottom: 1rem;
  position: relative;
  top: 0;
  transition: 0.3s ease-out;
}

aside .menu {
  margin: 0 -1rem;
}

aside .menu .button {
  display: flex;
  align-items: center;
  text-decoration: none;
  padding: 0.5rem 1rem;
  transition: 0.3s ease-out;
}

aside .menu .button .material-symbols-outlined {
  font-size: 2rem;
  color: #1e293b;
  transition: 0.3s ease-out;
}

.iconC{
  width: 23px;
}

aside .menu .button .router-link-exact-active {
  border-right: 5px solid #f1f5f9;
}

aside .menu .button:hover {
  background-color: #f1f5f9;
}

aside .menu .button:hover .text {
  color: #3554D1;
}

aside .menu .button .router-link-exact-active {
  background-color: #f1f5f9;
}

aside .menu .button .router-link-exact-active .material-symbols-outlined{
  color: #3554D1;
}

aside .menu .button .router-link-exact-active .text{
  color: #3554D1;
}

aside .menu .button:hover .material-symbols-outlined {
  color: #3554D1;
}

aside .menu .button .text {
  color: #1e293b;
  transition: 0.3s ease-out;
}

aside h3 {
  opacity: 0;
  transition: 0.3s ease-out;
}

aside h3 {
  color: #64748b;
  font-size: 0.875rem;
  margin-bottom: 0.5rem;
  text-transform: uppercase;
}

aside .button .text {
  opacity: 0;
  transition: 0.3s ease-out;
}

aside .menu-toggle-wrap .menu-toggle {
  transition: 0.3s ease-out;
  background-color: #ffffff;
  border: 1.5px solid #3554D1;
  border-radius: 4px;
}

aside .menu-toggle-wrap .menu-toggle .material-symbols-outlined {
  font-size: 2rem;
  color: #1e293b;
  transition: 0.3s ease-out;
}

aside .menu-toggle-wrap .menu-toggle:hover {
  background-color: #3554D1;
  color: #ffffff;
}

aside .menu-toggle-wrap .menu-toggle:hover .material-symbols-outlined{
  color: #ffffff;
  transform: translateX(0.5rem);

}

aside.is-expanded {
  width: 200px;
}

aside.is-expanded h3 {
  opacity: 1;
}

aside.is-expanded .button .text {
  opacity: 1;
}

aside.is-expanded .menu-toggle-wrap {
  top: -1rem;
}

aside.is-expanded .button .material-symbols-outlined {
  margin-right: 1rem;
}

aside.is-expanded .menu-toggle-wrap .menu-toggle {
  transform: rotate(-180deg);
}

@media (max-width: 768px) {
  aside {
    position: fixed;
    z-index: 99;
  }
}
@media (max-width: 575px) {
  aside{
    padding-right: 0px;
  }
}

</style>

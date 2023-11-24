<template>
  <section>

  <navigation-bar :is-transparent="true" class="zup"></navigation-bar>

  <div class="portal">
    <SideBarView />

    <div class="dashboard_main">
      <right-content-view />
    </div>
  </div>
  </section>

</template>

<script setup>
import SideBarView from "./sideBarView.vue";
import RightContentView from "./rightContentView.vue";
import NavigationBar from "../GeneralComponents/navigationBar.vue";
</script>

<style scoped>
.zup {
  position: fixed;
  top: 0;
}
.dashboard_main {
  overflow: hidden;
  width: 100%;
  padding-left: var(--dashboard-width);
  will-change: padding-left;
  transition: all 0.5s cubic-bezier(0.215, 0.61, 0.355, 1);
}

.dashboard_main::after {
  content: "";
  display: none;
  position: fixed;
  z-index: 50;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: rgba(0, 0, 0, 0.5);
  transition: all 0.5s cubic-bezier(0.215, 0.61, 0.355, 1);
  pointer-events: none;
  opacity: 0;
}

@media (max-width: 991px) {
  .dashboard_main {
    padding-left: 0;
  }
  .dashboard_main::after {
    display: block;
  }
}

:root {
  --primary: #4ade80;
  --grey: #64748b;
  --dark: #1e293b;
  --dark-alt: #334155;
  --light: #f1f5f9;
  --sidebar-width: 300px;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Fira sans', sans-serif;
}

body {
  background: var(--light);
}

button {
  cursor: pointer;
  appearance: none;
  border: none;
  outline: none;
  background: none;
}

.portal {
  margin-top: 80px;
  display: flex;
}

.portal main {
  flex: 1 1 0;
  padding: 2rem;
}

@media (max-width: 991px) {
  /*.portal {*/
  /*  flex-direction: column;*/
  /*}*/
}

@media (max-width: 768px) {
  .portal main{
    padding-left: 6rem;
  }
  .dashboard_main{
    padding-left: 100px;
    padding-right: 20px;
  }
}

@media (max-width: 575px) {
  .dashboard_main{
    padding-right: 0;
    padding-left: 75px;
  }
}
</style>

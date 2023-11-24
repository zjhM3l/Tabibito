<template>

  <navigation-bar></navigation-bar>

  <div class="one2" id="chart2"></div>
  <div class="SepLine"></div>

  <div class="two2" id="chart3"></div>

</template>

<script>
import NavigationBar from "../GeneralComponents/navigationBar.vue";

export default {
  name: "chartViewMaps",
  components: {NavigationBar},

  mounted() {
    // 使用JavaScript将Pyecharts图表嵌入到容器中

    const chartContainer2 = document.getElementById("chart2");
    chartContainer2.innerHTML = '<iframe src="../../../dist/map_world.html" frameborder="0" style="width:100%;height:600px;margin-top: 10%"></iframe>';

    const chartContainer3 = document.getElementById("chart3");
    chartContainer3.innerHTML = '<iframe src="../../../dist/map_globe_3d.html" frameborder="0" style="width:100%;height:550px;margin-top: 3%"></iframe>';

  },
}
</script>

<style scoped>


.one2{
  margin-left: 25%;
}

.two2{
  margin-left: 25%;
}

.SepLine{
  border: #bbb8b8 solid 0.5px;
}

</style>
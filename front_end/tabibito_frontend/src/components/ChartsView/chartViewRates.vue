<template>

  <navigation-bar></navigation-bar>
  <div class="one3" id="chart5"></div>

  <div class="SepLine"></div>

  <div class="one3" id="chart4"></div>

</template>

<script>
import NavigationBar from "../GeneralComponents/navigationBar.vue";

export default {
  name: "chartViewRates",
  components: {NavigationBar},

  mounted() {
    // 使用JavaScript将Pyecharts图表嵌入到容器中

    const chartContainer4 = document.getElementById("chart4");
    chartContainer4.innerHTML = '<iframe src="../../../dist/reservation_rate_liquid.html" frameborder="0" style="width:100%;height:550px;margin-top:3%"></iframe>';

    const chartContainer5 = document.getElementById("chart5");
    chartContainer5.innerHTML = '<iframe src="../../../dist/reservation_rate_guage.html" frameborder="0" style="width:100%;height:550px;margin-top: 10%"></iframe>';
  },
}
</script>

<style scoped>


.one3{
  margin-left: 25%;
}

.two3{
  margin-left: 25%;
}

.SepLine{
  border: #bbb8b8 solid 0.5px;
}

</style>
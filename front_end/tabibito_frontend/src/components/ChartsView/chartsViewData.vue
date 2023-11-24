<template>

  <navigation-bar></navigation-bar>

<div class="con1">
  <div class="t11"></div>
  <div class="one1" id="chart1"></div>

  <div class="SepLine"></div>

  <div class="t12"></div>
  <div class="two1" id="chart6"></div>
</div>

</template>

<script>
import * as echarts from 'echarts';
import NavigationBar from "../GeneralComponents/navigationBar.vue";

export default {
  components: {NavigationBar},
  mounted() {
    // 使用JavaScript将Pyecharts图表嵌入到容器中
    const chartContainer1 = document.getElementById("chart1");
    chartContainer1.innerHTML = '<iframe src="../../../dist/orders_of_types_15.html" frameborder="0" style="width:100%;height:600px;margin-top: 10%"></iframe>';

    const chartContainer6 = document.getElementById("chart6");
    chartContainer6.innerHTML = '<iframe src="../../../dist/wordcloud_diamond.html" frameborder="0" style="width:100%;height:550px;margin-top: 3%"></iframe>';
  },

}

</script>

<style>
.con1{
}

.one1{
  margin-left: 25%;
}

.two1{
  margin-left: 25%;
}

.SepLine{
  border: #bbb8b8 solid 0.5px;
}

</style>

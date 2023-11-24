<template>
  <div class="one1" id="chart1"></div>

</template>

<script>
export default {
  name: "chartDataOne",

  mounted() {
    // 使用JavaScript将Pyecharts图表嵌入到容器中
    const chartContainer1 = document.getElementById("chart1");
    chartContainer1.innerHTML = '<iframe src="../../../dist/orders_of_types_15.html" frameborder="0" style="width:100%;height:600px;"></iframe>';

  },
}

</script>

<style scoped>

</style>
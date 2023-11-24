<template>
  <div class="dropdown">
    <div class="dropdownContainer">
      <div class="dropdownItem" v-for="item in dropdown_item" @click="handleClick(item)">
        <div class="dropdownItemIcon" :style="item.icon"></div>
        <div class="dropdownItemText">{{item.text}}</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['is_currency', 'dropdown_item'],
  name: "dropDown.vue",
  methods:{
    handleClick(item){
      if (this.is_currency){
        this.$emit('changeCurrency', item.icon, item.text);
      }else {
        this.$router.push(item.path)
      }
    }
  },
  emits: ['changeCurrency']
}
</script>

<style scoped>
.dropdownContainer{
  width: 100px;
  background-color: #ffffff;
  border-radius: var(--border-radius);
  box-sizing: border-box;
  padding: 10px;
  position: absolute;
  z-index: 10000;
}
.dropdownContainer::before{
  content: '';
  display: block;
  position: absolute;
  width: 100px;
  height: 25px;
  top: -25px;
}
.dropdownItem{
  width: 100%;
  height: 30px;
  display: flex;
  align-items: center;
  border-radius: var(--border-radius);
  cursor: pointer;
}
.dropdownItem:hover{
  background-color: rgba(53, 84, 209, 0.05);
  color: #3554D1;
  transition: .1s ease-out;
}
.dropdownItemIcon{
  width: 35%;
  height: 20px;
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center;
}
.dropdownItemText{
  width: 65%;
  height: 100%;
  line-height: 30px;
  text-align: center;
  font-size: 14px;
}
</style>
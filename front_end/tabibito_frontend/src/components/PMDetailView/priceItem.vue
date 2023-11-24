<template>
  <div class="stepContainer">
    <div class="stepTitleBar" @click="handleExpand">
      <div class="stepTitle">{{"Pay Item " + (itemIndex + 1) + ": " + itemData.chargeName}}</div>
      <div class="actions">
        <n-popconfirm
            @positive-click="handleDeleteStep"
        >
          <template #trigger>
            <div class="actionButton deleteButtonIcon" @click.stop=""></div>
          </template>
          {{ $t('priceItem.areYouSureYouWantToDeleteThisStepTheInformationWil') }}
        </n-popconfirm>
        <div class="actionButton" :class="expandButtonIcon"></div>
      </div>
    </div>
    <n-collapse-transition :show="show">
      <div class="stepContent">
        <div class="inputTitle">{{ $t('priceItem.chargeName') }}</div>
        <div class="input_form">
          <input type="text" v-model="itemData.chargeName" required>
          <label class="input_label">{{ $t('priceItem.chargeName') }}</label>
        </div>
        <div class="inputTitle">{{ $t('priceItem.chargeDescription') }}</div>
        <div class="input_form">
          <textarea type="text" v-model="itemData.chargeDescription" required></textarea>
          <label class="input_label">{{ $t('priceItem.chargeDescription') }}</label>
        </div>
      </div>
    </n-collapse-transition>
  </div>


</template>

<script>
import {ref} from "vue";

export default {
  props:['itemData', 'itemIndex'],
  name: "priceItem",
  emits: ['deleteCharge'],
  setup(props){
    let show = ref(true);
    let expandButtonIcon = ref("collapseIcon");
    function handleExpand(){
      if (show.value){
        expandButtonIcon.value = "expandIcon";
        show.value = false;
      }else {
        expandButtonIcon.value = "collapseIcon";
        show.value = true;
      }
    }
    return{
      show,
      expandButtonIcon,
      handleExpand,
    }
  },
  methods:{
    handleDeleteStep(){
      this.$emit('deleteCharge', this.itemIndex);
    }
  }
}
</script>

<style scoped>
.stepContainer{
  width: 100%;
  border: #DDDDDD 1px solid;
  border-radius: 4px;
  box-sizing: border-box;
  padding: 0 20px;
}
  .stepTitleBar{
    width: 100%;
    height: 60px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .stepTitle{
    font-size: 20px;
  }
  .actions{
    display: flex;
  }
  .actionButton{
    width: 30px;
    height: 30px;
    background-repeat: no-repeat;
    background-position: center;
    background-size: contain;
  }
  .deleteButtonIcon{
    background-image: url("../../assets/close.svg");
    transition: .2s;
  }
  .deleteButtonIcon:hover{
    border-radius: 100%;
    background-color: #DDDDDD;
    transition: .2s;
  }
  .expandIcon{
    transform: rotateZ(180deg);
    background-image: url("../../assets/ChevronUp.svg");
    transition: .3s;
  }
  .collapseIcon{
    background-image: url("../../assets/ChevronUp.svg");
    transition: .3s;
  }
  .inputTitle{
    margin: 10px 0;
    font-weight: 500;
    font-size: 18px;
    line-height: 1.875;
  }
  .input_form{
    position: relative;
    transition: all 0.2s cubic-bezier(0.165, 0.84, 0.44, 1);
    display: flex;
    margin: 10px;
  }
  .inner_input_form{
    position: relative;
    transition: all 0.2s cubic-bezier(0.165, 0.84, 0.44, 1);
    display: flex;
    width: 30%;
  }
  .input_label{
    line-height: 1 !important;
    font-size: 14px !important;
    color: #697488;
  }
  .input_form label {
    position: absolute;
    top: 26px;
    padding: 0 15px;
    pointer-events: none;
    font-size: 14px;
    transition: all 0.2s cubic-bezier(0.165, 0.84, 0.44, 1);
  }
  .input_form input,textarea {
    border: 1px solid #DDDDDD;
    width: 100%;
    font-size: 15px;
    border-radius: 4px;
    /*padding: 0 15px;*/
    padding-top: 20px;
    padding-left: 15px;
    min-height: 48px;
    transition: all 0.2s cubic-bezier(0.165, 0.84, 0.44, 1);
  }
  .input_form textarea{
    min-height: 80px;
  }
  .input_form input:focus,textarea:focus {
    outline: 2px solid #000000 !important;
  }
  .input_form input:focus ~ label, .input_form input:valid ~ label {
    transform: translateY(-10px);
  }
  .input_form textarea:focus ~ label, .input_form textarea:valid ~ label {
    transform: translateY(-10px);
  }
  .input_form textarea{
    box-sizing: border-box;
    padding-top: 35px;
  }
  .timeInputForm{
    display: flex;
    width: 100%;
    align-items: center;
    justify-content: space-between;
    padding: 0 10px;
    box-sizing: border-box;
  }
  .timeInputForm *{
    width: calc((100% - 20px)/3);
  }
</style>

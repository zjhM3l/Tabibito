<template>
    <div class="chatbox">
      <div class="conversation">
        <div class="message" v-for="(item, index) in messages" :key="index" :class="{'sent': item.type === 'sent', 'received': item.type === 'received'}">
          <div class="message-content">{{ item.content }}</div>
        </div>
        <div ref="scroll" class="scroll"></div>
      </div>
      <div class="input-box">
        <input type="text" class="input" v-model="inputText" @keydown.enter="send" placeholder="请输入...">
        <button class="send" @click="send">发送</button>
      </div>
    </div>
</template>

<script>
import {defineComponent} from "vue";
import { Configuration, OpenAIApi } from "openai";

//ldl
const configuration = new Configuration({
  apiKey: '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',
});
//whc
// const configuration = new Configuration({
//   apiKey: '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',
// });
//zjh
// const configuration = new Configuration({
//   apiKey: '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',
// });
const openai = new OpenAIApi(configuration);

export default defineComponent( {
  name: "gptChatView",
  data() {
    return {
      inputText: '',
      messages: []
    }
  },
  methods: {
    async send() {
      if (this.inputText) {
        // Add user message to messages array
        this.messages.push({
          type: 'sent',
          content: this.inputText
        });

        // Call OpenAI API to get chat response
        const completion = await openai.createChatCompletion({
          model: "gpt-3.5-turbo",
          messages: [{role: "assistant", content: this.inputText}],
        });

        // Extract chat response and add it to messages array
        const responseContent = completion.data.choices[0].message.content;
        this.messages.push({
          type: 'received',
          content: responseContent
        });

        // Clear input field and scroll to bottom
        this.inputText = '';
        this.$nextTick(() => {
          this.scrollToBottom();
        });

      }
    },
    scrollToBottom() {
      this.$refs.scroll.scrollIntoView({ behavior: 'smooth' });
    },
  }
})
</script>

<style scoped>
.chatbox {
  background-color: #DFEFF7;
  border: 1px solid #B2D0E5;
  border-radius: 5px;
  width: 320px;
  height: 500px;
  position: fixed;
  bottom: 20px;
  right: 20px;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.conversation {
  height: 80%;
  flex: 1;
  overflow-y: scroll; /* 修改为 scroll */
  padding: 10px;
  display: flex;
  flex-direction: column;
}

.message {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin-bottom: 10px;
}

.message-content {
  font-size: 16px;
  padding: 10px;
  border-radius: 5px;
  max-width: 200px;
  word-wrap: break-word;
}

.sent .message-content {
  background-color: #F8F8F8;
  align-self: flex-end;
}

.received .message-content {
  background-color: #E3EEFF;
  align-self: flex-start;
}

.input-box {
  display: flex;
  align-items: center;
  padding: 10px;
}

.input {
  border: none;
  border-radius: 20px;
  padding: 10px;
  flex: 1;
  margin-right: 10px;
  background-color: #F2F6FA;
}

.send {
  border: none;
  border-radius: 20px;
  padding: 10px 20px;
  background-color: #4B7BFF;
  color: white;
  cursor: pointer;
}

</style>

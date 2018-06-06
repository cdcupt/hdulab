<template>
  <div class="components-container">
    <div v-html="title"></div>
    <div class="editor-container">
      <markdown-editor id="contentEditor" ref="contentEditor" v-model="content" :height="250" :zIndex="20"></markdown-editor>
    </div>
    <div>
        <textarea v-model="report" placeholder="结果报告" :rows="20" :cols="35"></textarea>
    </div>
    <el-button @click="submit" style="margin-top:80px;" type="primary" icon="el-icon-document">提交</el-button>
    
  </div>
</template>

<script>
import MarkdownEditor from '@/components/MarkdownEditor'
import { fetchProblem } from '@/api/problem'
import { putResult } from '@/api/result'
import showdown from 'showdown'

const content = `
## 请在这里插入代码
`

export default {
  name: 'markdown-demo',
  components: { MarkdownEditor },
  data() {
    return {
      content: content,
      title: '',
      report: ''
    }
  },
  created() {
    const name = this.$route.params.id
    this.fetchData(name)
  },
  methods: {
    fetchData(id) {
      fetchProblem(id).then(response => {
        const converter = new showdown.Converter()
        this.title = converter.makeHtml(response.data.data.content)
      }).catch(err => {
        console.log(err)
      })
    },
    submit() {
      const nac = {
        name: this.$route.params.id,
        result: this.content
      }
      putResult(nac).then(response => {
        console.log(response.data.data)
        this.report = response.data.data
      }).catch(err => {
        console.log(err)
      })
    }
  }
}
</script>



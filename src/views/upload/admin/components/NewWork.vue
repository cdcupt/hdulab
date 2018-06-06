<template>
<el-dialog title="新建题目" 
          :visible.sync="thisVisible"
          @close='onDialogClose'
          @open='onDialogOpen'
          :before-close="newWorkBeforeClose">
  <div style="margin: 20px;"></div>
  <el-form label-position="left" label-width="50px" ref='newWorkForm' :model="form">
    <el-form-item label="名称">
      <el-input v-model="name" auto-complete="off"></el-input>
    </el-form-item>
    <el-input
      type="textarea"
      :rows="5"
      placeholder="请输入题目描述"
      v-model="textarea">
    </el-input>
    <el-upload
      class="upload-demo"
      ref="upload"
      action="https://jsonplaceholder.typicode.com/posts/"
      :on-preview="handlePreview"
      :on-remove="handleRemove"
      :file-list="fileList"
      :auto-upload="false">
      <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
      <el-button style="margin-left: 10px;" size="small" type="success" @click="submitUpload">上传到服务器</el-button>
      <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div>
    </el-upload>
  </el-form>
  <span slot="footer" class="dialog-footer">
    <el-button @click="Cancel">取 消</el-button>
    <el-button type="primary" @click="Confirm">确 定</el-button>
  </span>
</el-dialog>  
</template>


<script>
  import { putWork } from '@/api/upload'
  export default {
    name: 'NewWork',
    props: { // 子组件需要显式的用props声明期待的数据
      newWorkVisible: Boolean // dialog的visible状态
    },
    data() {
      return {
        thisVisible: false, // 当前dialog的visible状态
        btnLoadingWork: false, // 确定按钮的Loading状态
        name: '',
        textarea: '',
        fileList: []
      }
    },
    watch: {
      newWorkVisible(val, oldVal) {
        this.thisVisible = val
      }
    },
    methods: {
      newWorkBeforeClose(done) {
        done()
      },
      onDialogClose() {
        this.onDataReset()
        this.$emit('newWorkDialogClose')
      },
      onDialogOpen(done) {
        done()
      },
      onDataReset() {
        this.$refs['newWorkForm'] && this.$refs['newWorkForm'].resetFields()
        this.name = ''
        this.textarea = ''
        this.fileList = []
      },
      Cancel() {
        this.$emit('newWorkDialogClose')
        this.thisVisible = false
      },
      Confirm() {
        alert(this.fileList)
        var a = { 'name': this.name, 'content': this.textarea, 'author': '柴代晨' }
        putWork(a)
        this.Cancel()
      },
      submitUpload() {
        this.$refs.upload.submit()
      },
      handleRemove(file, fileList) {
        console.log(file, fileList)
      },
      handlePreview(file) {
        console.log(file)
      }
    }
}
</script>


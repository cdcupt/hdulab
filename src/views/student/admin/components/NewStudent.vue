<template>
<el-dialog title="新增学生" 
          :visible.sync="thisVisible"
          @close='onDialogClose'
          @open='onDialogOpen'
          :before-close="newStudentBeforeClose">
  <el-form ref='newStudentForm' :model="form">
    <el-form-item label="姓名" :label-width="formLabelWidth">
      <el-input v-model="name" auto-complete="off"></el-input>
    </el-form-item>
    <el-form-item label="班级" :label-width="formLabelWidth">
      <el-input v-model="mclass" auto-complete="off"></el-input>
    </el-form-item>
  </el-form>
  <span slot="footer" class="dialog-footer">
    <el-button @click="Cancel">取 消</el-button>
    <el-button type="primary" @click="Confirm">确 定</el-button>
  </span>
</el-dialog>  
</template>


<script>
  import { putStudent } from '@/api/student'
  export default {
    name: 'NewStudent',
    props: { // 子组件需要显式的用props声明期待的数据
      newStudentVisible: Boolean // dialog的visible状态
    },
    data() {
      return {
        thisVisible: false, // 当前dialog的visible状态
        btnLoadingIP: false, // 确定按钮的Loading状态
        name: '',
        mclass: ''
      }
    },
    watch: {
      newStudentVisible(val, oldVal) {
        this.thisVisible = val
      }
    },
    methods: {
      newStudentBeforeClose(done) {
        done()
      },
      onDialogClose() {
        this.onDataReset()
        this.$emit('newStudentDialogClose')
      },
      onDialogOpen(done) {
        done()
      },
      onDataReset() {
        this.$refs['newStudentForm'] && this.$refs['newStudentForm'].resetFields()
        this.name = ''
        this.mclass = ''
      },
      Cancel() {
        this.$emit('newStudentDialogClose')
        this.thisVisible = false
      },
      Confirm() {
        var a = { 'name': this.name, 'class': this.mclass }
        putStudent(a)
        this.Cancel()
      }
    }
}
</script>


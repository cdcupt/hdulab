<template>
  <div class="student">
  <div class="app-container">
    <el-row type='flex' justify='space-between' class='role-op-info'>
      <!--新建和删除按钮 左边栏-->
      <el-col :span='12' class='role-op-info-left'>
        <el-button type='success' @click='handleAdd'>新建</el-button>
        <el-button type='success' @click='handleDelAll'>删除</el-button>
      </el-col>
      
      <!--查询框 右边栏-->
      <el-col :span='12' class='role-op-info-right'>
          <el-autocomplete placeholder='请输入以查询'
                           value-key='roleName'
                           v-model='queryStr'
                           :fetch-suggestions="queryRoleList"
                           @keyup.enter.native='queryAtPage'>
          </el-autocomplete>
          <el-button type='primary'
                   class='role-op-info-btn'
                   icon='el-icon-my-chaxun'
                   @click='queryAtPage'>查询
        </el-button>
      </el-col>
    </el-row>
  
    <el-table :data="list" v-loading.body="listLoading" element-loading-text="Loading" border fit highlight-current-row
              @selection-change="handleSelectionChange">
      <el-table-column align='center' type='selection' width="55"/>
      <el-table-column align="center" prop="name" label='姓名' width="300">
      </el-table-column>
      <el-table-column align="center" prop="class" label='班级' width="300">
      </el-table-column>
      <el-table-column align="center" prop="homework" label='作业成绩' sortable width="250">
      </el-table-column>
      <el-table-column align="center" prop="time" label='最后登录时间' sortable width="500">
      </el-table-column>
    </el-table>
    </div>
    <new-student :newStudentVisible='newStudentVisible'
            @newStudentDialogClose='newStudentDialogClose'></new-student>
  </div>
</template>

<script>
import { getStudent, delStudent } from '@/api/student'
import NewStudent from './components/NewStudent'

export default {
  components: { NewStudent },
  data() {
    return {
      list: null,
      listLoading: true,
      input: '',
      newStudentVisible: false,
      multiSelects: []
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    fetchData() {
      this.listLoading = true
      getStudent(this.listQuery).then((response) => {
        this.list = response.data.data
        this.listLoading = false
      })
    },
    handleAdd() {
      this.newStudentVisible = true
      this.fetchData()
    },
    handleSelectionChange(selects) {
      this.multiSelects = selects
    },
    handleDelAll() {
      const { length } = this.multiSelects
      if (length > 1) { // 删除多个角色
        this.$confirm(`确认删除这 ${length} 个角色?`, { type: 'warning' })
          .then(() => {
            const deletes = []
            this.multiSelects.forEach(T => deletes.push(T.name))
            var params = new URLSearchParams()
            params.append('name', JSON.stringify(deletes))
            delStudent(params)
          }).then(() => this.fetchData())
          .catch(() => {})
      } else if (length === 1) { // 删除一个角色
        this.$confirm(`确认删除角色 ${this.multiSelects[0].name} ?`, { type: 'warning' })
          .then(() => {
            var params = new URLSearchParams()
            params.append('name', JSON.stringify(this.multiSelects[0].name))
            delStudent(params)
          }).then(() => this.fetchData())
          .catch(() => {})
      }
    },
    newStudentDialogClose() {
      this.newStudentVisible = false
      this.fetchData()
    }
  }
}
</script>

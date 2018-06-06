<template>
  <div class="upload">
  <div class="app-container">
    <el-row type='flex' justify='space-between' class='role-op-info'>
      <!--新建和删除按钮 左边栏-->
      <el-col :span='12' class='role-op-info-left'>
        <el-button type='success' @click='handleAdd' icon='el-icon-my-xinjian'>上传</el-button>
        <el-button type='success' @click='handleDelAll' icon='el-icon-my-shanchu-m'>删除</el-button>
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
      <el-table-column align="center" prop="name" label='题目名称' width="300">
      </el-table-column>
      <el-table-column align="center" prop="author" label='作者' width="300">
      </el-table-column>
      <el-table-column align="center" prop="difficulty" label='完成情况' sortable width="250">
      </el-table-column>
      <el-table-column align="center" prop="date" label='最后修改时间' sortable width="500">
      </el-table-column>
    </el-table>
    </div>
    <new-work :newWorkVisible='newWorkVisible'
            @newWorkDialogClose='newWorkDialogClose'></new-work>
  </div>
  </template>

<script>
import { getWork, delWork } from '@/api/upload'
import NewWork from './components/NewWork'
export default {
  components: { NewWork },
  data() {
    return {
      list: null,
      listLoading: true,
      input: '',
      newWorkVisible: false,
      newOPVisible: false,
      multiSelects: [],
      ipSelects: [],
      nowRow: 0
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    fetchData() {
      this.listLoading = true
      getWork(this.listQuery).then(response => {
        this.list = response.data.data.items
        this.listLoading = false
      })
    },
    handleAdd() {
      this.newWorkVisible = true
      // alert(this.newIPVisible)
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
            delWork(params)
          }).then(() => this.fetchData())
          .catch(() => {})
      } else if (length === 1) { // 删除一个角色
        this.$confirm(`确认删除角色 ${this.multiSelects[0][name]} ?`, { type: 'warning' })
          .then(() => {
            var params = new URLSearchParams()
            params.append('name', JSON.stringify(this.multiSelects[0].name))
            delWork(params)
          }).then(() => this.fetchData())
          .catch(() => {})
      }
    },
    newWorkDialogClose() {
      this.newWorkVisible = false
    }
  }
}
</script>

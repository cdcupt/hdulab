<template>
  <div class="student-container">
    <component :is="currentRole"></component>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import adminUpload from './admin'
import editorUpload from './editor'

export default {
  name: 'student',
  components: { adminUpload, editorUpload },
  data() {
    return {
      currentRole: 'adminUpload'
    }
  },
  computed: {
    ...mapGetters([
      'roles'
    ])
  },
  created() {
    if (!this.roles.includes('admin')) {
      this.currentRole = 'editorUpload'
    }
  }
}
</script>

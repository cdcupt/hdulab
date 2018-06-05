<template>
  <div class="student-container">
    <component :is="currentRole"></component>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import adminStudent from './admin'
import editorStudent from './editor'

export default {
  name: 'student',
  components: { adminStudent, editorStudent },
  data() {
    return {
      currentRole: 'adminStudent'
    }
  },
  computed: {
    ...mapGetters([
      'roles'
    ])
  },
  created() {
    if (!this.roles.includes('admin')) {
      this.currentRole = 'editorStudent'
    }
  }
}
</script>

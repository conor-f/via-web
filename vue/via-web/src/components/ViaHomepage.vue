<template>
  <div id="body-container">
    <ViaSidebar
      v-if="shouldShowSidebar"
      />

    <splitpanes
      class="default-theme"
      horizontal
      >
      <pane min-size="50">
        <ViaMap/>
      </pane>

      <pane
        size="30"
        v-if="shouldShowTables"
        >
        <ViaDetailTables/>
      </pane>
    </splitpanes>
  </div>
</template>

<script>
import ViaSidebar from './ViaSidebar.vue'
import ViaMap from './ViaMap.vue'
import ViaDetailTables from './ViaDetailTables.vue'

import { Splitpanes, Pane } from 'splitpanes'
import 'splitpanes/dist/splitpanes.css'


export default {
  name: 'ViaHomepage',
  components: {
    ViaSidebar,
    ViaMap,
    ViaDetailTables,
    Splitpanes,
    Pane
  },
  data() {
    return {
    }
  },
  computed: {
    shouldShowSidebar() {
      const urlParams = new URLSearchParams(window.location.search)
      return urlParams.get("show_sidebar") != "false"
    },
    shouldShowTables() {
      // const urlParams = new URLSearchParams(window.location.search)
      return this.$store.getters.shouldShowDetailsTableGetter

      //return urlParams.get("show_tables") == "true" || stateInfo
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#body-container {
  margin-left: 0;
  margin-right: 0;
  height: 100vh;
  width: 100%;

  display: flex;
}
</style>

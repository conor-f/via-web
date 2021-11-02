<template>
  <div id="body-container">
    <ViaSidebar
      v-if="shouldShowSidebar"
      />

    <splitpanes
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
      return this.$store.state.shouldShowDetailsTable
    }
  },
  mounted() {
    const urlParams = new URLSearchParams(window.location.search)
    const shouldShow = urlParams.get("show_tables") == "true" || false

    this.$store.commit(
      'updateShouldShowDetailsTable',
      shouldShow
    )
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style >
#body-container {
  margin-left: 0;
  margin-right: 0;
  height: 100vh;
  width: 100%;

  display: flex;
}

.splitpanes__splitter {
  background-color: #ccc;
  position: relative;
}
.splitpanes__splitter:before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  transition: opacity 0.4s;
  background-color: rgba(50, 50, 50, 0.3);
  opacity: 0;
  z-index: 10000;
}
.splitpanes__splitter:hover:before {
  opacity: 1;
}
.splitpanes--horizontal > .splitpanes__splitter:before {top: -30px;bottom: -30px;width: 100%;}

</style>

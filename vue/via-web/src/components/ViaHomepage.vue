<template>
  <div class="row" id="body-row">
    <ViaSidebar/>
    <ViaMap/>
  </div>
  <ViaDetailTables/>
</template>

<script>
import ViaSidebar from './ViaSidebar.vue'
import ViaMap from './ViaMap.vue'
import ViaDetailTables from './ViaDetailTables.vue'

export default {
  name: 'ViaHomepage',
  components: {
    ViaSidebar,
    ViaMap,
    ViaDetailTables
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#body-row {
  margin-left: 0;
  margin-right: 0;
}
</style>

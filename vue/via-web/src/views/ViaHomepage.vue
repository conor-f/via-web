<template>
  <div id="body-container">
    <ViaSidebar
      v-if="$store.state.showSidebar"
      />

    <splitpanes
      horizontal
      >
      <pane min-size="50">
        <ViaMap
          ref="viaMapComponent"
          />
      </pane>

      <pane
        size="30"
        v-if="showDetailsTable"
        >
        <ViaDetailTables
          @detailsTableRowSegmentClick="handleDetailsTableRowSegmentClick"/>
      </pane>
    </splitpanes>
  </div>
</template>

<script>
import ViaSidebar from '../components/ViaSidebar.vue'
import ViaMap from '../components/ViaMap.vue'
import ViaDetailTables from '../components/ViaDetailTables.vue'

import { Splitpanes, Pane } from 'splitpanes'
import 'splitpanes/dist/splitpanes.css'

import { mapState } from 'vuex'


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
    return { }
  },
  computed: {
    ...mapState([
      'showSidebar',
      'showDetailsTable'
    ]),
  },
  methods: {
    handleDetailsTableRowSegmentClick(event) {
      this.$refs.viaMapComponent.highlightSegment(event)
    }
  },
  mounted() {
    this.$store.commit(
      'updateShowSidebar',
      this.$route.query.showSidebar
    )
    this.$store.commit(
      'updateShowDetailsTable',
      this.$route.query.showDetailsTable
    )

    this.$store.commit(
      'updateLat',
      parseFloat(this.$route.query.lat) 
    )
    this.$store.commit(
      'updateLng',
      parseFloat(this.$route.query.lng) 
    )
    this.$store.commit(
      'updateZoomLevel',
      parseInt(this.$route.query.zoomLevel) 
    )

    this.$store.dispatch('getGeojsonFromAPI')
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

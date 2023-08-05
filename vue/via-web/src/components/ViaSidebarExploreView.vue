<template>

  <div id="inputs_container">
    <form id="pull_journeys_form">
      <!-- Time ranges: -->
      <label for="earliest_date">
        Earliest:
      </label>
      <br/>

      <input
        type="month"
        v-model="earliestDate"
        min="2021-01"
        />
      <br/>
      <br/>

      <label for="latest_date">
        Latest:
      </label>
      <br/>

      <input
        type="month"
        v-model="latestDate"
        max="2022-12"
        />
      <br/>
      <br/>
      <!-- End time ranges -->

      <label for="selectedMetric">
        Focus Metric
      </label>
      <select
        v-model="selectedMetric"
        :style="{
          'margin-left': '10px'
        }"
      >
        <option value="quality">Quality</option>
        <option value="usage">Usage</option>
        <option value="speed">Speed</option>
      </select>

      <label for="mergeRoadSegments">
        Merge Data By Road Name
      </label>
      <input
        type="checkbox"
        v-model="mergeRoadSegments"
        :style="{
          'margin-left': '10px'
        }"
        />

      <label for="showDetailsTable">
        Show Details Table
      </label>
      <input
        type="checkbox"
        v-model="showDetailsTable"
        :style="{
          'margin-left': '10px'
        }"
        />
    </form>
  </div>

</template>

<script>
import { mapState } from 'vuex'


export default {
  name: 'ViaSidebarExploreView',
  data() {
    return {
    }
  },
  computed: {
    ...mapState([
      'earliestDate',
      'latestDate',
      'mergeRoadSegments',
      'showDetailsTable',
    ]),
    earliestDate: {
      get() {
        return this.$store.state.earliestDate
      },
      set(val) {
        this.$store.commit('updateEarliestDate', val)
        this.$store.dispatch('getGeojsonFromAPI')
      }
    },
    latestDate: {
      get() {
        return this.$store.state.latestDate
      },
      set(val) {
        this.$store.commit('updateLatestDate', val)
        this.$store.dispatch('getGeojsonFromAPI')
      }
    },
    mergeRoadSegments: {
      get() {
        return this.$store.state.mergeRoadSegments
      },
      set(val) {
        this.$store.commit('updateMergeRoadSegments', val)
      }
    },
    showDetailsTable: {
      get() {
        return this.$store.state.showDetailsTable
      },
      set(val) {
        this.$store.commit('updateShowDetailsTable', val)
      }
    },
    selectedMetric: {
      get() {
        return this.$store.state.selectedMetric
      },
      set(val) {
        this.$store.commit('updateSelectedMetric', val)
      }
    }
  },
  methods: { },
  mounted() { }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.journeyRadioButton {
  margin-left: 0.5rem;
}
</style>

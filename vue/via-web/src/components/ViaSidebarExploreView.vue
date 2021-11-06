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
        max="2023-12"
        />
      <br/>
      <br/>
      <!-- End time ranges -->

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
    showDetailsTable: {
      get() {
        return this.$store.state.showDetailsTable
      },
      set(val) {
        this.$store.commit('updateShowDetailsTable', val)
      }
    },
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

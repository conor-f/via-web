<template>
  <ViaHomepage/>
</template>

<script>
import axios from 'axios'

import ViaHomepage from './components/ViaHomepage.vue'

export default {
  name: 'App',
  components: {
    ViaHomepage
  },
  // TODO: This is messy and bad and shouldn't be done here...
  mounted() {
    const urlParams = new URLSearchParams(window.location.search)

    const earliestTime = urlParams.get("earliest_time") || "2021-01"
    const latestTime = urlParams.get("latest_time") || "2023-01"
    const journeyType = urlParams.get("journey_type") || "bike"

    axios.get(
      // TODO: This host shouldn't be hardcoded.
      "https://via-api.randombits.host/journeys/get_geojson?" +
      "earliest_time=" + earliestTime +
      "&latest_time=" + latestTime +
      "&journey_type=" + journeyType
    ).then(response => {
      // Pretty sure these shouldn't be set in this way.
      this.$store.commit('updateGeojson', response.data)
      this.$store.commit('updateTableDetails', response.data.features)
    }).catch(error => {
      console.log(error);
    })
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: left;
  color: #2c3e50;
  margin: 0px;
}
</style>

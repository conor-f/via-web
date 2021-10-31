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
    axios.get(
      "http://localhost:8081/journeys/get_geojson?earliest_time=2021-01&latest_time=2023-01&journey_type=bike"
    ).then(response => {
      this.$store.commit('updateGeojson', response.data)
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

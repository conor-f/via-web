<template>

  <div id="inputs_container">
    <form id="pull_journeys_form">
      <!-- Time ranges: -->
      <label for="earliest_date">Earliest:</label>
      <input type="month" id="earliest_date" v-model="earliestDate" min="2021-01">

      <br/><br/>

      <label for="latest_date">Latest (inclusive):</label>
      <input type="month" id="latest_date" v-model="latestDate" max="2023-12"><br/><br/>
      <!-- End time ranges -->

      <!-- Journey type: -->
      <input type="radio" id="all_journeys" v-model="journeyType" value="all">
      <label for="all">All Journeys</label><br>
      <input type="radio" checked="checked" id="bike" v-model="journeyType" value="bike">
      <label for="bike">Bike</label><br>
      <input type="radio" id="bus" v-model="journeyType" value="bus">
      <label for="bus">Bus</label><br>
      <input type="radio" id="car" v-model="journeyType" value="car">
      <label for="car">Car</label><br>
      <!-- End journey type -->

      <br/>

      <label for="showDetailsTable">Show Details Table</label>
      <input
        type="checkbox"
        id="showDetailsTable"
        v-model="showDetailsTable"
        :style="{
          'margin-left': '10px'
        }"
        @change="toggleDetailsTable"
        />

      <br/>

      <button
        type="button"
        @click="submitForm()"
        >
        Submit
      </button>
    </form>
  </div>

</template>

<script>
import axios from 'axios'

export default {
  name: 'ViaSidebarExploreView',
  data() {
    return {
      earliestDate: '2021-01',
      latestDate: '2023-01',
      journeyType: 'bike',
      // TODO: I think this is bad practice...
      showDetailsTable: false
    }
  },
  methods: {
    submitForm() {
      axios.get(
        // TODO: This should be populated intelligently.
        "https://via-api.randombits.host/journeys/get_geojson?earliest_time="
        + this.earliestDate + "&latest_time=" + this.latestDate
        + "&journey_type=" + this.journeyType,
      ).then(response => {
        this.$store.commit('updateGeojson', response.data)
      }).catch(error => {
        console.log(error);
      })
    },
    toggleDetailsTable() {
      // TODO: This is trash. Need to be using router.
      let searchParams = new URLSearchParams(window.location.search)
      if (this.showDetailsTable) {
        searchParams.set('show_tables', this.showDetailsTable)
      } else {
        searchParams.delete('show_tables')
      }

      let newurl = window.location.protocol + "//" + window.location.host + window.location.pathname + '?' + searchParams.toString()
      window.history.pushState({path: newurl}, '', newurl)

      this.$store.commit(
        'updateShouldShowDetailsTable',
        this.showDetailsTable
      )
    }
  },
  mounted() {
    this.showDetailsTable = this.$store.state.shouldShowDetailsTable
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>

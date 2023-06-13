import { createApp } from 'vue'
import { createStore } from 'vuex'
import { createRouter, createWebHistory } from 'vue-router'

import axios from 'axios'
import L from 'leaflet'

import ViaHomepage from './views/ViaHomepage.vue'


function mergeStreetGeoJson(state) {

  let roadQualitiesMap = {};

  state.geojsonResponse.features.forEach((thing) => {
    if (Object.prototype.hasOwnProperty.call(roadQualitiesMap, thing.properties.name)) {
      roadQualitiesMap[thing.properties.name].qualities.push(thing.properties.avg);
      roadQualitiesMap[thing.properties.name].usages.push(thing.properties.count);
      roadQualitiesMap[thing.properties.name].speeds.push(thing.properties.speed);
    } else {
      roadQualitiesMap[thing.properties.name] = {
        qualities: [thing.properties.avg],
        usages: [thing.properties.count],
        speeds: [thing.properties.speed]
      };
    }
  });

  const average = array => array.reduce((a, b) => a + b) / array.length;

  state.geojsonResponse.features.forEach((feature) => {
    if (feature.properties.name !== undefined) {
      feature.properties.count = Math.max.apply(null, roadQualitiesMap[feature.properties.name].usages);
      if (average(roadQualitiesMap[feature.properties.name].speeds) != 0) {
        // No speeds given, dirty way of doing this
        feature.properties.speed = average(roadQualitiesMap[feature.properties.name].speeds);
      }
      feature.properties.avg = average(roadQualitiesMap[feature.properties.name].qualities);
    }
  });
}


function updateURLHelper(state) {
  const url = new URL(window.location)

  url.searchParams.set(
    'showDetailsTable',
    state.showDetailsTable
  )
  url.searchParams.set(
    'selectedMetric',
    state.selectedMetric
  )
  url.searchParams.set(
    'earliestDate',
    state.earliestDate
  )
  url.searchParams.set(
    'latestDate',
    state.latestDate
  )
  url.searchParams.set(
    'lat',
    state.lat
  )
  url.searchParams.set(
    'lng',
    state.lng
  )
  url.searchParams.set(
    'zoomLevel',
    state.zoomLevel
  )

  history.pushState('', 'Via - Road Quality Analysis', url);
}

const store = createStore({
  state() {
    return {
      // UI Controllers:
      showSidebar: null,
      showDetailsTable: null,
      selectedMetric: 'quality',

      // Form Values:
      earliestDate: '2021-01',
      latestDate: '2022-12',

      // Map Details:
      lat: 53.35,
      lng: -6.28,
      zoomLevel: 12,
      latLngBounds: null, // This is the North-West and South-East LatLng.

      // Computed Results:
      geojsonResponse: null,  // Used for the map layer.
      tableDetails: null  // Filtered version of the response for the table.
    }
  },
  mutations: {
    updateShowSidebar(state, val) {
      // Return true if val is unset or anything not falsey.
      if (val !== undefined && (val == 'false' || !val)) {
        state.showSidebar = false
      } else {
        state.showSidebar = true
      }
    },
    updateShowDetailsTable(state, val) {
      if (val == 'false' || !val) {
        state.showDetailsTable = false
      } else {
        state.showDetailsTable = true
      }
      updateURLHelper(state)
    },
    updateSelectedMetric(state, val) {
      state.selectedMetric = val
      updateURLHelper(state)
      state.geojsonResponse = JSON.parse(JSON.stringify(state.geojsonResponse))
      mergeStreetGeoJson(state);
    },
    updateEarliestDate(state, val) {
      state.earliestDate = val
      updateURLHelper(state)
    },
    updateLatestDate(state, val) {
      state.latestDate = val
      updateURLHelper(state)
    },
    updateLat(state, val) {
      if (!Number.isNaN(val)) {
        state.lat = val
        updateURLHelper(state)
      }
    },
    updateLng(state, val) {
      if (!Number.isNaN(val)) {
        state.lng = val
        updateURLHelper(state)
      }
    },
    updateZoomLevel(state, val) {
      if (!Number.isNaN(val)) {
        state.zoomLevel = val
        updateURLHelper(state)
      }
    },
    updateLatLngBounds(state, val) {
      state.latLngBounds = val
    },
    updateGeojson(state, geojsonResponse) {
      state.geojsonResponse = geojsonResponse
      mergeStreetGeoJson(state);
    },
    updateTableDetails(state, tableDetails) {
      state.tableDetails = tableDetails
    },
  },
  actions: {
    getGeojsonFromAPI({commit, state, dispatch}) {
      axios.get(
        // TODO: This should be populated even more intelligently haha...
        process.env.API_URL + "/get_geojson?earliest_time="
        + state.earliestDate + "&latest_time=" + state.latestDate
      ).then(response => {
        console.log("Looking for the API? This is the raw data you can use! Get in touch on Github if you want more details:")
        console.log(response.data)

        commit('updateGeojson', response.data)
        dispatch('filterTableDetails')
      }).catch(error => {
        console.log(error);
      })
    },
    filterTableDetails({commit, state}) {
      if (state.geojsonResponse === null) {
        return;
      }
      let filteredDetails = state.geojsonResponse.features.filter((f) => {
        // TODO: This looks like a bug in vue-leaflet. Mixed up coords.
        let p = L.latLng(
          f.geometry.coordinates[0][1],
          f.geometry.coordinates[0][0]
        )

        if (state.latLngBounds == null) {
          return true
        }

        // TODO: This contains method looks visually incorrect.
        return state.latLngBounds.contains(p)
      })

      commit('updateTableDetails', filteredDetails)
    }
  },
})

const routes = [
  {
    path: '/',
    name: 'Home',
    component: ViaHomepage,
    // TODO: This only lets us see the params as route properties, not
    // component props...
    props: true
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes: routes
})

import App from './App.vue'

import PrimeVue from 'primevue/config'
import DataTable from 'primevue/datatable'
import Column from 'primevue/column'
import InputText from 'primevue/inputtext'

import 'primevue/resources/themes/saga-blue/theme.css'
import 'primevue/resources/primevue.min.css'
import 'primeicons/primeicons.css'

const app = createApp(App)

app.use(store)
app.use(router)
app.use(PrimeVue)

app.component('DataTable', DataTable)
app.component('Column', Column)
app.component('InputText', InputText)

app.mount('#app')

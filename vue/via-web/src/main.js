import { createApp } from 'vue'
import { createStore } from 'vuex'

const store = createStore({
  state () {
    return {
      geojsonResponse: null,
      tableDetails: null,
      shouldShowDetailsTable: false
    }
  },
  mutations: {
    updateGeojson(state, geojsonResponse) {
      state.geojsonResponse = geojsonResponse
    },
    updateTableDetails(state, tableDetails) {
      state.tableDetails = tableDetails
    },
    updateShouldShowDetailsTable(state, val) {
      state.shouldShowDetailsTable = val
    }
  },
  getters: {
    geojsonResponseGetter: state => {
      return state.geojsonResponse
    },
    tableDetailsGetter: state => {
      return state.tableDetails
    },
    shouldShowDetailsTableGetter: state => {
      return state.shouldShowDetailsTable
    }
  }
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
app.use(PrimeVue)

app.component('DataTable', DataTable)
app.component('Column', Column)
app.component('InputText', InputText)

app.mount('#app')

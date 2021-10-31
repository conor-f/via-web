import { createApp } from 'vue'
import { createStore } from 'vuex'

const store = createStore({
  state () {
    return {
      geojsonResponse: null
    }
  },
  mutations: {
    updateGeojson(state, geojsonResponse) {
      state.geojsonResponse = geojsonResponse
    }
  }
})

import App from './App.vue'

const app = createApp(App)
app.use(store)

app.mount('#app')

<template>
  <div id="map-container">
    <div id="map-div">
      <l-map
        v-model="zoom"
        v-model:zoom="zoom"
        :center="[53.35, -6.26]"
        :zoomAnimation="true"
        >
        <l-tile-layer
          url="https://api.mapbox.com/styles/v1/mapbox/streets-v11/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoicGhvbmVtYW4iLCJhIjoiY2tzazlwendiMDZ3NTJvcG50dzBlZDIzZCJ9.L0wR8vdrRgO4RQR6yLF6UA"
          id="mapbox/streets-v11"
          :tileSize="512"
          :options="{
            zoomOffset: -1
          }"
          attribution='Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>'
          />
        <l-geo-json
          :geojson="geojsonLayer"
          :options="geojsonOptions"
          />
      </l-map>
    </div>
  </div>
</template>

<script>
import "leaflet/dist/leaflet.css";

import {
  LMap,
  LTileLayer,
  LGeoJson
} from "@vue-leaflet/vue-leaflet";


export default {
  name: 'ViaMap',
  components: {
    LMap,
    LTileLayer,
    LGeoJson,
  },
  data() {
    return {
      zoom: 12,
      geojsonOptions: {
        style: this.geojsonStyle,
        onEachFeature: this.geojsonOnEachFeature
      }
    };
  },
  methods: {
    geojsonStyle(feature) {
      return {
        color: this.getColour(
          Math.max.apply(
            Math,
            [feature.properties.avg],
            50
          ) / 50
        ),
        weight: 5.5
      }
    },
    getColour(value) {
      var hue = ((1 - value) * 120).toString(10);
      return [ "hsl(", hue, ", 100%, 50%)" ].join("");
    },
    geojsonOnEachFeature(feature, layer) {
      // A general method run on each feature. These bind popups for on
      // layer click (default) and also on mouseover/out. Just the road
      // name for now which isn't always populated.

      layer.bindPopup(
        "<h4 style='text-align: center'>Details:</h3>" +
        "Road Name: " + feature.properties.name + "<br/>" +
        "Quality: " + feature.properties.avg
      )

      // const popup = new ViaMapRoadPopup()
      // layer.bindPopup(popup.$mount().$el)

      layer.on('mouseover', function() {
        this.openPopup()
      })

      layer.on('mouseout', function() {
        this.closePopup()
      })
    }
  },
  computed: {
    geojsonLayer() {
      return this.$store.state.geojsonResponse
    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#map-container {
  padding-right: 0;
  padding-left: 0;

  width: 100%;
  height: 100%;
}

#map-div {
  width: 100%;
  height: 100%;
}
</style>

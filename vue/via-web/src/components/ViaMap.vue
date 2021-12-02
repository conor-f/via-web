<template>
  <div id="map-container">
    <div id="map-div">
      <l-map
        v-model="zoomLevel"
        v-model:zoom="zoomLevel"
        :zoomAnimation="true"
        @update:bounds="mapMoveHandler"
        @move="mapMoveHandler"
        @ready="mapReadyHandler"
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
        <l-polyline
          :lat-lngs="coordsToHighlight"
          color="royalblue"
          :weight="highlightedSegmentWeight"
          :opacity="highlightedSegmentOpacity"
          :zIndex="3"
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
  LGeoJson,
  LPolyline
} from "@vue-leaflet/vue-leaflet";

import { mapState } from 'vuex'


export default {
  name: 'ViaMap',
  components: {
    LMap,
    LTileLayer,
    LGeoJson,
    LPolyline
  },
  data() {
    return {
      geojsonOptions: {
        style: this.geojsonStyle,
        onEachFeature: this.geojsonOnEachFeature
      },
      coordsToHighlight: [],
      showHighlightedSegment: false,
      highlightedSegmentOpacity: 1.0,
      highlightedSegmentWeight: 30.0
    };
  },
  methods: {
    geojsonStyle(feature) {
      let minVal = 20
      let maxVal = 60
      let percent = 100 * ((feature.properties.avg - minVal) / (maxVal - minVal))

      if (this.$store.state.selectedMetric == 'quality') {
        minVal = 0
        maxVal = 50
        percent = 100 * ((feature.properties.avg - minVal) / (maxVal - minVal))
      }
      if (this.$store.state.selectedMetric == 'usage') {
        minVal = 0
        maxVal = 2
        percent = 100 * ((feature.properties.count - minVal) / (maxVal - minVal))
      }
      if (this.$store.state.selectedMetric == 'speed') {
        minVal = 0
        maxVal = 10
        percent = 100 * ((feature.properties.speed - minVal) / (maxVal - minVal))
      }
      if (this.$store.state.selectedMetric == 'danger') {
        minVal = 0
        maxVal = 2
        percent = 100 * (1 - 
          ((feature.properties.collisions.length - minVal) / (maxVal - minVal))
        )
      }

      return {
        color: this.getColour(percent),
        weight: 125 * (1.0 / this.zoomLevel)
      }
    },
    getColour(value) {
      return [ "hsl(", value, ", 100%, 50%)" ].join("");
    },
    geojsonOnEachFeature(feature, layer) {
      // A general method run on each feature. These bind popups for on
      // layer click (default) and also on mouseover/out. Just the road
      // name for now which isn't always populated.
      function getCollisionsText(collisions) {
        if (collisions.length == 0) {
          return "No collisions."
        }

        let collisionsText = "Collisions (" + collisions.length + "):<br/>"

        for (let collision of collisions) {
          collisionsText += "<ul>"
          collisionsText += "<li>Time of Day: "
          collisionsText += collision.hour
          collisionsText += "</li>"
          collisionsText += "<li>Fatalities: "
          collisionsText += collision.num_fatal
          collisionsText += "</li>"
          collisionsText += "<li>Minor Injuries: "
          collisionsText += collision.num_minor
          collisionsText += "</li>"
          collisionsText += "<li>Serious Injuries: "
          collisionsText += collision.num_serious
          collisionsText += "</li>"
          collisionsText += "<li>Severity: "
          collisionsText += collision.severity
          collisionsText += "</li>"
          collisionsText += "</ul>"
        }

        return collisionsText
      }

      layer.bindPopup(
        "<h4 style='text-align: center'>Details:</h3>" +
        "Road Name: " + feature.properties.name + "<br/>" +
        "Quality: " + feature.properties.avg + "<br/>" +
        "Speed: " + (3.6 * parseFloat(feature.properties.speed)).toPrecision(2) + " km/h <br/>" +
        "Usage: " + feature.properties.count + "<br/>" +
        getCollisionsText(feature.properties.collisions)
      )

      // TODO: Can't find a way to make the component popup.
      // const popup = new ViaMapRoadPopup()
      // layer.bindPopup(popup.$mount().$el)

      layer.on('mouseover', function() {
        this.openPopup()
      })

      layer.on('mouseout', function() {
        this.closePopup()
      })
    },
    mapReadyHandler(event) {
      // event.flyTo(
      event.setView(
        {
          lat: this.lat,
          lng: this.lng
        },
        this.zoomLevel
      )
    },
    mapMoveHandler(event) {
      if (typeof(event.getBounds) === 'function') {
        this.$store.commit('updateLatLngBounds', event.getBounds())
        this.$store.commit('updateLat', event.getCenter().lat)
        this.$store.commit('updateLng', event.getCenter().lng)
      } else if (
        typeof(event.target) !== 'undefined' &&
        typeof(event.target.getBounds) === 'function'
      ) {
        this.$store.commit('updateLatLngBounds', event.target.getBounds())
        this.$store.commit('updateLat', event.target.getCenter().lat)
        this.$store.commit('updateLng', event.target.getCenter().lng)
      } else {
        this.$store.commit('updateLatLngBounds', event)
      }

      // FIXME: This happens too frequently, if click and drag moving
      // and are zoomed out a lot things slow down to a crawl
      this.$store.dispatch('filterTableDetails')
    },
    fadeOutHighlightedSegment(opacity=1) {
      if (opacity > 0) {
        opacity -= 0.05

        this.highlightedSegmentOpacity = opacity
        this.highlightedSegmentWeight = opacity * 30

        setTimeout( () => {
          this.fadeOutHighlightedSegment(opacity)
        }, 100)
      } else {
        this.showHighlightedSegment = false;
      }
    },
    highlightSegment(event) {
      let coords = Array()

      for (let point of event.segmentGeometry) {
        coords.push(
          Array(point[0][1], point[0][0]),
          Array(point[1][1], point[1][0])
        )
      }

      this.coordsToHighlight = coords

      this.showHighlightedSegment = true
      this.fadeOutHighlightedSegment()
    }
  },
  computed: {
    ...mapState([
      'lat',
      'lng',
      'zoomLevel',
      'geojsonResponse',
    ]),
    lat: {
      get() {
        return this.$store.state.lat
      },
      set(val) {
        this.$store.commit('updateLat', parseFloat(val))
      }
    },
    lng: {
      get() {
        return this.$store.state.lng
      },
      set(val) {
        this.$store.commit('updateLng', parseFloat(val))
      }
    },
    zoomLevel: {
      get() {
        return this.$store.state.zoomLevel
      },
      set(val) {
        this.$store.commit('updateZoomLevel', val)
      }
    },
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

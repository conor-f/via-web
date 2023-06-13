<template>
  <div id="examplesContainer">
    <p>
      These quick links will showcase the different ways you can explore data
      with Via. At any point you can copy the URL in the address bar and share
      it with someone and they will see the exact same content you are.
    </p>
    <ul>
      <li>
        <a href="?showDetailsTable=false&selectedMetric=speed&earliestDate=2021-01&latestDate=2022-12&lat=53.33544106215165&lng=-6.268184297104635&zoomLevel=16">South Circular Road Speed</a>
      </li>
      <li>
        <a href="?showDetailsTable=true&selectedMetric=quality&earliestDate=2021-01&latestDate=2022-12&lat=53.33028999762885&lng=-6.2530673670966985&zoomLevel=16">Grand Canal Cycle Lane Quality</a>
      </li>
      <li>
        <a href="?showDetailsTable=true&selectedMetric=usage&earliestDate=2021-01&latestDate=2022-12&lat=53.33471863080541&lng=-6.2694597244262695&zoomLevel=15">Most Used Roads</a>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'ViaSidebarExamplesView',
  data() { },
  computed: { },
  methods: { },
  mounted() { }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>

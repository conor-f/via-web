<template>
  <DataTable
    :value="formattedRows"
    :showGridLines="true"
    :autoLayout="true"
    :rowHover="true"
    responsiveLayout="scroll"
    :scrollable="true"
    scrollDirection="both"
    :stripedRows="true"
    scrollHeight="flex"
    v-model:filters="filters"
    filterDisplay="menu"
    @row-click="handleRowClick"
    >
    <Column
      field="segment"
      header="Segment"
      :style="{width: '40%'}"
      :showFilterMenu="true"
      :showClearButton="true"
      >
      <template #filter="{ filterModel, filterCallback }">
        <InputText
          type="text"
          v-model="filterModel.value"
          @input="filterCallback()"
          />
      </template>
    </Column>
    <Column
      field="quality"
      header="Quality"
      :sortable="true"
      :style="{width: '15%'}"
      />
    <Column
      field="usage"
      header="Usage"
      :sortable="true"
      :style="{width: '15%'}"
      />
    <Column
      field="speed"
      header="Speed"
      :sortable="true"
      :style="{width: '15%'}"
      />
  </DataTable>
</template>

<script>
import { FilterMatchMode } from "primevue/api";

export default {
  name: 'ViaDetailTables',
  components: {
  },
  data() {
    return {
      filters: {
        global: {
          value: null,
          matchMode: FilterMatchMode.CONTAINS
        },
        segment: {
          value: null,
          matchMode: FilterMatchMode.CONTAINS
        }
      }
    }
  },
  computed: {
    formattedRows() {
      let a = this.$store.state.tableDetails

      if (a == null) {
        return []
      }

      let returnMe = []
      for (let e of a) {
        if (
          e.properties.name == '' ||
          e.properties.name == null ||
          e.properties.name.toString().includes(',') ||
          isNaN(parseInt(e.properties.avg)) ||
          isNaN(parseInt(e.properties.count)) ||
          isNaN(parseFloat(e.properties.speed))
        ) {
          continue
        }

        returnMe.push({
          'segment': e.properties.name,
          'quality': parseInt(e.properties.avg),
          'usage': parseInt(e.properties.count),
          'speed': parseFloat(e.properties.speed).toPrecision(2),
          'startCoords': e.geometry.coordinates[0],
          'endCoords': e.geometry.coordinates[1],
        })
      }

      var groupedByRoadName = returnMe.reduce(function (r, a) {
          r[a.segment] = r[a.segment] || [];
          r[a.segment].push(a);
          return r;
      }, Object.create(null));

      const average = (array) => array.reduce((a, b) => a + b) / array.length;

      var groupedStats = [];
      for (var items in groupedByRoadName) {
        var props = groupedByRoadName[items];
        var qualities = props.map(function (currentElement) {
          return currentElement['quality']
        })
        var usages = props.map(function (currentElement) {
          return currentElement['usage']
        })
        var speeds = props.map(function (currentElement) {
          return parseFloat(currentElement['speed'])
        })
        var geometry = props.map(function (currentElement) {
          return [
            currentElement['startCoords'],
            currentElement['endCoords']
          ]
        })

        groupedStats.push({
          'quality': average(qualities).toPrecision(2),
          'usage': usages.reduce(function(a, b) {
            return Math.max(a, b);
          }, 0),
          'segment': items,
          'speed': (average(speeds) * 3.6).toPrecision(2),  // m/s -> km/h
          'geometry': geometry
        });
      }

      return groupedStats;
    }
  },
  methods: {
    handleRowClick(event) {
      this.$emit(
        'detailsTableRowSegmentClick',
        {
          segmentGeometry: event.data.geometry
        }
      )
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.p-column-filter-matchmode-dropdown {
  display: none !important;
}
</style>

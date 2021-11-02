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
      field="quality"
      header="Speed"
      :sortable="true"
      :style="{width: '15%'}"
      />
    <Column
      field="usage"
      header="Traffic Incidents"
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
      let a = this.$store.state.geojsonResponse

      if (a == null) {
        return []
      }

      let returnMe = []
      for (let e of a.features) {
        if (
          e.properties.name == '' ||
          e.properties.name == null ||
          e.properties.name.toString().includes(',') ||
          isNaN(parseInt(e.properties.avg)) ||
          isNaN(parseInt(e.properties.count))
        ) {
          continue
        }

        returnMe.push({
          'segment': e.properties.name,
          'quality': parseInt(e.properties.avg),
          'usage': parseInt(e.properties.count)
        })
      }

      return returnMe
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

<template>
  <!-- Collapsed -->
  <span
    v-if="!isExpanded && !isCustomIcon"
    class="fa fa-2x fa-fw"
    :class="collapsedIcon"
  >
  </span>

  <span v-if="!isExpanded && isCustomIcon">
    <img :src="collapsedIcon" height="30" width="30" />
  </span>

  <!-- Expanded -->
  <span
    v-if="isExpanded && !isCustomIcon"
    class="fa fa-2x fa-fw mr-3"
    :class="expandedIcon"
  >
  </span>

  <span v-if="isExpanded && isCustomIcon" class="mr-3">
    <img :src="expandedIcon" height="30" width="30" class="mr-3" />
  </span>
</template>

<script>
export default {
  name: "ViaSidebarItemIcon",
  props: {
    collapsedIcon: {
      required: true,
    },
    expandedIcon: {
      default: (props) => props.collapsedIcon,
    },
    isCustomIcon: {
      type: Boolean,
    },
    isExpanded: {
      required: true,
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>

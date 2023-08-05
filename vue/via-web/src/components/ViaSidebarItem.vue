<template>
  <div class="bg-dark list-group-item list-group-item-action">
    <div class="d-flex w-100 justify-content-start align-items-center">
      <!-- Icon -->
      <ViaSidebarItemIcon
        :collapsedIcon="collapsedIcon"
        :expandedIcon="expandedIcon"
        :isCustomIcon="isCustomIcon"
        :isExpanded="isExpanded"
      />

      <!-- Expanded menu text (and subcontent indicator) -->
      <span
        v-if="isExpanded"
        class="mr-3"
        :class="{
          'subcontent-expanded': hasSubContent && shouldShowSlot,
          'subcontent-collapsed': hasSubContent && !shouldShowSlot,
        }"
        @click="handleMenuItemClick()"
      >
        {{ expandedText }}
      </span>
    </div>

    <!-- Subcontent -->
    <div
      v-if="isExpanded && hasSubContent && shouldShowSlot"
      class="subcontent"
    >
      <slot />
    </div>
  </div>
</template>

<script>
import ViaSidebarItemIcon from "./ViaSidebarItemIcon.vue";

export default {
  name: "ViaSidebarItem",
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
    expandedText: {
      required: true,
    },
    isExpanded: {
      required: true,
    },
    hasSubContent: {
      type: Boolean,
    },
    href: {
      default: "",
    },
  },
  data() {
    return {
      shouldShowSlot: false,
    };
  },
  methods: {
    toggleShowSlot() {
      this.shouldShowSlot = this.hasSubContent && !this.shouldShowSlot;
    },
    handleMenuItemClick() {
      if (this.href != "") {
        window.location.href = this.href;
      }
      if (!this.hasSubContent) {
        return;
      } else {
        this.toggleShowSlot();
      }
    },
  },
  components: {
    ViaSidebarItemIcon,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.list-group-item {
  color: white;
}

.list-group-item:hover {
  background-color: #1d2124 !important;
}

.subcontent-collapsed::after {
  content: "\f0d7";
  font-family: FontAwesome;
  display: inline;
  text-align: right;
  padding-left: 10px;
}

.subcontent-expanded::after {
  content: "\f0da";
  font-family: FontAwesome;
  display: inline;
  text-align: right;
  padding-left: 10px;
  padding-right: 10px;
}

.subcontent {
  height: auto;
  padding-top: 20px;
  padding-left: 30px;
  font-size: 0.9rem;
  width: 260px;
}
</style>

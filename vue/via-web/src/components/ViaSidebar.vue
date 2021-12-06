<template>
  <div
    id="via-sidebar"
    class="d-none d-md-block"
    :class="{'sidebar-expanded': isExpanded, 'sidebar-collapsed': !isExpanded}"
    >
    <ul class="list-group">
      <ViaSidebarItem
        collapsedIcon="fa-angle-double-right"
        expandedIcon="fa-angle-double-left"
        expandedText="Collapse"
        :isExpanded="isExpanded"
        @click="toggleIsExpanded()"
        >
      </ViaSidebarItem>

      <ViaSidebarItem
        collapsedIcon="/logo.png"
        isCustomIcon
        expandedText="About"
        :isExpanded="isExpanded"
        hasSubContent
        >
        <p>
          Via is a way to monitor road safety for cyclists.
        </p>
        <p>
          It has a strong emphasis on privacy, with no personally
          identifiable information being stored or transmitted, and
          all default options offering strong protections.
          For example, Via will not share the time of day, the
          beginning or end points of a journey or any means of
          linking one journey to another by default.
        </p>
        <p>
          If you want to help have a more transparent, complete
          coverage of cycling road quaity, you can download the
          app <a class="plain-link" style="display: inline" href="https://github.com/RobertLucey/via-app/releases/latest">here</a>.
        </p>
      </ViaSidebarItem>

      <ViaSidebarItem
        collapsedIcon="fa-search"
        expandedText="Explore"
        :isExpanded="isExpanded"
        hasSubContent
        >
        <ViaSidebarExploreView/>
      </ViaSidebarItem>

      <ViaSidebarItem
        collapsedIcon="fa-lightbulb-o"
        expandedText="Examples"
        :isExpanded="isExpanded"
        hasSubContent
        >
        <ViaSidebarExamplesView/>
      </ViaSidebarItem>

      <ViaSidebarItem
        collapsedIcon="fa-twitter"
        expandedText="Tweet"
        :isExpanded="isExpanded"
        href="https://twitter.com/intent/tweet?text=Check%20out%20Via%20-%20It%27s%20visualizing%20road%20quality%20for%20cyclists%3A%20https%3A%2F%2Fviaroads.com"
        >
      </ViaSidebarItem>

      <ViaSidebarItem
        collapsedIcon="fa-github"
        expandedText="Contribute"
        :isExpanded="isExpanded"
        href="https://github.com/conor-f/via-web"
        >
      </ViaSidebarItem>
    </ul>
  </div>
</template>

<script>
import ViaSidebarItem from './ViaSidebarItem.vue'
import ViaSidebarExploreView from './ViaSidebarExploreView.vue'
import ViaSidebarExamplesView from './ViaSidebarExamplesView.vue'

export default {
  name: 'ViaSidebar',
  data() {
    return {
      isExpanded: false
    }
  },
  methods: {
    toggleIsExpanded() {
      this.isExpanded = !this.isExpanded;
    }
  },
  components: {
    ViaSidebarItem,
    ViaSidebarExploreView,
    ViaSidebarExamplesView,
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#via-sidebar {
  min-height: 100vh;
  background-color: #333;
  padding: 0;
}

.sidebar-expanded {
  /*
  width: 230px;
  max-width: 230px;*/
}

.sidebar-collapsed {
  /*width: 60px;*/
}
</style>

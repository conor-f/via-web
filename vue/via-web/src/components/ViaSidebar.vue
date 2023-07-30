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
          With a strong emphasis on privacy, the <a
            href="https://github.com/RobertLucey/via-app/releases/latest">Via
            app</a> calculates the quality of roads you cycle on and allows
          them to be aggregated with all other journeys so you can get a full
          view of what roads cyclists use, what condition the roads are in and how
          efficient different routes are.
        </p>
        <p>
          Feel free to start exploring by expanding the Explore tab below,
          or use the Examples section to see some interesting default views.
          <a href="mailto:via@randombits.host">Get in touch</a> for any and all
          feedback or to get more details about the project.
        </p>
        <p>
          If you want to help have a more transparent, complete
          coverage of cycling road quaity, you can download the
          app <a href="https://github.com/RobertLucey/via-app/releases/latest">here</a>.
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

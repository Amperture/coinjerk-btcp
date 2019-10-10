<template>
  <div>
    <v-navigation-drawer
      v-model="navDrawer.model"
      bottom
      clipped
      app
    ></v-navigation-drawer>
    <v-app-bar
      clipped-left
      dark
      color="accent"
      app
    >
        <v-app-bar-nav-icon
          v-if="navDrawer.type !== 'permanent'"
          @click.stop="navDrawer.model = !navDrawer.model"
        ></v-app-bar-nav-icon>
        <img 
          src="@/assets/coinjerk-header.png"
          style="max-height:100%"
          @click="$router.push('/')"
        />
        <div class='flex-grow-1'></div>
        <v-switch
          v-model="$vuetify.theme.dark"
          color="primary"
          prepend-icon="mdi-brightness-7"
          append-icon="mdi-brightness-3"
          hide-details
        ></v-switch>
    </v-app-bar>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'header-bar',

  components: {
  },

  data: () => ({
    navDrawer: {
      model: null,
      clipped: true,
      floating: false,
      mini: false,
    },
  })
}
</script>

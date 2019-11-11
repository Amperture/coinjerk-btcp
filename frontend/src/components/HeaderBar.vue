<template>
  <div>
    <v-navigation-drawer
      v-model="navDrawer.model"
      bottom
      clipped
      app
    >
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="title">
            CoinJerk
          </v-list-item-title>
          <v-list-item-subtitle>
            Accept Tips in Bitcoin,
          </v-list-item-subtitle>
          <v-list-item-subtitle>
            Lightning,
          </v-list-item-subtitle>
          <v-list-item-subtitle>
            and other Cryptocurrency!
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list
        v-if='isAuthenticated'
        dense
        nav
        >
        <v-list-item
          v-for="item in loginItems"
          :key="item.title"
          link
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
      <v-list
        dense
        nav
        >
        <v-list-item
          v-for="item in standardItems"
          :key="item.title"
          link
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar
      clipped-left
      dark
      color="accent"
      app
    >
        <v-app-bar-nav-icon
          @click.stop="navDrawer.model = !navDrawer.model"
        ></v-app-bar-nav-icon>
        <img 
          src="@/assets/coinjerk-header-stroke.png"
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
        <LoginDialog
          v-if="!isAuthenticated"
        />
    </v-app-bar>
  </div>
</template>

<script>
// @ is an alias to /src
import LoginDialog from '@/components/LoginDialog'
import { mapGetters } from 'vuex'

export default {
  name: 'header-bar',

  components: {
    LoginDialog,
  },

  computed: {
    ...mapGetters(['isAuthenticated'])
  }, 

  data: () => ({
    navDrawer: {
      model: null,
      clipped: true,
      floating: false,
      mini: false,
    },
    loginItems: [
      { title: 'Dashboard', icon: 'mdi-view-dashboard' },
      { title: 'Tips', icon: 'mdi-bitcoin' },
      { title: 'User Settings', icon: 'mdi-settings' },
    ],
    standardItems: [
      { title: 'About', icon: 'mdi-help-circle' },
    ],
    adminItems: [
      { title: 'Admin Panel', icon: 'mdi-view-dashboard-variant' },
    ],
    logoutItems: [
      { title: 'Get Started', icon: 'mdi-login-variant' },
    ],
  })
}
</script>

<template>
  <div class="text-center">
    <v-dialog
      persistent
      v-model="dialog"
      width="500"
    >
      <template v-slot:activator="{ on }">
        <v-btn
          class='mx-4'
          v-on="on"
          dark
        >
        Get Started!
        </v-btn>
      </template>

      <v-card>
        <v-tabs
          v-model="tab"
          class="elevation-2"
          dark
          centered
          grow
        >
          <v-tabs-slider></v-tabs-slider>

          <v-tab
            key="login"
            href="#tab-login"
          >
            Login
          </v-tab>

          <v-tab
            key="signup"
            href="#tab-signup"
          >
            Signup
          </v-tab>

          <v-tab-item
            key="login"
            value="tab-login"
          >
            <v-card
              flat
              tile
            >
              <LoginCard/>
            </v-card>
          </v-tab-item>

          <v-tab-item
            key="signup"
            value="tab-signup"
          >
            <v-card
              flat
              tile
            >
              <v-card-text>dingle card</v-card-text>
            </v-card>
          </v-tab-item>

        </v-tabs>
        <v-btn color="blue darken-1" text @click="dialog = false">Close</v-btn>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import LoginCard from '@/components/LoginCard'

export default {
  components: {
    LoginCard,
  },

  data: () => ({
      dialog: false,
      tab: null,
      tabs: 2,
  }),
}
</script>

<style>
</style>

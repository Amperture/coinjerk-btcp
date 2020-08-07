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
            <LoginCard
              @closedialog='dialog = false'
            />
          </v-tab-item>

          <v-tab-item
            key="signup"
            value="tab-signup"
          >
            <RegisterCard
              @closedialog='dialog = false'
            />
          </v-tab-item>

        </v-tabs>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import LoginCard from '@/components/LoginCard'
import RegisterCard from '@/components/RegisterCard'

export default {
  components: {
    LoginCard, RegisterCard
  },

  data: () => ({
      dialog: false,
      tab: null,
      tabs: 2,
  }),

  methods: {
    closeDialog(){
      this.dialog = false;
    }, 
  },
}
</script>

<style>
</style>

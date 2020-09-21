<template>
  <v-app>
    <HeaderBar/>
    <v-content>
      <router-view/>
    </v-content>
  </v-app>
</template>

<script>
import HeaderBar from '@/components/HeaderBar.vue';

export default {
  name: 'App',
  created() {
    this.$store.dispatch('auth/getRegistrationEnabled')
    console.log('%cIs Registration Enabled?',
      'color: green; background: black; font-weight:bold')
  },
  components: {
    HeaderBar,
  },
  data: () => ({
    //
  }),
};
</script>

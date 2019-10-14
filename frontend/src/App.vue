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
  components: {
    HeaderBar,
  },
  data: () => ({
    //
  }),
};
</script>

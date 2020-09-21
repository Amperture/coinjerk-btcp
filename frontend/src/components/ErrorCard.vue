<template>
  <v-card>
    <v-toolbar dense>
      <v-toolbar-title>Oh no! There was an error!</v-toolbar-title>
      <v-spacer></v-spacer>
    </v-toolbar>
    <v-card-title>
      {{ error_code }}
    </v-card-title>
  </v-card>
</template>

<script>
  export default {
    props: {
      error_code: String,
    },
  }
</script>

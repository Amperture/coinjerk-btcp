<template>
  <div>
    <v-container>
      <BTCPayConnectorChecker/>
    </v-container>
  </div>
</template>

<script>
import BTCPayConnectorChecker from '@/components/BTCPayConnectorChecker'

export default {
    name: 'dashboard',

    components: {
        BTCPayConnectorChecker
    }, 

    data: () => ({
    }),
}
</script>

<style>
</style>

<template>
  <div>
    <v-container>
      <BTCPayConnectorChecker/>
      <StreamElementsConnectorChecker/>
    </v-container>
  </div>
</template>

<script>
import BTCPayConnectorChecker from '@/components/BTCPayConnectorChecker'
import StreamElementsConnectorChecker from '@/components/StreamElementsConnectorChecker'

export default {
    name: 'dashboard',

    components: {
        BTCPayConnectorChecker, 
        StreamElementsConnectorChecker 
    }, 

    data: () => ({
    }),
}
</script>

<style>
</style>

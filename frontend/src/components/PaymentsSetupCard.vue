<template>
  <v-card>
    <v-card-title>
      Payment Processor Setup
    </v-card-title>
    <v-card-subtitle>
      Payment Processor: {{ server_host }}
    </v-card-subtitle>
    <v-card-text>
      <PaymentsSetupBTCPayDialog/>
    </v-card-text>
  </v-card>
</template>

<script>
import { mapState } from 'vuex'
import PaymentsSetupBTCPayDialog from '@/components/PaymentsSetupBTCPayDialog'

export default {
  components: {
    PaymentsSetupBTCPayDialog,
  },
  computed: mapState({
    server_host: state => state.payments.server_host,
  }),

  created () {
    this.$store.dispatch('payments/getSetupPaymentProcessor')
  }
}
</script>

<style>
</style>

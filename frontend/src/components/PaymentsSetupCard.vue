<template>
  <v-card>
    <v-card-title>
      Payment Processor Setup
    </v-card-title>
    <v-card-subtitle>
      Payment Processor: {{ payment_setup_type }}
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
    payment_setup_type: state => state.payments.payment_setup_type,
  }),

  created () {
    this.$store.dispatch('alerts/getSetupPaymentProcessor')
  }
}
</script>

<style>
</style>

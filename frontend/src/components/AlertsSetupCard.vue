<template>
  <v-card>
    <v-card-title>
      Alert Service Setup
    </v-card-title>
    <v-card-subtitle>
      Alert Account Type: {{ alert_account_type }}
    </v-card-subtitle>
    <v-card-text>
      <AlertsSetupStreamelementsDialog/>
    </v-card-text>
  </v-card>
</template>

<script>
import { mapState } from 'vuex'
import AlertsSetupStreamelementsDialog from '@/components/AlertsSetupStreamelementsDialog'

export default {
  components: {
    AlertsSetupStreamelementsDialog,
  },
  computed: mapState({
    alert_account_type: state => state.alerts.alert_account_type,
  }),

  created () {
    this.$store.dispatch('alerts/getSetupAlertsService')
  }
}
</script>

<style>
</style>

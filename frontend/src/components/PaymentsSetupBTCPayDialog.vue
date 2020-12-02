<template>
  <div>
    <v-dialog v-model='dialog'>
      <template v-slot:activator='{ on, attrs}'>
        <v-btn
          v-bind='attrs'
          v-on='on'
        >SET UP BTCPAYSERVER</v-btn>
      </template>
      <v-card>
        <v-card-title>
          BTCPayServer Setup
        </v-card-title>
        <v-card-text>
          <v-form
            ref="form"
            lazy-validation
            >
            <v-text-field
              v-model="btcpayserver_credentials.host"
              :rules="rules.required"
              label="BTCPayServer Base URL"
            ></v-text-field>
            <v-checkbox
              v-model='btcpayserver_credentials.onion_service'
              label="Tor Onion Address?"
            ></v-checkbox> 

            <v-text-field
              v-model="btcpayserver_credentials.code"
              :type='"password"'
              :rules="rules.requied"
              label="BTCPayServer Pairing Code"
            ></v-text-field>
            <v-btn class='mr-4' @click='submit'>
              Submit BTCPayServer Credentials
            </v-btn>
          </v-form>
        </v-card-text>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
export default {
  data() { 
    return {
      btcpayserver_credentials: {
        type: 'btcpay', 
        host: '',
        code: '', 
        onion_service: false
      },
      dialog: false,
      rules: {
        required: value => !!value || 'This field is required!',
      },
    }
  }, 
  methods: {
    submit() {
      this.$store.dispatch(
        'payments/setupPaymentAccountAction', 
        this.btcpayserver_credentials
      )
    }
  },
}
</script>

<style>
</style>

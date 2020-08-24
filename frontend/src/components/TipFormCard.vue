<template>
  <v-card class="elevation-4">
    <InvoiceDialog
      ref='invoiceDialog'
      v-bind='invoiceDialogProps'
    />
    <v-toolbar color='primary' flat>
      <v-toolbar-title
        class='title align-end tip-username'
        >Tip to {{ displayName }}!</v-toolbar-title>
      <div class="flex-grow-1"></div>
    </v-toolbar>
    <v-card-text>
      <v-form
        @submit.prevent='createInvoice'
        >
        <v-row>
          <v-col cols="12">
            <v-text-field label="Name" name="login" type='text' clearable
              prepend-icon="mdi-account-box"
              hint="Optional. Twitch or Twitter name preferred."
              :rules='[rules.nameMaxLength, rules.nameAlphaNumeric]'
              v-model='tipFormFields.name'
              />
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="5">
            <v-select v-model='selectedCurrency' :items='currencies'
              label="Denomination" prepend-icon='mdi-currency-usd'
              />
          </v-col>
          <v-col>
            <v-text-field label='Amount' v-model='tipFormFields.price' min='0'
              step='.1' type='number' :rules='[rules.pricePositiveValue]'
            />
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12">
            <v-textarea auto-grow row-height=1 counter label="Message"
              prepend-icon="mdi-comment-text" :rules='[rules.messageMaxLength]'
              hint="Would you like to leave a message for the broadcaster? You can do so here!"
              v-model='tipFormFields.message'
            />
          </v-col>
        </v-row>
        <v-row>
          <v-btn
            class='mx-4'
            v-on='on'
            dark
            @click="createInvoice"
          >
            Create Invoice!
          </v-btn>
        </v-row>
      </v-form>
    </v-card-text>
    <v-card-actions>
    </v-card-actions>
  </v-card>
</template>

<script>
import InvoiceDialog from '@/components/InvoiceDialog';
//import { mapActions } from 'vuex'
export default {

  props: {
    displayName: {
      type: String,
      required: true
    },
    username: {
      type: String,
      required: true
    },
    paymentAPIs: {
      type: Array,
      required: true
    },
    currencies: {
      type: Array,
      default: function() {
        return [
          {
            text: 'Satoshis',
            value: "sats",
          },
          {
            text: 'Bitcoins (BTC)',
            value: "btc",
          },
          {
            text: 'US Dollar (USD)',
            value: "usd",
          },
        ]
      },
    },
  },

  components: {
    InvoiceDialog
  },

  methods: {
    createInvoice () {
      this.$refs.invoiceDialog.invoiceStatus = "loading"
      this.$refs.invoiceDialog.dialog = true

      this.$store.dispatch('payments/getInvoiceFromPayServer', {
        params: this.tipFormFields
      }).then((response) => {
        this.invoiceDialogProps.paymentTabs = response.data
      }).catch((error) => {
        console.log(error)
      })

      // TODO: placeholder, make API call to create invoice here
      setTimeout(() => (this.$refs.invoiceDialog.invoiceStatus = 'waitingForPayment'), 1000)
      // ENDTODO
    },
  },

  data: function() { return {
    selectedCurrency: this.currencies[0],

    rules: {
      required: value => !!value || 'This field is required!',
      nameMaxLength: value => value.length <= 25 || "No more than 25 characters!",
      nameAlphaNumeric: value => {
        const pattern = /^[a-zA-Z0-9]*$/
        return pattern.test(value) || "Letters and Numbers only, sorry."
      },
      messageMaxLength: value => value.length <= 255 || "No more than 255 characters!",
      pricePositiveValue: value => value > 0 || "You can't send nothing!"
    },

    tipFormFields: {
      username: this.username,
      message: '',
      price: 1,
      name: '',
    },
    invoiceDialogProps: {
      paymentTabs: []
    },

  }},
}
</script>

<style>
</style>

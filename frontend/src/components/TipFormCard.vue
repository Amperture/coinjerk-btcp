<template>
  <v-card class="elevation-4">
    <InvoiceDialog
      ref='invoiceDialog'
    />
    <v-toolbar
      color="primary"
      dark
      flat
      >
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
            <v-text-field
              label="Name"
              name="login"
              prepend-icon="mdi-account-box"
              type="text"
              clearable
              hint="Optional. Twitch or Twitter name preferred."
              :rules='[rules.nameMaxLength, rules.nameAlphaNumeric]'
              />
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="5">
            <v-select
              v-model='selectedCurrency'
              :items="currencies"
              label="Denomination"
              prepend-icon="mdi-currency-usd"
              />
          </v-col>
          <v-col>
            <v-text-field
              label='Amount'
              v-model="height"
              min="0"
              step=".1"
              type="number"
            />
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12">
            <v-textarea
              auto-grow
              row-height=1
              prepend-icon="mdi-comment-text"
              label="Message"
              hint="Would you like to leave a message for the broadcaster? You can do so here!"
              counter
              :rules='[rules.messageMaxLength]'
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
export default {

  props: {
    displayName: {
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
    createInvoice: function () {
      this.$refs.invoiceDialog.invoiceStatus = "loading"
      this.$refs.invoiceDialog.dialog = true

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
    },
    drawer: false,

  }},
}
</script>

<style>
</style>

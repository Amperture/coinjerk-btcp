<template>
  <v-dialog
    v-model='dialog'
    max-width='400'
  >
    <v-snackbar
      :timeout='clipboardNotification.timeout'
      v-model='clipboardNotification.display'
      multi-line
      absolute
      bottom
    >
    "{{ clipboardNotification.data }}"  has been copied to your clipboard.
    </v-snackbar>
    <v-card class='text-center'>
      <v-card-text
        v-show="showInvoiceLoader"
      >
        <v-row>
          <v-col>
            <v-progress-circular
              indeterminate
              :size=200
              :width=20
              color='primary'
            />
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            Invoice is generating...
          </v-col>
        </v-row>
      </v-card-text>
      <v-card-text
        v-show='showInvoicePaymentWaiting'
      >
      <v-tabs
        v-model='tab'
        centered
        icons-and-text
      >
        <v-tab-slider></v-tab-slider>

        <v-tab
          v-for='pTab in paymentTabs'
          :key='pTab.id'
          :href='`#${pTab.id}`'
        >
          {{ pTab.name }}
          <v-icon
            v-for='icon in pTab.icons'
            :key='icon'
          >{{ icon }}</v-icon>
        </v-tab>
      </v-tabs>

      <v-tabs-items v-model='tab'>
        <v-tab-item
          v-for='pTab in paymentTabs'
          :key='pTab.id'
          :id='pTab.id'
          :value='pTab.id'
        >
          <v-row>
            <v-col>
              <QrcodeVue
                :value='pTab.walletLink'
                size='320'
                level='H'
              ></QrcodeVue>
            </v-col>
          </v-row>
          <v-row
            dense
            v-show='pTab.amount.display'
          >
            <v-col>
              <v-text-field
                readonly
                outlined
                no-resize
                rounded
                dense
                label='Amount:'
                @click="clipboardCopy(pTab.amount.value)"
                :value='pTab.amount.value + " " + "BTC" '
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row dense>
            <v-col>
              <v-text-field
                readonly
                outlined
                no-resize
                rounded
                dense
                label='Send To:'
                @click="clipboardCopy(pTab.address)"
                :value="pTab.address"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row dense>
            <v-col>
              <v-btn 
                depressed 
                large 
                :href="pTab.walletLink"
                target="_blank"
                color="primary"
              >
                <v-icon left>mdi-open-in-new</v-icon> Open In External Wallet 
              </v-btn>
            </v-col>
          </v-row>
        </v-tab-item>
      </v-tabs-items>

      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script>
import QrcodeVue from 'qrcode.vue'

export default {
  components: {
   QrcodeVue
  },

  props: {
  },

  data: () => ({
    dialog: false,
    tab: null,
    invoiceStatus: null,
    invoiceLink: null,
    invoiceOnion: true,
    clipboardNotification: {
      display: false,
      timeout: 3000,
      data: '',
    },
    paymentTabs: [
      {
        'id'          : 'btc',
        'name'        : 'Bitcoin',
        'icons'       : [ 'mdi-bitcoin', ],
        'address'     : 'bc1qvcjn825jd5zceml9j727a4fl6v5f8n9ssrryqe',
        'amount'      : {
          'value' : '0.0001',
          'symbol': 'BTC',
          'display' : true,
        },
        'walletLink'  : 'bitcoin:bc1qlf3p6ts3nph6qgewfe4uux8dn4cscte3jyvv7x?amount=0.00010234',
      },
      {
        'id'          : 'btclnd',
        'name'        : 'Bitcoin (LN)',
        'icons'       : [ 'mdi-flash-circle' ],
        'address'     : 'lnbc102340n1p0nvzp9pp5mhgk5ujh5l2ehd2mjzkhulerv36409dhewmyr0g8yeyg0ae0fnksdp82pskjepqw3hjqctdwqszsnmjv3jhygzfgsazq2gcqzpgxqzupsp55h6v8ljcpje655l2wxs03vdva5j4lr6a6w5upm90huddvm00tupq9qy9qsqc4n4xqpp02ee8nsn8ugcekx7axth73u0wuhn2wjnp204qetcz7n8v9pgudtlfuqtyyspm6eqmfxegf5n988tzj39pnvz6n05d53uywcqgrjn2j',
        'amount'      : {
          'value' : '0.0001',
          'symbol': 'BTC',
          'display' : false,
        },
        'walletLink'  : 'lightning:lnbc102340n1p0nvzp9pp5mhgk5ujh5l2ehd2mjzkhulerv36409dhewmyr0g8yeyg0ae0fnksdp82pskjepqw3hjqctdwqszsnmjv3jhygzfgsazq2gcqzpgxqzupsp55h6v8ljcpje655l2wxs03vdva5j4lr6a6w5upm90huddvm00tupq9qy9qsqc4n4xqpp02ee8nsn8ugcekx7axth73u0wuhn2wjnp204qetcz7n8v9pgudtlfuqtyyspm6eqmfxegf5n988tzj39pnvz6n05d53uywcqgrjn2j',
      },
    ],
  }),

  computed: {

    showInvoiceLoader: function () {
      return this.invoiceStatus === "loading"
    },

    showInvoicePaymentWaiting: function() {
      return this.invoiceStatus === "waitingForPayment"
    },
  },

  methods: {
    closeDialog(){
      this.dialog = false;
    },
    async clipboardCopy(val){
      await navigator.clipboard.writeText(val);
      this.clipboardNotification.data = val;
      if (val.length > 50){
        this.clipboardNotification.data = val.substring(0, 50) + ' [ ... ]'
      }
      this.clipboardNotification.display = true;
    },
  },
}
</script>

<style>
.v-progress-circular {
  margin: 1rem
}
</style>

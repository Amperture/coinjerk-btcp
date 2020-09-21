<template>
  <v-dialog v-model='dialog' max-width='400'>
    <v-snackbar absolute bottom multi-line
                :timeout='clipboardNotification.timeout'
                v-model='clipboardNotification.display'>
      "{{ clipboardNotification.data }}"  has been copied to your clipboard.
    </v-snackbar>
      <v-card class='text-center'>
        <v-card-text v-show='showInvoiceLoader'>
          <v-row>
            <v-col>
              <v-progress-circular indeterminate :size=200 :width=20
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
        <v-card-text v-show='showInvoicePaymentWaiting'>
          <v-tabs v-model='tab' centered icons-and-text>
            <v-tab-slider></v-tab-slider>
            <v-tab v-for='pTab in paymentTabs' :key='pTab.id'
                   :href='`#${pTab.id}`'
                   >
              {{ pTab.name }}
              <v-icon v-for='icon in pTab.icons' :key='icon'>
                {{ icon }}
              </v-icon>
            </v-tab>
          </v-tabs>
          <v-tabs-items v-model='tab'>
            <v-tab-item :key='pTab.id' :id='pTab.id' :value='pTab.id'
                        v-for='pTab in paymentTabs'
                        >
              <v-row>
                <v-col class='qrbox py-6 my-2 px-0'>
                  <QrcodeVue :value='pTab.walletLink' size='320' level='H'/>
                </v-col>
              </v-row>
              <v-row dense v-show='pTab.amount.display'>
                <v-col>
                  <v-text-field readonly outlined no-resize rounded dense
                                label='Amount:'
                                @click="clipboardCopy(pTab.amount.value)"
                                :value='pTab.amount.value + " " + "BTC" '
                                />
                </v-col>
              </v-row>
              <v-row >
                <v-col>
                  <v-text-field readonly outlined no-resize rounded dense
                                label='Send To:'
                                @click="clipboardCopy(pTab.address)"
                                :value="pTab.address"
                                />
                </v-col>
              </v-row>
              <v-row dense>
                <v-col>
                  <v-btn depressed large :href="pTab.walletLink"
                         target="_blank" color='primary'>
                    <v-icon left>
                      mdi-open-in-new
                    </v-icon> Open In External Wallet
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
    paymentTabs: {
      type: Array,
      default: function(){return []},
    }
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
.qrborder{
  /*
  border: 10px solid white;
  */
}
.qrbox{
  background: white;
}
</style>

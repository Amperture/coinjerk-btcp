<template>
  <v-app id="inspire">
    <v-container class="fill-height" fluid>
      <v-row align='center' justify='center'>
        <TipFormCard/>
      </v-row>
    </v-container>
    <v-footer
      color="indigo"
      app
    >
      <span class="white--text">&copy; 2019</span>
    </v-footer>
  </v-app>
</template>

<script>
import TipFormCard from '@/components/TipFormCard'

  export default {
    props: {
      username: String,
      source: String,
    },
    
    components: {
      TipFormCard,
    },

    created () {
      let btcPayModalScript = document.createElement('script')
      btcPayModalScript.setAttribute('src', "https://btcpay960873.lndyn.com/modal/btcpay.js")
      document.head.appendChild(btcPayModalScript)
    },

    methods: {
      invoiceModal(){
        window.btcpay.showInvoice('9LemhFi3Qzdekorw85PpHv')
      },

    }, 

    data: () => ({
      drawer: false,
      currencies: [
        'USD',
        'BTC',
        'satoshis'
      ]
    }),
  }
</script>

<style>
.tip-username{
  text-shadow: 2px 2px 0 #000,
             -1px -1px 0 #000,
              1px -1px 0 #000,
              -1px 1px 0 #000,
               1px 1px 0 #000;
}

</style>

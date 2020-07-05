<template>
  <v-app id="inspire">
    <v-container
      class="fill-height"
      fluid
    >
      <v-row
        align="center"
        justify="center"
      >
        <v-col class="text-center">
          <v-card
            max-width="800"
            class='mx-auto'>
            <v-img
              src="https://coinjerk.com/static/img/tip/default_header.jpg"
            >
              <v-card-title
                class="title align-end fill-height tip-username"
                >Tip {{ username }}
              </v-card-title>
            </v-img>
            <v-card-text>
              <v-form>
                <v-row>
                  <v-col cols="8">
                    <v-text-field
                      label="Name"
                      name="login"
                      prepend-icon="mdi-account-box"
                      type="text"
                      clearable
                      hint="Optional. Twitch or Twitter name preferred."
                    ></v-text-field>
                  </v-col>
                  <v-col cols="4">
                    <v-select
                      :items="currencies"
                      label="Currency/Denomination"
                      prepend-icon="mdi-currency-usd"
                    />
                  </v-col>
                </v-row>
                <v-row>
                  Choose Amount Here
                </v-row>
                <v-row>
                  <v-col cols="12"
                  >
                    <v-textarea
                      auto-grow="true"
                      row-height=1
                      prepend-icon="mdi-comment-text"
                      label="Message"
                      hint="Would you like to leave a message for the broadcaster? You can do so here!"
                    />
                  </v-col>
                </v-row>
                <v-row>
                  <v-btn 
                    color="blue darken-1" 
                    text 
                    @click="invoiceModal"
                  >Login</v-btn>
                </v-row>
              </v-form>
            </v-card-text>
          </v-card>
        </v-col>
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
  export default {
    props: {
      username: String,
      source: String,
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

<template>
  <v-app id="inspire">
    <v-navigation-drawer
      v-model="drawer"
      app
    >
      <v-list dense>
        <v-list-item >
          <v-list-item-action>
            <v-icon>mdi-home</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Home</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item >
          <v-list-item-action>
            <v-icon>mdi-contact-mail</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Contact</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar
      app
      color="green darken-4"
      dark
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>CoinJerk WIP</v-toolbar-title>
    </v-app-bar>

    <v-content>
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

                >Tip Amperture
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
                      ></v-textarea>
                    </v-col>
                  </v-row>
                  <v-row>
                    BTCPay Button Here, on the right
                  </v-row>
                </v-form>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
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
      this.$vuetify.theme.dark = true
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

<template>
  <div class="home">
    <v-card
      flat
      class="mx-auto"
    >
      <v-card-title 
        class='display-3 logo-text justify-center'
      >
        <p class='text-center logo-text'>
          Welcome to Coin<span class='primary--text'>Jerk</span>
        </p>
      </v-card-title>

      <v-card-subtitle 
        class="pb-0 justify-center display-2"
      >
        <p class='logo-text center-text text-center'>
        The Live Streamer's 
        <span class='primary--text'>Non-Custodial</span> Bitcoin Tip Tracker
        </p>
      </v-card-subtitle>

      <v-card-text class="justify-center display-1">
        <div class="raleway-text text-center">
          Bridging the gap between the Bitcoin Lightning Network and your
          favorite Streaming Overlays!
        </div>
      </v-card-text>
    </v-card>
    <v-container
      fluid
    >
      <v-row
        justify=center
        align=start
      >
        <v-col
          cols=12
          md=4
        >
          <v-card
            class="px-md-4"
          >
            <v-subheader class='justify-center py-md-1'>
                Supported Stream Overlays
            </v-subheader>
            <v-list
            >
              <v-list-item-group v-model='supportedOverlays'>
                <v-list-item
                  v-for="(overlay, i) in supportedOverlays"
                  :key="i"
                >
                  <v-list-item-avatar>
                    <v-img 
                      max-height="100%"
                      :src="overlay.avatar"/>
                  </v-list-item-avatar>
                  <v-list-item-content>
                    <v-list-item-title v-html="overlay.name">
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>
                      ...and more to come!
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>

              </v-list-item-group>
            </v-list>
          </v-card>
        </v-col>
        <v-col
          cols=12
          md=4
        >
          <v-card
            class="px-md-4"
          >
            <v-subheader class='justify-center py-md-1'>
                Supported Payment Services
            </v-subheader>
            <v-list
            >
              <v-list-item-group v-model='supportedPayments'>
                <v-list-item
                  v-for="(payment, i) in supportedPayments"
                  :key="i"
                >
                  <v-list-item-avatar>
                    <v-img 
                      max-height="100%"
                      :src="payment.avatar"/>
                  </v-list-item-avatar>
                  <v-list-item-content>
                    <v-list-item-title v-html="payment.name">
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>
                      ...and more to come!
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>

              </v-list-item-group>
            </v-list>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'home',

  components: [
  ],

  data: () => ({
    supportedOverlays: [
      {
        avatar: require('@/assets/streamelements_logo.png'),
        name: 'StreamElements',
        url: 'https://streamelements.com'
      },
    ],

    supportedPayments: [
      {
        avatar: require('@/assets/btcpayserver_logo.png'),
        name: 'BTCPayServer',
        url: 'https://btcpayserver.org'
      },
    ],

  })
}
</script>

<style>
.logo-text{
  font-family: "Raleway", sans-serif;
  font-weight: 700;
  overflow-wrap: normal;
  word-break: normal;
}

.raleway-text{
  font-family: "Raleway", sans-serif;
  font-weight: 400;
}
</style>

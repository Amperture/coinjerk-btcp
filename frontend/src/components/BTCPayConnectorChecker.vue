<template>
  <v-card
    flat
    :loading='cardLoading'
    justify="center"
    class="px-md-4"
    >
    <v-expansion-panels>
      <v-expansion-panel>
        <v-expansion-panel-header v-slot="{ open }">
          <v-row no-gutters>
            <v-col cols="4">BTCPay Server Setup</v-col>
            <v-col
              cols="8"
              class="text--secondary"
              >
              <v-fade-transition leave-absolute>
                <span v-if="open">Set up your BTCPayServer Connection Here!</span>
                <v-row
                  v-else
                  no-gutters
                  style="width: 100%"
                  >
                  <v-col 
                    cols="6"
                    v-html="server_host"
                    />
                </v-row>
              </v-fade-transition>
            </v-col>
          </v-row>
        </v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-row
            :loading="formLoading"
            justify="space-around"
            no-gutters
            >
            <v-col cols="3">
              <v-form
                ref='form'
                v-model='valid'
                lazy-validation
                >
                <v-text-field
                  v-model="serverURL"
                  :rules="serverURLRules"
                  label="BTCPayServer URL"
                  required
                  ></v-text-field>
                <v-text-field
                  v-model="pairingCode"
                  label="Server Pairing Code"
                  required
                  ></v-text-field>
                <v-btn 
                  :loading="formLoading"
                  @click="submit" 
                  :disabled="!valid"
                  >Connect</v-btn>
              </v-form>
            </v-col>
          </v-row>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
  </v-card>
</template>

<script>
import { mapState } from 'vuex'

export default {

  data: function() {
    return {
      valid: true,

      server_host: "Not Set Up",

      cardLoading: false,
      formLoading: false,

      serverURL: '',
      serverURLRules: [
        v => !!v || "We need a Server to connect to!",
      ],

      pairingCode: '',
      pairingCodeRules: [
        v => !!v || "The server won't accept a connection without a code!",
      ]
    }
  },

  methods: {
    submit(){
      if(this.$refs.form.validate()){
        this.formLoading = true
        this.$store.dispatch('btcpaySetup',{
          url: this.serverURL,
          code: this.pairingCode, 
        })
          .then()
          .catch()
      }
    }
  },

  mounted: function() {
    this.$store.dispatch('getUserPayServerAction')
  }, 
}
</script>

<style>
</style>


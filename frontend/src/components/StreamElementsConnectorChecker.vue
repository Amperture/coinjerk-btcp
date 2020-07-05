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
            <v-col cols="4">StreamElements</v-col>
            <v-col
              cols="8"
              class="text--secondary"
              >
              <v-fade-transition leave-absolute>
                <span v-if="open">Set up your StreamElements Connection Here!</span>
                <v-row
                  v-else
                  no-gutters
                  style="width: 100%"
                  >
                  <v-col 
                    cols="6"
                    v-html=""
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
                  type="password"
                  v-model="channelID"
                  :rules="channelIDRules"
                  label="Channel ID"
                  required
                  ></v-text-field>
                <v-text-field
                  type="password"
                  v-model="channelJWT"
                  :rules="channelJWTRules"
                  label="JWT Key"
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

  computed: {
    ...mapState({
    })
  },

  data: function() {
    return {
      valid: true,

      cardLoading: false,
      formLoading: false,

      channelID: '',
      channelIDRules: [
        v => !!v || "I mean if you want to connect to Streamelements, you have an account there...",
      ],

      channelJWT: '',
      channelJWTRules: [
        v => !!v || "We need credentials to make tips on Streamelements!",
      ]
    }
  },

  methods: {
    submit(){
      if(this.$refs.form.validate()){
        this.formLoading = true
        this.$store.dispatch('streamElementsSetupAction',{
          channelID: this.channelID,
          channelJWT: this.channelJWT, 
        })
          .then((data) => {
          })
          .catch()
      }
    }
  },

  mounted: function() {
    this.$store.dispatch('getUserPayServerAction')
  }, 
}
</script>

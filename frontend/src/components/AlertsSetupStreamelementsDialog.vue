<template>
  <div>
    <v-dialog v-model='dialog'>
      <template v-slot:activator='{ on, attrs}'>
        <v-btn
          v-bind='attrs'
          v-on='on'
        >SET UP STREAMELEMENTS</v-btn>
      </template>
      <v-card>
        <v-card-title>
          StreamElements Setup
        </v-card-title>
        <v-card-text>
          <v-form
            ref="form"
            v-model="valid"
            lazy-validation
            >
            <v-text-field
              v-model="streamelements_credentials.client_id"
              :type="'password'"
              :rules="rules.required"
              label="StreamElements Client ID"
            ></v-text-field>

            <v-text-field
              v-model="streamelements_credentials.jwt_token"
              :type='"password"'
              :rules="rules.requied"
              label="StreamElements JWT Token"
            ></v-text-field>
            <v-btn class='mr-4' @click='submit'>
              Submit StreamElements Credentials
            </v-btn>
          </v-form>
        </v-card-text>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
export default {
  data() { 
    return {
      streamelements_credentials: {
        type: 'streamelements', 
        client_id: '', 
        jwt_token: '', 
      },
      dialog: false,
      rules: {
        required: value => !!value || 'This field is required!',
      },
    }
  }, 
  methods: {
    submit() {
      this.$store.dispatch(
        'alerts/setupAlertAccountAction', 
        this.streamelements_credentials
      )
    }
  },
}
</script>

<style>
</style>

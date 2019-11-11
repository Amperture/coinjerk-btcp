<template>
  <div>
    <v-card 
      flat
      :loading='loading'
    >
      <v-card-text>
        <v-form
          ref='form'
          lazy-validation
        >
          <v-text-field 
            v-model='username'
            prepend-icon="mdi-account"
            label="Username"
            :rules='usernameRules'
          ></v-text-field>
          <v-text-field 
            v-model='password'
            prepend-icon="mdi-lock"
            label="Password"
            type="password"
            :rules='passwordRules'
          ></v-text-field>
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-btn 
          color="blue darken-1" 
          text 
          @click="cancelLogin()"
        >Cancel</v-btn>
        <v-btn 
          color="blue darken-1" 
          text 
          @click="submit"
        >Login</v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
import { mapState } from 'vuex'
export default {

  data: function () {
    return {
      loading: false,

      username: '',
      usernameRules: [
        v => !!v || 'Look, obviously you have a username...',
      ],

      password: '',
      passwordRules: [
        v => !!v || 'Don\'t try and tell me you don\'t have a password...',
      ],

    }
  },

  computed: mapState({
    //surveys: state => state.surveys
  }),

  methods: {
    cancelLogin(){
      this.$refs.form.reset()
      this.$emit('closedialog')
    },

    submit(){
      if(this.$refs.form.validate()){
        this.loading = true
        this.$store.dispatch('login', { 
            username: this.username,
            password: this.password,
          })
          .then((data) => {
            console.log(data) // eslint-disable-line no-console
            this.loading = false
            this.$router.push('/dashboard')
          })
          .catch((error) => {
            this.loading = false
            console.log(error.data) // eslint-disable-line no-console
          })
      } 
    }, 
  },
  
}
</script>

<style>
</style>

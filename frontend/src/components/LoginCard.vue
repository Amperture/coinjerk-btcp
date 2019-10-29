<template>
  <div>
    <v-card flat>
      <v-card-text>
        <v-form
          ref='form'
          v-model='valid'
          lazy-validation
        >
          <v-text-field 
            v-model='username'
            label="Username"
            :rules='usernameRules'
          ></v-text-field>
          <v-text-field 
            v-model='password'
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
          @click="beepoLoginCard"
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
    surveys: state => state.surveys
  }),

  methods: {
    cancelLogin(){
      this.$refs.form.reset()
      this.username = '';
      this.password = '';
      this.$emit('closedialog')
    },
    login(){
      this.$store.dispatch(
        'login', 
        { 
          username: this.username,
          password: this.password,
        }
      ).then(() => this.$router.push('/dashboard'))

    }, 
  },
  
}
</script>

<style>
</style>

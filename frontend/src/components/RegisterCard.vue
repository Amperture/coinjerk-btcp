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
            prepend-icon='mdi-account'
            v-model='username'
            label="Username"
            :rules='usernameRules'
          ></v-text-field>
          <v-text-field 
            prepend-icon='mdi-lock'
            v-model='password'
            label="Password"
            type="password"
            :rules='passwordRules'
          ></v-text-field>
          <v-text-field 
            prepend-icon='mdi-lock'
            v-model='confirmPassword'
            label="Confirm Password"
            type="password"
            :rules='confirmPasswordRules'
          ></v-text-field>
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-btn 
          color="blue darken-1" 
          text 
          @click="cancelRegistration()"
        >Cancel</v-btn>
        <v-btn 
          color="blue darken-1" 
          text 
          @click="submit"
        >Regsiter</v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
export default {
  props: ['closedialog'],

  data: function () {
    return {
      username: '',
      usernameRules: [
        v => !!v || 'No really, what do you want to be called?', 
        v => v.length >= 3 || 'At least three characters long, please.',
      ],

      password: '',
      passwordRules: [
        v => !!v || 'I\'m not letting you in without making a password.',
        v => v.length >= 8 || 'At least eight characters long, please.',
      ],

      confirmPassword: '',
      confirmPasswordRules: [
        v => v === this.password || 
          "Did you already forget the password you want?",
      ],

    }
  },

  methods: {
    cancelRegistration(){
      this.$refs.form.reset()
      this.$emit('closedialog')
    },

    submit(){
      if(this.$refs.form.validate()){
        this.loading = true
        this.$store.dispatch('register', { 
            username: this.username,
            password: this.password,
          })
          .then((data) => {
            this.loading = false
            this.$router.push('/dashboard')
          })
          .catch((error) => {
            this.loading = false
          })
      } 
    }, 
  },
  
}
</script>

<style>
</style>

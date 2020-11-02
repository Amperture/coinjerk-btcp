<template>
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
</template>

<script>
</script>

<style>
</style>

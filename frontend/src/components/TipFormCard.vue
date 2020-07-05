<template>
  <v-card class="elevation-12">
    <v-toolbar
      color="primary"
      dark
      flat
    >
      <v-toolbar-title
        class='title align-end tip-username'
        >Tip to Someone!</v-toolbar-title>
      <div class="flex-grow-1"></div>
      <v-tooltip bottom>
      </v-tooltip>
      <v-tooltip right>
      </v-tooltip>
    </v-toolbar>
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
          />
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
          <v-col cols="12">
            <v-textarea
              auto-grow="true"
              row-height=1
              prepend-icon="mdi-comment-text"
              label="Message"
              hint="Would you like to leave a message for the broadcaster? You can do so here!"
              />
          </v-col>
        </v-row>
      </v-form>
    </v-card-text>
    <v-card-actions>
      <div class="flex-grow-1"></div>
      <v-btn color="primary">Login</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
</script>

<style>
</style>

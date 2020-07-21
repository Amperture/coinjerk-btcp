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
          <v-col cols="12">
            <v-text-field
              label="Name"
              name="login"
              prepend-icon="mdi-account-box"
              type="text"
              clearable
              hint="Optional. Twitch or Twitter name preferred."
              :rules='[rules.nameMaxLength, rules.nameAlphaNumeric]'
            />
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="4">
            <v-select
              :items="currencies"
              label="Denomination"
              prepend-icon="mdi-currency-usd"
              />
          </v-col>
          <v-col>
            <v-text-field
              label='Amount'
              v-model="height"
              min="0"
              step=".1"
              type="number"
            ></v-text-field>
          </v-col>
          </v-row>
          <v-row>
          <v-col cols="12">
            <v-textarea
              auto-grow="true"
              row-height=1
              prepend-icon="mdi-comment-text"
              label="Message"
              hint="Would you like to leave a message for the broadcaster? You can do so here!"
              counter
              :rules='[rules.messageMaxLength]'
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
  export default {
    data: () => ({
      rules: {
        required: value => !!value || 'This field is required!',
        nameMaxLength: value => value.length <= 25 || "No more than 25 characters!",
        nameAlphaNumeric: value => {
          const pattern = /^[a-zA-Z0-9]*$/
          return pattern.test(value) || "Letters and Numbers only, sorry."
        },
        messageMaxLength: value => value.length <= 255 || "No more than 255 characters!",
      },
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
</style>

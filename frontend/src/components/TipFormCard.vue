<template>
  <v-card class="elevation-12">
    <v-toolbar
      color="primary"
      dark
      flat
    >
      <v-toolbar-title>Tip to Someone!</v-toolbar-title>
      <div class="flex-grow-1"></div>
      <v-tooltip bottom>
      </v-tooltip>
      <v-tooltip right>
      </v-tooltip>
    </v-toolbar>
    <v-card-text>
      <v-form>
        <v-row>
          <v-text-field
            clearable
            label="Name"
            name="login"
            rounded=true
            outlined=true
            hint="Who is sending? (Optional)"
            prepend-icon="mdi-account"
            type="text"
          ></v-text-field>
          <v-text-field
            clearable
            label="Name"
            name="login"
            rounded=true
            outlined=true
            hint="Who is sending? (Optional)"
            prepend-icon="mdi-account"
            type="number"
          ></v-text-field>
        </v-row>
        <v-text-field
          id="password"
          label="Password"
          name="password"
          prepend-icon="mdi-lock"
          type="password"
        ></v-text-field>
      </v-form>
    </v-card-text>
    <v-card-actions>
      <div class="flex-grow-1"></div>
      <v-btn color="primary">Login</v-btn>
    </v-card-actions>
  </v-card>
</template>

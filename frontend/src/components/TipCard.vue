<template>
  <v-card class="elevation-12">
    <v-toolbar
      color="primary"
      dark
      flat
    >
      <v-toolbar-title>Login form</v-toolbar-title>
      <div class="flex-grow-1"></div>
      <v-tooltip bottom>
        <template v-slot:activator="{ on }">
          <v-btn
            :href="source"
            icon
            large
            target="_blank"
            v-on="on"
          >
            <v-icon>mdi-code-tags</v-icon>
          </v-btn>
        </template>
        <span>Source</span>
      </v-tooltip>
      <v-tooltip right>
        <template v-slot:activator="{ on }">
          <v-btn
            icon
            large
            href="https://codepen.io/johnjleider/pen/pMvGQO"
            target="_blank"
            v-on="on"
          >
            <v-icon>mdi-codepen</v-icon>
          </v-btn>
        </template>
        <span>Codepen</span>
      </v-tooltip>
    </v-toolbar>
    <v-card-text>
      <v-form>
        <v-text-field
          label="Login"
          name="login"
          prepend-icon="person"
          type="text"
        ></v-text-field>

        <v-text-field
          id="password"
          label="Password"
          name="password"
          prepend-icon="lock"
          type="password"
        ></v-text-field>
      </v-form>
    </v-card-text>
    <v-card-actions>
      <div class="flex-grow-1"></div>
      <v-btn color="primary">Poopoo</v-btn>
    </v-card-actions>
  </v-card>
</template>

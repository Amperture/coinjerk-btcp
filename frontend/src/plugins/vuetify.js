import Vue from 'vue';
import Vuetify from 'vuetify/lib';
import '@mdi/font/css/materialdesignicons.css'

Vue.use(Vuetify);

export default new Vuetify({
  icons: {
    iconfont: 'mdi',
  },
  theme: {
    dark: true,
    themes: {

      light: {
        accent: "#29aae2",
        secondary: "#29aae2",
      },
      dark: {
        primary: "#29aae2",
        accent: "#000000",
      }
    }
  },
});

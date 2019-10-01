import '@mdi/font/css/materialdesignicons.css' // Ensure you are using css-loader
import Vue from 'vue';
import Vuetify from 'vuetify/lib';

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    dark: false,
    themes: {
      dark: {
          primary: '#0a0a0b',
          secondary: '#181a1b',
          accent: '#56bce8'
      }
    }
  },
  icons: {
    iconfont: 'mdi',
  },
});

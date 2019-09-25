import '@mdi/font/css/materialdesignicons.css' // Ensure you are using css-loader
import Vue from 'vue';
import Vuetify from 'vuetify/lib';

import colors from 'vuetify/lib/util/colors'

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    dark: true,
    themes: {
      dark: {
        primary: colors.blue.lighten2,
        secondary: colors.green.lighten4,
        accent: colors.indigo.base,
      }
    }
  },
  icons: {
    iconfont: 'mdi',
  },
});

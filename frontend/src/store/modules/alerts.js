import api from '@/api'
import auth from '../modules/auth'

const state = {
  user_account: '',
  status: '',
  alert_account_type: '',
}

const getters = {
  hasAccount: state => !!state.token,
  status: state => state.status,
}

const actions = {
  getSetupAlertsService(context){
    if(state.alert_account_type != ''){
      return state.alert_account_type
    }
    if(auth.getters.isAuthenticated()){
      api.alerts.fetchSetupAlertsStatus()
        .then(response => {
          context.commit("CONFIRM_ALERT_SERVICE_TYPE", response.data)
          return 0
        })
        .catch(error => {
          console.log(error)
        })
    }
  },

  setupAlertAccountAction(context, data){
    return api.alerts.alertsAccountSetup(data)
      .then(response => {
        // eslint-disable-next-line no-console
        console.log(response)
      })
      .catch(error => {
        // eslint-disable-next-line no-console
        console.log(error)
      })
  }
}

const mutations = {
  CONFIRM_ALERT_SERVICE_TYPE(state, payload){
    state.alert_account_type = payload.type
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}

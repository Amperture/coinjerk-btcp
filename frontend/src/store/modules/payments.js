import api from '@/api'
import auth from '../modules/auth'

const state = {
  server_host: '',
}

const getters = {
}

const actions = {

  getSetupPaymentProcessor(context){
    if(state.server_host != ''){
      return state.server_host
    }
    if(auth.getters.isAuthenticated()){
      api.payments.fetchSetupPaymentsStatus()
        .then(response => {
          context.commit("CONFIRM_PAYMENT_PROCESSOR", response.data)
          return 0
        })
        .catch(error => {
          console.log(error)
        })
    }
  },

  getInvoiceFromPayServer(context, data){
    return api.payments.fetchInvoiceFromPaymentServer(data.params)
  },

  getUserPaymentServer(context, data){
    return api.payments.fetchUserPaymentServer(data.username)
  },


  setupPaymentAccountAction(context, data){
    return api.payments.paymentProcessSetup(data)
      .then(response => {
        // eslint-disable-next-line no-console
        console.log(response)
      })
      .catch(error => {
        // eslint-disable-next-line no-console
        console.log(error)
      })
  },

}

const mutations = {
  CONFIRM_PAYMENT_PROCESSOR(state, payload){
    state.server_host = payload.server_host
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}

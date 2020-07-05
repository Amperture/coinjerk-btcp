import api from '@/api'

const state = {
  user_account: '',
  status: ''
}

const getters = {
  hasAccount: state => !!state.token,
  status: state => state.status,
}

const actions = {
  //getStreamElementsAccount(context){
  getStreamElementsAccount(){
    api.streamelements.fetchStreamElementsUserInfo()
      .then(response => {
        // eslint-disable-next-line no-console
        console.log(response.data)
      })
      .catch(error => {
        // eslint-disable-next-line no-console
        console.log(error.data)
      })
  },

  streamElementsSetup(context, data){
    return api.streamelements.streamElementsUserSetup(data)
      .then(response => {
        // eslint-disable-next-line no-console
        console.log(response)
      })
      .catch(error => {
        console.log(error) // eslint-disable-line no-console
      })
  }
}

const mutations = {
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}

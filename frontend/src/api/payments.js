import axios from 'axios'
import { API_URL } from '@/api'

export function fetchSetupPaymentsStatus(){
  return axios.get(
    `${API_URL}/api/payments/setup`,
  )
}

export function paymentProcessSetup(setupData){
  return axios.post(
    `${API_URL}/api/payments/setup`,
    setupData
  )
}

export function fetchUserPaymentServer(username){
  return axios.get(
    `${API_URL}/api/payments`,
    { params: { username: username } }
  )
}

export function fetchInvoiceFromPaymentServer(params){
  return axios.post(
    `${API_URL}/api/payments`,
    params
  )
}

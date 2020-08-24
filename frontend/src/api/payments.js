import axios from 'axios'
import { API_URL } from '@/api'

export function paymentProcessSetup(setupData){
  return axios.post(
    `${API_URL}/api/payments`,
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

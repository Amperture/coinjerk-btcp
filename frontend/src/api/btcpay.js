import axios from 'axios'
import { API_URL } from '@/api'

export function btcPayServerSetup(setupData){
  return axios.post(
    `${API_URL}/api/connectors/btcpay`,
    setupData
  )
}

export function fetchUserPayServer(){
  return axios.get(
    `${API_URL}/api/connectors/btcpay`,
  )
}

import axios from 'axios'
import { API_URL } from '@/api'

export function streamElementsUserSetup(setupData){
  return axios.post(
    `${API_URL}/api/connectors/streamelements`,
    setupData
  )
}

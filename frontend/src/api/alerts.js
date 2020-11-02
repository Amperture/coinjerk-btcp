import axios from 'axios'
import { API_URL } from '@/api'

export function alertsAccountSetup(setupData){
  console.log(setupData)
  return axios.post(
    `${API_URL}/api/alerts/setup`,
    setupData
  )
}

export function fetchSetupAlertsStatus(){
  return axios.get(
    `${API_URL}/api/alerts/setup`,
  )
}

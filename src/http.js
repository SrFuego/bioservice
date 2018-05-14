import axios from 'axios'
import {BASE_URL} from './utils/variables'
// axios.defaults.timeout = 5000
axios.defaults.baseURL = `${BASE_URL}:8000`
export default axios

import axios from 'axios'


// base URL set up
const request = axios.create({
  baseURL: 'http://geek.itheima.net/v1_0',
  timeout: 5000
})


/*
Add request interceptors to intercept requests before they are sent, 
allowing for the insertion of custom configurations.
*/

request.interceptors.request.use((config)=> {
    return config
  }, (error)=> {
    return Promise.reject(error)
})

// processing returned data
request.interceptors.response.use((response)=> {
    return response.data
  }, (error)=> {
    return Promise.reject(error)
})

export { request }
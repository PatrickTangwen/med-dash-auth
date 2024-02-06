import {getToken} from '@/utils'
import { Navigate } from 'react-router-dom'


export function AuthRoute({children}){
    const token = getToken()
    // if token is correct, then route to corresponding page
    if(token) {
        return<>{children}</>
    }
    // if token is incorrect, then back the login page
    else{
        return <Navigate to={'/login'} replace/>
    }
}
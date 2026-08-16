import React, {createContext, useState, useContext} from "react";
const AuthContext = createContext();
function Login() {
 const {login} = useContext(AuthContext);
 return <button onClick={login}>Login</button>;
}
export default function App() {
 const [user, setUser] = useState(null);
 const login = () => setUser("Admin");
 return (
 <AuthContext.Provider value={{login}}>
 {user ? <h2>Welcome {user}</h2> : <Login />}
 </AuthContext.Provider>
 );
} 
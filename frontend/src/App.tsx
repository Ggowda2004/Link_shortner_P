import { useState } from "react"
import { api } from "./api"

function App() {

  const handleSubmit = async() =>{
    const response = await api.post(
      "/shorten",
      {
      original_url: url
    }
  )

  console.log(response.data)
  }

  const [url, setUrl] = useState("")
  return (
    <div>
      <h1>URL Shortener</h1>
      <input 
        type="text"
        placeholder="Enter url"
        value={url}
        onChange={(e)=>setUrl(e.target.value)}/>

      <p>{url}</p>

      <button onClick={handleSubmit}>Shorten</button>
    </div>
  )
}

export default App
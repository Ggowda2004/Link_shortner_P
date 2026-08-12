// import { useEffect, useState } from "react"
// import { api } from "../api"
// import "../App.css"


// function Home() {
//   const [url, setUrl] = useState("")
//   const [shortenedUrl, setShortenedUrl] = useState("")
//   const [urls, setUrls] = useState([])
//   const [error, setError] = useState("")

//   const fetchUrls = async () => {
//     try {
//       const response = await api.get("/all_urls")
//       setUrls(response.data)
//     } catch (error) {
//       console.error("Error loading URLs:", error)
//     }
//   }

//   useEffect(() => {
//     fetchUrls()
//   }, [])

//   const handleSubmit = async (e) => {
//     e.preventDefault()

//     setError("")
//     if (!url) {
//       setError("Please enter a URL")
//       return
//     }

//     try {
//       // Basic client-side validation
//       // Using the URL constructor to ensure it's a valid URL
//       // This will throw for invalid inputs
//       new URL(url)
//     } catch (err) {
//       setError("Invalid URL format")
//       return
//     }

//     try {
//       const response = await api.post("/shorten", {
//         original_url: url,
//       })
//       setShortenedUrl(response.data.short_url)
//       fetchUrls()
//     } catch (error) {
//       console.error("Error shortening URL:", error)
//       setError(error?.response?.data?.detail || "Failed to shorten URL")
//     }
//   }

//   return (
//     <div className="page-container">
//       <div className="main-wrapper">
//         <div className="card-box">
//           <h1 className="main-title">URL Shortener</h1>

//           <form onSubmit={handleSubmit} className="form-layout">
//             <div className="input-group">
//               <input
//                 type="text"
//                 placeholder="Enter long URL here..."
//                 value={url}
//                 onChange={(e) => setUrl(e.target.value)}
//                 className="url-input"
//               />
//               <button type="submit" className="submit-btn">
//                 Shorten URL
//               </button>
//             </div>

//             {url && (
//               <p className="preview-text">
//                 <strong>Preview:</strong> {url}
//               </p>
//             )}

//             {error && (
//               <p className="error-text">{error}</p>
//             )}

//             {shortenedUrl && (
//               <div className="success-box">
//                 <p className="success-label">Success! Your shortened URL:</p>
//                 <a href={shortenedUrl} target="_blank" rel="noreferrer" className="result-link">
//                   {shortenedUrl}
//                 </a>
//                 <button
//                   onClick={() => navigator.clipboard.writeText(shortenedUrl)}
//                   className="copy-btn"
//                 >
//                   Copy
//                 </button>
//               </div>
//             )}
//           </form>
//         </div>

//         {urls.length > 0 && (
//           <div className="card-box">
//             <div className="analytics-header">
//               <h2 className="section-title">Saved URLs History</h2>
//               <button onClick={fetchUrls} className="refresh-btn">
//                 🔄 Refresh Analytics
//               </button>
//             </div>

//             <ul className="history-list">
//               {urls.slice().reverse().map((item) => (
//                 <li key={item.id} className="history-item">
//                   <div className="links-group">
//                     <span className="field-label">Original Link</span>
//                     <a href={item.original_url} target="_blank" rel="noreferrer" className="original-link">
//                       {item.original_url}
//                     </a>

//                     <span className="field-label">Short Link</span>
//                     <a href={`http://localhost:8080/${item.short_code}`} target="_blank" rel="noreferrer" className="short-link">
//                       {`http://localhost:8080/${item.short_code}`}
//                     </a>
//                     <button
//                       onClick={() => navigator.clipboard.writeText(`http://localhost:8080/${item.short_code}`)}
//                       className="copy-btn"
//                     >
//                       Copy
//                     </button>
//                   </div>

//                   <div className="badge-wrapper">
//                     <span className="click-badge">📊 {item.click_count ?? 0} clicks</span>
//                   </div>
//                 </li>
//               ))}
//             </ul>
//           </div>
//         )}
//       </div>
//     </div>
//   )
// }

// export default Home






import { useEffect, useState } from "react"
import { api } from "../api"
import "../App.css"

function Home() {
  const [url, setUrl] = useState("")
  const [shortenedUrl, setShortenedUrl] = useState("")
  const [urls, setUrls] = useState([])
  const [error, setError] = useState("")

  // 👇 DYNAMIC URL RESOLUTION: Looks for the Vite environment variable, falls back safely to localhost
  const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://localhost:8080";

  const fetchUrls = async () => {
    try {
      const response = await api.get("/all_urls")
      setUrls(response.data)
    } catch (error) {
      console.error("Error loading URLs:", error)
    }
  }

  useEffect(() => {
    fetchUrls()
  }, [])

  const handleSubmit = async (e) => {
    e.preventDefault()

    setError("")
    if (!url) {
      setError("Please enter a URL")
      return
    }

    try {
      // Basic client-side validation
      // Using the URL constructor to ensure it's a valid URL
      // This will throw for invalid inputs
      new URL(url)
    } catch (err) {
      setError("Invalid URL format")
      return
    }

    try {
      const response = await api.post("/shorten", {
        original_url: url,
      })
      // Ensure the displayed short URL also targets your environment base instead of whatever the backend returns
      const code = response.data.short_code || response.data.short_url?.split("/").pop();
      setShortenedUrl(`${API_BASE_URL}/${code}`)
      fetchUrls()
    } catch (error) {
      console.error("Error shortening URL:", error)
      setError(error?.response?.data?.detail || "Failed to shorten URL")
    }
  }

  return (
    <div className="page-container">
      <div className="main-wrapper">
        <div className="card-box">
          <h1 className="main-title">URL Shortener</h1>

          <form onSubmit={handleSubmit} className="form-layout">
            <div className="input-group">
              <input
                type="text"
                placeholder="Enter long URL here..."
                value={url}
                onChange={(e) => setUrl(e.target.value)}
                className="url-input"
              />
              <button type="submit" className="submit-btn">
                Shorten URL
              </button>
            </div>

            {url && (
              <p className="preview-text">
                <strong>Preview:</strong> {url}
              </p>
            )}

            {error && (
              <p className="error-text">{error}</p>
            )}

            {shortenedUrl && (
              <div className="success-box">
                <p className="success-label">Success! Your shortened URL:</p>
                <a href={shortenedUrl} target="_blank" rel="noreferrer" className="result-link">
                  {shortenedUrl}
                </a>
                <button
                  onClick={() => navigator.clipboard.writeText(shortenedUrl)}
                  className="copy-btn"
                >
                  Copy
                </button>
              </div>
            )}
          </form>
        </div>

        {urls.length > 0 && (
          <div className="card-box">
            <div className="analytics-header">
              <h2 className="section-title">Saved URLs History</h2>
              <button onClick={fetchUrls} className="refresh-btn">
                🔄 Refresh Analytics
              </button>
            </div>

            <ul className="history-list">
              {urls.slice().reverse().map((item) => {
                // Dynamically construct the functional short URL based on your hosting platform
                const finalShortUrl = `${API_BASE_URL}/${item.short_code}`;
                
                return (
                  <li key={item.id} className="history-item">
                    <div className="links-group">
                      <span className="field-label">Original Link</span>
                      <a href={item.original_url} target="_blank" rel="noreferrer" className="original-link">
                        {item.original_url}
                      </a>

                      <span className="field-label">Short Link</span>
                      {/* FIXED: Swapped hardcoded localhost links for dynamic parameters */}
                      <a href={finalShortUrl} target="_blank" rel="noreferrer" className="short-link">
                        {finalShortUrl}
                      </a>
                      <button
                        onClick={() => navigator.clipboard.writeText(finalShortUrl)}
                        className="copy-btn"
                      >
                        Copy
                      </button>
                    </div>

                    <div className="badge-wrapper">
                      <span className="click-badge">📊 {item.click_count ?? 0} clicks</span>
                    </div>
                  </li>
                );
              })}
            </ul>
          </div>
        )}
      </div>
    </div>
  )
}

export default Home
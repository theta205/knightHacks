import { Route, Routes, Link, useNavigate } from 'react-router-dom'
import { useState } from 'react'
import Landing from './Landing'
import Result from './Result'
import './App.css'
import './loopa.svg'

export default function App() {
  const [query, setQuery] = useState('')
  const [redirect, setRedirect] = useState(false)
  const navigate = useNavigate()

  if(redirect === true) navigate(`/${query}`)

  return (
    <div className='App'>
      <div className="SearchPanel">
        <div className="logo"><span style={{color: "#533EBE"}}>K</span>NIGHT MARKET</div>
        <div tabIndex={0} onKeyDown={(e) => { if(e.key == 'Enter'){console.log('Pressed!'); setRedirect(true)}}} className="searchBarContainer">
          <input type="text" placeholder="Shop online with the power of AI..." className="searchBar" value={query} onChange={(e) => { setQuery(e.target.value)} }>
          </input >
          {/* <div className="searchBarText">Shop online with the power of <span className='italic'>AI</span>...</div> */}
          <Link to={`${query}`}><div className='loopa' >
              <svg width="15" height="15" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg">
                <g clip-path="url(#clip0_1_18)">
                <path d="M0.1927 13.911L3.57259 10.528C2.66109 9.41769 2.11664 7.99538 2.11664 6.44766C2.11664 2.89036 5.00102 0.00598145 8.55832 0.00598145C12.1156 0.00598145 15 2.89036 15 6.44766C15 10.005 12.1156 12.8893 8.55832 12.8893C7.00449 12.8893 5.57912 12.3388 4.46574 11.4212L1.08585 14.801C0.691273 15.162 0.321167 14.9295 0.1927 14.801C-0.0642328 14.5472 -0.0642328 14.1648 0.1927 13.911ZM13.7429 6.44766C13.7429 3.58469 11.4213 1.26312 8.55832 1.26312C5.69535 1.26312 3.37072 3.58469 3.37072 6.44766C3.37072 9.31063 5.69229 11.6322 8.55526 11.6322C11.4182 11.6322 13.7429 9.31063 13.7429 6.44766Z" fill="white"/>
                </g>
                <defs>
                <clipPath id="clip0_1_18">
                <rect width="15" height="15" fill="white" transform="matrix(-1 0 0 1 15 0)"/>
                </clipPath>
                </defs>
              </svg>
            </div></Link>
        </div>
      </div>
      <Routes>
        <Route path='/' element={<Landing/>}/>
        <Route path='/:id' element={<Result/>}/>
      </Routes>
    </div>
  )
}

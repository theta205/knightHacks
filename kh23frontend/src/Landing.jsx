import { Link } from 'react-router-dom'
import img1 from './img1.png'
import img2 from './img2.png'
import img3 from './img3.png'

export default function Landing() {
    return(
        <>
        <div className="egTitle">EXAMPLE SEARCHES</div>
        <div className="cardContainer">
            <div className="card1">
                <div className='pictureContainer1'>
                    <img src={img1} alt="" />
                </div>
                <div className='cardTitle1'>HEADPHONES</div>
                <Link to="/headphones">
                <div className="cardFooter">
                    <div className="cardSearch">SEARCH</div>
                </div>
                </Link>
            </div>
            <div className="card1">
                <div className='pictureContainer1'>
                    <img src={img2} alt="" />
                </div>
                <div className='cardTitle1'>LAPTOPS</div>
                <Link to="/laptops">
                <div className="cardFooter">
                    <div className="cardSearch">SEARCH</div>
                </div>
                </Link>
            </div>
            <div className="card1">
                <div className='pictureContainer1'>
                    <img src={img3} alt="" />
                </div>
                <div className='cardTitle1'>VACUUMS</div>
                <Link to="/vacuums">
                <div className="cardFooter">
                    <div className="cardSearch">SEARCH</div>
                </div>
                </Link>
            </div>
        </div>
        </>
    )
}
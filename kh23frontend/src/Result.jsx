import { useParams } from "react-router-dom"
import { useState } from "react"
import amaz from './img8.png'
import goog from './img9.png'

export default function Result() {
    const { id } = useParams()
    const [isLoading, setIsLoading] = useState(true); // Create a loading state
    const [data, setData] = useState([]); // Create a state for data

    useEffect(() => {
        // Use an asynchronous function to fetch data
        const fetchData = async () => {
            try {
                const response = await fetch(`http://localhost:8000/${id}`);
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                const jsonData = await response.json();
                setData(jsonData); // Set the data once it's fetched
            } catch (error) {
                console.error('Error fetching data:', error);
            } finally {
                setIsLoading(false); // Set loading to false when done
            }
        };

        fetchData(); // Call the fetch function when the component mounts
    }, [id]);

    // Display a loading message while waiting for fetch
    if (isLoading) {
        return <div>The loading takes a while, please wait...</div>
    }
 
    // const data = [
    //     {
    //         productName: "Macbook M3 Air 13 2023",
    //         rank: 1,
    //         price: 1200.0,
    //         summary: "Extraordinary battery life. Best consumer laptop in 2023. Powered by a powerful M2 Apple Silicon CPU.",
    //         picture: "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6509/6509650_sd.jpg;maxHeight=640;maxWidth=550"
    //     },
    //     {
    //         productName: "Macbook M3 Air 13 2023",
    //         rank: 1,
    //         price: 1200.0,
    //         summary: "Extraordinary battery life. Best consumer laptop in 2023. Powered by a powerful M2 Apple Silicon CPU.",
    //         picture: "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6509/6509650_sd.jpg;maxHeight=640;maxWidth=550"
    //     },
    //     {
    //         productName: "Macbook M3 Air 13 2023",
    //         rank: 1,
    //         price: 1200.0,
    //         summary: "Extraordinary battery life. Best consumer laptop in 2023. Powered by a powerful M2 Apple Silicon CPU.",
    //         picture: "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6509/6509650_sd.jpg;maxHeight=640;maxWidth=550"
    //     },
    //     {
    //         productName: "Macbook M3 Air 13 2023",
    //         rank: 1,
    //         price: 1200.0,
    //         summary: "Extraordinary battery life. Best consumer laptop in 2023. Powered by a powerful M2 Apple Silicon CPU.",
    //         picture: "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6509/6509650_sd.jpg;maxHeight=640;maxWidth=550"
    //     },
    //     {
    //         productName: "Macbook M3 Air 13 2023",
    //         rank: 1,
    //         price: 1200.0,
    //         summary: "Extraordinary battery life. Best consumer laptop in 2023. Powered by a powerful M2 Apple Silicon CPU.",
    //         picture: "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6509/6509650_sd.jpg;maxHeight=640;maxWidth=550"
    //     },
    //     {
    //         productName: "Macbook M3 Air 13 2023",
    //         rank: 1,
    //         price: 1200.0,
    //         summary: "Extraordinary battery life. Best consumer laptop in 2023. Powered by a powerful M2 Apple Silicon CPU.",
    //         picture: "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6509/6509650_sd.jpg;maxHeight=640;maxWidth=550"
    //     }
    // 
    return(
    <>
    <div className="cardContainer">
        <div className="card">
            <div className='pictureContainer'>
                <img src={data[0].picture} alt="" />
            </div>
            <div className='cardTitle'>{data[0].productName}</div>
            <div className="cardSummary">{data[0].summary}</div>
            <div className="kitchen">
                <div className="amaz"><a href={`https://amazon.com/s?k=${data[0].productName}`}><img style={{height:"21px", width:"21px"}} src={amaz} alt="" /></a></div>
                <div className="price">$1200</div>
                <div className="goog"><a href={`https://google.com/search?q=${data[0].productName}`}><img style={{height:"21px", width:"21px"}} src={goog} alt="" /></a></div>
            </div>
        </div>
        <div className="card">
            <div className='pictureContainer'>
                <img src={data[1].picture} alt="" />
            </div>
            <div className='cardTitle'>{data[1].productName}</div>
            <div className="cardSummary">{data[1].summary}</div>
           <div className="kitchen">
                <div className="amaz"><a href={`https://amazon.com/s?k=${data[1].productName}`}><img style={{height:"21px", width:"21px"}} src={amaz} alt="" /></a></div>
                <div className="price">$1200</div>
                <div className="goog"><a href={`https://google.com/search?q=${data[1].productName}`}><img style={{height:"21px", width:"21px"}} src={goog} alt="" /></a></div>
            </div>
        </div>
        <div className="card">
            <div className='pictureContainer'>
                <img src={data[2].picture} alt="" />
            </div>
            <div className='cardTitle'>{data[2].productName}</div>
            <div className="cardSummary">{data[2].summary}</div>
           <div className="kitchen">
                <div className="amaz"><a href={`https://amazon.com/s?k=${data[2].productName}`}><img style={{height:"21px", width:"21px"}} src={amaz} alt="" /></a></div>
                <div className="price">$1200</div>
                <div className="goog"><a href={`https://google.com/search?q=${data[2].productName}`}><img style={{height:"21px", width:"21px"}} src={goog} alt="" /></a></div>
            </div>
        </div>
    </div>
    <div className="cardContainer">
        <div className="card">
            <div className='pictureContainer'>
                <img src={data[3].picture} alt="" />
            </div>
            <div className='cardTitle'>{data[3].productName}</div>
            <div className="cardSummary">{data[3].summary}</div>
            <div className="kitchen">
                <div className="amaz"><a href={`https://amazon.com/s?k=${data[3].productName}`}><img style={{height:"21px", width:"21px"}} src={amaz} alt="" /></a></div>
                <div className="price">$1200</div>
                <div className="goog"><a href={`https://google.com/search?q=${data[3].productName}`}><img style={{height:"21px", width:"21px"}} src={goog} alt="" /></a></div>
            </div>
        </div>
        <div className="card">
            <div className='pictureContainer'>
                <img src={data[4].picture} alt="" />
            </div>
            <div className='cardTitle'>{data[4].productName}</div>
            <div className="cardSummary">{data[4].summary}</div>
            <div className="kitchen">
                <div className="amaz"><a href={`https://amazon.com/s?k=${data[4].productName}`}><img style={{height:"21px", width:"21px"}} src={amaz} alt="" /></a></div>
                <div className="price">$1200</div>
                <div className="goog"><a href={`https://google.com/search?q=${data[4].productName}`}><img style={{height:"21px", width:"21px"}} src={goog} alt="" /></a></div>
            </div>
        </div>
        <div className="card">
            <div className='pictureContainer'>
                <img src={data[5].picture} alt="" />
            </div>
            <div className='cardTitle'>{data[5].productName}</div>
            <div className="cardSummary">{data[5].summary}</div>
            <div className="kitchen">
                <div className="amaz"><a href={`https://amazon.com/s?k=${data[5].productName}`}><img style={{height:"21px", width:"21px"}} src={amaz} alt="" /></a></div>
                <div className="price">$1200</div>
                <div className="goog"><a href={`https://google.com/search?q=${data[5].productName}`}><img style={{height:"21px", width:"21px"}} src={goog} alt="" /></a></div>
            </div>
        </div>
    </div>
    </>
    )
}
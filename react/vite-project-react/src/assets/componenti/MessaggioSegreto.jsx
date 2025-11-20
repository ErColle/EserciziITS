import {useState} from "react"

const MessaggioSegreto = () => {

    const [mostra, setMostra] = useState(false)

    return (
        <div>
            <button onClick = {() => {setMostra(!mostra)}}> { mostra?"nascondi": "mostra"} </button>
            {mostra && <p>messaggio segreto</p>}
        </div>
    )
}

export default MessaggioSegreto
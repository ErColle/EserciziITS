import { useState } from 'react'

const Termostato = () => {
    const [temperatura, setTemperatura] = useState(0)

    const aumenta = () => setTemperatura(prevTemp => prevTemp + 1)
    const diminuisci = () => setTemperatura(prevTemp => prevTemp - 1)
    
    return(
        <div>
            <h1> Temperatura: {temperatura}</h1>
            <button onClick = {aumenta} >+</button>
            <button onClick = {diminuisci} >-</button>
    
        </div>
    )
}

export default Termostato

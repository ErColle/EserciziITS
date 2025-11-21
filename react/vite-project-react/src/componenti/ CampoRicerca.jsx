import React from "react";
import { useState } from "react";

const CampoRicerca = () => {

    const [testoRicerca, setTestoRicerca] = useState("")
    return (
        <div>
            <input
                type="text" value={testoRicerca} onChange={(e) => setTestoRicerca(e.target.value)}
            />

            <p>{testoRicerca}</p>

        </div>
    )

}

export default CampoRicerca
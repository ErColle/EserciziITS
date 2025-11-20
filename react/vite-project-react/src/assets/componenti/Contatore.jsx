import React, { useState } from 'react';

const Contatore = () => {
  const [count, setCount] = useState(0);

  const aggiunta = () => {
    setCount(count + 1);
  };

  const rimozione = () => {
    setCount(count - 1);
  };

  return (
    <div>
      <h2>{count}</h2>
      <button onClick={aggiunta} className="btn btn-primary">
        Aggiungi +1
      </button>
      <button onClick={rimozione} className="btn btn-danger">
        Rimuovi -1
      </button>
    </div>
  );
};

export default Contatore;
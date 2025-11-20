import React, { useState } from 'react'

const Checkbox_counter = () => {
    const skills = [
        { id: 1, name: "JavaScript" },
        { id: 2, name: "React" },
        { id: 3, name: "Vue" },
        { id: 4, name: "Angular" },
        { id: 5, name: "TypeScript" },
        { id: 6, name: "Node.js" },
        { id: 7, name: "PHP" },
        { id: 8, name: "Laravel" },
        { id: 9, name: "WordPress" },
        { id: 10, name: "CSS/SASS" }
    ];


    const [checked, setChecked] = useState(0)

    const check_count = () => {
        
    }

    return (
        <div>
            <h2>Selenziona le tue skill </h2>
    {skills.map((skill) => (
        <div>
            <input type='checkbox'/>
            <label>{skill.name}</label>
        </div>
    ))}
        </div>
    );
}

export default Checkbox_counter
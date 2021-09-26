import React from 'react'
import { useState } from 'react';

const Input = ({onSubmit}) => {
    const [people, setPeople] = useState([]);

    const handleKeyDown = (e) => {
        if (e.key === 'Enter') {
            const person = e.target.value;
            e.target.value = '';
            setPeople((oldPeople) => [...oldPeople, person]);
        }
    };

    const handleSubmit = () => {
        onSubmit(people);
    };

    return (
        <>
            <h2>People</h2>
            <input type="text" placeholder="Enter names" onKeyDown={handleKeyDown} />
            <ul>
                {people.map((item) => (
                    <li key={item}>{item}</li>
                ))}
            </ul>
            {people.length > 0 && <button type="submit" onClick={handleSubmit}>Submit</button>}
        </>
    )
}

export default Input;
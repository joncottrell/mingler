import React from 'react'
import { useState } from 'react';

const Input = ({onSubmit}) => {
    const [people, setPeople] = useState([]);
    const [weeks, setWeeks] = useState(0);

    const handleKeyDown = (e) => {
        if (e.key === 'Enter') {
            const person = e.target.value;
            e.target.value = '';
            setPeople((oldPeople) => [...oldPeople, person]);
        }
    };

    const handleSubmit = () => {
        onSubmit(people, weeks);
    };

    const handleWeeksChange = (e) => {
        setWeeks(parseInt(e.target.value));
    };

    return (
        <>
            <h2>People</h2>
            <input type="text" pattern="[0-9]*" placeholder="Weeks" onChange={handleWeeksChange} />
            <br />
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
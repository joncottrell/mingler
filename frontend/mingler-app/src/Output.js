import React from 'react';

const Output = ({schedule}) => {

    return (
        <>
        <ol>
            {schedule && 
                schedule.map((week, index) => <li key={index}>{week.map((pair) => "(" + pair[0] + ", " + pair[1] + ")")}</li>)
            }
        </ol>
        </>
    )
};

export default Output;
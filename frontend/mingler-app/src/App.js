import React, { useState } from 'react';

import './App.css';
import Input from './Input';
import Output from './Output';
import submitPeople from './mingleApi';



function App() {

  const [schedule, setSchedule] = useState(null);

  const handleSubmit = (people) => {
    submitPeople(people, (s) => {
      setSchedule(s);
    });
  };

  return (
    <div className="App">
      <header className="App-header">
        <p>
          Schedule your team's one on ones!
        </p>
        <Input onSubmit={handleSubmit} />
        <Output schedule={schedule} />
      </header>
    </div>
  );
}

export default App;

import axios from 'axios';

const api = axios.create();

const submitPeople = (people, onSuccess) => {
    const requestData = { people }
    api.post('/', requestData).then((response) => {
        onSuccess(response.data);
    }).catch ((err) => {
        console.log(err);
    });
}

export default submitPeople;
import axios from 'axios';

const api = axios.create();

const submitPeople = (people, weeks, onSuccess) => {
    const requestData = { people, weeks }
    api.post('/', requestData).then((response) => {
        onSuccess(response.data);
    }).catch ((err) => {
        console.log(err);
    });
}

export default submitPeople;
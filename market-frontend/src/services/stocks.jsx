import api from './apiConfig';

async function getStocks(filtros = {}){
    try {
        console.log(api)
        const response = await api.get('http://localhost:8000/stocks/', {params: filtros});
        return response.data;
    } catch (e){
        return
    }
}

export default getStocks;
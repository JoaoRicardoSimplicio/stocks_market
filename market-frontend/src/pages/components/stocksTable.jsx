import { useState, useEffect, ObjectRow } from 'react';

import { Table } from 'react-bootstrap';

import getStocks from '../../services/stocks';


const StocksTable = function () {

  const [stocks, setStocks] = useState([]);


  useEffect(async () => {
    const result = await getStocks();
    setStocks(result);
  }, [])

  return (
    <Table striped bordered hover stocks>
      <thead>
        <tr>
          <th>Stocks</th>
          <th>Last Price</th>
          <th>Price 2</th>
          <th>Price 3</th>
          <th>Price 4</th>
        </tr>
      </thead>
      <tbody>
        {
          Object.entries(stocks).map(([stock, prices]) =>
            <tr>
              <td>{stock}</td>
              <td>{JSON.stringify(prices).split(',')[0] ? JSON.stringify(prices).split(',')[0].split('":"')[1].split('"}')[0] : '-'}</td>
              <td>{JSON.stringify(prices).split(',')[1] ? JSON.stringify(prices).split(',')[1].split('":"')[1].split('"}')[0] : '-'}</td>
              <td>{JSON.stringify(prices).split(',')[2] ? JSON.stringify(prices).split(',')[2].split('":"')[1].split('"}')[0] : '-'}</td>
              <td>{JSON.stringify(prices).split(',')[3] ? JSON.stringify(prices).split(',')[3].split('":"')[1].split('"}')[0] : '-'}</td>
            </tr>
          )
        }
      </tbody>
    </Table>
    );
}

export default StocksTable;
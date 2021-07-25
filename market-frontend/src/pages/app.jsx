import React from 'react';

import NavBarComponent from './components/layout/navBar';
import StocksTable from './components/stocksTable';


const App = function () {
    
    return (
        <>
            <div>
                <NavBarComponent pageMenuName="Stocks"/>,
            </div>
            <StocksTable/>
        </>
    );
}

export default App;
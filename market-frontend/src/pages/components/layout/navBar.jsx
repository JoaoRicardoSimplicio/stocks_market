import React from 'react';

import { Navbar, Nav } from 'react-bootstrap';

const NavBarComponent = function ({ pageMenuName = "Stocks", }) {
    return (
        <Navbar bg="light" expand="lg">
            <Navbar.Brand href="#home">{pageMenuName}</Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
                <Nav className="mr-auto">
                    <Nav.Link href="#home"></Nav.Link>
                    <Nav.Link href="#link">Link</Nav.Link>
                </Nav>
            </Navbar.Collapse>
        </Navbar>
    );
}

export default NavBarComponent;
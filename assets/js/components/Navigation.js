var React = require('react');

module.exports = React.createClass({
    render: function(){
        return (
        <nav id="navbar" className="navbar navbar-default" role="navigation">
            <a className="navbar-brand" href="#">Title</a>
            <ul className="nav navbar-nav">
                <li className="active">
                    <a href="#">Home</a>
                </li>
                <li>
                    <a href="#">Link</a>
                </li>
            </ul>
        </nav>
        )
    }
})